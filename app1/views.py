from django.shortcuts import render

# Create your views here.
def first(request):
    d={'name':'gowthami','number':'6578676'}
    return render(request,'first.html',context=d)


    