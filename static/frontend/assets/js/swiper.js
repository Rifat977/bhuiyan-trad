const swiper = new Swiper(".swiper", {
    slidesPerView: 1,
    spaceBetween: 10,
    allowSlideNext: true,
    allowSlidePrev: true,
    // using "ratio" endpoints
    autoplay: {
        delay: 3000,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    breakpoints: {
        "@0.75": {

            slidesPerView: 3,
            spaceBetween: 40,
        },
        "@1.00": {
            slidesPerView: 3,
            spaceBetween: 100,
        },
        "@1.50": {

            slidesPerView: 3,
            spaceBetween: 200,
        },
    },
});

const swipers = document.querySelector(".swiper").swiper;

// Now you can use all slider methods like
swipers.slideNext();