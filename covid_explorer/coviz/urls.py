from django.urls import path, register_converter

from . import views


class ISODateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value):
        import datetime
        return datetime.date.fromisoformat(value)

    def to_url(self, value):
        import datetime
        return value.strftime('%Y-%m-%d')

register_converter(ISODateConverter, 'isodate')

urlpatterns = [
    path('', views.index, name='index'),
    path("map/<isodate:date>/", views.map, name='map'),
]
