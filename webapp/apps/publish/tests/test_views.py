import json
from decimal import Decimal

import pytest

from django.contrib.auth import get_user_model, get_user
from guardian.shortcuts import assign_perm, remove_perm

from webapp.apps.users.models import Project, Profile

from webapp.apps.publish.serializers import PublishSerializer


@pytest.mark.django_db
class TestPublishViews:
    def test_get(self, client):
        resp = client.get("/publish/")
        assert resp.status_code == 200

    def test_post(self, client):
        post_data = {
            "title": "New-Model",
            "description": "**Super** new!",
            "package_defaults": "import newmodel",
            "parse_user_adjustments": "import newmodel",
            "run_simulation": "import newmodel",
            "server_size": [4, 8],
            "installation": "install me",
            "inputs_style": "paramtools",
            "meta_parameters": "{}",
        }
        resp = client.post("/publish/api/", post_data)
        assert resp.status_code == 401

        client.login(username="modeler", password="modeler2222")
        resp = client.post("/publish/api/", post_data)
        assert resp.status_code == 200

        project = Project.objects.get(
            title="New-Model", owner__user__username="modeler"
        )
        assert project
        assert project.server_cost

    def test_get_detail_api(self, client, test_models):
        exp = {
            "title": "Detail-Test",
            "description": "desc",
            "package_defaults": "import me",
            "parse_user_adjustments": "import me",
            "run_simulation": "import me",
            "server_size": ["4", "2"],
            "exp_task_time": 20,
            "installation": "install me",
            "inputs_style": "paramtools",
            "meta_parameters": {},
            "server_cost": Decimal("0.1"),
        }
        owner = Profile.objects.get(user__username="modeler")
        project = Project.objects.create(owner=owner, **exp)
        resp = client.get("/publish/api/modeler/Detail-Test/detail/")
        assert resp.status_code == 200
        data = resp.json()
        serializer = PublishSerializer(project, data=data)
        assert serializer.is_valid()
        assert serializer.validated_data == dict(exp, **{"meta_parameters": "{}"})

    def test_put_detail_api(self, client, test_models, profile, password):
        put_data = {
            "title": "Used-for-testing",
            "description": "hello world",
            "package_defaults": "import test",
            "parse_user_adjustments": "import test",
            "run_simulation": "import test",
            "server_size": [2, 4],
            "installation": "install",
            "inputs_style": "paramtools",
            "meta_parameters": "{}",
        }
        # not logged in --> not authorized
        resp = client.put(
            "/publish/api/modeler/Used-for-testing/detail/",
            data=put_data,
            content_type="application/json",
        )
        assert resp.status_code == 401

        # not the owner --> not authorized
        client.login(username="sponsor", password="sponsor2222")
        resp = client.put(
            "/publish/api/modeler/Used-for-testing/detail/",
            data=put_data,
            content_type="application/json",
        )
        assert resp.status_code == 401

        # logged in and owner --> do update
        client.login(username="modeler", password="modeler2222")
        resp = client.put(
            "/publish/api/modeler/Used-for-testing/detail/",
            data=put_data,
            content_type="application/json",
        )
        assert resp.status_code == 200
        project = Project.objects.get(
            title="Used-for-testing", owner__user__username="modeler"
        )
        assert project.package_defaults == put_data["package_defaults"]

        # Description can't be empty.
        resp = client.put(
            "/publish/api/modeler/Used-for-testing/detail/",
            data=dict(put_data, **{"description": None}),
            content_type="application/json",
        )
        assert resp.status_code == 400

        # test add write_project permission allows update
        put_data["package_defaults"] = "import helloworld"
        client.login(username=profile.user.username, password=password)
        resp = client.put(
            "/publish/api/modeler/Used-for-testing/detail/",
            data=put_data,
            content_type="application/json",
        )
        # make sure "tester" doesn't have access already.
        assert resp.status_code == 401

        project = Project.objects.get(
            title="Used-for-testing", owner__user__username="modeler"
        )
        assign_perm("write_project", profile.user, project)
        resp = client.put(
            "/publish/api/modeler/Used-for-testing/detail/",
            data=put_data,
            content_type="application/json",
        )
        assert resp.status_code == 200
        project = Project.objects.get(
            title="Used-for-testing", owner__user__username="modeler"
        )
        assert project.package_defaults == put_data["package_defaults"]
        remove_perm("write_project", profile.user, project)
        assert not profile.user.has_perm("write_project", project)

    def test_get_detail_page(self, client, test_models):
        resp = client.get("/modeler/Used-for-testing/detail/")
        assert resp.status_code == 200
