"""space URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.urls import path, include
from django.http import FileResponse
from django.conf import settings
from django.contrib import admin
from django.views.generic import View

from . import views

class WellKnownView(View):
    def get(self, request, file_path):
        file = os.path.join(settings.BASE_DIR, '.well-known', file_path)
        return FileResponse(open(file, 'rb'))

class ACME(View):
    def get(self, request, file_path):
        file = os.path.join(settings.BASE_DIR, '.well-known/acme-challenge', file_path)
        return FileResponse(open(file, 'rb'))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Interational_Space_Station_Location/', views.space_iss_API),
    path('People_In_Space/', views.space_people_in_space_API),
    path('Weather_On_Mars/', views.space_weather_on_mars_API),
    path('Astronomy_Picture_Of_The_Day/', views.space_pic_of_the_day_API),
    path('Asteroids_Near_Earth_Objects/', views.space_asteroids_API),
    path('Coronal_Mass_Ejections/', views.space_coronal_API),
    path('Geomagnetic_Storm/', views.space_geomagnetic_API),
    path('Interplanetary_Shock/', views.space_interplanetary_shock_API),
    path('Solar_Flare/', views.space_solar_flare_API),
    path('Solar_Energetic_Particle/', views.space_solar_particle_API),
    path('Radiation_Belt_Enhancement/', views.space_radiation_belt_API),
    path('High_Speed_Streams/', views.space_high_speed_streams_API),
    path('WSA_Enlil_Solar_Wind_Prediction/', views.space_wsa_enlil_API),
    path('NASA_Notifications/', views.space_nasa_notifications_API),
    path('Natural_Events/', views.space_natural_events_API),
    path('Earth_Polychromatic_Imaging_Camera/', views.space_earth_poly_image_API),
    path('Known_Celestial_Body_Count/', views.space_known_bodies_API),
    path('Planets/', views.space_planets_API),
    path('Rovers/', views.space_rovers_API),
    path('.well-known/<path:file_path>', WellKnownView.as_view()),
    path('.well-known/acme-challenge/<path:file_path>', ACME.as_view()),    
]