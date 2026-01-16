/* Tu che ne sAI? - landing main.js
   Nota per manutenzione:
   - Per nascondere una sezione: aggiungi class="is-hidden" al relativo <section>.
   - In futuro qui dentro possiamo spostare eventi/materiali in una struttura dati e renderizzarli.
*/

window.LANDING_CONFIG = window.LANDING_CONFIG || {
  // terreno pronto: quando vorrai, eventi/materiali possono stare qui
  events: [],
  materials: [],
};

// micro-smooth-scroll for internal anchors (if you add a nav later)
    document.addEventListener('click', (e) => {
      const a = e.target.closest('a[href^="#"]');
      if(!a) return;
      const id = a.getAttribute('href');
      if(id.length < 2) return;
      const el = document.querySelector(id);
      if(!el) return;
      e.preventDefault();
      el.scrollIntoView({behavior:'smooth', block:'start'});
    });
