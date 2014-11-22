from django.contrib import admin

# Register your models here.
from .models import Track

from actions import export_as_excel

class TrackAdmin(admin.ModelAdmin):
	list_display  = ('artist','title', 'order', 'album', 'player', 'es_pharrel')
	list_filter   = ('artist', 'album') #Filtros en django
	search_fields = ('title','artist__first_name')
	list_editable = ('title',)
	actions = (export_as_excel,)#Export to excel
	raw_id_fields = ('artist',)#Cuando me traiga artistas solo muestreme el id

	def es_pharrel(self , obj):
		return obj.id == 1

	es_pharrel.boolean = True #Para que no salga true o false si no un icono cooll	

admin.site.register(Track, TrackAdmin)

