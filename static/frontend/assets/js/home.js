const swiper = new Swiper(".swiper", {
  slidesPerView: 1,
  spaceBetween: 10,
  
  autoplay: {
    delay: 3000,
  },
 
  breakpoints: {
    "@0.75": {
      slidesPerView: 1,
      spaceBetween: 40,
    },
    "@1.00": {
      slidesPerView: 2,
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
