# Generated by Django 3.1.4 on 2020-12-03 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            "insert into commons_ageranges values (1, 0, 18);" +
            "insert into commons_ageranges values (2, 18, 25);" +
            "insert into commons_ageranges values (3, 25, 35);" +
            "insert into commons_ageranges values (4, 35, 50);" +
            "insert into commons_ageranges values(5, 50, 65);" +

            "insert into commons_incomeranges values (1, 0, 500);" +
            "insert into commons_incomeranges values (2, 500, 1000);" +
            "insert into commons_incomeranges values (3, 1000, 1500);" +
            "insert into commons_incomeranges values (4, 1500, 2000);" +
            "insert into commons_incomeranges values (5, 2000, 2500);" +

            "insert into commons_categories values (1, 'Food');" +
            "insert into commons_categories values (2, 'Sport & Recreation');" +
            "insert into commons_categories values (3, 'Others');"
        )
    ]
