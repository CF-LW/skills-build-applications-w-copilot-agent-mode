from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='hero@marvel.com', name='Iron Man', team='Marvel')
        self.assertEqual(user.email, 'hero@marvel.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel', members=['Iron Man', 'Captain America'])
        self.assertEqual(team.name, 'Marvel')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user='Iron Man', type='Running', duration=30, date='2026-02-08')
        self.assertEqual(activity.type, 'Running')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(team='Marvel', points=100)
        self.assertEqual(lb.team, 'Marvel')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='Marvel')
        self.assertEqual(workout.name, 'Pushups')
