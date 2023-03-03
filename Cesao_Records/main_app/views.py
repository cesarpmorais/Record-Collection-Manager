from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from main_app.models import Record

# Create your views here.
def main_page(request):
    my_records = Record.objects.all().order_by('album__name')
    
    context = {
        'my_records': my_records,
    }
    
    return render(
        request=request,
        template_name='main_app/main_page.html',
        context=context
    )