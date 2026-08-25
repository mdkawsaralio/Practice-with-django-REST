


from django.urls import path,include
from watchlist_app.api.views import Movielist,MovieDetails,Reviewlist,ReviewDetails,ReviewCreate,StreamflatfromdetailsVS
from rest_framework.routers import DefaultRouter

routers=DefaultRouter()
# routers.register('stream',StreamflatformVS,basename='streamplatform')
routers.register('stream',StreamflatfromdetailsVS,basename='streamplatform')



urlpatterns = [
    path('',Movielist.as_view(),name='movie-list'),
    path('<int:pk>',MovieDetails.as_view(),name='movie-details'),
    path('',include(routers.urls)),
    # path('stream/',StreamPlatformAV.as_view(),name='stream-platform'),
    # path('stream/<int:pk>',StreamDetailsAV.as_view(),name='streamplatform-detail'),
    
    path('<int:pk>/review-create',ReviewCreate.as_view(),name='review-create'),
    path('<int:pk>/review',Reviewlist.as_view(),name='review-list'),
    path('review/<int:pk>',ReviewDetails.as_view(),name='review-details'),
]
