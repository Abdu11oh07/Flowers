from django.urls import path
from .views import index, posts_by_gullar, posts_by_turlar

urlpatterns = [
    path('', index, name='home'),
    path('turlar/<int:turlar_id>/', posts_by_turlar, name='turlar'),
    path('gullar/<int:gullar_id>/', posts_by_gullar, name='gullar'),
]
