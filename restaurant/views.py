from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions

from .models import Booking,Menu
from .serializers import BookingSerializer,MenuSerializer


#class MenuItemView(generics.ListCreateView):
#    def get(self, request):
#        items = Menu.objects.all()
#        serializer= MenuSerializer(items, many=True)
#        return Response(serializer.data)
#    def post(self, request):
#
#        serializer= MenuSerializer(data=request.data)
#        if serializer.is_valid():
 #           serializer.save()
#            return Response({"status": "success", "data": serializer.data})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
   queryset = Booking.objects.all()
   serializer_class = BookingSerializer
   permission_classes = [permissions.IsAuthenticated]




#def sayHello(request):
 #return HttpResponse('Hello World')

#def index(request):
#    return render(request, 'index.html', {})