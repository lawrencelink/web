'''
    Copyright (C) 2017 Gitcoin Core 

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.

'''
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import EmailSubscriber, Stat, LeaderboardRank, Match

# Register your models here.
class GeneralAdmin(admin.ModelAdmin):
    ordering = ['-id']


admin.site.register(Match, GeneralAdmin)
admin.site.register(Stat, GeneralAdmin)
admin.site.register(EmailSubscriber, GeneralAdmin)
admin.site.register(LeaderboardRank, GeneralAdmin)
