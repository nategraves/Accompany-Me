$(function() {
	$('#email_send').click(function() {
		var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;

		$(".error").remove();
		var hasError = false;

		var email = $('#id_email').val();
		if (email === '') {
			$('#id_email_label').after("<span class='error'>Please enter a valid email address</span>");
			hasError = true;
		} else if (!emailReg.test(email)) {
			$('#id_email_label').after("<span class='error'>Please enter a valid email address</span>");
			hasError = true;
		}

		if(hasError === true) { return false; }
		$.post('trip/invite/', function(data) {
			alert('tried posting');
		});
	});
});
