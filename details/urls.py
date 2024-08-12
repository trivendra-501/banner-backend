from django.urls import path
# from .views import list_banners, create_banner, get_banner, update_banner, delete_banner

# urlpatterns = [
#     path('banner/', list_banners, name='list_banners'),
#     path('banner/<int:pk>/', get_banner, name='get_banner'),
#     path('banner/create/', create_banner, name='create_banner'),
#     path('banner/<int:pk>/update/', update_banner, name='update_banner'),
#     path('banner/<int:pk>/delete/', delete_banner, name='delete_banner'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update_banner/', views.update_banner, name='update_banner'),
]
