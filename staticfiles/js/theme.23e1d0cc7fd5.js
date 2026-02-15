/**
 * Dark Mode / Theme Toggler
 * Persists preference in localStorage and toggles 'data-theme' attribute on <html>
 */

document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('theme-toggle');
    const icon = themeToggle ? themeToggle.querySelector('i') : null;

    // Check for saved user preference, if any, on load of the website
    const currentTheme = localStorage.getItem('theme') || 'light';

    // Apply valid theme to document
    if (currentTheme === 'dark') {
        document.documentElement.setAttribute('data-theme', 'dark');
        if (icon) {
            icon.classList.remove('bi-moon');
            icon.classList.add('bi-sun');
        }
    }

    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            const current = document.documentElement.getAttribute('data-theme');

            if (current === 'dark') {
                // Switch to Light
                document.documentElement.removeAttribute('data-theme');
                localStorage.setItem('theme', 'light');
                if (icon) {
                    icon.classList.remove('bi-sun');
                    icon.classList.add('bi-moon');
                }
            } else {
                // Switch to Dark
                document.documentElement.setAttribute('data-theme', 'dark');
                localStorage.setItem('theme', 'dark');
                if (icon) {
                    icon.classList.remove('bi-moon');
                    icon.classList.add('bi-sun');
                }
            }
        });
    }
});
