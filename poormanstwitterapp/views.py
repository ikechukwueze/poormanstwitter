from django.shortcuts import render
from .models import Tweet, TweetAuthor
from .serializers import TweetSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


def home_page(request):
    return render(request, 'poormanstwitterapp/index.html')


@api_view(['GET', 'POST'])
def get_or_post_tweets(request):
    if request.method == 'GET':
        sort_order = request.query_params.get('sortby', 'default')
        sort_order_dict = {
            'author-desc': '-tweet_author__name',
            'author-asc': 'tweet_author__name',
            'date-asc': 'tweet_datetime',
            'default': '-tweet_datetime'
        }

        all_tweets = Tweet.objects.all().order_by(sort_order_dict[sort_order])
        serializer = TweetSerializer(all_tweets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['tweet_author']
            tweet = serializer.validated_data['tweet']
            author, created = TweetAuthor.objects.get_or_create(name=name)

            posted_tweet = Tweet.objects.create(tweet_author=author, tweet=tweet)
            all_tweets = Tweet.objects.filter(tweet_datetime__lte=posted_tweet.tweet_datetime).order_by('-tweet_datetime')
            serializer = TweetSerializer(all_tweets, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
