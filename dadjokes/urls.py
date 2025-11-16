from django.urls import path
from . import views

urlpatterns = [
    # HTML Views
    path('', views.random_view, name='random'),
    path('random', views.random_view, name='random'),
    path('jokes', views.jokes_view, name='jokes'),
    path('joke/<int:pk>', views.joke_detail_view, name='joke_detail'),
    path('pictures', views.pictures_view, name='pictures'),
    path('picture/<int:pk>', views.picture_detail_view, name='picture_detail'),

    # REST API Views
    path('api/', views.api_random_joke, name='api_random'),
    path('api/random', views.api_random_joke, name='api_random_joke'),
    path('api/jokes', views.JokeListCreateAPIView.as_view(), name='api_jokes'),
    path('api/joke/<int:pk>', views.JokeDetailAPIView.as_view(), name='api_joke_detail'),
    path('api/pictures', views.PictureListAPIView.as_view(), name='api_pictures'),
    path('api/picture/<int:pk>', views.PictureDetailAPIView.as_view(), name='api_picture_detail'),
    path('api/random_picture', views.api_random_picture, name='api_random_picture'),
]
