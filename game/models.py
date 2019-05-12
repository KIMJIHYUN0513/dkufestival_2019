from django.db import models

# Create your models here.


class Record(models.Model):
    name = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    body = models.TextField(max_length=20)

    def __str__(self):  # method overriding
        return self.name

    def name_summary(self):
        return self.name[:10]

    def body_summary(self):
        return self.body[:20]
