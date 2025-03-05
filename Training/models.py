from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from UserLogin.models import EmployeeLogin

class Training(models.Model):
    training_date = models.DateField()
    training_title = models.CharField(max_length=100, null=True)
    training_objective = models.TextField()
    training_speaker = models.CharField(max_length=100, null=True)
    is_closed = models.BooleanField(default=False)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.training_title

class ParticipantResponse(models.Model):
    employee = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE, related_name='participant_user')
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    action = models.BooleanField(default=False)
    is_evaluated = models.BooleanField(default=False)
    is_approved = models.CharField(max_length=10,default="Pending")
    date_responded = models.DateTimeField(auto_now_add=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.employee.name} - {self.training}'
        
class TrainingForm(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    employee = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE, related_name='training_participants')
    evaluation_to = models.ForeignKey(ParticipantResponse, on_delete=models.CASCADE, null=True)

    # content
    job_related = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    explain_clearly = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    suitable_topic = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])

    # organized
    clear_goals = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    met_goals = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    easy_follow = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    easy_understand = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])

    # speaker
    speaker_knowledge = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    clear_communication = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    answered_questions = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])

    # resources
    training_org = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    facilities = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    materials = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])

    # feedback
    interest = models.TextField(null=True)
    future_recommendations = models.TextField(null=True)
    related_subjects = models.TextField(null=True)

    app_work1 = models.TextField(null=True)
    app_work2 = models.TextField(null=True)
    target_date = models.DateField()
    actual_date = models.DateField()

    app_self1 = models.TextField(null=True)
    app_self2 = models.TextField(null=True)
    
    #supervisor
    result_impact = models.TextField(blank=True)
    recommendation = models.TextField(blank=True)
    assessment = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True)

    submitted_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)


    def __str__(self):
        return f'{self.employee.name}-{self.evaluation_to.training.training_title}'
    
class TrainingApproval(models.Model):
    training = models.ForeignKey(ParticipantResponse, on_delete=models.CASCADE)
    approver = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE)
    date_approved = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.training.training.training_title} - {self.approver.name}'