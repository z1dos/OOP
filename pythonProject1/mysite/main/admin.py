from django.contrib import admin
from .models import DefUser
from .models import Bb, AdditionalImage, Caregory, AddCommentary
from .forms import BbAdminForm


class AddCommentaryComInLine(admin.TabularInline):
   model = AddCommentary


class AdditionalImageInline(admin.TabularInline):
   model = AdditionalImage


class CategoryAdmin(admin.ModelAdmin):
   list_display = ['name']


class BbAdmin(admin.ModelAdmin):
   list_display = ('author', 'title', 'description', 'category', 'image', 'status', 'created')
   fields = ('author', 'status', 'title', 'description', 'category', 'image')
   inlines = (AdditionalImageInline, AddCommentaryComInLine)
   list_filter = ('status', 'category')
   form = BbAdminForm
   # class Meta:
   #    model = Bb
   #    if (Bb.status == 'Выполнено'):
   #       fields = ('author', 'status', 'title', 'description', 'category', 'image')
   #       inlines = (AdditionalImageInline, AddCommentaryComInLine)


admin.site.register(Bb, BbAdmin)

admin.site.register(Caregory, CategoryAdmin)

admin.site.register(DefUser)

admin.site.register(AdditionalImage)

