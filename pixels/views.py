from django.shortcuts import render
from .models import Pixel
from django.db import models


def home(request):
    pixels = Pixel.objects.all()
    context = {
        'pixels':pixels
    }
    return  render(request, 'pixels/home.html', context)

    def search_results(request):
        if 'pixel' in request.GET and request.GET["pixel"]:
            search_term = request.GET.get("pixel")
            searched_images = Pixel.search_by_title(search_term)
            message = f"{search_term}"
            return render(request, 'pixels/search.html',{"message":message,"pixels": searched_images})
        else:
            message = "You haven't searched for any image category"
            return render(request, 'pixels/search.html', {"message": message})
        @classmethod
        def search_by_title(cls,search_term):
            Pixel = cls.objects.filter(title__icontains=search_term)
            return Pixel