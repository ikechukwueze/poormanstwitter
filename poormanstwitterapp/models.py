from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class TweetAuthor(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Tweet(models.Model):
    tweet_author = models.ForeignKey(TweetAuthor, on_delete=models.CASCADE)
    tweet = models.CharField(max_length=50)
    tweet_datetime = models.DateTimeField(auto_now=True)
    formatted_date_time = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'tweets'

    def __str__(self):
        return self.tweet_author.name


@receiver(post_save, sender=Tweet)
def format_tweet_date(sender, instance, created, **kwargs):
    date_time_format = '%H:%M · %d %b %Y'
    if created:
        instance.formatted_date_time = instance.tweet_datetime.strftime(date_time_format)
        instance.save()