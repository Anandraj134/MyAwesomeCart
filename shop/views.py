from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return HttpResponse("About")
    # return render(request, 'shop/index.html')


def contact(request):
    return HttpResponse("contact")
    # return render(request, 'shop/index.html')


def tracker(request):
    return HttpResponse("tracker")
    # return render(request, 'shop/index.html')


def search(request):
    return HttpResponse("search")
    # return render(request, 'shop/index.html')


def productView(request):
    return HttpResponse("Product View")
    # return render(request, 'shop/index.html')


def checkout(request):
    return HttpResponse("checkout")
    # return render(request, 'shop/index.html')
