from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import HellowSerializer ,UserProfileSerailzer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import UserProfile
from .permissions import UpdateOwnProfile,UpdateOwnStatusProfile
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .serializer import ProfileFeedItemSeralizer
from .models import ProfileFeedItem
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Create your views here.


class HellowApiView(APIView):
    serializer_class=HellowSerializer

    def get(self,request,format=None):

        an_apiview=[
            'Uses HTTP methods as function (get ,post , patvh, put , delete)',
            'Is Similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manualy to URLs',
        ]

        context1={'message':'Hellow!!!','api_apiview':an_apiview}
        context2={'message':'Hellow!!!'}
        context3={'api_apiview':an_apiview}
        return Response(context1,status=status.HTTP_202_ACCEPTED)

    def post(self,request):
        serializer=HellowSerializer(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message="Hellow {}".format(name)
            return Response({"message":message},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        return Response({'method':'PUT'})

    def Patch(self,request,pk=None):
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        return Response({'method':'DELETE'})



class HellowApiViewSets(viewsets.ViewSet):
        serializer_class=HellowSerializer

        def list(self, request):
            an_apiview=[
                'Uses HTTP methods as function (get ,post , patvh, put , delete)',
                'Is Similar to a traditional Django View',
                'Gives you the most control over you application logic',
                'Is mapped manualy to URLs',
            ]
            context1={'message':'Hellow!!!','api_apiview':an_apiview}
            return Response(context1,status=status.HTTP_200_OK)
            

        def create(self, request):
            serializer=HellowSerializer(data=request.data)

            if serializer.is_valid():
                name=serializer.validated_data.get('name')
                message="Hellow {}".format(name)
                return Response({"message":message},status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        def retrieve(self, request, pk=None):
            return Response({"retrieve":"RETRIEVE"})

        def update(self, request, pk=None):
            return Response({"Update":"Update"})

        def partial_update(self, request, pk=None):
            return Response({"Partial_Update":"Partial_Update"})

        def destroy(self, request, pk=None):
            return Response({"Destroy":"Destroy"})



class ProfileApiViewSets(viewsets.ModelViewSet):
    """ Handle And Create Profile API"""
    serializer_class=UserProfileSerailzer
    queryset=UserProfile.objects.all()

    authentication_classes=(TokenAuthentication,)
    permission_classes=(UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email')



class UserLoginApiView(ObtainAuthToken):
    """ Handle Creating user authentication tokens """
    renderer_classes =api_settings.DEFAULT_RENDERER_CLASSES



class UserProfileFeedViewSet(viewsets.ModelViewSet):
        """Handles creting , reading and updating profile feed item """
        authentication_classes =(TokenAuthentication,)
        permission_classes=(UpdateOwnStatusProfile,
        IsAuthenticatedOrReadOnly,)



        serializer_class=ProfileFeedItemSeralizer
        queryset=ProfileFeedItem.objects.all()


        """ Override create object behavoir"""
        def perform_create(self,serializer):
            """set the user profile to the logged in user"""
            serializer.save(user_profile=self.request.user)


