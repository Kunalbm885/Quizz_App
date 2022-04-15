# Generated by Django 4.0.4 on 2022-04-14 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer_Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student', models.CharField(max_length=100)),
                ('Teacher', models.CharField(default=1, max_length=100)),
                ('Quiz_Name', models.CharField(max_length=300)),
                ('Question', models.CharField(default=1, max_length=300)),
                ('Option1', models.CharField(default=10, max_length=100)),
                ('Option2', models.CharField(default=10, max_length=100)),
                ('Option3', models.CharField(default=10, max_length=100)),
                ('Option4', models.CharField(default=10, max_length=100)),
                ('answer', models.CharField(default=10, max_length=100)),
                ('marks', models.BigIntegerField(default=1, max_length=3)),
                ('Selected_Ans', models.CharField(default=1, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AttemptedQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(default=1, max_length=100)),
                ('sname', models.CharField(max_length=100)),
                ('qname', models.CharField(max_length=50)),
                ('isattempted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teacher', models.CharField(default=1, max_length=100)),
                ('quiznameques', models.CharField(max_length=100)),
                ('question', models.CharField(max_length=300)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('marks', models.BigIntegerField(default=1, max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='QuizInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacherassigname', models.CharField(max_length=50)),
                ('quizname', models.CharField(max_length=50)),
                ('totaltime', models.CharField(default=1, max_length=50)),
                ('noofquest', models.CharField(default=2, max_length=50)),
                ('Duedate', models.CharField(default=1, max_length=50)),
                ('Time', models.CharField(default=1, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='QuizReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student', models.CharField(max_length=100)),
                ('Teacher', models.CharField(default=1, max_length=100)),
                ('Date', models.CharField(default=1, max_length=100)),
                ('Time', models.CharField(default=1, max_length=100)),
                ('QuizName', models.CharField(max_length=300)),
                ('Score', models.CharField(max_length=100)),
                ('Total_Marks', models.CharField(default=10, max_length=100)),
                ('Percentage', models.CharField(max_length=100)),
                ('Correct', models.CharField(max_length=100)),
                ('Incorrect', models.CharField(max_length=100)),
                ('Total', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentname', models.CharField(max_length=50)),
                ('studentemail', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('studentrollno', models.BigIntegerField(verbose_name=20)),
                ('studentpass', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teachername', models.CharField(max_length=50)),
                ('teacheremail', models.EmailField(max_length=30, primary_key=True, serialize=False)),
                ('teacherpass', models.CharField(max_length=50)),
            ],
        ),
    ]
