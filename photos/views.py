from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Image, Location




# Create your views here.
def my_Photo(request):
    photo  = Image.show_all_images()
    locations = Location.objects.all()
    return render(request, 'all-photos/photo.html',{"photo":photo,"location":locations})


def search_results(request):
    if 'search' in request.GET and request.GET["search"]:
        category = request.GET.get("search")
        searched_image = Image.search_image_by_category(category)
        locations = Location.objects.all()
        message = f"{category}"

        return render (request,'all-photos/search.html',{"message":message,"images":searched_image,"location":locations})

    else:
        message = "You haven't searched for any term"
        return render (request, 'all-photos/search.html',{"message":message})
