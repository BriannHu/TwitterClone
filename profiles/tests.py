from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Profile

# Create your tests here.

User = get_user_model()

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='abc', password='password')
        self.user2 = User.objects.create_user(username='abc2', password='password2')

    def test_profile_created_via_signal(self):
        qs = Profile.objects.all()
        self.assertEqual(qs.count(), 2)
    
    def test_following(self):
        first = self.user
        second = self.user2
        first.profile.followers.add(second) # second user now following first
        second_user_following_whom = second.following.all() # from a user, check other user is being followed
        first_user_following_no_one = first.following.all() # check new user is not following anyone
        qs = second_user_following_whom.filter(user=first)
        self.assertTrue(qs.exists())
        self.assertFalse(first_user_following_no_one.exists())
        
