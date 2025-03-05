from rest_framework import serializers
from .models import TheWireNews
from django.utils import timezone

class TheWireNewsSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    category = serializers.CharField(source='category.category')
    title = serializers.CharField(source='news_title')
    subtitle = serializers.SerializerMethodField()

    class Meta:
        model = TheWireNews
        fields = ['id','image', 'category', 'title', 'subtitle']

    def get_subtitle(self, obj):
        now = timezone.now()
        diff = now - obj.published_at 
        seconds = diff.total_seconds() 

        print(f"Author: {obj.author}, Username: {obj.author.username if obj.author else 'No Author'}")

        if seconds < 60:
            time_ago = f"{int(seconds)} sec ago"
        elif seconds < 3600:
            minutes = int(seconds // 60)
            time_ago = f"{minutes} min ago"
        elif seconds < 86400:
            hours = int(seconds // 3600)
            time_ago = f"{hours} hr ago"
        else:
            days = int(seconds // 86400)
            time_ago = f"{days} days ago"
        
        return f"{obj.author.name if obj.author else 'Unknown Author'} • {time_ago}"

