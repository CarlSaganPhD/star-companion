from django.shortcuts import render
from .models import search_resources

# Create your views here.


def resource_search(request):
    results = []
    if "resource" in request.GET:
        resource_name = request.GET["resource"]
        results = search_resources(resource_name)
    return render(request, "search.html", {"results": results})
