from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos_app', '0003_contenido_curso_inscripcion'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.RunSQL(
                    sql=[
                        'PRAGMA foreign_keys = OFF;',
                        'DROP TABLE IF EXISTS "cursos_app_encargado_curso";',
                        (
                            'CREATE TABLE "cursos_app_encargado_curso" ('
                            '"encargado_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, '
                            '"profesor_id" integer NOT NULL REFERENCES "auth_user" ("id") '
                            'DEFERRABLE INITIALLY DEFERRED'
                            ');'
                        ),
                        'CREATE INDEX "cursos_app_encargado_curso_profesor_id" '
                        'ON "cursos_app_encargado_curso" ("profesor_id");',
                        'PRAGMA foreign_keys = ON;',
                    ],
                    reverse_sql=migrations.RunSQL.noop,
                ),
            ],
            state_operations=[
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
            ],
        ),
    ]