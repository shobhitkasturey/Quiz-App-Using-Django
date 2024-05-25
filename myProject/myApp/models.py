from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)
    correct_answer = models.IntegerField()

    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

