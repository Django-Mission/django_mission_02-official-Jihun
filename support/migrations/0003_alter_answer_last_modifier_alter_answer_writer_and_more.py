# Generated by Django 4.0.4 on 2022-04-19 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0002_answer_last_modifier_faq_last_modifier_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='last_modifier',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_answer_writer', to=settings.AUTH_USER_MODEL, verbose_name='최종 답변자'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='writer',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='답변자'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='writer',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='생성자'),
        ),
    ]