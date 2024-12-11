from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
# class Account(AbstractBaseUser):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     username = models.CharField(max_length=50, unique=True)
#     email = models.CharField(max_length=100, unique=True)
#     phone_number = models.CharField(max_length=50)

#     # required
#     date_joined = models.DateTimeField(auto_now_add=True)
#     last_login = models.DateTimeField(auto_now_add=True)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#     is_superadmin = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

#     objects = BaseUserManager()

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return self.is_active

#     def has_module_perms(self, add_label):
#         return True

#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'


# class MontyorProfile(models.Model):
#     user = models.OneToOneField(Account, on_delete=models.CASCADE)
#     address_line_1 = models.CharField(max_length=100, blank=True, null=True)
#     address_line_2 = models.CharField(max_length=100, blank=True, null=True)
#     #profile_picture= models.ImageField(blank=True, upload_to='userprofile')
#     city = models.CharField(blank=True, max_length=20)
#     state = models.CharField(max_length=50)
#     country = models.CharField(max_length=50)
#     # created_at = models.DateTimeField(auto_now_add=True)
#     # updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.user.first_name

#     def full_address(self):
#         return self.address_line_1+ " " + self.address_line_2



class Idare(models.Model):
    adi = models.CharField(max_length=50, null=True, verbose_name="İdarənin adı")
    yerlesdiyi_rayon = models.CharField(max_length=50, blank=True, null=True, verbose_name="Ünvanı")
    telefon_nomresi = models.CharField(max_length=15, blank=True, null=True, verbose_name="Telefon nömrəsi")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Qeydə alan", related_name='Ordubad_Idare')
    qeydə_alinma_tarixi = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    user2 = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Sonuncu defe düzəliş edən", related_name='Ordubad_Idare2')
    sonuncu_duzəlis_tarixi = models.DateTimeField(null=True, blank=True, auto_now_add=True, verbose_name="Sonuncu duzəliş tarixi")

    def __str__(self):
        return self.adi

    class Meta:
        verbose_name = 'İdarə'
        verbose_name_plural = 'İdarə haqqinda məlumat'

class Ats(models.Model):
    adi = models.CharField(max_length=30, unique=True, null=True, verbose_name="Adı")
    yerlesdiyi_unvan = models.CharField(max_length=50, blank=True, null=True, verbose_name="Ünvanı")
    telefon_nomresi = models.CharField(max_length=15, blank=True, null=True, verbose_name="Telefon nömrəsi")
    ats_ip = models.CharField(max_length=15,blank=True, null=True, verbose_name="ATS-in IP adresi")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Qeydə alan", related_name='Ordubad_Ats')
    qeydə_alinma_tarixi = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    user2 = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Sonuncu defe düzəliş edən", related_name='Ordubad_Ats2')
    sonuncu_duzəlis_tarixi = models.DateTimeField(null=True, blank=True, auto_now_add=True, verbose_name="Sonuncu duzəliş tarixi")

    def __str__(self):
        return self.adi

    class Meta:
        verbose_name = 'ATS'
        verbose_name_plural = 'ATS-lər'


class Montyor(models.Model):
    adi = models.CharField(max_length=30, null=True, verbose_name="Adı")
    telefon_nomresi = models.CharField(max_length=15, blank=True, null=True, verbose_name="Telefon nömrəsi")
    tehkim_olunmus_paylayici_skaflar = models.ManyToManyField('PaylayiciSkaf', through='Tehkimolunma',
                                                              through_fields=('montyor', 'paylayiciskaf', 'kpaylayiciskaf'), blank=True, null=True, verbose_name="Təhkim olunmuş paylayıcı skaflar")
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Qeydə alan", related_name='Ordubad_Montyor')
    qeydə_alinma_tarixi = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    user2 = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Sonuncu defe düzəliş edən", related_name='Ordubad_Montyor2')
    sonuncu_duzəlis_tarixi = models.DateTimeField(null=True, blank=True, auto_now_add=True, verbose_name="Sonuncu duzəliş tarixi")

    def __str__(self):
        return self.adi

    class Meta:
        verbose_name = 'Montyor'
        verbose_name_plural = 'Montyorlar'


class PaylayiciSkaf(models.Model):
    STATUS_CHOICES = [
        ('tps', 'tps'),
        ('ops', 'ops'),
    ]

    skafin_nomresi = models.CharField(max_length=11, null=True, unique=True, verbose_name="Şkafın nömrəsi") 
    novu = models.CharField(max_length=12, choices=STATUS_CHOICES, blank=True, null=True, verbose_name="Növü")
    mudafie_xetti = models.CharField(max_length=10, blank=True, null=True, verbose_name="Müdafiə xətti")
    magistral = models.CharField(max_length=10, blank=True, null=True, verbose_name="Magistral")
    bolme = models.CharField(max_length=20, blank=True, null=True, verbose_name="Bölmə")
    qeyd = models.CharField(max_length=50, blank=True, null=True, verbose_name="Qeyd")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Qeydə alan", related_name='Ordubad_PaylayiciSkaf')
    qeydə_alinma_tarixi = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    user2 = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Sonuncu defe düzəliş edən", related_name='Ordubad_PaylayiciSkaf2')
    sonuncu_duzəlis_tarixi = models.DateTimeField(null=True, blank=True, auto_now_add=True, verbose_name="Sonuncu duzəliş tarixi")

 #   tabe_oldugu_idare = models.ForeignKey(Idare, on_delete=models.PROTECT, blank=True, null=True)
    # tehkim_olunmus_montyor = models.ManyToManyField(Montyor,  blank=True, verbose_name='Təhkim olummus montyor')
    def __str__(self):
        return self.skafin_nomresi

    class Meta:
        verbose_name = 'Paylayıcı şkaf'
        verbose_name_plural = 'Paylayıcı şkaflar'


class PaylayiciSkafdakiKabelNomreleri(models.Model):
    paylayici_skafi = models.ForeignKey(PaylayiciSkaf, on_delete=models.SET_NULL,  null=True, verbose_name="Paylayıcı şkaf")
    kabelin_nomresi = models.CharField(max_length=10,  null=True, unique=True, verbose_name="Kabelin nömrəsi")
    qeyd = models.CharField(max_length=50, blank=True, null=True, verbose_name="Qeyd")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Qeydə alan", related_name='Ordubad_PaylayiciSkafdakiKabelNomreleri')
    qeydə_alinma_tarixi = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    user2 = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Sonuncu defe düzəliş edən", related_name='Ordubad_PaylayiciSkafdakiKabelNomreleri2')
    sonuncu_duzəlis_tarixi = models.DateTimeField(null=True, blank=True, auto_now_add=True, verbose_name="Sonuncu duzəliş tarixi")


    # bagli_oldugu_paylayici_skaf = models.ManyToManyField(PaylayiciSkaf)

    def __str__(self):
        return f"{self.paylayici_skafi}  {self.kabelin_nomresi}"

    class Meta:
        verbose_name = 'Paylayici Şkafdaki Kabel nömrəsi'
        verbose_name_plural = 'Paylayici Şkafdaki Kabel Nomrələri'



class KomekciPaylayiciSkaf(models.Model):
    STATUS_CHOICES = [
        ('tps', 'tps'),
        ('ops', 'ops'),
    ]

    bagli_oldugu_paylayici_skaf = models.ForeignKey(PaylayiciSkaf, on_delete=models.SET_NULL, null=True, verbose_name="Əsas paylayıcı şkaf")
    kskafin_nomresi = models.CharField(max_length=11, null=True, unique=True, verbose_name="Köməkçi şkaf")
    novu = models.CharField(max_length=12, choices=STATUS_CHOICES, blank=True, null=True, verbose_name="Növü")
    
    mudafie_xetti = models.CharField(max_length=10, blank=True, null=True, verbose_name="Müdafiə xətti")
    magistral = models.CharField(max_length=10, blank=True, null=True, verbose_name="Magistral")
    bolme = models.CharField(max_length=20, blank=True, null=True, verbose_name="Bölmə")
    qeyd = models.CharField(max_length=50, blank=True, null=True, verbose_name="Qeyd")
#    tabe_oldugu_idare = models.ForeignKey(Idare, on_delete=models.PROTECT, blank=True, null=True)
    
    # tehkim_olunmus_montyor = models.ManyToManyField(Montyor,  blank=True, verbose_name='Təhkim olummus montyor')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Qeydə alan", related_name='Ordubad_KomekciPaylayiciSkaf')
    qeydə_alinma_tarixi = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    user2 = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Sonuncu defe düzəliş edən", related_name='Ordubad_KomekciPaylayiciSkaf2')
    sonuncu_duzəlis_tarixi = models.DateTimeField(null=True, blank=True, auto_now_add=True, verbose_name="Sonuncu duzəliş tarixi")

    def __str__(self):
        return self.kskafin_nomresi

    class Meta:
        verbose_name = 'Köməkçi Paylayıcı şkaf'
        verbose_name_plural = 'Köməkçi Paylayıcı şkaflar'
        

class KomekciPaylayiciSkafdakiKabelNomreleri(models.Model):
    paylayici_skafi = models.ForeignKey(KomekciPaylayiciSkaf, on_delete=models.SET_NULL,  null=True, verbose_name="Köməkçi paylayıcı şkaf")
    kskafdaki_kabelin_nomresi = models.CharField(max_length=10,  null=True, unique=True, verbose_name="Köməkçi paylayıcı şkafdaki kabel nömrəsi")
    qeyd = models.CharField(max_length=50, blank=True, null=True, verbose_name="Qeyd")
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Qeydə alan", related_name='Ordubad_KomekciPaylayiciSkafdakiKabelNomreleri')
    qeydə_alinma_tarixi = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    user2 = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Sonuncu defe düzəliş edən", related_name='Ordubad_KomekciPaylayiciSkafdakiKabelNomreleri2')
    sonuncu_duzəlis_tarixi = models.DateTimeField(null=True, blank=True, auto_now_add=True, verbose_name="Sonuncu duzəliş tarixi")

    # bagli_oldugu_paylayici_skaf = models.ManyToManyField(PaylayiciSkaf)

    def __str__(self):
        return f"{self.paylayici_skafi} {self.kskafdaki_kabelin_nomresi}"

    class Meta:
        verbose_name = 'Komekci Paylayici Şkafdaki Kabel nömrəsi'
        verbose_name_plural = 'Komekci Paylayici Şkafdaki Kabel Nomrələri'


class Muqavile(models.Model):
    muqavile_nomresi = models.CharField(max_length=10, null=True, verbose_name="Müqavilə nömrəsi")
    muqavileni_tarixi = models.DateField(null=True, verbose_name="Müqavilənin tarixi")
    qeyd = models.CharField(max_length=50, blank=True, null=True, verbose_name="Qeyd")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Qeydə alan", related_name='Ordubad_Muqavile')
    qeydə_alinma_tarixi = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    user2 = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Sonuncu defe düzəliş edən", related_name='Ordubad_Muqavile2')
    sonuncu_duzəlis_tarixi = models.DateTimeField(null=True, blank=True, auto_now_add=True, verbose_name="Sonuncu duzəliş tarixi")

    def __str__(self):
        return f"{self.muqavile_nomresi} / {self.muqavileni_tarixi}"
    
    class Meta:
        verbose_name = 'Müqavilə'
        verbose_name_plural = 'Müqavilələr'


class Tehkimolunma(models.Model):
    montyor = models.ForeignKey(Montyor, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Montyor")
    paylayiciskaf = models.ForeignKey(PaylayiciSkaf, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Paylayıcı şkaf")
    kpaylayiciskaf = models.ForeignKey(KomekciPaylayiciSkaf, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Köməkçi paylayıcı skaf")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Qeydə alan", related_name='Ordubad_Tehkimolunma')
    qeydə_alinma_tarixi = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    user2 = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Sonuncu defe düzəliş edən", related_name='Ordubad_Tehkimolunma2')
    sonuncu_duzəlis_tarixi = models.DateTimeField(null=True, blank=True, auto_now_add=True, verbose_name="Sonuncu duzəliş tarixi")

    def __str__(self):
        return str(self.montyor)



class Nomreler(models.Model):
    KABEL_CEKILME = [
        ('yeralti', 'yeralti'),
        ('hava', 'hava')
    ]

    nomre = models.CharField(max_length=11, unique=True, verbose_name="Nömrə")
    abonent = models.CharField(max_length=50, blank=True, null=True, verbose_name="Abonent")
    unvan = models.CharField(max_length=50, blank=True, verbose_name="Abonentin ünvanı")
    eskaf = models.ForeignKey(PaylayiciSkafdakiKabelNomreleri, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Paylayıcı şkaf/kabel_nömrəsi")
    kskaf = models.ForeignKey(KomekciPaylayiciSkafdakiKabelNomreleri, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Köməkçi paylayıcı şkaf/kabel_nömrəsi")
    ats = models.ForeignKey(Ats, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ATS")
    ats_oturma_yeri = models.CharField(max_length=15, blank=True, null=True, verbose_name="ATS-də oturma yeri")
    internet_port_nomresi = models.CharField(max_length=50, null=True, blank=True, verbose_name="İnternet port nömrəsi")
    muqavile = models.ForeignKey(Muqavile, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Müqavilə nömrəsi/tarixi")
    abonentin_elaqe_nomresi = models.CharField(max_length=25, blank=True, null=True, verbose_name="Abonentin əlaqə nömrəsi")
    qeyd = models.CharField(max_length=50, blank=True, null=True, verbose_name="Qeyd")
    sahenin_nomresi = models.CharField(max_length=20, blank=True, verbose_name="Sahənin nömrəsi")
    kabelin_cekilme_veziyyeti = models.CharField(max_length=10, choices=KABEL_CEKILME, blank=True,null=True, verbose_name="Kabelin çəkilmə vəziyyəti")
    qirmaqlarin_yeri = models.CharField(max_length=25, blank=True, verbose_name="Qırmaqların yeri")
    uzunlugu = models.IntegerField(blank=True, null=True, verbose_name="Uzunluğu")
    derece = models.CharField(max_length=20, blank=True, verbose_name="Dərəcə")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Qeydə alan", related_name='Ordubad_Nomreler')
    qeydə_alinma_tarixi = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    user2 = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Sonuncu defe düzəliş edən", related_name='Ordubad_Nomreler2')
    sonuncu_duzəlis_tarixi = models.DateTimeField(null=True, blank=True, auto_now_add=True, verbose_name="Sonuncu duzəliş tarixi")
# Diğer alanlar
    def esas_skaf(self):
        return f"{self.esas_skaf}"
    
    def komekci_skaf(self):
        return f"{self.kskaf}"

    def __str__(self):
        return self.nomre

    class Meta:
        verbose_name = 'Nömrə'
        verbose_name_plural = 'Nömrələr'


class ZedelenmeninXarakteristikasi(models.Model):
    sebeb = models.CharField(max_length=50, null=True, blank=True, unique=True, verbose_name="Yeni xarakteristika")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Qeydə alan", related_name='Ordubad_ZedelenmeninXarakteristikasi')
    qeydə_alinma_tarixi = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    user2 = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Sonuncu defe düzəliş edən", related_name='Ordubad_ZedelenmeninXarakteristikasi2')
    sonuncu_duzəlis_tarixi = models.DateTimeField(null=True, blank=True, auto_now_add=True, verbose_name="Sonuncu duzəliş tarixi")

    def __str__(self):
        return str(self.sebeb)
    
    class Meta:
        verbose_name = 'Zədələnmənin xarakteristikası'
        verbose_name_plural = 'Zədələnmənin xarakteristikaları'
    

    
class OlculmusZedeninXususiyyeti(models.Model):
    sebeb = models.CharField(max_length=50, null=True, blank=True, unique=True, verbose_name="Yeni Xüsusiyyət")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Qeydə alan", related_name='Ordubad_OlculmusZedeninXususiyyeti')
    qeydə_alinma_tarixi = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    user2 = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Sonuncu defe düzəliş edən", related_name='Ordubad_OlculmusZedeninXususiyyeti2')
    sonuncu_duzəlis_tarixi = models.DateTimeField(null=True, blank=True, auto_now_add=True, verbose_name="Sonuncu duzəliş tarixi")

    def __str__(self):
        return str(self.sebeb)
    class Meta:
        verbose_name = 'Ölçülmüş zəfənin xarakteristikası'
        verbose_name_plural = 'Ölçülmüş zədənin xarakteristikaları'    




class ZedelenmelerinQeydiyyatiJurnali(models.Model):
    abonent= models.ForeignKey(Nomreler, on_delete=models.DO_NOTHING,verbose_name="Abonent")

    zedelenmenin_xarakteristikasi = models.ForeignKey(ZedelenmeninXarakteristikasi, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name="Zədələnmənin xarakteristikası")
    melumatin_daxil_oldugu_vaxt = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name="Məlumatın daxil olduğu vaxt")
    melumatin_mezmunu = models.CharField(max_length=60, blank=True, null=True, verbose_name="Məlumatın məzmunu")

    temire_verilme_vaxti = models.DateTimeField(blank=True, null=True, verbose_name="Təmirə verilmə vaxtı")
    kime_temire_verilib = models.ForeignKey(Montyor, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name="Kimə təmirə verilib")
    olculmus_zedenin_xususiyyeti = models.ForeignKey(OlculmusZedeninXususiyyeti, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name="Ölçülmüş zədənin xüsusiyyəti")

    temir_edildiyi_vaxt = models.DateTimeField(blank=True, null=True, verbose_name="Təmir edildiyi vaxt")
    kim_terefinden_temir_edilib = models.CharField(max_length=50, blank=True, null=True, verbose_name="Kim tərəfindən təmir edilib")
    temir_edilen_zedenin_xususiyyeti = models.CharField(max_length=60, blank=True, null=True, verbose_name="Təmir edilən zədənin xüsusiyyəti")

    statusu = models.BooleanField(default=False, verbose_name="Statusu")
    qeyd = models.CharField(max_length=100, null=True, blank=True, verbose_name="Qeyd")
    operator = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Qeydə alan", related_name='Ordubad_ZedelenmelerinQeydiyyatiJurnali')
    operator2 = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Sonuncu defe düzəliş edən", related_name='Ordubad_ZedelenmelerinQeydiyyatiJurnali2')
    sonuncu_duzəlis_tarixi = models.DateTimeField(null=True, blank=True, auto_now=True, verbose_name="Sonuncu duzəliş tarixi")
    # introducer = models.ForeignKey(User, 
    #     help_text = "This field will be calculated automatically", 
    #     blank=True, null=True, on_delete=models.CASCADE) 

    def __str__(self):
        return str(self.abonent)
    
    def abonentin_adi(self):
        return f"{self.abonent.abonent}"
    
    
    class Meta:
        verbose_name = 'Zədələnmələrin qeydiyatı'
        verbose_name_plural = 'Zədələnmələrin qeydiyyatı'
