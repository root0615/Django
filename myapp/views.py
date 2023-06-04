from django.shortcuts import render
from myapp.models import Loanlist
from django.http.response import HttpResponse
import json

# Create your views here.
def mainFunc(request):
    return render(request, "main.html")

def listFunc(request):
    return render(request, "list.html")

def testFunc(request):
    if request.method == 'GET':
        data = Loanlist.objects.all()
        # print(data)
        ldata = []
        for i in data:
            dic = {'no':i.l_book_no, 'm_id':i.l_m_id}
            ldata.append(dic)
        
        return HttpResponse(json.dumps(ldata), content_type = "application/json")