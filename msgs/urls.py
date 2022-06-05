from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateMsgAPIView.as_view(), name='get_post_msgs'),
    path('<int:pk>/', views.RetrieveUpdateDestroyMsgAPIView.as_view(), name='get_delete_update_msg'),
    path('my/', views.MsgsViewSet.as_view(), name='get_my_post_msgs'),
]