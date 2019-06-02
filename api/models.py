from django.db import models

# Create your models here.

class Booking(models.Model):
	id = models.IntegerField(primary_key=True, db_index=True)
	user_id = models.IntegerField(db_index=True,null=True, blank=True)
	vehicle_model_id = models.IntegerField(null=True, blank=True)
	package_id = models.CharField(max_length=20, blank=True, null=True)
	travel_type_id = models.CharField(max_length=20, blank=True, null=True)
	from_area_id = models.CharField(max_length=20, blank=True, null=True)
	to_area_id = models.CharField(max_length=20, blank=True, null=True)
	from_city_id = models.CharField(max_length=20, blank=True, null=True)
	to_city_id = models.CharField(max_length=20, blank=True, null=True)
	from_date = models.DateTimeField(db_index=True, null=True, blank=True)
	to_date = models.DateTimeField(db_index=True, null=True, blank=True)
	online_booking = models.IntegerField(null=True, blank=True)
	mobile_site_booking = models.IntegerField(null=True, blank=True)
	booking_created = models.DateTimeField(db_index=True, null=True, blank=True)
	from_lat = models.DecimalField(max_digits=20, decimal_places=8, null=True, blank=True)
	from_long = models.DecimalField(max_digits=20, decimal_places=8, null=True, blank=True)
	to_lat = models.DecimalField(max_digits=20, decimal_places=8, null=True, blank=True)
	to_long = models.DecimalField(max_digits=20, decimal_places=8, null=True, blank=True)
	car_cancellation = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return str(user_id) + " ===> " + str(from_date) + " -- " + str(to_date)

