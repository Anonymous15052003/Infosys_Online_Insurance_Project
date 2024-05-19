# Generated by Django 5.0.4 on 2024-05-19 07:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("online_insurance", "0007_policy_alter_agentavailability_agent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="agentavailability",
            name="agent",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="agentavailability",
            name="agent_district",
            field=models.CharField(
                choices=[
                    ("Ahmadnagar", "Ahmadnagar"),
                    ("Akola", "Akola"),
                    ("Amravati", "Amravati"),
                    ("Aurangabad", "Aurangabad"),
                    ("Bhandara", "Bhandara"),
                    ("Buldhana", "Buldhana"),
                    ("Chandrapur", "Chandrapur"),
                    ("Dhule", "Dhule"),
                    ("Gadchiroli", "Gadchiroli"),
                    ("Gondia", "Gondia"),
                    ("Hingoli", "Hingoli"),
                    ("Jalgaon", "Jalgaon"),
                    ("Jalna", "Jalna"),
                    ("Kolhapur", "Kolhapur"),
                    ("Latur", "Latur"),
                    ("MumbaiCity", "Mumbai City"),
                    ("MumbaiSuburban", "Mumbai Suburban"),
                    ("Nagpur", "Nagpur"),
                    ("Nanded", "Nanded"),
                    ("Nandurbar", "Nandurbar"),
                    ("Nashik", "Nashik"),
                    ("Osmanabad", "Osmanabad"),
                    ("Palghar", "Palghar"),
                    ("Parbhani", "Parbhani"),
                    ("Pune", "Pune"),
                    ("Raigad", "Raigad"),
                    ("Ratnagiri", "Ratnagiri"),
                    ("Sangli", "Sangli"),
                    ("Satara", "Satara"),
                    ("Sindhudurg", "Sindhudurg"),
                    ("Solapur", "Solapur"),
                    ("Thane", "Thane"),
                    ("Wardha", "Wardha"),
                    ("Washim", "Washim"),
                    ("Yavatmal", "Yavatmal"),
                ],
                max_length=100,
                verbose_name="District",
            ),
        ),
        migrations.AlterField(
            model_name="agentavailability",
            name="status",
            field=models.CharField(
                choices=[("available", "Available"), ("unavailable", "Unavailable")],
                max_length=20,
                verbose_name="Status",
            ),
        ),
    ]