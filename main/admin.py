from django.contrib import admin

from .models import *
# Register your models here.


class SkillTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ProjectTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Settings)
admin.site.register(SocialLink)
admin.site.register(AboutMe)
admin.site.register(Experience)
admin.site.register(ExperienceType)
admin.site.register(AboutMeMore)
admin.site.register(Skill)
admin.site.register(SkillType, SkillTypeAdmin)
admin.site.register(ProjectType, ProjectTypeAdmin)
admin.site.register(Project)
admin.site.register(Contact)
