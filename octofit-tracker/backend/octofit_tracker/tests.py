from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Marvel")
        self.user = User.objects.create(name="Tony Stark", email="ironman@marvel.com", team=self.team)
        self.workout = Workout.objects.create(name="Super Strength", description="Heavy lifting.")
        self.activity = Activity.objects.create(user=self.user, activity="Engineering", duration=60)
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)

    def test_user(self):
        self.assertEqual(self.user.name, "Tony Stark")
        self.assertEqual(self.user.team.name, "Marvel")

    def test_team(self):
        self.assertEqual(self.team.name, "Marvel")

    def test_activity(self):
        self.assertEqual(self.activity.activity, "Engineering")

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.score, 100)

    def test_workout(self):
        self.assertEqual(self.workout.name, "Super Strength")
