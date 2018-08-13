from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from core.models import Location , Skills , Course,CandidateProfile,Profile
from core.forms import SignUpForm
from django.http import HttpResponse
import json
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import datetime

@login_required
def home(request):
    c = Course.objects.all()
    l = Location.objects.all()
    s = Skills.objects.all()
    diction = {'location': l , 'skill': s , 'course' : c}
    return render(request,'home.html' , diction )



@require_http_methods(["POST"])
@login_required
@csrf_exempt
def check_profile(request):
    data = dict(request.POST.iterlists())
    experience = {0:[0,1] , 1:[2,3,4] , 2:[4,5,6] , 3:[6,7,8]}
    location = map(int , data.get('locat[]', []))
    skills = map(int , data.get('ski[]' , []))
    expe = map(int , data.get('expe[]' , []))
    try:
        expe = experience.get(expe[0] , [])
    except:
	expe = []
    candidate = CandidateProfile.objects.filter(Q(current_location_id__in = location) & 
							Q(skills__in = skills) & 
							Q(work_ex__in = expe)
						)
    return JsonResponse(serializers.serialize('json', candidate), safe=False)



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



@require_http_methods(["POST"])
@login_required
@csrf_exempt
def download_profile(request):
    date = datetime.datetime.now()
    date = date.date()
    data = dict(request.POST.iterlists())
    serial_no = data.get('serial')[0]
    profile = Profile.objects.get(id = request.user.id)
    if profile.last_profile_download_date == date:
        status = True
        msg = "YOU CAN'T DOWNLOAD MORE THAN ON PROFILE A DAY"
    else:
        status = True
        msg = "YOUR FILE IS DOWNLOADING"
        profile.last_profile_download_date = date
	profile.save()
    data = {"status" : status , "message" : msg}
    return HttpResponse(json.dumps(data))
