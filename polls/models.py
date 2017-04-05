from django.db import models
#from django.contrib.admin.models import User

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class todo(models.Model):
    text=models.CharField(max_length=100)
    # user=models.ForeignKey(User)
    def __str__(self):
        return self.text