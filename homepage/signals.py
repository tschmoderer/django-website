from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from .models import Profile, Homepage

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        content_type = ContentType.objects.get_for_model(Profile)
        permission = Permission.objects.create(
            codename='can_edit_profile_{0}'.format(instance.id), 
            name='Edit profile of {0}'.format(instance.username), 
            content_type=content_type            
            )
        instance.user_permissions.add(permission)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=User)
def create_user_homepage(sender, instance, created, **kwargs):
    if created:
        Homepage.objects.create(user=instance)
        content_type = ContentType.objects.get_for_model(Homepage)
        permission = Permission.objects.create(
            codename='can_edit_homepage_{0}'.format(instance.id), 
            name='Edit homepage of {0}'.format(instance.username), 
            content_type=content_type            
            )
        instance.user_permissions.add(permission)

@receiver(post_save, sender=User)
def save_homepage(sender, instance, **kwargs):
    instance.homepage.save()

