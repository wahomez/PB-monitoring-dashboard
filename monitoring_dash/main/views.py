from django.shortcuts import render, HttpResponse
from .models import *
from .utils import *

# Create your views here.
def dashboard(request):
    qs = Test.objects.all()
    x = [x.Date for x in qs]
    y = [y.Close for y in qs]
    chart = get_plot(x,y)

    return render(request, 'main/dashboard.html', {'chart': chart})