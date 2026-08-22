


from django.urls import path
from watchlist_app.api import views

urlpatterns = [
    path('list/',views.Movielist().as_view(),name='movie-list'),
    path('<int:pk>',views.movie_details,name='movie-details')
]
