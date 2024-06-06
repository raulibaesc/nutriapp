from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class User(AbstractUser):
    telefono = models.IntegerField(null=True,blank=True)

    is_patient =models.BooleanField(default=False)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='patient',null=True,blank=True)
    peso = models.IntegerField(null=True,blank=True)
    altura = models.IntegerField(null=True,blank=True)
    fecha_nacimiento = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.user.username
@receiver(post_save,sender=User)
def create_patient(sender, instance, created, **kwargs):
    if created and instance.is_patient ==True:
        Patient.objects.create(user=instance)
        instance.patient.save()
    else:
        return
#@receiver(post_save,sender=User)
#def save_user_patient(sender,instance,**kwargs):
    

#post_save.connect(create_patient, sender=User)
#post_save.connect(save_user_patient,sender=User)
