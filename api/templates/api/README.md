# LocaleTask

<h3>1.) To get bookings :</h3>

  GET request : http://35.232.78.35:8080/bookings/

        - It will return first 100 results ordered based on id field.

        GET request : http://35.232.78.35:8080/bookings/?page=1

        - Next 100 results

        GET request : http://35.232.78.35:8080/bookings/?page=2
        - So on...
        
<h3>2.) To save data in PostgreSQL:</h3>
  POST request : http://35.232.78.35:8080/bookings/
  
        Headers : {
            "Content-Type": "application/json"
        }
        
        Body : {
            "id": 192631,
            "user_id": 33406,
            "vehicle_model_id": 12,
            "package_id": null,
            "travel_type_id": "2",
            "from_area_id": "585",
            "to_area_id": "168",
            "from_city_id": null,
            "to_city_id": null,
            "from_date": "2013-01-02T16:00:00Z",
            "to_date": null,
            "online_booking": 0,
            "mobile_site_booking": 0,
            "booking_created": "2013-01-02T14:24:00Z",
            "from_lat": "12.97677000",
            "from_long": "77.57270000",
            "to_lat": "12.99313000",
            "to_long": "77.59828000",
            "car_cancellation": 1
        }
        
<h3>3.) To Query:</h3><br>
        GET request : http://35.232.78.35:8080/query/

        - Pass any number of parameters on which you want to query.
        Ex.

        a.] http://35.232.78.35:8080/query/?vehicle_model_id=28&user_id=22177&page=2
            - It will return all records which has vehicle_model_id=28 and user_id=22177
            
        b.] http://35.232.78.35:8080/query/?vehicle_model_id=28&user_id=22177&car_cancellation=1
 
