from django.shortcuts import render
from  django.http import HttpResponse

from .models import Image, Location


def index(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render(request, 'global-frames/index.html', {'images': images[::-1], 'locations': locations})


def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'global-frames/location.html', {'location_images': images})


def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:#-->to check if the query exists
        category = request.GET.get("imagesearch") #--->to check if the query has an photo
        searched_images = Image.search_by_category(category) #-->to march the query term see if it matches a title
        message = f"{category}"
        print(searched_images)
        return render(request, 'global-frames/search.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any valid image category"
        return render(request, 'global-frames/search.html', {"message": message})