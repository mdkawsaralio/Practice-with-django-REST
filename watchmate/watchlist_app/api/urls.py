


from django.urls import path
from watchlist_app.api.views import Movielist,MovieDetails,StreamPlatform

urlpatterns = [
    path('list/',Movielist.as_view(),name='movie-list'),
    path('<int:pk>',MovieDetails.as_view(),name='movie-details'),
    path('stream/',StreamPlatform.as_view(),name='stream-platform')
]
