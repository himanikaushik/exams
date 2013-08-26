# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import Http404
from core.models import Question


def home(request):
    try:
        if request.method == 'GET':
            qs = Question.objects.all()
            return render_to_response('home.html', {'qs':qs}, context_instance = RequestContext(request))
    except:
        raise Http404
        
