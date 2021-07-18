from django.contrib.auth import get_user_model
from django.db import models


class Rubric(models.Model):
    name = models.CharField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    score1 = models.IntegerField(default=0, name="Asked meaningful clarifying questions")
    score2 = models.IntegerField(default=0, name="Identified inputs and outputs 		")
    score3 = models.IntegerField(default=0, name="Visually illustrated the problem domain")

    score4 = models.IntegerField(default=0, name="Identified optimal data structure and/or algorithm")

    score5 = models.IntegerField(default=0, name="Presented & understood a working algorithm")

    score6 = models.IntegerField(default=0, name="Final code was syntactically correct")

    score7 = models.IntegerField(default=0, name="Final code was idiomatically correct")

    score8 = models.IntegerField(default=0, name="Solution was the best possible option")

    score9 = models.IntegerField(default=0, name="Stepped through their solution")

    score10 = models.IntegerField(default=0, name="Big O time and space are analyzed")

    score11 = models.IntegerField(default=0, name="Explain an approach to testing")

    score12 = models.IntegerField(default=0, name="Verbalized their thought process")

    score13 = models.IntegerField(default=0, name="Used correct terminology")

    score14 = models.IntegerField(default=0, name="Used the time available effectively")

    score15 = models.IntegerField(default=0, name="Was not overconfident (not listening to suggestions)")

    score16 = models.IntegerField(default=0, name="Was not under-confident (unsure of known algorithm)")

    score17 = models.IntegerField(default=0, name="Whiteboard was readable (penmanship and spacing)")


    total = models.IntegerField(default=0, name="Total Score")


    comments = models.TextField(default="", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
