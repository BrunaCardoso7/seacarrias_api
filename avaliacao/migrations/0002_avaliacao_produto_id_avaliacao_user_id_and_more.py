# Generated by Django 5.1.7 on 2025-03-09 01:24

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("avaliacao", "0001_initial"),
        ("produto", "0002_produto_preco_estimado"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="avaliacao",
            name="produto_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="produtoavaliado",
                to="produto.produto",
            ),
        ),
        migrations.AddField(
            model_name="avaliacao",
            name="user_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="avaliar",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="avaliacao",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="avaliacao",
            name="nota",
            field=models.IntegerField(),
        ),
    ]
