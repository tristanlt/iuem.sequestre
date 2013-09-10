$(document).ready(function() {

if ($('#form-widgets-typemachine').length != 0) {
	$.get('xmltypemachine', function(d){ 
		tagshtml="<div id=\"typemachine-proposed-tags\">"
		$(d).find('li').each(function(){
							var tag = $(this).text();
							tagshtml=tagshtml+" <span class=\"typemachine-proposed-tag\">" + tag + "</span>";
							});
		tagshtml = tagshtml + "</div>";
		$(tagshtml).insertAfter($('#form-widgets-typemachine'));
		$( ".typemachine-proposed-tag" ).click(function() {
			$('#form-widgets-typemachine').val($(this).text());
		});
	})
}
if ($('#form-widgets-typesecret').length != 0) {
	$.get('xmltypesecret', function(d){ 
		tagshtml="<div id=\"typesecret-proposed-tags\">"
		$(d).find('li').each(function(){
							var tag = $(this).text();
							tagshtml=tagshtml+" <span class=\"typesecret-proposed-tag\">" + tag + "</span>";
							});
		tagshtml = tagshtml + "</div>";
		$(tagshtml).insertAfter($('#form-widgets-typesecret'));
		$( ".typesecret-proposed-tag" ).click(function() {
			$('#form-widgets-typesecret').val($(this).text());
		});
	})
}


});