from django.conf.urls import url
from .views import BookingSerializerView, QueryView, index

app_name = 'api'

urlpatterns = [
	url(r'^$', index, name='doc'),
	url(r'^bookings/$', BookingSerializerView.as_view(), name='bookings'),
	url(r'^query/$', QueryView.as_view(), name='query'),
	]