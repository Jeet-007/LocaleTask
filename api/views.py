from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from .serializers import BookingSerializer
from .models import Booking
# Create your views here.

class BookingSerializerView(APIView):
	permission_classes = (AllowAny,)

	def get(self, request, format=None):
		start = 0
		if request.GET.get('page'):
			start = int(request.GET.get('page'))*100

		bookings = Booking.objects.all().order_by('id')[start:start+100]
		serialized_bookings = BookingSerializer(bookings, many=True)
		return Response({"status": status.HTTP_200_OK, "total_results":bookings.count(), "page": start/100, "results": serialized_bookings.data})

	def post(self, request, format=None):
		print(request.data)
		id = request.data.get('id')
		user_id = request.data.get('user_id')
		vehicle_model_id = request.data.get('vehicle_model_id')
		package_id = request.data.get('package_id')
		travel_type_id = request.data.get('travel_type_id')
		from_area_id = request.data.get('from_area_id')
		to_area_id = request.data.get('to_area_id')
		from_city_id = request.data.get('from_city_id')
		to_city_id = request.data.get('to_city_id')
		from_date = request.data.get('from_date')
		to_date = request.data.get('to_date')
		online_booking = request.data.get('online_booking')
		mobile_site_booking = request.data.get('mobile_site_booking')
		booking_created = request.data.get('booking_created')
		from_lat = request.data.get('from_lat')
		from_long = request.data.get('from_long')
		to_lat = request.data.get('to_lat')
		to_long = request.data.get('to_long')
		car_cancellation = request.data.get('car_cancellation')

		try:
			Booking.objects.create(id=id, user_id=user_id, vehicle_model_id=vehicle_model_id, package_id=package_id,
				travel_type_id=travel_type_id, from_area_id=from_area_id, to_area_id=to_area_id, from_city_id=from_city_id,
				to_city_id=to_city_id, from_date=from_date, to_date=to_date, online_booking=online_booking, mobile_site_booking=mobile_site_booking,
				booking_created=booking_created, from_lat=from_lat, from_long=from_long, to_lat=to_lat, to_long=to_long, car_cancellation=car_cancellation)
			return Response({"status": status.HTTP_201_CREATED})
		except Exception as e:
			return Response({"status": status.HTTP_400_BAD_REQUEST, "message":str(e)})
	

class QueryView(APIView):
	permission_classes = (AllowAny,)

	def get(self, request, format=None):
		attribute_list = [field.name for field in Booking._meta.fields]
		kwargs, start = {}, 0
		for q in request.GET:
			if q in attribute_list:
				kwargs[q] = request.GET.get(q)

		if request.GET.get('page'):
			start = int(request.GET.get('page'))*100
		try:
			results = Booking.objects.filter(**kwargs).order_by('id')[start:start+100]
			serialized_results = BookingSerializer(results, many=True)
			return Response({"status": status.HTTP_200_OK, "total_results": results.count(), "page": start/100, "results": serialized_results.data})
		except Exception as e:
			return Response({"status": status.HTTP_204_NO_CONTENT, "message": str(e)})