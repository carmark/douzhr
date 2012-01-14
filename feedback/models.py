from django.db import models

# Create your models here.

class Feedback (models.Model):
    name = models.CharField(max_length=10)
    subject = models.CharField(max_length=30)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    qq_msn = models.CharField(max_length=20)
    content = models.TextField()
    submit_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-id', '-submit_date',)
    
    def __unicode__(self):
        return self.name


