from django.db import models # noqa


class Question(models.Model):
    question_text = models.CharField(max_length=225)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# python manage.py makemigrations
# python manage.py migrate
# python manage.py startapp apps
