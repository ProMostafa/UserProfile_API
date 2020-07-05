from rest_framework import serializers
from .models import UserProfile ,ProfileFeedItem


class HellowSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)


class UserProfileSerailzer(serializers.ModelSerializer):
    """Serializer a user profile object """

    class Meta:
        model=UserProfile
        #fields='__all__'
        #fields=('id','email','name','password','is_superuser')
        fields=('id','email','name','password')
        extra_kwargs={
            'password':{
                'write_only':True ,
                'style':{'input_type':'password'}
            }

        }

        

    def create(self,validated_data):
        """Create And rteurn a new user """
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user


class ProfileFeedItemSeralizer(serializers.ModelSerializer):

    class Meta:
        model=ProfileFeedItem
        fields=('id','user_profile','status_text','created_on')
        extra_kwargs={'user_profile':{'read_only':True}}
