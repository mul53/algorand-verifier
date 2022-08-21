from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

from main.modules.utils import Utils
from .forms import AppForm, AppVersionForm
from .models import App, AppVersion
from .modules.verification import Verification

def index(request):
    apps = AppVersion.objects.order_by('-verified_at')[:5]
    return render(request, 'index.html', { 'apps': apps })

def app(request, app_id):
    app = App.objects.get(id=app_id)
    appVersion = AppVersion.objects.filter(app=app).last()
    return render(request, 'app.html', { 'app': app, 'appVersion' : appVersion })

def app_versions(request, app_id):
    app = App.objects.get(id=app_id)
    appVersions = AppVersion.objects.filter(app=app)
    return render(request, 'app_versions.html', { 'appVersions': appVersions })

def app_version(request, app_id, app_version):
    app = App.objects.get(id=app_id)
    appVersion = AppVersion.objects.get(app=app, source_version=app_version)
    return render(request, 'app_version.html', { 'appVersion': appVersion })

def verify(request):
    appForm = AppForm(request.POST)
    appVersionForm = AppVersionForm(request.POST)

    if request.method == 'POST':
        if appForm.is_valid() and appVersionForm.is_valid():
            verifier = Verification(request.POST)
            (success, compiled_code) = verifier.verify_contract()

            if success:
                compiled_approval = compiled_code.get('app_approval')
                compiled_clear_state = compiled_code.get('app_clear')

                app = appForm.save()
                appVersion = appVersionForm.save(commit=False)
                appVersion.app = app;
                appVersion.source_compiled_clear = compiled_clear_state
                appVersion.source_compiled_approval = compiled_approval
                appVersion.source_decompiled_clear = Utils.fetch_decompiled_code(compiled_clear_state) 
                appVersion.source_decompiled_approval = Utils.fetch_decompiled_code(compiled_approval)
                appVersion.save()

                messages.success(request, 'Verification Success.')
                return HttpResponseRedirect(reverse('app', args=(app.id,)))
            else:
                messages.error(request, 'Verification Failed.')
    else:
        appForm = AppForm()
        appVersionForm = AppVersionForm()

    return render(request, 'verify.html', { 'appForm': appForm, 'appVersionForm': appVersionForm })

def lookup(request):
    return render(request, 'lookup.html')

def update(request, app_id):
    app = App.objects.get(id=app_id)
    appVersionForm = AppVersionForm(request.POST)

    if request.method == 'POST':
        if appVersionForm.is_valid():
            verifier = Verification(request.POST)
            (success, compiled_code) = verifier.verify_contract()

            if success:
                compiled_approval = compiled_code.get('app_approval')
                compiled_clear_state = compiled_code.get('app_clear')
                
                appVersion = appVersionForm.save(commit=False)
                appVersion.app = app;
                appVersion.source_compiled_clear = compiled_clear_state
                appVersion.source_compiled_approval = compiled_approval
                appVersion.source_decompiled_clear = Utils.fetch_decompiled_code(compiled_clear_state) 
                appVersion.source_decompiled_approval = Utils.fetch_decompiled_code(compiled_approval)
                appVersion.save()

                messages.success(request, 'Verification Success.')
                return HttpResponseRedirect(reverse('app', args=(app.id,)))
            else:
                messages.error(request, 'Verification Failed.')
    else:
        appVersionForm = AppVersionForm()

    return render(request, 'update.html', { 'app': app, 'appVersionForm': appVersionForm })
