from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """Pagina principal do learning_log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    topic = Topic.objects.order_by('data_added')
    context = {'topics': topic}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-data_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)