from rest_framework.decorators import api_view
from rest_framework import generics,mixins
from user_app.api.serializer import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class Resisteruser(generics.CreateAPIView):
    serializer_class=RegistrationSerializer
    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            token,created=Token.objects.get_or_create(user=user)
            return Response({
                "user":user.username,
                "email":user.email,
                "Token": token.key
            },)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class logout(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
       request.user.auth_token_delete()
       return Response({'message':'sussessfully logout'})




# @api_view(["POST"])
# def registeruser(request):
#     if request.method=="POST":
#         serializer=RegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             return serializer.data
#         else:
#             return serializer.errors




