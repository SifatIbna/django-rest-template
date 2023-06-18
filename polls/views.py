from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from django.http import Http404
from django.forms.models import model_to_dict

from .models import Poll
# Create your views here.

def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]

    data = {
        "results":list(polls.values("question","created_by__username","pub_date"))
    }
    return JsonResponse(data)

def polls_detail(request,pk):
    print(pk)
    try:
        poll = Poll.objects.get(pk=pk)
    except Poll.DoesNotExist:
        raise Http404("Id doesn't exist")
    data = {
        "results":{
            "question":poll.question,
            "pub_date":poll.pub_date
        }
    }

    return JsonResponse(data)

