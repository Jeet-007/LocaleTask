from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Booking

class BookingSerializer(ModelSerializer):

	class Meta:
		model = Booking
		fields = '__all__'
		