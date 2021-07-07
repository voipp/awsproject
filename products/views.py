import datetime

from django.core import serializers
from django.http import HttpResponse, Http404, JsonResponse
from .models import Product


def index(request):
    return HttpResponse("Hello, world. You're at the products index")


def add(request, product_id):
    pr = Product(id=product_id, pub_date=datetime.datetime.now())

    pr.save()

    print(Product.objects.__class__)

    return JsonResponse(serializers.serialize('json', [pr]), safe=False)


def extract(request, product_id):
    try:
        found = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404("Product with id=%s does not exist" % product_id)

    return JsonResponse(serializers.serialize('json', [found]), safe=False)


def delete(request, product_id):
    try:
        found = Product.objects.get(id=product_id)
        found.delete()
    except Product.DoesNotExist:
        raise Http404("Product with id=%s does not exist" % product_id)

    return JsonResponse(serializers.serialize('json', [found]), safe=False)