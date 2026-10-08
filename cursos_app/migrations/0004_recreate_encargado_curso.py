from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos_app', '0003_contenido_curso_inscripcion'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encargado_curso',
            name='n_encargado',
        ),
        migrations.RemoveField(
            model_name='encargado_curso',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='encargado_curso',
            name='telefono',
        ),
        migrations.AddField(
            model_name='encargado_curso',
            name='profesor',
            field=models.ForeignKey(
                on_delete=models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]