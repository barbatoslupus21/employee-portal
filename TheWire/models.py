from django.db import models
from UserLogin.models import EmployeeLogin

class NewCategory(models.Model):
    category = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.category

class TheWireNews(models.Model):
    author = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE, related_name='news_author')
    category = models.ForeignKey(NewCategory, on_delete=models.CASCADE, related_name='news_category')
    image = models.ImageField(upload_to='news/', blank=True)
    news_title = models.CharField(max_length=200, null=True)
    news_content = models.TextField(null=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.news_title
