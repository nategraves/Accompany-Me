function getFlickr() {
	var api_key = '003772641d5986c33ac7f1ebb2444b01';
	var api_url = 'http://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=' + api_key + '&format=json&text={{where}}&sort=interestingness-desc&privacy_filter=1&safe_search=1&media=photos&per_page=8&jsoncallback=?';
	$.getJSON(api_url, function(data){
		$.each(data.photos.photo, function(k,v){
			var link_url = 'http://flickr.com/' + v.owner + '/' + v.id;
			var img_url = 'http://farm' + v.farm + '.static.flickr.com/' + v.server + '/' + v.id + '_' + v.secret + '_s.jpg';
			$('#photos').append("<a href='" + link_url + "'><img src='" + img_url + "'/>");
		}); 
	}); 
} 
