from django.contrib.auth import get_user_model

import pytest

from webapp.apps.users.models import Profile, Project, is_profile_active

User = get_user_model()


@pytest.mark.django_db
class TestUserModels:
    def test_construct_user(self):
        user = User.objects.create(username="tester", email="tester@email.com")
        assert user.username
        assert user.email

    def test_project(self):
        p = Project(name="test project", server_cost=36)
        assert p.server_cost_in_secs == 0.01
        assert p.n_secs_per_penny == 1.0
        assert p.run_cost(1) == 0.01
        assert p.run_cost(0.5, adjust=True) == 0.01
        assert p.run_cost(0.5, adjust=False) < 0.01
        assert p.run_cost(2) == 0.02
        assert Project.dollar_to_penny(0.01) == 1

    def test_create_profile(self, user):
        profile = Profile.objects.create(user=user, is_active=True)
        assert profile
        assert profile.user == user
        assert profile.is_active == True
        assert is_profile_active(user) == True
        profile.is_active = False
        assert profile.is_active == False
        assert is_profile_active(user) == False

    def test_profile_costs(self, profile, test_models):
        """See conftest for initial values in test_models"""
        assert profile.costs() == {"January 2019": 1.0, "February 2019": 1.0}

    def test_profile_runs(self, profile, test_models, billing_data):
        runs = profile.runs()

        # check that all apps are queried.
        billing_names = {data["name"] for _, data in billing_data.items()}
        assert billing_names == set(runs.keys())

        testapprun = test_models[0]
        assert len(runs["Used for testing"].all()) == 1
        for run in runs["Used for testing"].all():
            assert run == testapprun

        sponsoredtestapprun = test_models[1]
        assert len(runs["Used for testing sponsored apps"].all()) == 1
        for run in runs["Used for testing sponsored apps"].all():
            assert run == sponsoredtestapprun

    def test_project_show_sponsor(self, test_models):
        """See conftest for initial values in test_models."""
        reg, sponsored = test_models
        assert reg.project.display_sponsor == "Not sponsored"
        assert sponsored.project.display_sponsor == "sponsor"
