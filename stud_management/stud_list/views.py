from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

# Create your views here.


# creating the view list
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        # 'all_items': '/',
        # 'Search by Category': '/?category=category_name',
        # 'Search by Subcategory': '/?subcategory=category_name',
        # 'Add': '/create',
        # 'Update': '/update/pk',
        # 'Delete': '/item/pk/delete',
        
        
        'all_items': '/',
        'Search by studentName': '/?name=student_name',
        'Search by studentRoll': '/?roll=student_roll',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete',
        
        'name':'alvi<str>',
        'roll':'23<int>',
        'email':'example@gmail.com<str>',
        'group':'engineer/doctor/lawyer etc<str>'
    }

    return Response(api_urls)


# This is part is for Create view
@api_view(['POST'])
def add_items(request):
    item = ItemSerializer(data=request.data)

    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    
    if item.is_valid():
        item.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# This part is for List view
@api_view(['GET'])
def view_items(request):
    if request.query_params:
        items = Item.objects.filter(**request.query_params.dict())
    else:
        items = Item.objects.all()
    
    if items:
        serializer = ItemSerializer(items, many = True)
        return Response(serializer.data)
    else:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    
    
# This part is for update view
@api_view(['PUT'])
def update_items(request, pk):
    item = Item.objects.get(pk = pk)
    data = ItemSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    

# This part is for Delete view
@api_view(['DELETE'])
def delete_items(request,pk):
    item = get_object_or_404(Item,pk = pk)
    item.delete()
    return Response(status=status.HTTP_202)