from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import Story
import random

sentences = []
editing = False
prompt = ""

# Create your views here.
def home(request):
    return render(request, 'webapp/home.html')

def write(request):
    global editing
    global prompt

    if prompt == "":
        prompt = generatePrompt()

    suggestion = ""

    if request.POST:
        if request.POST.get("text"):
            newSentence = request.POST["text"]
            sentences.append(newSentence)

            if not editing:
                suggestion = generateSuggestion(newSentence)
            editing = not editing
    elif request.GET.get("new"):
        sentences.clear()
        editing = False
        prompt = generatePrompt()

    return render(request, 'webapp/write.html',
                  context={"prompt": prompt, "sentences": sentences, "suggestion": suggestion})

def about(request):
    return render(request, 'webapp/about.html')

def generatePrompt():
    topics = ["a hotheaded penguin", "a wizened chihuahua", "a murderous toucan",
              "an exponentially multiplying swarm of beagles"]
    curTopic = topics[random.randrange(0, len(topics))]
    return "Write about " + curTopic

def generateSuggestion(newSentence):
    return "Placeholder suggestion from WriterBot"
