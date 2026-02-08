from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', members=['Iron Man', 'Captain America', 'Thor'])
        dc = Team.objects.create(name='DC', members=['Superman', 'Batman', 'Wonder Woman'])

        # Create users
        User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel')
        User.objects.create(email='cap@marvel.com', name='Captain America', team='Marvel')
        User.objects.create(email='thor@marvel.com', name='Thor', team='Marvel')
        User.objects.create(email='superman@dc.com', name='Superman', team='DC')
        User.objects.create(email='batman@dc.com', name='Batman', team='DC')
        User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='DC')

        # Create activities
        Activity.objects.create(user='Iron Man', type='Running', duration=30, date='2026-02-08')
        Activity.objects.create(user='Batman', type='Cycling', duration=45, date='2026-02-08')

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=150)
        Leaderboard.objects.create(team='DC', points=120)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='Marvel')
        Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
