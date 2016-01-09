from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ticket(models.Model):
    STATUSES = (
        (0, 'open'),
        (1, 'closed'),
    )
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=200)
    status = models.IntegerField(max_length=1, choices=STATUSES)
    author = models.ForeignKey(User, related_name='author')
    assignee = models.ForeignKey(User, related_name='assignee')
    created_date = models.DateTimeField(auto_now_add=True)
