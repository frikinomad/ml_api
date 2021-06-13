from django.shortcuts import render, redirect
from dotenv import load_dotenv
from rest_framework.views import APIView
import requests
from rest_framework import status
from rest_framework.response import Response
import os
import base64
from django.http import JsonResponse
import datetime

load_dotenv()
client_id = os.getenv('Client_Id')
client_secret = os.getenv('Client_Secret')
client_creds = f"{client_id}:{client_secret}"
client_cred_base64 = base64.b64encode(client_creds.encode())

def Authspotify(request):
    token_endpoint = requests.post('https://accounts.spotify.com/api/token', data={'grant_type': 'client_credentials'}, headers={'Authorization': f'Basic {client_cred_base64.decode()}'})
    token_json = token_endpoint.json()


    status_code = token_endpoint.status_code in range(200, 299)
    print(status_code)
    if status_code:
        now = datetime.datetime.now()
        access_token = token_json['access_token']
        token_type = token_json['token_type']
        expires_in = token_json['expires_in']
        expires = now + datetime.timedelta(seconds=expires_in)
        did_expire = expires < now
    print(type(access_token))
    audio_feature_endpoint = requests.get('https://api.spotify.com/v1/audio-features/61APOtq25SCMuK0V5w2Kgp', headers = {"Authorization": f"Bearer {access_token}"})
    print(audio_feature_endpoint.text)
    return JsonResponse(token_json)
