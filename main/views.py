from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from .models import *
from .rest import ContactRest


def index(request):
    conf = Settings.objects.get(pk=1)
    conf.views += 1
    conf.save()

    context = {
        'conf': Settings.objects.get(pk=1),
        'about': AboutMe.objects.get(pk=1),
        'more': AboutMeMore.objects.all(),
        'exp_types': ExperienceType.objects.all(),
        'edu': Experience.objects.filter(experience_id=1),
        'course': Experience.objects.filter(experience_id=2),
        'work': Experience.objects.filter(experience_id=3),
        'skill_types': SkillType.objects.all(),
        'project_types': ProjectType.objects.all(),
        'projects': Project.objects.all(),
        'social': SocialLink.objects.all(),
    }
    return render(request, 'main/index.html', context)


class ContactRestView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactRest


def hand404(request, exception):
    return render(request, template_name='main/err404.html', status=404)

