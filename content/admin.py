from django.contrib import admin

# Register your models here.

from content import models
from users import models as models_user
admin.site.register(models.NewContent)
admin.site.register(models.NewCourses)
admin.site.register(models.Questions)
admin.site.register(models.level_lable)
admin.site.register(models_user.UserInfo)
admin.site.register(models_user.AdminUser)
