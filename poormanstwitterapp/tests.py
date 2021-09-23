from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .models import Tweet, TweetAuthor

# Create your tests here.

class HomePageTest(SimpleTestCase):
    def test_home_page_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_home_page_template(self):
        resp = self.client.get(reverse('home_page'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'poormanstwitterapp/index.html')


class TweetModelTest(TestCase):
    def setUp(self):
        author = TweetAuthor.objects.create(name='Sam')
        Tweet.objects.create(tweet_author=author, tweet='Hello world.')
    
    def test_tweet_author(self):
        author = TweetAuthor.objects.get(id=1)
        expected_author = f'{author.name}'
        self.assertEqual(expected_author, 'Sam')

    def test_tweet_content(self):
        tweet = Tweet.objects.get(id=1)
        expected_author = f'{tweet.tweet_author.name}'
        expected_tweet = f'{tweet.tweet}'
        self.assertEqual(expected_author, 'Sam')
        self.assertEqual(expected_tweet, 'Hello world.')