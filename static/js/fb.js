function fbLogin() {
	FB.getLoginStatus(function(response) {
		if (response.authResponse) {
			FB.api('/me', function(response) {
				getFBFriends();     
			});
		} else {
			$('#fb-photo-holder').append("<a id='fb-button' href='#'><image src='/static/images/facebook-connect.png'/></a>");
			$('#fb-button').click(function() {
				FB.login(function(response) {
					getFBFriends();
				}, {scope: 'email, publish_stream'});
			}); 
		}
	});
}

function getFBFriends() {
	if ($('#fb-button')) {
		$('#fb-button').remove();
	}
	FB.api('/me/friends', function(response) {
		for(i=0; i<=23; i++) {
			var fb_url = 'http://facebook.com/' + response.data[i].id;
			var fb_photo_url = 'https://graph.facebook.com/' + response.data[i].id + '/picture/';
			var linked_image = "<div class='fb-photo'><a href='" + fb_url + "'/><img src='" + fb_photo_url + "'/></a><p><a href=" + fb_url + ">" + response.data[i].name + "</a></p></div>";
			$('#fb-photo-holder').append(linked_image);
		}
		$('#fb-photo-holder').append("<br class='clear'/>");
	});
}
