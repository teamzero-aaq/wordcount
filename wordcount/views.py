from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    wordarray = {}
    for word in wordlist:
        if word in wordarray:
            wordarray[word] += 1
        else:
            wordarray[word] = 1
    sortedword = sorted(wordarray.items(), key=operator.itemgetter(1), reverse = True )
    return render(request,'count.html',{'fulltext':fulltext , 'count':len(wordlist), 'sortedword':sortedword})