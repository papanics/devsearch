from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView, # generate a token based on the user.
    TokenRefreshView, # generate a refresh toolkit.
)


urlpatterns = [

    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #basically anytime the token expires, it will send a refresh token to generate a new token.

    path('', views.getRoutes),
    path('projects/', views.getProjects),
    path('projects/<str:pk>', views.getProject),
    path('projects/<str:pk>/vote/', views.projectVote),
]