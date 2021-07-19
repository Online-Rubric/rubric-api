from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator


class Rubric(models.Model):
    proctor = models.CharField(max_length=256)
    student = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )

    time_start = models.TimeField
    time_end = models.TimeField

    challenge = models.CharField(max_length=256)

    #Asked meaningful clarifying questions
    clarify_question = models.IntegerField(default=0, name="clarify_question", validators=[MaxValueValidator(2)])

    #Identified inputs and outputs
    inputs_outputs = models.IntegerField(default=0, name="inputs_outputs", validators=[MaxValueValidator(2)])

    #Visually illustrated the problem domain
    illustrate_problem = models.IntegerField(default=0, name="illustrate_problem", validators=[MaxValueValidator(2)])

    #"Identified optimal data structure and/or algorithm"
    optimal_structure = models.IntegerField(default=0, name="optimal_structure", validators=[MaxValueValidator(4)])

    interpret_question_notes = models.TextField()

    #Presented & understood a working algorithm
    working_algorithm = models.IntegerField(default=0, name="working_algorithm", validators=[MaxValueValidator(4)])

    #"Final code was syntactically correct"
    syntactically_correct = models.IntegerField(default=0, name="syntactically_correct", validators=[MaxValueValidator(3)])

    #Final code was idiomatically correct
    idiomatically_correct = models.IntegerField(default=0, name="idiomatically_correct", validators=[MaxValueValidator(3)])

    #Solution was the best possible option
    best_solution = models.IntegerField(default=0, name="best_solution", validators=[MaxValueValidator(2)])

    solve_problem_notes = models.TextField()

    #Stepped through their solution
    walkthrough_solution = models.IntegerField(default=0, name="walkthrough_solution", validators=[MaxValueValidator(3)])

    #Big O time and space are analyzed
    big_o = models.IntegerField(default=0, name="big_o", validators=[MaxValueValidator(3)])

    #Explain an approach to testing
    testing = models.IntegerField(default=0, name="testing", validators=[MaxValueValidator(3)])

    analyze_solution_notes = models.TextField()

    score12 = models.IntegerField(default=0, name="Verbalized their thought process", validators=[MaxValueValidator(6)])

    #Used correct terminology
    terminology = models.IntegerField(default=0, name="terminology", validators=[MaxValueValidator(2)])

    #Used the time available effectively
    use_time = models.IntegerField(default=0, name="use_time", validators=[MaxValueValidator(1)])

    #Was not overconfident (not listening to suggestions)
    overconfident = models.IntegerField(default=0, name="overconfident", validators=[MaxValueValidator(1)])

    #Was not under-confident (unsure of known algorithm
    underconfident = models.IntegerField(default=0, name="underconfident", validators=[MaxValueValidator(1)])

    #Whiteboard was readable (penmanship and spacing)
    whiteboard = models.IntegerField(default=0, name="whiteboard", validators=[MaxValueValidator(1)])

    communicate_effectively_notes = models.TextField()

    #Total Score
    total = models.IntegerField(default=0, name="total")


    comments = models.TextField(default="", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
