$(document).ready(function () {
			  $(".navbar-toggle").on("click", function () {
				    $(this).toggleClass("active");
			  });
		});

$('#nav-affix').affix({
    offset: {
        top: $('#nav-affix').offset().top
    }
});