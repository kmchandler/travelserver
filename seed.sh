#!/bin/bash
rm -rf travelserverapi/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations travelserverapi
python3 manage.py migrate travelserverapi
python3 manage.py loaddata users
python3 manage.py loaddata trips
python3 manage.py loaddata itinerary_items
python3 manage.py loaddata events
python3 manage.py loaddata flights
python3 manage.py loaddata lodgings
python3 manage.py loaddata rental_cars
python3 manage.py loaddata trains
python3 manage.py loaddata notes
python3 manage.py loaddata share_requests
python3 manage.py loaddata shared_trips
