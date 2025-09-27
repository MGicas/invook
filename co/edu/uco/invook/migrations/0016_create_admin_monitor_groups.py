from django.db import migrations

ADMIN = "ADMIN"
MONITOR = "MONITOR"

def create_groups(apps, schema_editor):
    group_model = apps.get_model("auth", "Group")
    group_model.objects.get_or_create(name=ADMIN)
    group_model.objects.get_or_create(name=MONITOR)

def remove_groups(apps, schema_editor):
    group_model = apps.get_model("auth", "Group")
    group_model.objects.filter(name__in=[ADMIN, MONITOR]).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('invook', '0015_administrativeprofile'),
        ('auth', '__latest__'),
    ]

    operations = [
        migrations.RunPython(create_groups, reverse_code=remove_groups),
    ]
