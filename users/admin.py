from django.contrib import admin
from users.models import User, UserAnswer,UserPassedTest

admin.site.register(User)
admin.site.register(UserAnswer)
admin.site.register(UserPassedTest)