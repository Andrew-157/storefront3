from django.core.cache import cache
from django.shortcuts import render
from rest_framework.views import APIView
import logging
import requests

logger = logging.getLogger(__name__)


class HelloView(APIView):
    def get(self, request):
        logger.info('Calling httpbin...')
        response = requests.get('https://httpbin.org/delay/2')
        logger.info('Received the Response')
        data = response.json()
        return render(request, 'hello.html', {'name': data})
