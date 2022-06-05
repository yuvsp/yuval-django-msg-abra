from django.db import models


class Msg(models.Model):
    # sender = models.CharField(max_length=20)
    receiver = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    unread = models.BooleanField(default=1)
    objects = models.Manager()
    creator = models.ForeignKey('auth.User', related_name='msgs', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']


