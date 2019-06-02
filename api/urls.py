from django.conf.urls import url
from .views import BookingSerializerView, QueryView

app_name = 'api'

urlpatterns = [
	url(r'^bookings/$', BookingSerializerView.as_view(), name='bookings'),
	url(r'^query/$', QueryView.as_view(), name='query'),
	]