# Generated by Django 4.2.1 on 2023-06-04 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('Gender', 'Gender'), ('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('married', models.CharField(choices=[('Married', 'Married'), ('Yes', 'Yes'), ('No', 'No')], max_length=50)),
                ('dependents', models.CharField(choices=[('Dependents', 'Dependents'), ('0', '0'), ('1', '1'), ('2', '2'), ('More than 2', 'More than 2')], max_length=50)),
                ('education', models.CharField(choices=[('Education', 'Education'), ('Graduate', 'Graduate'), ('Not Graduate', 'Not Graduate')], max_length=50)),
                ('self_employed', models.CharField(choices=[('Self Employed', 'Self Employed'), ('Yes', 'Yes'), ('No', 'No')], max_length=50)),
                ('applicant_income', models.IntegerField(default=0)),
                ('co_applicant_income', models.IntegerField(default=0)),
                ('loan_amount', models.IntegerField(default=0)),
                ('loan_amount_term', models.IntegerField(default=0)),
                ('credit_history', models.CharField(choices=[('Credit History', 'Credit History'), ('0', '0'), ('1', '1')], max_length=50)),
                ('property_area', models.CharField(choices=[('Area', 'Area'), ('Urban', 'Urban'), ('Rural', 'Rural'), ('Semi Urban', 'Semi Urban')], max_length=50)),
                ('status', models.CharField(choices=[('Approved', 'Approved'), ('Declined', 'Declined')], max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]