from django.shortcuts import render
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder
import random
import time
import json
from django.urls import resolve

# Create your views here.

def getToken(request):
    appId = '7fcd66f8061649e4b70c14a183de6d48'
    appCertificate = '04f5f3390a504c86a9fe524ef13f073d'
    channelName = request.GET.get('channel')
    uid = random.randint(1, 300)

    expirationTime = 3600*24
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirationTime
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token':token, 'uid':uid}, safe=False)

def lobby(request):
    return render(request, 'base/lobby.html')
    
def room(request):
    return render(request, 'base/room.html')
