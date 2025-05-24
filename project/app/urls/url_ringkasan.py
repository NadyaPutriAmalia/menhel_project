from django.urls import path
from app.views import view_ringkasan as views
from app.views import view_ringkasan as views

urlpatterns = [
    path('ringkasan', views.ringkasan, name='ringkasan'),
    path('analisis', views.analisis_view, name='analisis'),
]