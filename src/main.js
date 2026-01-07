import './style.css'

// Wait for DOM to be ready
document.addEventListener('DOMContentLoaded', function () {
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });

                // Trigger circle animation if navigating to contact section
                if (targetId === '#contact') {
                    // Wait for scroll to complete before drawing circle
                    setTimeout(() => {
                        const formElement = document.querySelector('#contact-form');
                        if (formElement) {
                            drawCircleHighlight(formElement);
                        }
                    }, 800);
                }
            }
        });
    });

    // Check if page loaded with #contact hash
    if (window.location.hash === '#contact') {
        setTimeout(() => {
            const formElement = document.querySelector('#contact-form');
            if (formElement) {
                drawCircleHighlight(formElement);
            }
        }, 1000);
    }
});

// Draw animated underline beneath element
function drawCircleHighlight(element) {
    console.log('Drawing underline highlight'); // Debug log

    // Remove any existing highlight
    const existingHighlight = document.querySelector('.highlight-underline');
    if (existingHighlight) {
        existingHighlight.remove();
    }

    // Get element dimensions
    const rect = element.getBoundingClientRect();

    // Create SVG element with fixed positioning
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.classList.add('highlight-underline');
    svg.style.position = 'fixed';
    svg.style.top = '0';
    svg.style.left = '0';
    svg.style.width = '100vw';
    svg.style.height = '100vh';
    svg.style.pointerEvents = 'none';
    svg.style.zIndex = '9999';

    // Create defs for gradient stroke
    const defs = document.createElementNS('http://www.w3.org/2000/svg', 'defs');
    const gradient = document.createElementNS('http://www.w3.org/2000/svg', 'linearGradient');
    gradient.setAttribute('id', 'underline-gradient');
    gradient.setAttribute('x1', '0%');
    gradient.setAttribute('y1', '0%');
    gradient.setAttribute('x2', '100%');
    gradient.setAttribute('y2', '0%');

    // Create gradient stops for opacity fade
    const stop1 = document.createElementNS('http://www.w3.org/2000/svg', 'stop');
    stop1.setAttribute('offset', '0%');
    stop1.setAttribute('style', 'stop-color:#3b82f6;stop-opacity:0.3');

    const stop2 = document.createElementNS('http://www.w3.org/2000/svg', 'stop');
    stop2.setAttribute('offset', '50%');
    stop2.setAttribute('style', 'stop-color:#3b82f6;stop-opacity:0.9');

    const stop3 = document.createElementNS('http://www.w3.org/2000/svg', 'stop');
    stop3.setAttribute('offset', '100%');
    stop3.setAttribute('style', 'stop-color:#3b82f6;stop-opacity:0.3');

    gradient.appendChild(stop1);
    gradient.appendChild(stop2);
    gradient.appendChild(stop3);
    defs.appendChild(gradient);
    svg.appendChild(defs);

    // Create hand-drawn underline path
    const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');

    // Position line below the element with some padding
    const padding = 10;
    const startX = rect.left - padding;
    const endX = rect.right + padding;
    const baseY = rect.bottom + 8;

    // Generate a slightly wobbly hand-drawn line
    const numPoints = 25;
    const segmentLength = (endX - startX) / numPoints;
    let pathData = '';

    for (let i = 0; i <= numPoints; i++) {
        const x = startX + (i * segmentLength);
        // Reduced vertical wobble for subtler effect
        const wobble = (Math.random() - 0.5) * 1.5;
        const y = baseY + wobble;

        if (i === 0) {
            pathData += `M ${x} ${y}`;
        } else {
            // Use quadratic curves for smoother hand-drawn effect
            const prevX = startX + ((i - 1) * segmentLength);
            const prevWobble = (Math.random() - 0.5) * 1;
            const controlX = (prevX + x) / 2;
            const controlY = baseY + prevWobble;

            pathData += ` Q ${controlX} ${controlY}, ${x} ${y}`;
        }
    }

    path.setAttribute('d', pathData);
    path.setAttribute('fill', 'none');
    path.setAttribute('stroke', 'url(#underline-gradient)');
    path.setAttribute('stroke-linecap', 'round');
    path.setAttribute('stroke-linejoin', 'round');

    // Variable stroke width - thicker in middle, thinner at ends
    const strokeWidthValues = [];
    for (let i = 0; i <= numPoints; i++) {
        const progress = i / numPoints;
        // Create a curve that's thicker in the middle
        const thickness = 1.5 + Math.sin(progress * Math.PI) * 2;
        strokeWidthValues.push(thickness);
    }
    // Use average thickness for now (SVG doesn't support variable stroke width easily)
    path.setAttribute('stroke-width', '3');

    svg.appendChild(path);
    document.body.appendChild(svg);

    // Calculate path length for animation
    const pathLength = path.getTotalLength();
    path.style.strokeDasharray = pathLength;
    path.style.strokeDashoffset = pathLength;

    console.log('Underline appended to body'); // Debug log

    // Animate the underline drawing from left to right
    setTimeout(() => {
        path.style.opacity = '1';
        path.style.transition = 'stroke-dashoffset 0.9s ease-in-out';
        path.style.strokeDashoffset = '0';

        // Smooth fade out after drawing
        setTimeout(() => {
            path.style.transition = 'opacity 1.5s ease-out';
            path.style.opacity = '0';
        }, 1000);

        // Remove element after animation completes
        setTimeout(() => {
            svg.remove();
        }, 2600);
    }, 50);
}
