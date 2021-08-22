from django import forms

"""
class TweetForm(forms.Form):
    tweet_author = forms.CharField(max_length=10, required=True,
                                    widget=forms.TextInput(
                                            attrs={'class':'form-control', 
                                                    'minlength':'2',
                                                    'id':'id_tweet_author',
                                                    'placeholder':'Username'}))

    tweet = forms.CharField(max_length=50, required=True,
                            widget=forms.TextInput(
                                    attrs={'class':'form-control', 
                                            'minlength':'2',
                                            'id':'id_tweet',
                                            'placeholder':"What's happening?"}))
"""


class TweetForm(forms.Form):
    tweet_author = forms.CharField(max_length=10, min_length=2, required=True)
    tweet = forms.CharField(max_length=50, min_length=2, required=True)