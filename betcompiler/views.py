from django.shortcuts import render
import json
import pandas as pd 

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
            #obj=main.oddsmatrix()
            #obj.compileOdds(1)
            a='{"name":{"0":"Bod\u00f8\/Glimt - Molde","1":"Brann - Lillestr\u00f8m","2":"Haugesund - Bodo\\\/Glimt","3":"Haugesund - Bod\u00f8\/Glimt","4":"Kristiansund - Troms\u00f8","5":"Lillestr\u00f8m - Stab\\u00e6k","6":"Lillestr\u00f8m - Stab\u00e6k","7":"Lillestr\u00f8m - Troms\u00f8","8":"Lillestr\u00f8m - Troms\u00f8 IL","9":"Molde - Rosenborg","10":"Odd - Ranheim","11":"Ranheim - Kristiansund","12":"Rosenborg - Sandefjord","13":"Sandefjord - Odd","14":"Sarpsborg - Str\u00f8msgodset IF","15":"Sarpsborg 08 - Str\u00f8msgodset","16":"Stab\u00e6k - V\u00e5lerenga","17":"Start - Sarpsborg 08","18":"Str\u00f8msgodset - Haugesund","19":"Troms\u00f8 - Brann","20":"V\\u00e5lerenga - Start","21":"V\u00e5lerenga - Start"},"home":{"0":3.0,"1":1.6,"2":2.05,"3":2.06,"4":2.25,"5":2.0,"6":2.0,"7":2.0,"8":1.83,"9":2.43,"10":1.95,"11":2.05,"12":1.22,"13":2.9,"14":2.37,"15":2.35,"16":2.45,"17":2.45,"18":2.0,"19":2.65,"20":1.615,"21":1.63},"draw":{"0":3.5,"1":3.75,"2":3.5,"3":3.5,"4":3.45,"5":3.5,"6":3.57,"7":4.05,"8":3.88,"9":3.5,"10":3.5,"11":3.5,"12":6.5,"13":3.35,"14":3.42,"15":3.4,"16":3.35,"17":3.4,"18":3.4,"19":3.25,"20":3.9,"21":3.92},"away":{"0":2.2,"1":5.5,"2":3.4,"3":3.65,"4":2.95,"5":3.5,"6":3.75,"7":4.3,"8":4.05,"9":2.75,"10":3.65,"11":3.5,"12":10.0,"13":2.375,"14":2.82,"15":3.0,"16":2.75,"17":2.7,"18":3.65,"19":2.55,"20":5.1,"21":5.5},"safe":{"0":0.0685483871,"1":0.0684544813,"2":0.063351891,"3":0.0431755381,"4":0.0682789136,"5":0.0666666667,"6":0.0446882526,"7":-0.0209585226,"8":0.0486099669,"9":0.0573803526,"10":0.067605502,"11":0.0559210526,"12":0.0684834958,"13":0.0604926961,"14":0.0645012524,"15":0.0503169572,"16":0.0656887095,"17":0.0677305699,"18":0.0637495285,"19":0.0716738878,"20":0.0668888889,"21":0.0479972694},"provider1":{"0":["Unibet"],"1":["Unibet"],"2":[],"3":["Expekt"],"4":["Unibet"],"5":["Expekt"],"6":["Expekt"],"7":["NT"],"8":["Expekt"],"9":["Olybet","Expekt"],"10":["Unibet"],"11":["Unibet"],"12":["Unibet"],"13":["Olybet"],"14":["Expekt"],"15":["Olybet"],"16":["Unibet"],"17":["Unibet"],"18":["Unibet"],"19":["Unibet"],"20":[],"21":["Expekt"]},"providerX":{"0":["Unibet"],"1":["Unibet"],"2":[],"3":["Unibet"],"4":["Unibet"],"5":[],"6":["Expekt"],"7":["Unibet"],"8":["Expekt"],"9":["Unibet"],"10":["Unibet"],"11":["Expekt"],"12":["Unibet"],"13":["Unibet"],"14":["Expekt"],"15":["Olybet"],"16":["Unibet"],"17":["Unibet"],"18":["Unibet"],"19":["Unibet"],"20":[],"21":["Expekt"]},"provider2":{"0":["Unibet"],"1":["Unibet"],"2":[],"3":["Unibet"],"4":["Unibet"],"5":[],"6":["Unibet"],"7":["Coolbet"],"8":["Expekt"],"9":["Olybet"],"10":["Unibet"],"11":["Unibet","Olybet"],"12":["Unibet"],"13":["Olybet"],"14":["Expekt"],"15":["Unibet"],"16":["Unibet"],"17":["Unibet"],"18":["Unibet"],"19":["Unibet"],"20":[],"21":["Unibet"]}}'
            df=pd.read_json(a)
            return Response(df.to_dict(orient='records'))
        return Response(None)
