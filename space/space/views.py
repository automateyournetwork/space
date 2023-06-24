import os
from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import space_api_to_get,space_api_output

def space_iss_API(request):
    refreshme = space_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = space_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = space_api_to_get(space_api = "http://api.open-notify.org/iss-now.json")
    savecommand.save()    
    os.system('python3 spaceAPI.py')
    latest_answer = space_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/space_answer.html', latest_proposed_dict)

def space_people_in_space_API(request):
    refreshme = space_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = space_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = space_api_to_get(space_api = "http://api.open-notify.org/astros.json")
    savecommand.save()    
    os.system('python3 spaceAPI.py')
    latest_answer = space_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/space_answer.html', latest_proposed_dict)

def space_weather_on_mars_API(request):
    refreshme = space_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = space_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = space_api_to_get(space_api = "https://api.nasa.gov/insight_weather/?api_key={ self.token }&feedtype=json&ver=1.0")
    savecommand.save()    
    os.system('python3 spaceAPI.py')
    latest_answer = space_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/space_answer.html', latest_proposed_dict)

def space_pic_of_the_day_API(request):
    refreshme = space_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = space_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = space_api_to_get(space_api = "https://api.nasa.gov/planetary/apod?api_key={ self.token }")
    savecommand.save()    
    os.system('python3 spaceAPI.py')
    latest_answer = space_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/space_answer.html', latest_proposed_dict)

def space_asteroids_API(request):
    refreshme = space_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = space_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = space_api_to_get(space_api = "https://api.nasa.gov/neo/rest/v1/feed?api_key={ self.token }")
    savecommand.save()    
    os.system('python3 spaceAPI.py')
    latest_answer = space_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/space_answer.html', latest_proposed_dict)

def space_coronal_API(request):
    refreshme = space_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = space_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = space_api_to_get(space_api = "https://api.nasa.gov/DONKI/CME?api_key={ self.token }")
    savecommand.save()    
    os.system('python3 spaceAPI.py')
    latest_answer = space_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/space_answer.html', latest_proposed_dict)

def space_geomagnetic_API(request):
    refreshme = space_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = space_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = space_api_to_get(space_api = "https://api.nasa.gov/DONKI/GST?startDate=2021-01-01&api_key={ self.token }")
    savecommand.save()    
    os.system('python3 spaceAPI.py')
    latest_answer = space_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/space_answer.html', latest_proposed_dict)

def space_interplanetary_shock_API(request):
    refreshme = space_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = space_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = space_api_to_get(space_api = "https://api.nasa.gov/DONKI/IPS?api_key={ self.token }")
    savecommand.save()    
    os.system('python3 spaceAPI.py')
    latest_answer = space_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/space_answer.html', latest_proposed_dict)

def space_solar_flare_API(request):
    refreshme = space_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = space_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = space_api_to_get(space_api = "https://api.nasa.gov/DONKI/FLR?api_key={ self.token }")
    savecommand.save()    
    os.system('python3 spaceAPI.py')
    latest_answer = space_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/space_answer.html', latest_proposed_dict)

def space_solar_particle_API(request):
    refreshme = space_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = space_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = space_api_to_get(space_api = "https://api.nasa.gov/DONKI/SEP?startDate=2023-01-01&api_key={ self.token }")
    savecommand.save()    
    os.system('python3 spaceAPI.py')
    latest_answer = space_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/space_answer.html', latest_proposed_dict)

def space_radiation_belt_API(request):
    refreshme = space_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = space_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = space_api_to_get(space_api = "https://api.nasa.gov/DONKI/RBE?api_key={ self.token }")
    savecommand.save()    
    os.system('python3 spaceAPI.py')
    latest_answer = space_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/space_answer.html', latest_proposed_dict)

def space_high_speed_streams_API(request):
    refreshme = space_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = space_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = space_api_to_get(space_api = "https://api.nasa.gov/DONKI/HSS?api_key={ self.token }")
    savecommand.save()    
    os.system('python3 spaceAPI.py')
    latest_answer = space_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/space_answer.html', latest_proposed_dict)

def space_wsa_enlil_API(request):
    refreshme = space_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = space_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = space_api_to_get(space_api = "https://api.nasa.gov/DONKI/WSAEnlilSimulations?api_key={ self.token }")
    savecommand.save()    
    os.system('python3 spaceAPI.py')
    latest_answer = space_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/space_answer.html', latest_proposed_dict)

def space_nasa_notifications_API(request):
    refreshme = space_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = space_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = space_api_to_get(space_api = "https://api.nasa.gov/DONKI/notifications?api_key={ self.token }")
    savecommand.save()    
    os.system('python3 spaceAPI.py')
    latest_answer = space_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/space_answer.html', latest_proposed_dict)

def space_natural_events_API(request):
    refreshme = space_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = space_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = space_api_to_get(space_api = "https://eonet.gsfc.nasa.gov/api/v2.1/events")
    savecommand.save()    
    os.system('python3 spaceAPI.py')
    latest_answer = space_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/space_answer.html', latest_proposed_dict)

def space_earth_poly_image_API(request):
    refreshme = space_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = space_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = space_api_to_get(space_api = "https://api.nasa.gov/EPIC/api/natural/date?api_key={ self.token }")
    savecommand.save()    
    os.system('python3 spaceAPI.py')
    latest_answer = space_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/space_answer.html', latest_proposed_dict)

def space_known_bodies_API(request):
    refreshme = space_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = space_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = space_api_to_get(space_api = "https://api.le-systeme-solaire.net/rest/knowncount/")
    savecommand.save()    
    os.system('python3 spaceAPI.py')
    latest_answer = space_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/space_answer.html', latest_proposed_dict)

def space_planets_API(request):
    refreshme = space_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = space_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = space_api_to_get(space_api = "https://api.le-systeme-solaire.net/rest/bodies?filter[]=isPlanet,eq,true")
    savecommand.save()    
    os.system('python3 spaceAPI.py')
    latest_answer = space_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/space_answer.html', latest_proposed_dict)