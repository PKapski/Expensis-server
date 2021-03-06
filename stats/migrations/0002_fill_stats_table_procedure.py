# Generated by Django 3.1.4 on 2021-01-03 16:07

from django.db import migrations

# noinspection SqlNoDataSourceInspection,SqlDialectInspection
procedure_body = "create or replace procedure fill_stats_table() language plpgsql as $$ declare " \
    "income_ranges cursor for select * from commons_incomerange;" \
    "age_ranges    cursor for select * from commons_agerange; " \
    "categories    cursor for select * from commons_category; " \
    "genderValue   varchar(1) := 'F';" \
    "begin " \
      "for income_range in income_ranges loop " \
        "for age_range in age_ranges loop " \
            "for category in categories loop " \
                "for gender in 1..2 loop " \
                    "if gender = 1 then " \
                        "genderValue := 'F'; " \
                        "else " \
                        "genderValue := 'M'; " \
                    "end if; " \
                        "insert into stats_stats (income_range_id, age_range_id, category_id, gender, value, count)  " \
                        "values (income_range.id, age_range.id, category.id, genderValue, 0, 0); " \
                "end loop; " \
            "end loop; " \
        "end loop; " \
      "end loop; " \
    "end; $$ "


class Migration(migrations.Migration):
    dependencies = [
        ('stats', '0001_model_creation'),
    ]

    operations = [
        migrations.RunSQL(procedure_body)
    ]
