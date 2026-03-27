const track = document.getElementById('track');
const trackReverse = document.getElementById('track-reverse');

const reverseStartOffset = -1200;
const scrollSpeed = -0.65;
const scrollSpeedReverse = 0.65;

// Apply initial offset immediately
trackReverse.style.transform = `translateX(${reverseStartOffset}px)`;

window.addEventListener('scroll', () => {
  const y = window.scrollY;

  const x = y * scrollSpeed;
  const xReverse = reverseStartOffset + (y * scrollSpeedReverse);

  track.style.transform = `translateX(${x}px)`;
  trackReverse.style.transform = `translateX(${xReverse}px)`;
});

// Fade in text on scroll
const fadeElements = document.querySelectorAll('.opacity-scroll');

function updateOpacity() {
  fadeElements.forEach(element => {
    const rect = element.getBoundingClientRect();
    const windowHeight = window.innerHeight;

    // Define where fade starts and ends
    const fadeStart = windowHeight * 0.5;
    const fadeEnd = windowHeight * 0.4;

    // Calculate opacity based on position between fadeStart and fadeEnd
    if (rect.top >= fadeStart) {
      // Below fade start - invisible
      element.style.opacity = 0;
    } else if (rect.top <= fadeEnd) {
      // Above fade end - fully visible
      element.style.opacity = 1;
    } else {
      // In between - calculate opacity
      const fadeRange = fadeStart - fadeEnd;
      const distanceFromStart = fadeStart - rect.top;
      let opacity = distanceFromStart / fadeRange;
      
      // Apply easing
      opacity = opacity ** 2;
      
      element.style.opacity = opacity;
    }
  });
}

window.addEventListener('scroll', updateOpacity);
updateOpacity();

// Slideshow functionality
const slides = document.querySelectorAll('.slide');
let currentSlide = 0;

function showNextSlide() {
  slides[currentSlide].classList.remove('active');
  currentSlide = (currentSlide + 1) % slides.length;
  slides[currentSlide].classList.add('active');
}

// Change slide every 3 seconds
setInterval(showNextSlide, 3000);