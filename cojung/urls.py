from django.urls import path
from .views import resolve_views,problem_views,base_views


app_name = 'cojung'

urlpatterns = [
    path('<int:problem_pk>/hard/',problem_views.harder,name='hard'),
    path('<int:problem_pk>/easy/',problem_views.easyer,name='easy'),
    path('resolve/create/<int:problem_id>/',resolve_views.Resolve_create,name='resolve_create'),
    path('<int:problem_id>/',base_views.detail,name='detail')
]