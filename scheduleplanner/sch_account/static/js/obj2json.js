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
	return ("<p id=\"" + id + "\">" + type + ": " + msg + "</p>")
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

