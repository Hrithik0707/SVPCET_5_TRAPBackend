from django.db import models

class PollOffensive(models.Model):
    # Sentence which is offensive
    offensive_sentence = models.CharField(max_length=400,blank=True,null=True),
    # no. of users voting yes or no
    vote_yes = models.IntegerField(blank=True,null=True),
    vote_no = models.IntegerField(blank=True,null=True),
    # will store mobile no. of the user started poll
    user_polled = models.IntegerField(blank=True,null=True),
    # List of users polled
    voter_pole = models.TextField(blank=True,null=True)

    def __str__(self):
        return str(self.offensive_sentence) 