from typing import Any, Optional
from django.core.management.base import BaseCommand
from django.utils import timezone
from api.serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help='Display All Users form database'
    def handle(self,*args,**kwargs):
        user = User.objects.all()
        serializer = UserSerializer(data = user,many=True)
        serializer.is_valid()
        self.stdout.write("User %s" % serializer.data)
    