from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .models import Tweet, TweetAuthor
from .serializers import TweetSerializer
from rest_framework import status
import json

# Create your tests here.

class HomePageTest(SimpleTestCase):
    def test_home_page_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_home_page_template(self):
        resp = self.client.get(reverse('home_page'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'poormanstwitterapp/index.html')


class AuthorModelTest(TestCase):
    def setUp(self):
        TweetAuthor.objects.create(name='Sam')
    
    def test_tweet_author(self):
        author = TweetAuthor.objects.get(id=1)
        expected_author = f'{author.name}'
        self.assertEqual(expected_author, 'Sam')


class TweetModelTest(TestCase):
    def setUp(self):
        author = TweetAuthor.objects.create(name='Sam')
        Tweet.objects.create(tweet_author=author, tweet='Hello world.')

    def test_tweet_content(self):
        tweet = Tweet.objects.get(id=1)
        expected_author = f'{tweet.tweet_author.name}'
        expected_tweet = f'{tweet.tweet}'
        self.assertEqual(expected_author, 'Sam')
        self.assertEqual(expected_tweet, 'Hello world.')


class GetTweetEndPointTest(TestCase):
    def setUp(self):
        author = TweetAuthor.objects.create(name='Sam')
        Tweet.objects.create(tweet_author=author, tweet='Hello world.')
    
    def test_get_tweet_endpoint_url(self):
        resp = self.client.get(reverse('get_or_post_tweets'))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_get_tweet_api(self):
        tweets = Tweet.objects.all()
        tweet_serializer = TweetSerializer(tweets, many=True)
        resp = self.client.get(reverse('get_or_post_tweets'))
        self.assertEqual(resp.data, tweet_serializer.data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)


class PostTweetEndPointTest(TestCase):
    def setUp(self):
        self.payload = {
            'tweet_author': 'Sam',
            'tweet': 'Hello world.'
        }

    def test_post_tweet_api(self):
        resp = self.client.post(
            reverse('get_or_post_tweets'),
            data=json.dumps(self.payload),
            content_type='application/json'
        )
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)