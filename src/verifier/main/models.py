from email.policy import default
from random import choices
from django.db import models

class App(models.Model):
    id = models.IntegerField(primary_key=True)

class SourceType(models.TextChoices):
    TEAL = 'TL', 'Teal'
    PYTEAL = 'PT', 'PyTeal'
    REACH = 'RH', 'Reach'

class SourcePyTealMode(models.TextChoices):
    SIGNATURE = 'SIG', 'Signature'
    APPLICATION = 'APP', 'Application'

class AppVersion(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    source_url = models.URLField(null=True, blank=True)
    source_approval_url = models.URLField(null=True, blank=True)
    source_clear_state_url = models.URLField(null=True, blank=True)
    source_version = models.IntegerField()
    source_raw = models.TextField(null=True, blank=True)
    source_approval = models.TextField(null=True, blank=True)
    source_clear_state = models.TextField(null=True, blank=True)
    source_compiled = models.TextField()
    source_compiled_approval = models.TextField(null=True, blank=True)
    source_compiled_clear = models.TextField(null=True, blank=True)
    source_decompiled_approval = models.TextField(null=True, blank=True)
    source_decompiled_clear = models.TextField(null=True, blank=True)
    source_pyteal_version = models.IntegerField(null=True, blank=True)
    source_type = models.CharField(
        max_length=2,
        choices=SourceType.choices, 
        default=SourceType.TEAL
    )
    source_pyteal_mode = models.CharField(
        max_length=3,
        choices=SourcePyTealMode.choices,
        default=SourcePyTealMode.APPLICATION,
        null=True,
        blank=True
    )
    verified_at = models.DateTimeField(auto_now_add=True)

