from django.db import models
from accounts.models import User



class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} -> {self.recipient}: {self.content}"