<<<<<<< HEAD
# Generated by Django 4.2.11 on 2024-05-04 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
=======
# Generated by Django 5.0.4 on 2024-05-04 16:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
>>>>>>> c46815c07918e406b1f30e8126e5dc0d9d390ab7


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('online_insurance', '0001_initial'),
=======
        ('online_insurance', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
>>>>>>> c46815c07918e406b1f30e8126e5dc0d9d390ab7
    ]

    operations = [
        migrations.CreateModel(
            name='AgentAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
=======
              
>>>>>>> c46815c07918e406b1f30e8126e5dc0d9d390ab7
                ('agent_phone', models.IntegerField()),
                ('status', models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable')], max_length=20)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
