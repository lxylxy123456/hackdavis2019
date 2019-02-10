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

from django.conf.urls import *
from . import views

urlpatterns = [
    url('^$', views.home, name='index'),
    url('^login/$', views.login, name='index'),
    url('^logout/$', views.logout, name='index'),
    url('^register/$', views.register, name='index'),
]

