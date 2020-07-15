# Created by Krishnarjun Singh
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def analyzer(request):
    # Main POST comand
    pctect = request.POST.get('text', 'default')

    #Checkboxes
    removepunc = request.POST.get('removepunction', 'off')
    countcharacter = request.POST.get('countcar', 'off')
    capitalization = request.POST.get('capitali', 'off')

    #Remove Punctioan
    if removepunc == 'on':
        punctioanList = '",?/!@#$%^&*()-_+=-*/:;}{[]'
        analyzed = ""
        for char in pctect:
            if char not in punctioanList:
                analyzed += char
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        return render(request, "analyzedIndex.html", params)

    # Count Char
    elif countcharacter == 'on':
        count = 0
        for char in pctect:
            count += 1
        params = {'purpose': 'Count Char', 'analyzed_text': count}
        return render(request, "analyzedIndex.html", params)

    #Capitalization
    elif capitalization == 'on':
        analyzedd = pctect.upper()
        params = {'purpose': 'Capitalizations..', 'analyzed_text': analyzedd}
        return render(request, "analyzedIndex.html", params)

    # Handle error
    else:
        params = {'analyzed_text': pctect}
        return render(request, "analyzedIndex.html", params)
