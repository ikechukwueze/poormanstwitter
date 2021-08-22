from rest_framework import serializers
from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    tweet_author = serializers.CharField()

    class Meta:
        model = Tweet
        fields = ['tweet_author', 'tweet', 'formatted_date_time']
        read_only_fields = ['formatted_date_time']