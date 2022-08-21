from django.http import JsonResponse
from main.models import App

def search_app(request):
    app = request.GET.get("app")
    apps = []
    if app:
        app_objects = App.objects.filter(id__startswith=app).values()
        for app_object in app_objects:
            apps.append(app_object)
    return JsonResponse({ 'status': 200, 'apps': apps })
