$(document).ready(function() {
	$.ajax({
  		url: 'http://localhost:51708/api/values',
  		method: 'GET',
		dataType : 'jsonp',
		success: function(response ){
			console.log(response);
		}
	});
});