function createParticle() {
    const particle = document.createElement('div');
    particle.classList.add('particle');
    const size = Math.random() * 20 + 5;
    particle.style.width = `${size}px`;
    particle.style.height = `${size}px`;
    const x = Math.random() * window.innerWidth;
    const y = Math.random() * window.innerHeight;
    particle.style.left = `${x}px`;
    particle.style.top = `${y}px`;
    const color = Math.random() > 0.5 ? '#2E86C1' : '#5DADE2';
    particle.style.backgroundColor = color;
    particle.style.animationDelay = `${Math.random() * 3}s`;
    document.body.appendChild(particle);
  }
  
  window.onload = () => {
    for (let i = 0; i < 50; i++) {
      createParticle();
    }
  };
  