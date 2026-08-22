from watchlist_app.models import Watchlist,StreamPlatform
from watchlist_app.api.serializers import Watchlistserializer,Streamplatformserializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



class Movielist(APIView):
    
    def get(self,request):
        movie=Watchlist.objects.all()
        serializer=Watchlistserializer(movie,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=Watchlistserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        else:
            return Response(serializer.errors)
        

class MovieDetails(APIView):
    
    def get(self,request,pk):
        try:
            movie=Watchlist.objects.get(pk=pk)
        except:
            return Response({'Error': "Movie not Found"})
        serializer=Watchlistserializer(movie)
        return Response(serializer.data)
        
    def put(self,request,pk ):
        movie=Watchlist.objects.get(pk=pk)
        serializer=Watchlistserializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        movie=Watchlist.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        



class StreamPlatform(APIView):
    def get(self,request):
        movie=StreamPlatform.objects.all()
        serializer=Streamplatformserializer(movie,many=True)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def post(self,request):
        serializer= Streamplatformserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,data={'data':'invalid request'})










# @api_view(['GET','POST'])
# def Wtachlist(request):
#     if request.method=='GET':
#         movies=Movie.objects.all()
#         serializer=MovieSerializer(movies,many=True)
#         return Response(serializer.data)
#     if request.method=='POST':
#         serializer=MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):
    
#     if request.method=='GET':
#         movies=Movie.objects.get(pk=pk)
#         serializer=MovieSerializer(movies)
#         return Response(serializer.data)
#     if request.method=='PUT':
#         movies=Movie.objects.get(pk=pk)
#         serializer=MovieSerializer(movies,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method=='DELETE':
#         movies=Movie.objects.get(pk=pk)
#         movies.delete()
#         movies.save()
#         return Response(status=status.HTTP_200_OK,data={'data':'successfully deleted'})
    