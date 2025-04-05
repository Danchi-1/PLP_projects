const floatingElements = document.querySelectorAll('.floating');
floatingElements.forEach(el => {
    el.addEventListener('mouseenter', () => {
        el.style.color = '#ff5733';
    });
    el.addEventListener('mouseleave', () => {
        el.style.color = '#fff';
    });
});