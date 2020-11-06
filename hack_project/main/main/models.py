from django.db import models

class Poll_on_offensive(models.Model):
    # Sentence which is offensive
    offensive_sentence = models.Charfield(max_length=400),
    sentence_id = models.Charfield(max_length=100),
    # no. of users voting yes or no
    vote_yes = models.IntegerField(blank=True,null=True),
    vote_no = models.IntegerField(blank=True,null=True),
    # will store mobile no. of the user started poll
    user_polled = models.IntegerField(blank=True,null=True)
    # List of users polled
    voter_pole = models.TextField()

    def __str__(self):
        return str(self.offensive_sentence) 