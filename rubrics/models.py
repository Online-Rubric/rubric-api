from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator


class Rubric(models.Model):
    proctor = models.CharField(max_length=256,name="proctor",)
    student = models.ForeignKey(
        get_user_model(), name="student", on_delete=models.CASCADE, null=True, blank=True
    )

    #We could do this as a charater field or as a time field
    time_start =models.CharField(max_length=256,name="time_start",)
    time_end = models.CharField(max_length=256,name="time_end",)

    challenge = models.CharField(max_length=256,name="challenge")

    #Asked meaningful clarifying questions
    clarify_question = models.IntegerField(default=0, name="clarify_question", type="score", validators=[MaxValueValidator(2)])

    #Identified inputs and outputs
    inputs_outputs = models.IntegerField(default=0, name="inputs_outputs", type="score", validators=[MaxValueValidator(2)])

    #Visually illustrated the problem domain
    illustrate_problem = models.IntegerField(default=0, name="illustrate_problem", type="score", validators=[MaxValueValidator(2)])

    #"Identified optimal data structure and/or algorithm"
    optimal_structure = models.IntegerField(default=0, name="optimal_structure", type="score", validators=[MaxValueValidator(4)])

    interpret_question_notes = models.TextField()

    #Presented & understood a working algorithm
    working_algorithm = models.IntegerField(default=0, name="working_algorithm", type="score", validators=[MaxValueValidator(4)])

    #"Final code was syntactically correct"
    syntactically_correct = models.IntegerField(default=0, name="syntactically_correct", type="score", validators=[MaxValueValidator(3)])

    #Final code was idiomatically correct
    idiomatically_correct = models.IntegerField(default=0, name="idiomatically_correct", type="score", validators=[MaxValueValidator(3)])

    #Solution was the best possible option
    best_solution = models.IntegerField(default=0, name="best_solution", type="score", validators=[MaxValueValidator(2)])

    solve_problem_notes = models.TextField()

    #Stepped through their solution
    walkthrough_solution = models.IntegerField(default=0, name="walkthrough_solution", validators=[MaxValueValidator(3)])

    #Big O time and space are analyzed
    big_o = models.IntegerField(default=0, name="big_o", type="score", validators=[MaxValueValidator(3)])

    #Explain an approach to testing
    testing = models.IntegerField(default=0, name="testing", type="score", validators=[MaxValueValidator(3)])

    analyze_solution_notes = models.TextField()

    #Verbalized their thought process
    thought_process = models.IntegerField(default=0, name="thought_process", type="score", validators=[MaxValueValidator(6)])

    #Used correct terminology
    terminology = models.IntegerField(default=0, name="terminology", type="score", validators=[MaxValueValidator(2)])

    #Used the time available effectively
    use_time = models.IntegerField(default=0, name="use_time", type="score", validators=[MaxValueValidator(1)])

    #Was not overconfident (not listening to suggestions)
    overconfident = models.IntegerField(default=0, name="overconfident", type="score", validators=[MaxValueValidator(1)])

    #Was not under-confident (unsure of known algorithm)
    underconfident = models.IntegerField(default=0, name="underconfident", type="score", validators=[MaxValueValidator(1)])

    #Whiteboard was readable (penmanship and spacing)
    whiteboard = models.IntegerField(default=0, name="whiteboard", type="score", validators=[MaxValueValidator(1)])

    communicate_effectively_notes = models.TextField()

    #Total Score
    total = models.IntegerField(default=0, name="total")


    comments = models.TextField(default="", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name

scores = Rubric.object.filter(type="score")
total_score = sum(scores)
percent = total_score/40
