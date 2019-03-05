from django.conf.urls import url
from django.views.generic import TemplateView

app_name = 'house'

urlpatterns = [
    url(r'', TemplateView.as_view(template_name="index.html")),
]