document.addEventListener('DOMContentLoaded', () => {
    const sections = document.querySelectorAll('.section');

    sections.forEach((section, index) => {
        setTimeout(() => {
            section.style.opacity = '1';
            section.style.transform = 'translateY(0)';
        }, index * 500);
    });

    const footer = document.querySelector('footer');
    footer.style.opacity = '1';
    footer.style.transform = 'translateY(0)';
});
