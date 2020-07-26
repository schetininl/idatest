from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.images import get_image_dimensions
from PIL import Image
from io import BytesIO
from urllib.parse import urlparse
from django.core.files.uploadedfile import InMemoryUploadedFile
import requests

from .models import Img
from .forms import NewImageForm, ImageForm


def index(request):
    images = Img.objects.order_by("-pk").all()
    return render(request, "index.html", {"images": images})


def get_remote_image(image_url):
    im = None
    name = ''
    try:
        r = requests.get(image_url, stream=True)
    except Exception:
        return None
    redirect("new")
    if r.status_code == 200:
        name = urlparse(image_url).path.split('/')[-1]
        i = Image.open(r.raw)
        buffer = BytesIO()
        if i.mode != "RGB":
            i = i.convert("RGB")
        i.thumbnail((i.width, i.height), Image.ANTIALIAS)
        i.save(buffer, format='JPEG')
        im = InMemoryUploadedFile(
            buffer,
            None,
            name,
            'image/jpeg',
            buffer.tell(),
            None)

    return {'im': im, 'name': name}


def new(request):
    if request.method == "POST":
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():

            if form.cleaned_data['imageFile'] and not form.cleaned_data['imageName'] :
                image = form.cleaned_data['imageFile']
                name = image.name
                width, height = get_image_dimensions(image)

            elif form.cleaned_data['imageName'] and not form.cleaned_data['imageFile']:
                img = get_remote_image(form.cleaned_data['imageName'])
                if img is None:
                    error = "Неверная ссылка"
                    return render(request, "new.html", {'form': form, 'error': error})
                image = img['im']
                name = img['name']
                width, height = get_image_dimensions(img['im'])

            else:
                error = "Можно использовать только один способ загрузки изображения"
                return render(request, "new.html", {'form': form, 'error': error})

            result = Img.objects.create(image=image, name=name, width=width, height=height)
            return redirect("img_view", img_id=result.pk)
            
    else:
        form = NewImageForm()
    return render(request, "new.html", {'form': form})


def img_view(request, img_id):
    image = get_object_or_404(Img, pk=img_id)
    attitude = image.width / image.height
    size = str(image.width)+'x'+str(image.height)
    form = ImageForm(request.POST or None, instance=image)
    if request.method == "POST" and form.is_valid():
        new_size = form.save(commit=False)
        if form.cleaned_data['height'] and not form.cleaned_data['width']:
            new_size.width = form.cleaned_data['height'] * attitude
        else:
            new_size.height = form.cleaned_data['width'] / attitude
        new_size.save()
        return redirect("img_view", img_id=image.pk)
    context = {"form": form, "image": image, "size": size}
    return render(request, "img_view.html", context)