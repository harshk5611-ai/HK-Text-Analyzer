# CBME
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyzed(request):
    removepunc = request.POST.get('removepunc', 'off')
    capfirst = request.POST.get('capfirst', 'off')
    counter = request.POST.get('counter', 'off')
    remnewlines = request.POST.get('remnewlines', 'off')
    remextraspc = request.POST.get('remextraspc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    djtext = request.POST.get('text', 'default')
    djlen = len(djtext)

    puncs = '''\!~`@#$%^&*()_+-={}[]:"|;'<>?,./'''

    analyzed = ''

    if removepunc == "on":
        analyzed = ""
        for char in djtext:
            if char not in puncs:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed



    if capfirst=="on":
        analyzed=djtext.title()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed



    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed


        
    if remnewlines=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed


        
    if (remextraspc == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed



    beflength = ''
    aftlength = ''
    if counter== 'on':
        beflength = f"Number Of Characters before Analyzation : '{djlen}' Characters."
        aftlength = f"Number Of Characters in Analyzed text : '{len(djtext)}' Characters."

        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed, "beforelength": beflength, "afterlength": aftlength}
    else:
        beflength = ''
        aftlength = ''
    
 

    return render(request, 'analyzed.html', params)


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')