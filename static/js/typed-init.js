// Initialize Typed.js for the typing animation
document.addEventListener('DOMContentLoaded', function() {
  if (typeof Typed !== 'undefined' && document.querySelector('.typed')) {
    try {
      new Typed('.typed', {
        strings: ['Full Stack Python Developer', 'Freelancer', 'Web Designer'],
        typeSpeed: 150,
        backSpeed: 30,
        backDelay: 2500,
        loop: true
      });
    } catch (e) {
      console.error('Error initializing Typed.js:', e);
    }
  }
});
