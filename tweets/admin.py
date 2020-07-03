from django.contrib import admin

# Register your models here.
from .models import Tweet, TweetLike

class TweetLikeAdmin(admin.TabularInline):
    model = TweetLike

class TweetAdmin(admin.ModelAdmin):
    inlines = [TweetLikeAdmin]
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model = Tweet

admin.site.register(Tweet, TweetAdmin)

# QUERY SET LOOKUPS
# search for all content of "lol"
# qs = Tweet.objects.filter(content="lol")
# search for all usernames of "lol"
# qs = Tweet.objects.filter(user__username="lol")
# search for all usernames case insensitive of "lol"
# qs = Tweet.objects.filter(user__username__iexact="lol")