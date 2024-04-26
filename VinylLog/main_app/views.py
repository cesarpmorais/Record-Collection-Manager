from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from main_app.models import Record, Song


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
    songs = Song.objects.filter(album__id=this_record.album.id)
    
    context = {
        'this_record': this_record,
        'songs': songs,
    }
    
    return render(
        request=request,
        template_name='main_app/record_page.html',
        context=context
    )