from django.urls import path
from seconda_app.views import esempio_if

app_name = "seconda_app"
urlpatterns = [
    path("es_if", esempio_if, name="es_if"),
]