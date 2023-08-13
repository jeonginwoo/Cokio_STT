from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Menu
from .serializers import MenuSerializer
from django.http import JsonResponse

from .models import TestMenuTable

def index(request):
    return render(request, 'main/index.html')


class MenuDetailView(APIView):
    def get(self,request,menu_key):
        try:
            menu = Menu.objects.get(name=menu_key)
            serializer = MenuSerializer(menu)
            return Response(serializer.data)
        except Menu.DoesNotExist:
            return Response({"error" : "Menu not found"}, status= 404)
        
def purchase(request):
    return render(request, 'main/purchase.html')

def speechRecognition(request):
    if request.method == 'POST':
        recordData = request.body

        with open('../test_record_data.mp3', 'wb') as mpeg:
            mpeg.write(recordData)

        data = {"message": "Response OK!"}

        return JsonResponse(data)
    
    return JsonResponse({"message": "This request is GET method"})

def testTable(request):
    menu_list = TestMenuTable.objects.all()
    context = {'menu_list': menu_list}
    return render(request, 'main/menu_list.html', context)

def menuDetail(request, menu_id):
    menu = TestMenuTable.objects.get(id=menu_id)
    context = {'menu': menu}
    return render(request, 'main/menu_detail.html', context)