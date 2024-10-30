from django.shortcuts import render
import requests
import requests.exceptions
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 


class WeatherAPIView(APIView):
    def get(self,request,location):
        api_key = "f909ae1b4b1035d31ed34415eef402341"
        url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}'
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            weather_data = response.json()
            return Response(weather_data,status = status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
                return Response({"error":str(e)},status = status.HTTP_400_BAD_REQUEST)
