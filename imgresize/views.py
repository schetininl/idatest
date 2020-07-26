from django.shortcuts import render, get_object_or_404
from .models import Image


def index(request):
    images = Image.objects.order_by("-pk").all()
    return render(request, "index.html", {"images": images})

def new(request):
    return render(request, "new.html")


def img_view(request, img_id):
    image = get_object_or_404(Image, pk=img_id)
    size = str(image.width)+'x'+str(image.height)
    return render(request, "img_view.html", {"image": image, "size": size})