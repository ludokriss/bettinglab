from django.shortcuts import render
import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from betcompiler import main
# Create your views here.

@api_view(['GET'])
def match_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        if request.GET.get('competition'):
            obj=main.oddsmatrix()
            obj.compileOdds(1)
            return Response(json.dumps(obj.maxodds.to_dict()))
        return Response(None)
