Landing page – static HTML/CSS

Repo con la landing page in HTML/CSS (asset grafici inclusi) e una roadmap per trasformarla in PHP con contenuti gestibili via database testuale (JSON) + toggle per mostrare o nascondere sezioni.

STATO ATTUALE
Layout boxed: 1400px
Sezioni in HTML (no framework)
Asset per sezione organizzati in cartelle
CSS e JS separabili

PROBLEMI NOTI

Sezione Il progetto:
- padding interno non coerente
- impaginazione blocchi a destra da sistemare

Sezione Podcast:
- impaginazione non fedele al mockup
- problemi di padding verticale

OBIETTIVI TECNICI

Conversione a PHP semplice:
- nessun CMS
- include/require
- template per sezione

Database testuale JSON:
- contenuti modificabili senza toccare layout
- nessun MySQL

Toggle sezioni:
- flag enabled nei JSON

Lavoro locale:
php -S localhost:8000

