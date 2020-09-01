# Generated by Django 2.1 on 2018-09-18 07:36

from django.conf import settings
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import kasa.utils
import kasa.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zaposlenik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'Korisničko ime je već u upotrebi.'}, help_text='Obavezno polje. 150 znakova ili manje.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=150, verbose_name='last name')),
                ('oib', models.CharField(max_length=11, validators=[kasa.validators.validate_OIB], verbose_name='OIB')),
                ('email', models.EmailField(blank=True, max_length=255, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Zaposlenik',
                'verbose_name_plural': 'Zaposlenici',
            },
        ),
        migrations.CreateModel(
            name='Artikl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=150, verbose_name='naziv')),
                ('maloprodajna_cijena', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='maloprodajna cijena')),
                ('pnp', models.BooleanField(default=False, verbose_name='Porez na potrošnju (PNP)')),
                ('jedinica', models.CharField(choices=[('KOM', 'kom'), ('L', 'l'), ('KG', 'kg'), ('DAN', 'dan'), ('SAT', 'sat')], default='KOM', max_length=10, verbose_name='jedinica')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'artikl',
                'verbose_name_plural': 'artikli',
            },
        ),
        migrations.CreateModel(
            name='Kupac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=150, verbose_name='naziv')),
                ('adresa', models.CharField(max_length=150, verbose_name='adresa')),
                ('oib', models.CharField(max_length=11, validators=[kasa.validators.validate_OIB], verbose_name='OIB')),
                ('napomena', models.CharField(blank=True, max_length=150, verbose_name='napomena')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'kupac',
                'verbose_name_plural': 'kupci',
            },
        ),
        migrations.CreateModel(
            name='NaplatniUredaj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('broj', models.IntegerField(verbose_name='broj')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'naplatni uređaj',
                'verbose_name_plural': 'naplatni uređaji',
            },
        ),
        migrations.CreateModel(
            name='PDV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stopa', models.IntegerField(verbose_name='Stopa PDV-a [%]')),
            ],
            options={
                'verbose_name': 'PDV',
                'verbose_name_plural': 'PDV',
            },
        ),
        migrations.CreateModel(
            name='Poslovnica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=150, verbose_name='naziv')),
                ('mjesto', models.CharField(max_length=150, verbose_name='mjesto')),
                ('adresa', models.CharField(max_length=150, verbose_name='adresa')),
                ('broj', models.IntegerField(verbose_name='broj')),
                ('oznaka', models.CharField(max_length=10, verbose_name='oznaka')),
                ('telefon', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='broj telefona nije ispravan', regex='^\\+?1?\\d{9,15}$')], verbose_name='telefon')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'poslovnica',
                'verbose_name_plural': 'poslovnice',
            },
        ),
        migrations.CreateModel(
            name='Racun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vrijeme_izdavanja', models.DateTimeField(auto_now_add=True, verbose_name='datum izdavanja')),
                ('broj', models.IntegerField(verbose_name='broj')),
                ('oznaka', models.CharField(default=kasa.utils.current_year, max_length=50, verbose_name='oznaka')),
                ('godina', models.IntegerField(verbose_name='godina')),
                ('nacin_placanja', models.CharField(choices=[('G', 'Gotovina'), ('K', 'Kartica'), ('T', 'Transakcijski račun'), ('O', 'Ostalo')], default='G', max_length=1, verbose_name='način plaćanja')),
                ('zki', models.CharField(max_length=60)),
                ('jir', models.CharField(max_length=60)),
                ('poruka_porezna', models.CharField(blank=True, max_length=200)),
                ('napomena', models.CharField(blank=True, max_length=60, verbose_name='napomena')),
                ('ukupni_iznos', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='ukupni iznos')),
                ('naziv_operatera', models.CharField(max_length=150, verbose_name='naziv operatera')),
                ('naziv_kupca', models.CharField(max_length=150, verbose_name='naziv kupca')),
                ('zakljucan', models.BooleanField(default=False, verbose_name='zakljucan')),
                ('kupac', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kasa.Kupac', verbose_name='kupac')),
                ('naplatni_uredaj', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kasa.NaplatniUredaj')),
                ('operater', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'racun',
                'verbose_name_plural': 'racuni',
            },
        ),
        migrations.CreateModel(
            name='RacunPorez',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stopa_poreza', models.IntegerField(verbose_name='stopa poreza')),
                ('osnovica_poreza', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='osnovica poreza')),
                ('iznos_poreza', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='iznos poreza')),
                ('ukupno', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='ukupno')),
                ('racun', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kasa.Racun')),
            ],
            options={
                'verbose_name': 'racun porez',
                'verbose_name_plural': 'racun porezi',
            },
        ),
        migrations.CreateModel(
            name='StavkaRacuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rbr', models.IntegerField(default=0, verbose_name='količina')),
                ('kolicina', models.IntegerField(verbose_name='količina')),
                ('naziv_artikla', models.CharField(max_length=150, verbose_name='naziv')),
                ('cijena_artikla', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='cijena')),
                ('pdv_artikla', models.IntegerField(verbose_name='PDV')),
                ('pnp_artikla', models.BooleanField(default=False, verbose_name='PNP')),
                ('ukupno', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='ukupno')),
                ('zakljucan', models.BooleanField(default=False, verbose_name='zakljucan')),
                ('artikl', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kasa.Artikl', verbose_name='artikl')),
                ('racun', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kasa.Racun')),
            ],
            options={
                'verbose_name': 'stavka računa',
                'verbose_name_plural': 'stavke računa',
            },
        ),
        migrations.CreateModel(
            name='Tvrtka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=150, verbose_name='naziv')),
                ('mjesto', models.CharField(max_length=150, verbose_name='mjesto')),
                ('adresa', models.CharField(max_length=150, verbose_name='adresa')),
                ('oib', models.CharField(max_length=11, validators=[kasa.validators.validate_OIB], verbose_name='OIB')),
                ('iban', models.CharField(blank=True, max_length=34, validators=[kasa.validators.validate_IBAN], verbose_name='IBAN')),
                ('u_sustavu_pdv', models.BooleanField(default=False, verbose_name='u sustavu PDV-a')),
                ('telefon', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='broj telefona nije ispravan', regex='^\\+?1?\\d{9,15}$')], verbose_name='telefon')),
                ('certifikat', models.FileField(blank=True, upload_to='certifikati/')),
                ('certifikat_lozinka', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'tvrtka',
                'verbose_name_plural': 'tvrtke',
            },
        ),
        migrations.AddField(
            model_name='poslovnica',
            name='tvrtka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kasa.Tvrtka'),
        ),
        migrations.AddField(
            model_name='naplatniuredaj',
            name='poslovnica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kasa.Poslovnica'),
        ),
        migrations.AddField(
            model_name='naplatniuredaj',
            name='zaposlenici',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='kupac',
            name='tvrtka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kasa.Tvrtka'),
        ),
        migrations.AddField(
            model_name='artikl',
            name='pdv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kasa.PDV'),
        ),
        migrations.AddField(
            model_name='artikl',
            name='tvrtka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kasa.Tvrtka'),
        ),
        migrations.AddField(
            model_name='zaposlenik',
            name='tvrtka',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='kasa.Tvrtka'),
        ),
        migrations.AlterUniqueTogether(
            name='racun',
            unique_together={('broj', 'naplatni_uredaj', 'godina')},
        ),
        migrations.AlterUniqueTogether(
            name='poslovnica',
            unique_together={('broj', 'tvrtka'), ('oznaka', 'tvrtka'), ('naziv', 'tvrtka')},
        ),
        migrations.AlterUniqueTogether(
            name='naplatniuredaj',
            unique_together={('broj', 'poslovnica')},
        ),
        migrations.AlterUniqueTogether(
            name='kupac',
            unique_together={('oib', 'naziv', 'tvrtka')},
        ),
        migrations.AlterUniqueTogether(
            name='artikl',
            unique_together={('naziv', 'tvrtka')},
        ),
        migrations.AlterUniqueTogether(
            name='zaposlenik',
            unique_together={('oib', 'tvrtka')},
        ),
    ]