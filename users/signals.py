from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.db import models
from .models import Profile
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    print('Profile Created')
    if created:
        user = instance
        profile = Profile.objects.create(
           user =  user,
           username = user.username,
           email = user.email,
           name = user.first_name
        )
        subject = 'Welcome to DevSearch'
        message = 'We are glad you are here!'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )
    # print('Profile and User Objects Created')
    # print('Instace:', instance)
    # print("Created:", created)

def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()




def delteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    # instance.user.delete()
    print("Deleting a User.....")


# post_save is getting called whenever we create a new profile or edit an existing profile
post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
# when a User is profile is deleted User should also be deleted
post_delete.connect(delteUser, sender=Profile)

# TO-DO
# User->Profile
# for deleting
# Profile is Deleted User should be deleted