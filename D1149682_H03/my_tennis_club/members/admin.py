from django.contrib import admin
from .models import Member
from .models import Court

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)

admin.site.register(Member, MemberAdmin)
admin.site.register(Court)