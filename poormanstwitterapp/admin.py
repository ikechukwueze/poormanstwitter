from django.contrib import admin
from .models import TweetAuthor, Tweet
# Register your models here.


class TweetAdmin(admin.ModelAdmin):
    readonly_fields = ('formatted_date_time',)


admin.site.register(TweetAuthor)
admin.site.register(Tweet, TweetAdmin)

