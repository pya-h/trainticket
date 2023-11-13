(function ($) {
	
	"use strict";

	// Page Ready


	// Header Scrolling Set White Background
	scrollNavBar();


	// Welcome Area background image
	if($('.welcome-area').length){
		$('.welcome-area .welcome-bg').css("background-image", "url(" + $('.welcome-area .welcome-bg').data('bg') + ")");
	}


	// Menu Dropdown Toggle
	if($('.menu-trigger').length){
		$(".menu-trigger").on('click', function() {	
			$(this).toggleClass('active');
			$('.header-area .nav').slideToggle(200);
		});
	}


	// Scroll animation init
	window.sr = new scrollReveal();


	// Home number counterup
	if($('.count-item').length){
		$('.count-item strong').counterUp({
			delay: 10,
			time: 1000
		});
	}


	// App single gallery
	if($('.gallery').length && $('.gallery-item').length){
		$('.gallery-item').magnificPopup({
			type: 'image',
			gallery: {
				enabled: true
			},
			zoom: {
				enabled: true,
				duration: 300,
				easing: 'ease-in-out',
			}
		});
	}


	// Page standard gallery
	if($('.page-gallery').length && $('.page-gallery-wrapper').length){
		$('.page-gallery').imgfix({
			scale: 1.1
		});

		$('.page-gallery').magnificPopup({
			type: 'image',
			gallery: {
				enabled: true
			},
			zoom: {
				enabled: true,
				duration: 300,
				easing: 'ease-in-out',
			}
		});
	}


	// Blog cover image
	if($('.blog-post-thumb').length){
		$('.blog-post-thumb .img').imgfix();
	}



	// Page loading animation
	$(window).on('load', function() {
		if($('.cover').length){
			$('.cover').parallax({
				imageSrc: $('.cover').data('image'),
				zIndex: '1'
			});
		}

		$(".loader-wrapper").animate({
			'opacity': '0'
		}, 600, function(){
			setTimeout(function(){
				// Parallax init
				if($('.parallax').length){
					$('.parallax').parallax({
						imageSrc: 'assets/images/photos/parallax.jpg',
						zIndex: '1'
					});
				}
				$(".loader-wrapper").css("visibility", "hidden").fadeOut();
			}, 300);
		});
	});



	// Header Scrolling Set White Background
	$(window).on('scroll', function() {
		scrollNavBar();
	});


	// Navbar Scroll Set White Background Function
	function scrollNavBar() {
		var width = $(window).width();
		if(width > 991) {
			var scroll = $(window).scrollTop();
			if (scroll >= 30) {
				$(".header-area").addClass("header-sticky");
				$(".header-area .dark-logo").css('display', 'block');
				$(".header-area .light-logo").css('display', 'none');
			}else{
				$(".header-area").removeClass("header-sticky");
				$(".header-area .dark-logo").css('display', 'none');
				$(".header-area .light-logo").css('display', 'block');
			}
		}
	}


})(window.jQuery);