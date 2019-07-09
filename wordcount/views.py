from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def count(request):
    fulltext=request.GET['fulltext']
    text=fulltext.split()
    worddict={}
    for word in text:
        if word in worddict:
            worddict[word]+=1
        else:
            worddict[word]=1
    sort=sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(text),'worddict':sort})