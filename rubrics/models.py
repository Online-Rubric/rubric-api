from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator


class Rubric(models.Model):
    name = models.CharField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    score1 = models.IntegerField(default=0, name="Asked meaningful clarifying questions", validators=MaxValueValidator(2))

    score2 = models.IntegerField(default=0, name="Identified inputs and outputs", validators=MaxValueValidator(2))

    score3 = models.IntegerField(default=0, name="Visually illustrated the problem domain", validators=MaxValueValidator(2))

    score4 = models.IntegerField(default=0, name="Identified optimal data structure and/or algorithm", validators=MaxValueValidator(4))

    interpret_question_notes = models.TextField()

    score5 = models.IntegerField(default=0, name="Presented & understood a working algorithm", validators=MaxValueValidator(4))

    score6 = models.IntegerField(default=0, name="Final code was syntactically correct", validators=MaxValueValidator(3))

    score7 = models.IntegerField(default=0, name="Final code was idiomatically correct", validators=MaxValueValidator(3))

    score8 = models.IntegerField(default=0, name="Solution was the best possible option", validators=MaxValueValidator(2))

    solve_problem_notes = models.TextField()

    score9 = models.IntegerField(default=0, name="Stepped through their solution", validators=MaxValueValidator(3))

    score10 = models.IntegerField(default=0, name="Big O time and space are analyzed", validators=MaxValueValidator(3))

    score11 = models.IntegerField(default=0, name="Explain an approach to testing", validators=MaxValueValidator(3))

    analyze_solution_notes = models.TextField()

    score12 = models.IntegerField(default=0, name="Verbalized their thought process", validators=MaxValueValidator(6))

    score13 = models.IntegerField(default=0, name="Used correct terminology", validators=MaxValueValidator(2))

    score14 = models.IntegerField(default=0, name="Used the time available effectively", validators=MaxValueValidator(1))

    score15 = models.IntegerField(default=0, name="Was not overconfident (not listening to suggestions)", validators=MaxValueValidator(1))

    score16 = models.IntegerField(default=0, name="Was not under-confident (unsure of known algorithm)", validators=MaxValueValidator(1))

    score17 = models.IntegerField(default=0, name="Whiteboard was readable (penmanship and spacing)", validators=MaxValueValidator(1))

    communicate_effectively_notes = models.TextField()


    total = models.IntegerField(default=0, name="Total Score")


    comments = models.TextField(default="", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
