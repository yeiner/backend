from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404

from .models import Track

def track_view(request, title):
	track = get_object_or_404(Track, title=title)	
	bio = track.artist.biography
	return render(request,'track.html',{'track':track,'bio':bio}) 

