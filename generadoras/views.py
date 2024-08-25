# class GetOfGenerations(APIView):
#     # def get(self, request):
#         def get(self, request):
#         try: 
#             r = requests.get('https://sitr.cnd.com.pa/m/pub/data/gen.json?1724278750486')
#             books = r.json()
#             return Response(books, status= 200)
            
#         except Exception as e: 
#             return Response({ 'message': e })


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
import requests


class GetOfGenerations(APIView):
    def post(self, request):
        try: 

            id = request.data.get('id')
            r = requests.get(f'https://sitr.cnd.com.pa/m/pub/data/gen.json?{id}')
            generador = r.json()
            return Response(generador, status= 200)
            
        except Exception as e: 
            return Response({ 'message': e })