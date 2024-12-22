# Made by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'harry'}
    return render(request,'index.html',params)

def analyze(request):
    # Getting the text
    djtext = request.POST.get('text','default')
    # checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newLineRemover = request.POST.get('newLineRemover','off')
    extraSpaceRemover = request.POST.get('extraSpaceRemover','off')
    # charCount = request.GET.get('charCount','off')

    # checking if on
    analyzed = djtext
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        dummy = ""
        for char in djtext:
            if char not in punctuations:
                dummy+=char
        analyzed = dummy

    if fullcaps == "on":
        analyzed = analyzed.upper()

    if newLineRemover == "on":
        analyzed = " ".join(analyzed.splitlines())

    if extraSpaceRemover == "on":
        dummy = ""
        for index, char in enumerate(analyzed):
            if not(index<len(analyzed)-1 and analyzed[index]==" " and analyzed[index+1]==" "):
                dummy+=char
        analyzed = dummy

    # elif charCount == "on":
    #     count = len(djtext)
    #     params = {'purpose': 'Removed New Line Characters', 'analyzedText': count}
    #     return render(request, 'analyze.html', params)

    params = {'purpose': 'Final Analysis', 'analyzedText': analyzed}
    # Analyze the text
    return render(request, 'analyze.html', params)
