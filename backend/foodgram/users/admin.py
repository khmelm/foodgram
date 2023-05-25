from django.contrib import admin

from .models import Subscription, UserFoodgram


class FollowingInLine(admin.TabularInline):
    model = Subscription
    fk_name = 'author'
    extra = 0


class FollowerInLine(admin.TabularInline):
    model = Subscription
    fk_name = 'user'
    extra = 0


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username')
    search_fields = ('username', 'email')
    list_filter = ('username', 'email')
    empty_value_display = '-пусто-'
    inlines = [FollowerInLine, FollowingInLine]


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'user')
    search_fields = ('author',)
    empty_value_display = '-пусто-'


admin.site.register(UserFoodgram, UserAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
