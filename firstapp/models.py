from django.db import models

# Create your models here.
class newclass(models.Model):
    new_num = models.IntegerField()
    
class newclass1(models.Model):
    # participate_class=participate_class,
    # user=
    # name=name,
    # phone_num=phone_num

    # participate_class = models.ForeignKey(
    # AiClass, on_delete=models.CASCADE, related_name='student')
    # user 와 1대1매칭
    # user = models.OneToOneField(
    # User, on_delete=models.CASCADE, related_name='student')
    name = models.CharField(max_length=10)
    phone_num = models.CharField(max_length=10)
