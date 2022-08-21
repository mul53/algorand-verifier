from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('verify', views.verify, name='verify'),
    path('lookup', views.lookup, name='lookup'),
    path('app/<int:app_id>', views.app, name='app'),
    path('app/<int:app_id>/update', views.update, name='update'),
    path('app/<int:app_id>/versions', views.app_versions, name='app_versions'),
    path('app/<int:app_id>/version/<int:app_version>', views.app_version, name='app_version')
]
