from django.contrib import admin
from .models import classeGrammaticale, ClasseNominale, MotEton, Traduction, Exemple

# Register your models here. 
class ExempleInline(admin.TabularInline):
    model = Exemple
    extra = 1

class TraductionInline(admin.TabularInline):
    model = Traduction
    extra = 2 


class TraductionAdmin(admin.ModelAdmin):
    list_display = ('id', 'mot', 'mot_francais')
    list_display_links = ('id', 'mot')
    inlines = [ExempleInline]

class ClassNominaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'description')
    list_display_links = ('id',)
    list_editable = ('description', 'nom')    

class classeGrammaticaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'abbreviation', 'nom')
    list_display_links = ('id',)
    list_editable = ('abbreviation', 'nom')

class MotEtonAdmin(admin.ModelAdmin):
    list_display = ('id', 'mot_eton', 'pluriel')
    list_display_links = ('mot_eton',)
    search_fields = ('mot_eton',)
    #list_editable = ('mot_francais',)
    #list_filter = ('mot_eton',)
    inlines = [TraductionInline]

 

admin.site.register(classeGrammaticale, classeGrammaticaleAdmin)

admin.site.register(MotEton, MotEtonAdmin)

admin.site.register(Traduction, TraductionAdmin)

admin.site.register(ClasseNominale, ClassNominaleAdmin)

 
