# 
# Schedule Planner https://devpost.com/software/hackdavis2019-w5spun
# Copyright (C) 2018  lxylxy123456, Yiling Chen, jingyizhu, wyr
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# 

from django.contrib import admin
from django.conf.urls import include, url

from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^static/(?P<path>.*)$', serve, settings.STATIC_DICT),
    url(r'^media/(?P<path>.*)$', serve, settings.MEDIA_DICT),

	url(r'^', include('sch_account.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
