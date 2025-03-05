from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from UserLogin.models import EmployeeLogin

class Quarter(models.Model):
    quarter = models.CharField(max_length=20, null=True)
    period = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=7, null=True, default="OPEN")
    created_by = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quarter
    
class UserResponse(models.Model):
    employee = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE, related_name='response_user')
    quarter = models.ForeignKey(Quarter, on_delete=models.CASCADE)
    action = models.BooleanField(default=False)
    date_responded = models.DateTimeField(auto_now_add=True)
    posted_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.employee} - {self.quarter}'

class SurveyForm(models.Model):

    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    employee = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE, related_name='survey_respondent')
    survey_to = models.ForeignKey(UserResponse, on_delete=models.CASCADE, null=True)

    # job satisfaction
    skills = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    knowledge_of_job = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    orientation_of_job = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    quality_of_supervision = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    training_and_development = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    job_description = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    opportunity_for_advancement = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    workload = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])

    # policy
    policy = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])

    # salary
    salary = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    salary_increase = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])

    # company facilities
    clinic = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    kiddie_garden = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    shuttle_service = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    locker_room = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    working_condition = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    workplace = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    comfort_room = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    canteen = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])

    # Relations program
    summer_outing = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    birthday_celebration = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    christmas_party = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    team_building = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])


    # feedback
    remarks = models.TextField(null=True)
    suggestions = models.TextField(null=True)

    submitted_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.employee.name}-{self.survey_to.quarter.quarter}'