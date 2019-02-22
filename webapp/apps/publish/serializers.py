from rest_framework import serializers

from webapp.apps.users.models import Project


class PublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "name",
            "description",
            "package_defaults",
            "parse_user_adjustments",
            "run_simulation",
            "server_cpu",
            "server_ram",
            "exp_task_time",
            "installation",
        )
