# Generated by Django 3.2.9 on 2021-11-26 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learningportal', '0004_remove_watchlistitem_watchlist_cant_repeat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlistitem',
            name='content',
        ),
        migrations.AddField(
            model_name='watchlistitem',
            name='content',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='learningportal.content'),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name='watchlistitem',
            constraint=models.UniqueConstraint(fields=('user', 'content'), name='already_in_watchlater'),
        ),
    ]