from django.db import models
 
# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField(max_length=100, primary_key=True)
    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    # relationship
    topic_name = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField()
    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date = models.DateField()
    author = models.CharField(max_length=100)
    email = models.EmailField(default='prasanth@gamil.com')
    empno = models.IntegerField()
    
    
    def __str__(self):
        return self.author

'''
# Shell retriving commands
# get all objects
# syntax--> models.objects.all()

 from app.models import *
>>> Topic.objects.all()
<QuerySet [<Topic: Naruto>, <Topic: Attack on Titans>, <Topic: Cricket>, <Topic: KingOfKotha>, <Topic: >]>
>>> Webpage.objects.all()
<QuerySet [<Webpage: Itachi>, <Webpage: Eren>]>
>>> AccessRecord.objects.all()
<QuerySet [<AccessRecord: sasuke>, <AccessRecord: Mikasa>]>
>>>

# get secpific rows objects
# syntax--> models.objects.all()

ONE ROW:(Topic)

>>> from app.models import *
>>> Topic.objects.get(topic_name)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'topic_name' is not defined
>>> Topic.objects.get(topic_name='Naruto')
<Topic: Naruto>
>>> Topic.objects.filter(topic_name='Naruto',)
<QuerySet [<Topic: Naruto>]>
>>>


ONE ROW:(Webpage)

>>> Webpage.objects.get(name='Eren')
<Webpage: Eren>
>>> Webpage.objects.filter(name='Eren')
<QuerySet [<Webpage: Eren>]>


ONE ROW:(accessRecords)

<AccessRecord: Mikasa>
>>> AccessRecord.objects.filter(author='Mikasa')
<QuerySet [<AccessRecord: Mikasa>]>


MORETHAN ONE ROWS:(Topic)






'''