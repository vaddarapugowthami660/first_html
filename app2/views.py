from django.shortcuts import render

# Create your views here.
def second(request):
    d={'name':'chinni','number':'6578676'}
    return render(request,'second.html',context=d)

