from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Contact


class ContactRest(HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']


