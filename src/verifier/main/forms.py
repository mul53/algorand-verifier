from django.forms import ModelForm, TextInput, ValidationError
from .models import AppVersion, App

class AppForm(ModelForm):
    class Meta:
        model = App
        fields = '__all__'
        exclude = []

class AppVersionForm(ModelForm):
    class Meta:
        model = AppVersion
        fields = '__all__'
        exclude = ['source_compiled', 'app']

    def clean_source_version(self):
        version = self.cleaned_data['source_version']
    
        try:
            app = App.objects.get(id=self.data['id'])
        except:
            app = None

        if app:
            appVersion = AppVersion.objects.filter(app=app).last()

            if int(version) <= int(appVersion.source_version):
                raise ValidationError('Source version should be greater than previous version')
        
        return version
