from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Devolve uma representacao em string do modelo."""
        return self.text
    
class Entry(models.Model):
    """Algo especifico aprendido sobre um assunto."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
            
    def __str__(self):
        """Devolve uma representacao em string do modelo"""
        return self.text[:50] + "..."