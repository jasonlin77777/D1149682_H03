from django.http import HttpResponse
from django.template import loader
from .models import Member
from .models import Court

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def court_members(request):
  mymembers = Court.objects.all().values()
  template = loader.get_template('all_courts.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def court_details(request, id):
  mymember = Court.objects.get(id=id)
  template = loader.get_template('details_court.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))