import django.contrib.admin.options as options
from django.apps import AppConfig

from .models import MarkdownField
from .widgets import MarkdownEditorWidget

# DIRTY HACK BELOW!
options.FORMFIELD_FOR_DBFIELD_DEFAULTS.update({
    MarkdownField: {'widget': MarkdownEditorWidget},
})


class DjangoTUIEditorConfig(AppConfig):
    name = 'django_tuieditor'
    verbose_name = 'Django TUI.Editor'
