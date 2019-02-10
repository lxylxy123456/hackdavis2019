/*
 Schedule Planner https://devpost.com/software/hackdavis2019-w5spun
 Copyright (C) 2018  lxylxy123456, Yiling Chen, jingyizhu, wyr
 
 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU Affero General Public License as
 published by the Free Software Foundation, either version 3 of the
 License, or (at your option) any later version.
 
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU Affero General Public License for more details.
 
 You should have received a copy of the GNU Affero General Public License
 along with this program.  If not, see <https://www.gnu.org/licenses/>. 
*/
function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie != '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) == (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}
function csrfSafeMethod(method) {
	// these HTTP methods do not require CSRF protection
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function create_banner(type, msg, id) {
	upper = type.charAt(0).toUpperCase() + type.substr(1);
	return ('  <div id="' + id + '" class="alert alert-' + type + ' alert-dismissible fade in" align="center">\
    <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>\
    <strong>' + upper + '!</strong> ' + msg + '\
  </div>')
}
function Ajax(url, type, data, banner) {
	$.ajax({
		url: url,
		type: type,
		data: data,
		dataType: "json",
		beforeSend: function(xhr, settings) {
			var csrftoken = getCookie('csrftoken');
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
	}).done(function(msg){
		id = 'banner-message-' + Date.now()
		banner.prepend(create_banner(msg['stat'], msg['msg'], id))
		$("#" + id).fadeOut(3000)
		if (msg['redirect'])
			setTimeout("window.location = \"" + msg['redirect'] + "\";", 1000);
		if (msg['reload'])
			setTimeout("window.location.reload()", 1000);
	});
}

