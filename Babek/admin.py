import datetime
from django.contrib import admin

from Babek.models import Ats, Idare, KomekciPaylayiciSkaf, KomekciPaylayiciSkafdakiKabelNomreleri, Montyor, Muqavile, OlculmusZedeninXususiyyeti, PaylayiciSkaf, Nomreler, Tehkimolunma, PaylayiciSkafdakiKabelNomreleri, \
    ZedelenmelerinQeydiyyatiJurnali, ZedelenmeninXarakteristikasi


from import_export import resources
from import_export.admin import ImportExportMixin, ImportExportModelAdmin, ExportActionModelAdmin





class TehkimolunmaInline(admin.TabularInline):
    model = Tehkimolunma
    extra = 1
    raw_id_fields = ['paylayiciskaf', 'kpaylayiciskaf' ]


class ZedelenmeInline(admin.TabularInline):
    model = ZedelenmelerinQeydiyyatiJurnali
    extra = 0
    fields = ['abonent','statusu','melumatin_daxil_oldugu_vaxt','zedelenmenin_xarakteristikasi',
                    'temire_verilme_vaxti', 'kime_temire_verilib', 'kim_terefinden_temir_edilib','temir_edildiyi_vaxt',
                    'temir_edilen_zedenin_xususiyyeti', 'qeyd']
    classes = ('collapse',)
    readonly_fields = ['abonent','statusu','melumatin_daxil_oldugu_vaxt','zedelenmenin_xarakteristikasi',
                    'temire_verilme_vaxti', 'kime_temire_verilib', 'kim_terefinden_temir_edilib','temir_edildiyi_vaxt',
                    'temir_edilen_zedenin_xususiyyeti', 'qeyd']

class IdareAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change, *args, **kwargs):
        if obj.user is None:
            obj.user = request.user
                
        obj.user.save_as_continue = request.user
        obj.user2 = request.user
        super(IdareAdmin, self).save_model(request, obj, form, change, *args, **kwargs)

    readonly_fields=['user', 'user2']
    list_display = ['adi', 'yerlesdiyi_rayon', 'telefon_nomresi', 'user','qeydə_alinma_tarixi','user2','sonuncu_duzəlis_tarixi']

    


class MontyorAdmin(ExportActionModelAdmin, admin.ModelAdmin):
    def save_model(self, request, obj, form, change, *args, **kwargs):
        if obj.user is None:
            obj.user = request.user
        
        obj.user.save_as_continue = request.user
        obj.user2 = request.user
        super(MontyorAdmin, self).save_model(request, obj, form, change, *args, **kwargs)

    

    list_display = ['adi','telefon_nomresi' ]
    readonly_fields=['user', 'user2']
    # filter_horizontal = ('tehkim_olunmus_paylayici_skaflar',)
    inlines = (TehkimolunmaInline,)


class PaylayiciSkafAdmin(ExportActionModelAdmin, admin.ModelAdmin):
    def save_model(self, request, obj, form, change, *args, **kwargs):
        if obj.user is None:
            obj.user = request.user
        
        obj.user.save_as_continue = request.user
        obj.user2 = request.user
        super(PaylayiciSkafAdmin, self).save_model(request, obj, form, change, *args, **kwargs)

    readonly_fields=['user', 'user2']

    list_display = ['skafin_nomresi', 'novu', 'mudafie_xetti',  'magistral', 'bolme', 'qeyd']
    # filter_horizontal = ('montyor', 'kabel_nomresi',)
    inlines = (TehkimolunmaInline,)
    list_filter = ['novu']
    search_fields = ['skafin_nomresi', 'magistral']

class PaylayiciSkafdakiKabelNomreleriAdmin(ExportActionModelAdmin, admin.ModelAdmin):
    def save_model(self, request, obj, form, change, *args, **kwargs):
        if obj.user is None:
            obj.user = request.user
        
        obj.user.save_as_continue = request.user
        obj.user2 = request.user
        super(PaylayiciSkafdakiKabelNomreleriAdmin, self).save_model(request, obj, form, change, *args, **kwargs)

    readonly_fields=['user', 'user2']

    list_display = ['paylayici_skafi','kabelin_nomresi']
    raw_id_fields = ['paylayici_skafi']
    search_fields = ['paylayici_skafi__skafin_nomresi', 'kabelin_nomresi__iexact']
   # inlines = (TehkimolunmaInline,)


class KomekciPaylayiciSkafAdmin(ExportActionModelAdmin,admin.ModelAdmin):
    def save_model(self, request, obj, form, change, *args, **kwargs):
        if obj.user is None:
            obj.user = request.user
        
        obj.user.save_as_continue = request.user
        obj.user2 = request.user
        super(KomekciPaylayiciSkafAdmin, self).save_model(request, obj, form, change, *args, **kwargs)

    readonly_fields=['user', 'user2']

    list_display = ['kskafin_nomresi', 'novu', 'bagli_oldugu_paylayici_skaf', 'mudafie_xetti', 'magistral', 'bolme', 'qeyd']
    # filter_horizontal = ('montyor', 'kabel_nomresi',)
    inlines = (TehkimolunmaInline,)
    list_filter = ['novu']
    search_fields = ['bagli_oldugu_paylayici_skaf__skafin_nomresi', 'kskafin_nomresi']

class KomekciPaylayiciSkafdakiKabelNomreleriAdmin(ExportActionModelAdmin,admin.ModelAdmin):
    def save_model(self, request, obj, form, change, *args, **kwargs):
        if obj.user is None:
            obj.user = request.user
        
        obj.user.save_as_continue = request.user
        obj.user2 = request.user
        super(KomekciPaylayiciSkafdakiKabelNomreleriAdmin, self).save_model(request, obj, form, change, *args, **kwargs)

    readonly_fields=['user', 'user2']

    list_display = ['paylayici_skafi','kskafdaki_kabelin_nomresi']
    raw_id_fields = ['paylayici_skafi']
    search_fields = ['paylayici_skafi__kskafin_nomresi','kskafdaki_kabelin_nomresi__iexact']
   # inlines = (TehkimolunmaInline,)

class MuqavileAdmin(ExportActionModelAdmin, admin.ModelAdmin):
    def save_model(self, request, obj, form, change, *args, **kwargs):
        if obj.user is None:
            obj.user = request.user
        
        obj.user.save_as_continue = request.user
        obj.user2 = request.user
        super(MuqavileAdmin, self).save_model(request, obj, form, change, *args, **kwargs)

    readonly_fields=['user', 'user2']

    list_display = ['muqavile_nomresi', 'muqavileni_tarixi']
    search_fields=['muqavile_nomresi__iexact', 'muqavileni_tarixi']
    list_filter =['muqavileni_tarixi']


class NomrelerAdmin(ExportActionModelAdmin, admin.ModelAdmin):
    def save_model(self, request, obj, form, change, *args, **kwargs):
        if obj.user is None:
            obj.user = request.user
        
        obj.user.save_as_continue = request.user
        obj.user2 = request.user
        super(NomrelerAdmin, self).save_model(request, obj, form, change, *args, **kwargs)

    readonly_fields=['user', 'user2']

    list_display = ['nomre', 'abonent', 'unvan', 'eskaf','kskaf', 'ats','ats_oturma_yeri','internet_port_nomresi','muqavile','abonentin_elaqe_nomresi','qeyd']
    list_filter = ['ats']
    raw_id_fields = ['kskaf','ats', 'eskaf','muqavile']
    search_fields = ['nomre__iexact', 'muqavile__muqavile_nomresi', 'eskaf__paylayici_skafi__skafin_nomresi__iexact', 'eskaf__kabelin_nomresi__iexact', ]
    list_display_links = ['nomre']
    list_per_page = 50
    inlines = (ZedelenmeInline,)


class ZedelenmeninXarakteristikasiAdmin(ExportActionModelAdmin, admin.ModelAdmin):
    def save_model(self, request, obj, form, change, *args, **kwargs):
        if obj.user is None:
            obj.user = request.user
        
        obj.user.save_as_continue = request.user
        obj.user2 = request.user
        super(ZedelenmeninXarakteristikasiAdmin, self).save_model(request, obj, form, change, *args, **kwargs)

    readonly_fields=['user', 'user2']

    list_display = ['sebeb']

class OlculmusZedeninXususiyyetiAdmin(ExportActionModelAdmin, admin.ModelAdmin):
    def save_model(self, request, obj, form, change, *args, **kwargs):
        if obj.user is None:
            obj.user = request.user
        
        obj.user.save_as_continue = request.user
        obj.user2 = request.user
        super(OlculmusZedeninXususiyyetiAdmin, self).save_model(request, obj, form, change, *args, **kwargs)

    readonly_fields=['user', 'user2']

    list_display = ['sebeb']

class ZedelenmelerinQeydiyyatiJurnaliAdmin(ExportActionModelAdmin, admin.ModelAdmin):
    def save_model(self, request, obj, form, change, *args, **kwargs):
        if obj.operator is None:
            obj.operator = request.user
        
        obj.operator.save_as_continue = request.user
        obj.operator2 = request.user
        super(ZedelenmelerinQeydiyyatiJurnaliAdmin, self).save_model(request, obj, form, change, *args, **kwargs)

    list_display = ['abonentin_adi','abonent', 'statusu','melumatin_daxil_oldugu_vaxt','zedelenmenin_xarakteristikasi',
                    'temire_verilme_vaxti', 'kime_temire_verilib', 'kim_terefinden_temir_edilib','temir_edildiyi_vaxt',
                    'temir_edilen_zedenin_xususiyyeti', 'operator','operator2','sonuncu_duzəlis_tarixi', 'qeyd']
   
    search_fields = ['abonent__nomre__iexact', 'melumatin_daxil_oldugu_vaxt']  # Arama yapmak istediğiniz alanları buraya ekleyin
    raw_id_fields = ['abonent']  # Başlığın açılan pencerede arama kutusu olarak görünmesini sağlar
    list_filter = ['statusu','kime_temire_verilib','zedelenmenin_xarakteristikasi', 'melumatin_daxil_oldugu_vaxt', 'temire_verilme_vaxti']
    list_per_page = 50
    readonly_fields = ['operator','operator2']


class AtsAdmin(ExportActionModelAdmin, admin.ModelAdmin):
    def save_model(self, request, obj, form, change, *args, **kwargs):
        if obj.user is None:
            obj.user = request.user
        
        obj.user.save_as_continue = request.user
        obj.user2 = request.user
        super(AtsAdmin, self).save_model(request, obj, form, change, *args, **kwargs)

    readonly_fields=['user', 'user2']

    list_display = ['adi', 'yerlesdiyi_unvan', 'telefon_nomresi', 'ats_ip']




admin.site.register(Idare, IdareAdmin)
admin.site.register(Montyor, MontyorAdmin)
admin.site.register(PaylayiciSkaf, PaylayiciSkafAdmin)
admin.site.register(Nomreler, NomrelerAdmin)
admin.site.register(PaylayiciSkafdakiKabelNomreleri, PaylayiciSkafdakiKabelNomreleriAdmin)
admin.site.register(KomekciPaylayiciSkafdakiKabelNomreleri, KomekciPaylayiciSkafdakiKabelNomreleriAdmin)
admin.site.register(ZedelenmelerinQeydiyyatiJurnali, ZedelenmelerinQeydiyyatiJurnaliAdmin)
admin.site.register(KomekciPaylayiciSkaf, KomekciPaylayiciSkafAdmin)
admin.site.register(Ats, AtsAdmin)
admin.site.register(ZedelenmeninXarakteristikasi, ZedelenmeninXarakteristikasiAdmin)
admin.site.register(OlculmusZedeninXususiyyeti, OlculmusZedeninXususiyyetiAdmin)
admin.site.register(Muqavile, MuqavileAdmin)