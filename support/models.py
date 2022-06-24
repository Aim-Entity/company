from pyexpat import model
from unicodedata import category
from django.db import models

TOPIC_CHOICES = (
    ("Bullying", "Bullying"),
    ("Mental Illness", "Mental Illness"),
    ("Stress", "Stress"),
    ("Disability", "Disability"),
    ("Despression", "Despression"),
)


class SupportCard(models.Model):
    question = models.CharField(max_length=250, null=True)
    answer = models.CharField(max_length=5000, null=True)
    topic = models.CharField(max_length=50, choices=TOPIC_CHOICES,
                             null=True, default="Bullying")

    def __str__(self):
        return f'{self.topic}: {self.question}'
