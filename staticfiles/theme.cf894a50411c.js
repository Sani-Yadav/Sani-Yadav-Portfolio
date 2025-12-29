/* Theme switcher for site
   - Saves choice to localStorage
   - Detects system preference
   - Injects a toggle into a sensible place (header if present, else floating FAB)
*/
(function(){
  const KEY = 'site-theme';
  const getPreferredTheme = ()=>{
    const stored = localStorage.getItem(KEY);
    if(stored) return stored;
    if(window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) return 'dark';
    return 'light';
  };

  const applyTheme = (theme)=>{
    if(theme === 'dark') document.documentElement.setAttribute('data-theme','dark');
    else document.documentElement.removeAttribute('data-theme');
    try{ localStorage.setItem(KEY, theme); }catch(e){}
  };

  const toggleTheme = ()=>{
    const current = document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
    const next = current === 'dark' ? 'light' : 'dark';
    applyTheme(next);
    updateKnob(next);
  };

  const createToggle = ()=>{
    const wrapper = document.createElement('div');
    wrapper.className = 'theme-toggle-wrapper';

    const btn = document.createElement('button');
    btn.setAttribute('aria-label','Toggle theme');
    btn.className = 'theme-toggle-button';
    btn.type = 'button';

    const knob = document.createElement('span');
    knob.className = 'theme-toggle-knob';
    btn.appendChild(knob);

    // Optional label icons
    const icon = document.createElement('span');
    icon.className = 'theme-toggle-icon';
    wrapper.appendChild(btn);

    btn.addEventListener('click', toggleTheme);

    return {wrapper, btn, knob};
  };

  let knobEl = null;
  const updateKnob = (theme)=>{
    if(!knobEl) return;
    if(theme === 'dark') document.documentElement.setAttribute('data-theme','dark');
    else document.documentElement.removeAttribute('data-theme');
  };

  const injectToggle = ()=>{
    const {wrapper, btn, knob} = createToggle();
    knobEl = knob;

    // Try to place inside header if present
    const header = document.querySelector('#header') || document.querySelector('header') || document.querySelector('.navbar');
    if(header){
      // place at top-right inside header
      wrapper.classList.add('theme-toggle');
      // create container to place nicely
      const container = document.createElement('div');
      container.style.marginLeft = 'auto';
      container.style.display = 'flex';
      container.style.alignItems = 'center';
      container.appendChild(wrapper);
      // Insert before first nav or at end
      const nav = header.querySelector('.navmenu') || header.querySelector('nav');
      if(nav && nav.parentNode){ nav.parentNode.insertBefore(container, nav.nextSibling); }
      else header.appendChild(container);
      container.prepend(btn);
    } else {
      // fallback: floating FAB
      const fab = document.createElement('div');
      fab.className = 'theme-toggle-fab';
      fab.appendChild(btn);
      document.body.appendChild(fab);
    }
    // set initial knob state
    const current = document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
    updateKnob(current);
  };

  // Initialize theme on DOMContentLoaded
  document.addEventListener('DOMContentLoaded', function(){
    const theme = getPreferredTheme();
    applyTheme(theme);
    injectToggle();
    // watch for system changes if no explicit user choice
    if(!localStorage.getItem(KEY) && window.matchMedia){
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e=>{
        applyTheme(e.matches ? 'dark' : 'light');
        updateKnob(e.matches ? 'dark' : 'light');
      });
    }
  });

})();
