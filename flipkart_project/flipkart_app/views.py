from django.shortcuts import render
from .models import item_list
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import json
# Create your views here.

def home(request):
    items = item_list.objects.all()
    return render(request,'home.htm',{"items":items})


def updateitem(request):
    data = json.loads(request.body)
    itemid = data['itemid']
    action = data['action']


    item = item_list.objects.get(id=itemid)


    print(item)
    return JsonResponse('item was added ',safe=False)