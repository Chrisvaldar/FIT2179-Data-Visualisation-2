// Main scripts for Data Viz Project

(function($) {

	$(window).load(function() {
		// Init Isotope
		var $container = $('#container').isotope({
			itemSelector: '.isotope-item',
			layoutMode: 'fitRows',
		});

		// Bind filter button click
		$('#filters').on('click', 'button', function() {
			var filterValue = $(this).attr('data-filter');
			// use filterFn if matches value

			$container.isotope({
				filter: filterValue
			});
		});

		// Bind sort button click
		$('#sorts').on('click', 'button', function() {
			var sortByValue = $(this).attr('data-sort-by');
			$container.isotope({
				sortBy: sortByValue
			});
		});

		// Change is-checked class on buttons
		$('.button-group').each(function(i, buttonGroup) {
			var $buttonGroup = $(buttonGroup);
			$buttonGroup.on('click', 'button', function() {
				$buttonGroup.find('.is-checked').removeClass('is-checked');
				$(this).addClass('is-checked');
			});
		});

	});


	$(document)
		.ready(function() {

			$('#toggle-family')
				.click(function() {
					$(this)
						.toggleClass('current');
					$('.toggle')
						.not(this)
						.removeClass('current');
					$('#family')
						.toggleClass('current-filter');
					$('#family')
						.slideToggle("slow");
					$('.button-group')
						.not('#family')
						.removeClass('current-filter');
					$('.button-group')
						.not('#family')
						.slideUp();
					$('#filters')
						.toggleClass('open');
					$(".dmbs-content")
						.toggleClass('active-family');
					$(".dmbs-content")
						.removeClass('active-shape')
					$(".dmbs-content")
						.removeClass('active-function')
					$(".dmbs-content")
						.removeClass('active-input')
					$(".dmbs-content")
						.removeClass('active-search')
					$("#nav-main")
						.addClass('hide-mobile');
					//$('#nav-main').slideToggle();
				});

			$('#close-family')
				.click(function() {
					$(".dmbs-content")
						.removeClass('active-family');
					$('#family')
						.removeClass('flip current-filter');
				});

			$('#toggle-input')
				.click(function() {
					$(this)
						.toggleClass('current');
					$('.toggle')
						.not(this)
						.removeClass('current');
					$('#input')
						.toggleClass('current-filter');
					$('#input')
						.slideToggle("slow");
					$('.button-group')
						.not('#input')
						.removeClass('current-filter');
					$('.button-group')
						.not('#input')
						.slideUp();
					$('#filters')
						.toggleClass('open');
					$(".dmbs-content")
						.toggleClass('active-input');
					$(".dmbs-content")
						.removeClass('active-shape')
					$(".dmbs-content")
						.removeClass('active-function')
					$(".dmbs-content")
						.removeClass('active-search')
					$(".dmbs-content")
						.removeClass('active-family')
					$("#nav-main")
						.addClass('hide-mobile');
					//$('#nav-main').slideToggle();
				});

			$('#close-input')
				.click(function() {
					$(".dmbs-content")
						.removeClass('active-input');
					$('#input')
						.removeClass('flip current-filter');
				});

			$('#toggle-function')
				.click(function() {
					$(this)
						.toggleClass('current');
					$('.toggle')
						.not(this)
						.removeClass('current');
					$('#function')
						.toggleClass('current-filter');
					$('#function')
						.slideToggle("slow");
					$('.button-group')
						.not('#function')
						.removeClass('current-filter');
					$('.button-group')
						.not('#function')
						.slideUp();
					$('#filters')
						.toggleClass('open');
					$(".dmbs-content")
						.toggleClass('active-function');
					$(".dmbs-content")
						.removeClass('active-shape')
					$(".dmbs-content")
						.removeClass('active-search')
					$(".dmbs-content")
						.removeClass('active-input')
					$(".dmbs-content")
						.removeClass('active-family')
					$("#nav-main")
						.addClass('hide-mobile');
					//$('#nav-main').slideToggle();
				});

			$('#close-function')
				.click(function() {
					$(".dmbs-content")
						.removeClass('active-function');
					$('#function')
						.removeClass('flip current-filter');
				});

			$('#toggle-shape')
				.click(function() {
					$(this)
						.toggleClass('current');
					$('.toggle')
						.not(this)
						.removeClass('current');
					$('#shape')
						.toggleClass('current-filter');
					$('#shape')
						.slideToggle("slow");
					$('.button-group')
						.not('#shape')
						.removeClass('current-filter');
					$('.button-group')
						.not('#shape')
						.slideUp();
					$('#filters')
						.toggleClass('open');
					$(".dmbs-content")
						.toggleClass('active-shape');
					$(".dmbs-content")
						.removeClass('active-search')
					$(".dmbs-content")
						.removeClass('active-function')
					$(".dmbs-content")
						.removeClass('active-input')
					$(".dmbs-content")
						.removeClass('active-family')
					$("#nav-main")
						.addClass('hide-mobile');
					//$('#nav-main').slideToggle();
				});

			$('#close-shape')
				.click(function() {
					$(".dmbs-content")
						.removeClass('active-shape');
					$('#shape')
						.removeClass('flip current-filter');
				});

			$('#toggle-search')
				.click(function() {
					$(this)
						.toggleClass('current');
					$('.toggle')
						.not(this)
						.removeClass('current');
					$('#search')
						.toggleClass('current-filter');
					$('#search')
						.slideToggle("slow");
					$('.button-group')
						.not('#search')
						.removeClass('current-filter');
					$('.button-group')
						.not('#search')
						.slideUp();
					$('#filters')
						.toggleClass('open');
					$(".dmbs-content")
						.toggleClass('active-search');
					$(".dmbs-content")
						.removeClass('active-shape')
					$(".dmbs-content")
						.removeClass('active-function')
					$(".dmbs-content")
						.removeClass('active-input')
					$(".dmbs-content")
						.removeClass('active-family')
					$("#nav-main")
						.addClass('hide-mobile');
					//$('#nav-main').slideToggle();
				});

			$('#close-search')
				.click(function() {
					$(".dmbs-content")
						.removeClass('active-search');
					$('#search')
						.removeClass('flip current-filter');
				});

			$("#s")
				.attr("placeholder", "Search for a visualization type");

			$("#nav-toggle")
				.click(function() {

					if ($("#nav-toggle")
						.hasClass("active")) {
						$('#nav-main')
							.hide();
						$("#nav-main")
							.removeClass('hide-mobile');
						$(".dmbs-content")
							.removeClass('active-search');
						$(".dmbs-content")
							.removeClass('active-shape')
						$(".dmbs-content")
							.removeClass('active-function')
						$(".dmbs-content")
							.removeClass('active-input')
						$(".dmbs-content")
							.removeClass('active-family')
						$(this)
							.removeClass("active");
					} else {
						$('#nav-main')
							.slideToggle();
						$(this)
							.toggleClass("active");
						$("#nav-main")
							.removeClass('hide-mobile');
					}

				});

			$("#nav-toggle")
				.click(function() {
					$('#filters .button-group')
						.removeClass("current-filter");
					$('.button-group')
						.slideUp();
				});

			$(".button-group .button")
				.click(function() {
					/*$('#filters .button-group').removeClass( "flip current-filter" );
					$(".dmbs-content").toggleClass('active-search');
					$(".dmbs-content").removeClass('active-shape')
					$(".dmbs-content").removeClass('active-function')
					$(".dmbs-content").removeClass('active-input')
					$(".dmbs-content").removeClass('active-family')
					$(".dmbs-content").removeClass('active-search')
					$( "#nav-toggle" ).removeClass("active")*/
					$("#nav-main")
						.addClass('hide-mobile');
				});

			if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
				$(".button-group .button")
					.click(function() {
						$('#filters .button-group')
							.removeClass("current-filter");
						$('#filters .button-group')
							.slideUp();
						$(".dmbs-content")
							.toggleClass('active-search');
						$(".dmbs-content")
							.removeClass('active-shape')
						$(".dmbs-content")
							.removeClass('active-function')
						$(".dmbs-content")
							.removeClass('active-input')
						$(".dmbs-content")
							.removeClass('active-family')
						$(".dmbs-content")
							.removeClass('active-search')
						$("#nav-toggle")
							.removeClass("active")
						$("#nav-main")
							.addClass('hide-mobile');
					});
			}

			/*var closeMenu = function(){
			    $('.button-group').removeClass('flip current-filter');
			    $('#nav-toggle').removeClass('active');
			    $(".dmbs-content").removeClass('active-family');
			    $(".dmbs-content").removeClass('active-shape')
			    $(".dmbs-content").removeClass('active-function')
			    $(".dmbs-content").removeClass('active-input')
			    $(".dmbs-content").removeClass('active-search')
			    
			}
			*/

			var isMobile = {
				Android: function() {
					return navigator.userAgent.match(/Android/i);
				},
				BlackBerry: function() {
					return navigator.userAgent.match(/BlackBerry/i);
				},
				iOS: function() {
					return navigator.userAgent.match(/iPhone|iPad|iPod/i);
				},
				Opera: function() {
					return navigator.userAgent.match(/Opera Mini/i);
				},
				Windows: function() {
					return navigator.userAgent.match(/IEMobile/i);
				},
				any: function() {
					return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());
				}
			};

			if (isMobile.any()) {
				console.log('You are using a mobile device!');
			} else {
				$(window)
					.scroll(function() {

						if ($(this)
							.scrollTop() > 0) {
							$('.current-filter')
								.slideUp();
						} else {
							$('.current-filter')
								.slideDown();
						}
					});
			}

	// Replace all SVG images with inline SVG
	$('img.svg')
		.each(function() {
			var $img = $(this);
			var imgID = $img.attr('id');
			var imgClass = $img.attr('class');
			var imgURL = $img.attr('src');

			$.get(imgURL, function(data) {
				// Get the SVG tag, ignore the rest
				var $svg = $(data)
					.find('svg');

				// Add replaced image's ID to the new SVG
				if (typeof imgID !== 'undefined') {
					$svg = $svg.attr('id', imgID);
				}
				// Add replaced image's classes to the new SVG
				if (typeof imgClass !== 'undefined') {
					$svg = $svg.attr('class', imgClass + ' replaced-svg');
				}

				// Remove any invalid XML tags as per http://validator.w3.org
				$svg = $svg.removeAttr('xmlns:a');

				// Replace image with new SVG
				$img.replaceWith($svg);

			}, 'xml');

		});
		
		// Initialize the Lightbox automatically for any links to images with extensions .jpg, .jpeg, .png or .gif
		$("a[href$='.jpg'], a[href$='.png'], a[href$='.jpeg'], a[href$='.gif']").fancybox();

		// Initialize the Lightbox and add rel="gallery" to all gallery images when the gallery is set up using [gallery link="file"] so that a Lightbox Gallery exists
		$(".gallery a[href$='.jpg'], .gallery a[href$='.png'], .gallery a[href$='.jpeg'], .gallery a[href$='.gif']").attr('rel', 'gallery').fancybox();

		// Initalize the Lightbox for any links with the 'video' class and provide improved video embed support
		$(".fancybox").fancybox({
			maxWidth: 800,
			maxHeight: 800,
			fitToView: true,
			autoSize: false,
			closeClick: false,
			openEffect: 'elastic',
			closeEffect: 'elastic',
			helpers: {
				title: {
					type: 'inside'
				}
			}
		});

		$('#input .slider').slick({
			dots: false,
			infinite: false,
			speed: 300,
			slidesToShow: 6,
			slidesToScroll: 2,
			variableWidth: true,
			responsive: [{
					breakpoint: 1024,
					settings: {
						slidesToShow: 2,
						slidesToScroll: 1
					}
				},
				{
					breakpoint: 600,
					settings: {
						slidesToShow: 4,
						slidesToScroll: 1
					}
				},
				{
					breakpoint: 480,
					settings: {
						slidesToShow: 2,
						slidesToScroll: 1
					}
				}
				// You can unslick at a given breakpoint now by adding:
				// settings: "unslick"
				// instead of a settings object
			]
		});

	});

})(jQuery);