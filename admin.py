from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin

from piston.models import Consumer
from basketauth.admin import ConsumerAdmin
from subscriptions.models import Subscription, Subscriber


class BasketAdmin(admin.sites.AdminSite):
    pass

site = BasketAdmin()
site.register(Group, GroupAdmin)
site.register(User, UserAdmin)
site.register(Consumer, ConsumerAdmin)
site.register(Subscriber)
site.register(Subscription)
