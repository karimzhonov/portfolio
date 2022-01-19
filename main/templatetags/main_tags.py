from django import template

from ..models import *


register = template.Library()


@register.simple_tag
def settings():
    return Settings.objects.get(pk=1)


@register.simple_tag()
def social_links():
    return SocialLink.objects.all()
