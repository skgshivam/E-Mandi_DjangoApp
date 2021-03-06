from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from accounts.models import *
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)


class UserBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'email','first_name','last_name']
        read_only_fields=[ 'username','first_name','last_name']

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = UserProfile
        fields = ( 'id', 'user','company', 'state', 'city','street', 'aadharcard', 'pincode', 'phone')
        read_only_fields=[ 'user']

class ProfilegetSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = UserProfile
        fields = ( 'company', 'state', 'city','street', 'aadharcard', 'pincode', 'phone')
        # read_only_fields=[ 'user']


class User2Serializer(serializers.ModelSerializer):
    
    profile=ProfileSerializer(write_only=True)
    
    
    class Meta:
        model = User
        fields = ('username', 'profile')

    def create(self, validated_data):
        # profile_data = validated_data.pop('profile')
        # user_instance = User.objects.create(**validated_data)
        # UserProfile.objects.create(user=user_instance, **profile_data)
        # return user_instance    
        raise ValidationError("Wrong method being called")

    def update(self, instance, validated_data):

        profiles_data= validated_data.pop('profile')
        profile1=instance.userprofile
        instance.save()
        profile1.company= profiles_data.get('company', profile1.company)
        profile1.state= profiles_data.get('state', profile1.state)
        profile1.city= profiles_data.get('city', profile1.city)
        profile1.street= profiles_data.get('street', profile1.street)
        profile1.aadharcard= profiles_data.get('aadharcard', profile1.aadharcard)
        profile1.pincode= profiles_data.get('pincode', profile1.pincode)
        profile1.phone= profiles_data.get('phone', profile1.phone)
        profile1.save()
        return instance




class UserSerializerWithToken(serializers.ModelSerializer):

    profile= ProfileSerializer(write_only=True)
    

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token


    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        validated_data['is_active']=False
        user_instance = User.objects.create(**validated_data)
        UserProfile.objects.create(user=user_instance, **profile_data)
        password = validated_data.pop('password', None)
        if password is not None:
            user_instance.set_password(password)
        user_instance.save()
        return (user_instance)
    

    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'first_name', 'last_name', 'email','profile')

class UserreviewSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')
    revieweduser = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserReview
        fields = ('id', 'user', 'revieweduser', 'review', 'rating',)
        # read_only_fields=[ 'avgrating']



class AvgRatingSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.user.username')
    # avgrating = serializers.ReadOnlyField(source='avgrating.revieweduser.user.username')

    class Meta:
        model = AvgRating
        fields = ('id', 'user','avgrating',)
        read_only_fields=[ 'avgrating','user']

