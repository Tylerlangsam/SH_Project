
# Generated by Django 4.0 on 2021-12-14 17:29


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Babysitter',
            fields=[
                ('babysitter_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('age', models.CharField(max_length=2)),
                ('gender', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('child_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('age', models.CharField(max_length=25)),
                ('gender', models.CharField(max_length=25)),
                ('babysitters', models.ManyToManyField(to='SafehandsApp.Babysitter')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('meal', models.CharField(max_length=255)),
                ('potty', models.CharField(max_length=255)),
                ('nap', models.CharField(max_length=255)),
                ('child_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SafehandsApp.child')),
            ],
        ),
    ]
