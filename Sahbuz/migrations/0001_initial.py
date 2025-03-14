# Generated by Django 4.2.4 on 2023-08-08 10:12

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
            name='Ats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adi', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='Adı')),
                ('yerlesdiyi_unvan', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ünvanı')),
                ('telefon_nomresi', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefon nömrəsi')),
                ('ats_ip', models.CharField(blank=True, max_length=15, null=True, verbose_name='ATS-in IP adresi')),
                ('qeydə_alinma_tarixi', models.DateTimeField(auto_now_add=True, null=True)),
                ('sonuncu_duzəlis_tarixi', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Sonuncu duzəliş tarixi')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_Ats', to=settings.AUTH_USER_MODEL, verbose_name='Qeydə alan')),
                ('user2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_Ats2', to=settings.AUTH_USER_MODEL, verbose_name='Sonuncu defe düzəliş edən')),
            ],
            options={
                'verbose_name': 'ATS',
                'verbose_name_plural': 'ATS-lər',
            },
        ),
        migrations.CreateModel(
            name='KomekciPaylayiciSkaf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kskafin_nomresi', models.CharField(max_length=11, null=True, unique=True, verbose_name='Köməkçi şkaf')),
                ('novu', models.CharField(blank=True, choices=[('tps', 'tps'), ('ops', 'ops')], max_length=12, null=True, verbose_name='Növü')),
                ('mudafie_xetti', models.CharField(blank=True, max_length=10, null=True, verbose_name='Müdafiə xətti')),
                ('magistral', models.CharField(blank=True, max_length=10, null=True, verbose_name='Magistral')),
                ('bolme', models.CharField(blank=True, max_length=20, null=True, verbose_name='Bölmə')),
                ('qeyd', models.CharField(blank=True, max_length=50, null=True, verbose_name='Qeyd')),
                ('qeydə_alinma_tarixi', models.DateTimeField(auto_now_add=True, null=True)),
                ('sonuncu_duzəlis_tarixi', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Sonuncu duzəliş tarixi')),
            ],
            options={
                'verbose_name': 'Köməkçi Paylayıcı şkaf',
                'verbose_name_plural': 'Köməkçi Paylayıcı şkaflar',
            },
        ),
        migrations.CreateModel(
            name='KomekciPaylayiciSkafdakiKabelNomreleri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kskafdaki_kabelin_nomresi', models.CharField(max_length=10, null=True, verbose_name='Köməkçi paylayıcı şkafdaki kabel nömrəsi')),
                ('qeyd', models.CharField(blank=True, max_length=50, null=True, verbose_name='Qeyd')),
                ('qeydə_alinma_tarixi', models.DateTimeField(auto_now_add=True, null=True)),
                ('sonuncu_duzəlis_tarixi', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Sonuncu duzəliş tarixi')),
                ('paylayici_skafi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Sahbuz.komekcipaylayiciskaf', verbose_name='Köməkçi paylayıcı şkaf')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_KomekciPaylayiciSkafdakiKabelNomreleri', to=settings.AUTH_USER_MODEL, verbose_name='Qeydə alan')),
                ('user2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_KomekciPaylayiciSkafdakiKabelNomreleri2', to=settings.AUTH_USER_MODEL, verbose_name='Sonuncu defe düzəliş edən')),
            ],
            options={
                'verbose_name': 'Komekci Paylayici Şkafdaki Kabel nömrəsi',
                'verbose_name_plural': 'Komekci Paylayici Şkafdaki Kabel Nomrələri',
            },
        ),
        migrations.CreateModel(
            name='Montyor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adi', models.CharField(blank=True, max_length=30, null=True, verbose_name='Adı')),
                ('telefon_nomresi', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefon nömrəsi')),
                ('qeydə_alinma_tarixi', models.DateTimeField(auto_now_add=True, null=True)),
                ('sonuncu_duzəlis_tarixi', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Sonuncu duzəliş tarixi')),
            ],
            options={
                'verbose_name': 'Montyor',
                'verbose_name_plural': 'Montyorlar',
            },
        ),
        migrations.CreateModel(
            name='Muqavile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muqavile_nomresi', models.CharField(max_length=10, null=True, verbose_name='Müqavilə nömrəsi')),
                ('muqavileni_tarixi', models.DateField(null=True, verbose_name='Müqavilənin tarixi')),
                ('qeyd', models.CharField(blank=True, max_length=50, null=True, verbose_name='Qeyd')),
                ('qeydə_alinma_tarixi', models.DateTimeField(auto_now_add=True, null=True)),
                ('sonuncu_duzəlis_tarixi', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Sonuncu duzəliş tarixi')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_Muqavile', to=settings.AUTH_USER_MODEL, verbose_name='Qeydə alan')),
                ('user2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_Muqavile2', to=settings.AUTH_USER_MODEL, verbose_name='Sonuncu defe düzəliş edən')),
            ],
            options={
                'verbose_name': 'Müqavilə',
                'verbose_name_plural': 'Müqavilələr',
            },
        ),
        migrations.CreateModel(
            name='Nomreler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomre', models.CharField(blank=True, max_length=11, unique=True, verbose_name='Nömrə')),
                ('abonent', models.CharField(blank=True, max_length=50, null=True, verbose_name='Abonent')),
                ('unvan', models.CharField(blank=True, max_length=50, verbose_name='Abonentin ünvanı')),
                ('ats_oturma_yeri', models.CharField(blank=True, max_length=15, null=True, verbose_name='ATS-də oturma yeri')),
                ('internet_port_nomresi', models.CharField(blank=True, max_length=50, null=True, verbose_name='İnternet port nömrəsi')),
                ('abonentin_elaqe_nomresi', models.CharField(blank=True, max_length=25, null=True, verbose_name='Abonentin əlaqə nömrəsi')),
                ('qeyd', models.CharField(blank=True, max_length=50, null=True, verbose_name='Qeyd')),
                ('sahenin_nomresi', models.CharField(blank=True, max_length=20, verbose_name='Sahənin nömrəsi')),
                ('kabelin_cekilme_veziyyeti', models.CharField(blank=True, choices=[('yeralti', 'yeralti'), ('hava', 'hava')], max_length=10, null=True, verbose_name='Kabelin çəkilmə vəziyyəti')),
                ('qirmaqlarin_yeri', models.CharField(blank=True, max_length=25, verbose_name='Qırmaqların yeri')),
                ('uzunlugu', models.IntegerField(blank=True, null=True, verbose_name='Uzunluğu')),
                ('derece', models.CharField(blank=True, max_length=20, verbose_name='Dərəcə')),
                ('qeydə_alinma_tarixi', models.DateTimeField(auto_now_add=True, null=True)),
                ('sonuncu_duzəlis_tarixi', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Sonuncu duzəliş tarixi')),
                ('ats', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Sahbuz.ats', verbose_name='ATS')),
            ],
            options={
                'verbose_name': 'Nömrə',
                'verbose_name_plural': 'Nömrələr',
            },
        ),
        migrations.CreateModel(
            name='OlculmusZedeninXususiyyeti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sebeb', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Yeni Xüsusiyyət')),
                ('qeydə_alinma_tarixi', models.DateTimeField(auto_now_add=True, null=True)),
                ('sonuncu_duzəlis_tarixi', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Sonuncu duzəliş tarixi')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_OlculmusZedeninXususiyyeti', to=settings.AUTH_USER_MODEL, verbose_name='Qeydə alan')),
                ('user2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_OlculmusZedeninXususiyyeti2', to=settings.AUTH_USER_MODEL, verbose_name='Sonuncu defe düzəliş edən')),
            ],
            options={
                'verbose_name': 'Ölçülmüş zəfənin xarakteristikası',
                'verbose_name_plural': 'Ölçülmüş zədənin xarakteristikaları',
            },
        ),
        migrations.CreateModel(
            name='PaylayiciSkaf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skafin_nomresi', models.CharField(max_length=11, null=True, unique=True, verbose_name='Şkafın nömrəsi')),
                ('novu', models.CharField(blank=True, choices=[('tps', 'tps'), ('ops', 'ops')], max_length=12, null=True, verbose_name='Növü')),
                ('mudafie_xetti', models.CharField(blank=True, max_length=10, null=True, verbose_name='Müdafiə xətti')),
                ('magistral', models.CharField(blank=True, max_length=10, null=True, verbose_name='Magistral')),
                ('bolme', models.CharField(blank=True, max_length=20, null=True, verbose_name='Bölmə')),
                ('qeyd', models.CharField(blank=True, max_length=50, null=True, verbose_name='Qeyd')),
                ('qeydə_alinma_tarixi', models.DateTimeField(auto_now_add=True, null=True)),
                ('sonuncu_duzəlis_tarixi', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Sonuncu duzəliş tarixi')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_PaylayiciSkaf', to=settings.AUTH_USER_MODEL, verbose_name='Qeydə alan')),
                ('user2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_PaylayiciSkaf2', to=settings.AUTH_USER_MODEL, verbose_name='Sonuncu defe düzəliş edən')),
            ],
            options={
                'verbose_name': 'Paylayıcı şkaf',
                'verbose_name_plural': 'Paylayıcı şkaflar',
            },
        ),
        migrations.CreateModel(
            name='ZedelenmeninXarakteristikasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sebeb', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Yeni xarakteristika')),
                ('qeydə_alinma_tarixi', models.DateTimeField(auto_now_add=True, null=True)),
                ('sonuncu_duzəlis_tarixi', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Sonuncu duzəliş tarixi')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_ZedelenmeninXarakteristikasi', to=settings.AUTH_USER_MODEL, verbose_name='Qeydə alan')),
                ('user2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_ZedelenmeninXarakteristikasi2', to=settings.AUTH_USER_MODEL, verbose_name='Sonuncu defe düzəliş edən')),
            ],
            options={
                'verbose_name': 'Zədələnmənin xarakteristikası',
                'verbose_name_plural': 'Zədələnmənin xarakteristikaları',
            },
        ),
        migrations.CreateModel(
            name='ZedelenmelerinQeydiyyatiJurnali',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('melumatin_daxil_oldugu_vaxt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Məlumatın daxil olduğu vaxt')),
                ('melumatin_mezmunu', models.CharField(blank=True, max_length=60, null=True, verbose_name='Məlumatın məzmunu')),
                ('temire_verilme_vaxti', models.DateTimeField(blank=True, null=True, verbose_name='Təmirə verilmə vaxtı')),
                ('temir_edildiyi_vaxt', models.DateTimeField(blank=True, null=True, verbose_name='Təmir edildiyi vaxt')),
                ('kim_terefinden_temir_edilib', models.CharField(blank=True, max_length=50, null=True, verbose_name='Kim tərəfindən təmir edilib')),
                ('temir_edilen_zedenin_xususiyyeti', models.CharField(blank=True, max_length=60, null=True, verbose_name='Təmir edilən zədənin xüsusiyyəti')),
                ('statusu', models.BooleanField(default=False, verbose_name='Statusu')),
                ('qeyd', models.CharField(blank=True, max_length=100, null=True, verbose_name='Qeyd')),
                ('sonuncu_duzəlis_tarixi', models.DateTimeField(auto_now=True, null=True, verbose_name='Sonuncu duzəliş tarixi')),
                ('abonent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Sahbuz.nomreler', verbose_name='Abonent')),
                ('kime_temire_verilib', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Sahbuz.montyor', verbose_name='Kimə təmirə verilib')),
                ('olculmus_zedenin_xususiyyeti', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Sahbuz.olculmuszedeninxususiyyeti', verbose_name='Ölçülmüş zədənin xüsusiyyəti')),
                ('operator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_ZedelenmelerinQeydiyyatiJurnali', to=settings.AUTH_USER_MODEL, verbose_name='Zədələnməni qeydə alan Operator')),
                ('operator2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_ZedelenmelerinQeydiyyatiJurnali2', to=settings.AUTH_USER_MODEL, verbose_name='Sonuncu defe düzəliş edən Operator2')),
                ('zedelenmenin_xarakteristikasi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Sahbuz.zedelenmeninxarakteristikasi', verbose_name='Zədələnmənin xarakteristikası')),
            ],
            options={
                'verbose_name': 'Zədələnmələrin qeydiyatı',
                'verbose_name_plural': 'Zədələnmələrin qeydiyyatı',
            },
        ),
        migrations.CreateModel(
            name='Tehkimolunma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qeydə_alinma_tarixi', models.DateTimeField(auto_now_add=True, null=True)),
                ('sonuncu_duzəlis_tarixi', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Sonuncu duzəliş tarixi')),
                ('kpaylayiciskaf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Sahbuz.komekcipaylayiciskaf', verbose_name='Köməkçi paylayıcı skaf')),
                ('montyor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Sahbuz.montyor', verbose_name='Montyor')),
                ('paylayiciskaf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Sahbuz.paylayiciskaf', verbose_name='Paylayıcı şkaf')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_Tehkimolunma', to=settings.AUTH_USER_MODEL, verbose_name='Qeydə alan')),
                ('user2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_Tehkimolunma2', to=settings.AUTH_USER_MODEL, verbose_name='Sonuncu defe düzəliş edən')),
            ],
        ),
        migrations.CreateModel(
            name='PaylayiciSkafdakiKabelNomreleri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kabelin_nomresi', models.CharField(max_length=10, null=True, verbose_name='Kabelin nömrəsi')),
                ('qeyd', models.CharField(blank=True, max_length=50, null=True, verbose_name='Qeyd')),
                ('qeydə_alinma_tarixi', models.DateTimeField(auto_now_add=True, null=True)),
                ('sonuncu_duzəlis_tarixi', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Sonuncu duzəliş tarixi')),
                ('paylayici_skafi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Sahbuz.paylayiciskaf', verbose_name='Paylayıcı şkaf')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_PaylayiciSkafdakiKabelNomreleri', to=settings.AUTH_USER_MODEL, verbose_name='Qeydə alan')),
                ('user2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_PaylayiciSkafdakiKabelNomreleri2', to=settings.AUTH_USER_MODEL, verbose_name='Sonuncu defe düzəliş edən')),
            ],
            options={
                'verbose_name': 'Paylayici Şkafdaki Kabel nömrəsi',
                'verbose_name_plural': 'Paylayici Şkafdaki Kabel Nomrələri',
            },
        ),
        migrations.AddField(
            model_name='nomreler',
            name='eskaf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Sahbuz.paylayiciskafdakikabelnomreleri', verbose_name='Paylayıcı şkaf/kabel_nömrəsi'),
        ),
        migrations.AddField(
            model_name='nomreler',
            name='kskaf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Sahbuz.komekcipaylayiciskafdakikabelnomreleri', verbose_name='Köməkçi paylayıcı şkaf/kabel_nömrəsi'),
        ),
        migrations.AddField(
            model_name='nomreler',
            name='muqavile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Sahbuz.muqavile', verbose_name='Müqavilə nömrəsi/tarixi'),
        ),
        migrations.AddField(
            model_name='nomreler',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_Nomreler', to=settings.AUTH_USER_MODEL, verbose_name='Qeydə alan'),
        ),
        migrations.AddField(
            model_name='nomreler',
            name='user2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_Nomreler2', to=settings.AUTH_USER_MODEL, verbose_name='Sonuncu defe düzəliş edən'),
        ),
        migrations.AddField(
            model_name='montyor',
            name='tehkim_olunmus_paylayici_skaflar',
            field=models.ManyToManyField(blank=True, null=True, through='Sahbuz.Tehkimolunma', to='Sahbuz.paylayiciskaf', verbose_name='Təhkim olunmuş paylayıcı skaflar'),
        ),
        migrations.AddField(
            model_name='montyor',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_Montyor', to=settings.AUTH_USER_MODEL, verbose_name='Qeydə alan'),
        ),
        migrations.AddField(
            model_name='montyor',
            name='user2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_Montyor2', to=settings.AUTH_USER_MODEL, verbose_name='Sonuncu defe düzəliş edən'),
        ),
        migrations.AddField(
            model_name='komekcipaylayiciskaf',
            name='bagli_oldugu_paylayici_skaf',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Sahbuz.paylayiciskaf', verbose_name='Əsas paylayıcı şkaf'),
        ),
        migrations.AddField(
            model_name='komekcipaylayiciskaf',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_KomekciPaylayiciSkaf', to=settings.AUTH_USER_MODEL, verbose_name='Qeydə alan'),
        ),
        migrations.AddField(
            model_name='komekcipaylayiciskaf',
            name='user2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_KomekciPaylayiciSkaf2', to=settings.AUTH_USER_MODEL, verbose_name='Sonuncu defe düzəliş edən'),
        ),
        migrations.CreateModel(
            name='Idare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adi', models.CharField(blank=True, max_length=50, null=True, verbose_name='İdarənin adı')),
                ('yerlesdiyi_rayon', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ünvanı')),
                ('telefon_nomresi', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefon nömrəsi')),
                ('qeydə_alinma_tarixi', models.DateTimeField(auto_now_add=True, null=True)),
                ('sonuncu_duzəlis_tarixi', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Sonuncu duzəliş tarixi')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_Idare', to=settings.AUTH_USER_MODEL, verbose_name='Qeydə alan')),
                ('user2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sahbuz_Idare2', to=settings.AUTH_USER_MODEL, verbose_name='Sonuncu defe düzəliş edən')),
            ],
            options={
                'verbose_name': 'İdarə',
                'verbose_name_plural': 'İdarə haqqinda məlumat',
            },
        ),
    ]
