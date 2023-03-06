from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from main_app.models import Record


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
    
    
def record_page(request, album_name, record_id):
    this_record = Record.objects.get(id=record_id)
    
    context = {
        'this_record': this_record,
    }
    
    return render(
        request=request,
        template_name='main_app/record_page.html',
        context=context
    )