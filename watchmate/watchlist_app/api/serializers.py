from rest_framework import serializers
from watchlist_app.models import StreamPlatform,Watchlist,Reviews
from django.core.validators import MaxLengthValidator



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reviews
        exclude=('watchlist',)

class Watchlistserializer(serializers.ModelSerializer):
    reviews=ReviewSerializer(many=True,read_only=True)
    class Meta:
        model=Watchlist
        fields='__all__'


class Streamplatformserializer(serializers.HyperlinkedModelSerializer):
    watchlist_data=Watchlistserializer(many=True,read_only=True)
    #watchlist_data=serializers.StringRelatedField(many=True)
    #watchlist_data=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='movie-details')
    class Meta:
        model=StreamPlatform
        fields='__all__'




# class MovieSerializer(serializers.ModelSerializer):
#     len_name=serializers.SerializerMethodField()
    
#     class Meta:
#         model=Movie
#         fields="__all__"
        
        
#     def validate(self,data):
#         if data['name']==data['description']:
#             return serializers.ValidationError("Title and description should not same")
#         else:
#             return data
    
#     def get_len_name(self,object):
#         length=len(object.name)
#         return length
        
    
    
#     def validate_name(self,value):
#         if value<2:
#             return serializers.ValidationError("Name is Too short")
#         else:
#             return value





# class MovieSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField()
#     description=serializers.CharField()
#     active=serializers.BooleanField()
    
#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.description=validated_data.get('description',instance.description)
#         instance.active=validated_data.get('active',instance.active)
#         instance.save()
#         return instance