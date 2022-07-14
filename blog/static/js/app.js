var swiper = new Swiper(".slide-1", {
	navigation: {
	  nextEl: ".swiper-button-next",
	  prevEl: ".swiper-button-prev",
	},
	autoplay: {
		delay: 2500,
		disableOnInteraction: false,
	},
});


var swiper = new Swiper(".slide-2", {
	slidesPerView: 1,
	spaceBetween: 10,
	autoplay: {
		delay: 1000,
		disableOnInteraction: false,
	},
	breakpoints: {
	  640: {
		slidesPerView: 2,
		spaceBetween: 10,
	  },
	  768: {
		slidesPerView: 4,
		spaceBetween: 20,
	  },
	  1024: {
		slidesPerView: 5,
		spaceBetween: 20,
	  },
	},
	loop: true,
});