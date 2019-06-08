from django.shortcuts import render,get_object_or_404;
from rest_framework import permissions;
from rest_framework import generics;
from rest_framework.exceptions import APIException;
from bins.models import Bin;
from bins.serializers import *;
from django.http import Http404;
from bins.permissions import (IsOwner,
IsPublicBin,IsSharedWith,IsPublic_IsSharedWith_IsOwner);
# Create your views here.
                              
class BinsListApiView(generics.ListAPIView):
    """
    used to retrieve bins to end user 
    if user is authenticated it will return queryset include bins created, public bins and bins shared with this user

    if user anonymous it will return public bins only 

    also you can query with order
    descinding order by date created
    http://127.0.0.1:8000/user/bins/?order=desc
    asinding order is default or by 
    http://127.0.0.1:8000/user/bins/?order=asc
    """
    model=Bin;
    serializer_class=BinSerializer;
    permission_classes=[permissions.AllowAny]
    def get_queryset(self):
        order=self.request.GET.get('order',None);
        user=self.request.user;
        if user.is_anonymous:
            if order is not None and order.strip().lower()=="desc":
                return Bin.objects.filter(public=True).order_by('-created');
            else:
                return Bin.objects.filter(public=True).order_by('created');
        else:
            
            user_bins=Bin.objects.filter(author=user);
            shared_with_user=Bin.objects.filter(shared_with=user);
            public_bins=Bin.objects.filter(public=True);
            # set all=False to prevent duplicates queries
            queryset=user_bins.union(public_bins,shared_with_user,all=False);
            if order is not None and order.strip().lower()=="desc":
                return queryset.order_by('-created');
            else:
                return queryset.order_by('created');

class BinCreateApiView(generics.CreateAPIView):
    """
    allow users to create bins 
    note we set author in bins field can be null and we set permission to AllowAny to enable anony,ous users to create thier bins and share it 
    """
    model=Bin;
    serializer_class=BinCreateUpdateSerializer;
    queryset=Bin.objects.all();
    permission_classes=[permissions.AllowAny,]
    def perform_create(self,serializer):
        print(self.request.user)
        if self.request.user:
            serializer.save(author=self.request.user);
class BinUpdateApiView(generics.
RetrieveUpdateAPIView):
    """
    allow author and only author of bin to update it to do so we set permissions on [IsAuthenticated,IsOwner]
    note IsOwner custom permission to enable only owner of bin to edit it
    """
    model=Bin;
    lookup_field='pk';
    serializer_class=BinCreateUpdateSerializer;
    queryset=Bin.objects.all();
    permission_classes=[permissions.IsAuthenticated,IsOwner]

class BinDestoryApiView(generics.
RetrieveDestroyAPIView):
    """
    allow author and only author of bin to delete it to do so we set permissions on [IsAuthenticated,IsOwner]
    
    """
    model=Bin;
    serializer_class=BinCreateUpdateSerializer;
    queryset=Bin.objects.all();
    permission_classes=(permissions.IsAuthenticated,IsOwner)

      
class BinDetailApiView(generics.RetrieveAPIView):
    """
    allow user to retrieve bin only if
    user created it or shared within user or bin is public 
    we write custom permission to check if one of the conditions is true
    """
    serializer_class=BinSerializer;
    model=Bin;
    permission_classes=[IsPublic_IsSharedWith_IsOwner,];
    lookup_field='pk';
    queryset=Bin.objects.all();

    
    
