import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

app = Celery("api")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.loader.override_backends["django-db"] = (
    "django_celery_results.backends.database:DatabaseBackend"
)

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
