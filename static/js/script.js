/* Author: 

*/

$(function() {
	$('#add_why').live('click', function(){
		$('#add_why').remove();
		$('.why').last().after("<input type='text' class='grid_5 alpha why' /><br class='clear'/>").slideDown();
		$('.why').last().after("<a href='#' id='add_why' class='grid_2 alpha omega'>Add another interest</a>");
	});
});




















