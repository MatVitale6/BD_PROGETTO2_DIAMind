# 8 Gennaio

Argomenti: CDN, DNS scheduling, Distribuzione Globale, HTTP Redirect, IP anycast, Scheduling Gerarchico, Siti mirror
.: Yes

## Distribuzione globale

Quando si è nel caso di `distribuzione globale` i server non stanno più tutti quanti all’interno di un data center o un load balancer ma stanno in giro per il mondo.

## Sistemi web distribuiti

Nei sistemi di distribuzione locale si è visto che si usa il meccanismo di `packet-redirection`; in questo caso si hanno `siti mirror`,`HTTP-redirect`,`DNS` e `IP-anycast`. Si parla anche di algoritmi e gerarchie di scheduling.

I server, a seconda del meccanismo di distribuzione, potrebbero avere:

- diversi nomi, diversi indirizzi IP
- un solo nome, diversi indirizzi IP
- un solo nome, un solo indirizzo IP

## Siti mirror

Questo meccanismo permette di avere lo stesso servizio corrispondente con tanti nomi diversi. Per esempio i nomi possono essere `www.site-italy.com`,`www.site-usa.com` con un indirizzo IP diverso per ogni nome e quindi per ogni server. A questo punto è l’utente che sceglie il server tipicamente da una pagina di partenza e quindi è proprio lui stesso a fare li meccanismo di redirezione scegliendo in base alla località geografica.

- `pro`: architettura semplice
- `contro`: replicazione visibile per l’utente e nessuna modalità di controllo della distribuzione del carico

---

## HTTP redirection

Questo meccanismo è la cosa più semplice da fare dal punto di vista tecnologico perchè fa parte dello standard dal `HTTP 1.0`. In pratica il server risponde dicendo che la risorsa che si sta cercando si trova da un altra parte.

Usando questo approccio si può realizzare uno scheduling distribuito, perchè tutti i server possono partecipare a riassegnare le richieste rendendo finalmente questo processo trasparente all’utente ma non per il client. La ridirezione può essere attraverso un indirizzo IP o un nome.

## HTTP redirection - politiche di redirect

Il meccanismo di attivazione può essere `centralizzato` cioè si ha un server specifico che bilancia il carico oppure è `distribuito` cioè qualsiasi server può bilanciare il carico, magari quando è in sovraccarico da la responsabilià a un altro server.

- `pro`: piena compatibilità con i client e con i server senza introdurre un punto critico la cui caduta rende indisponibile il sistema
- `contro`: consente di ridirigere solo le richieste HTTP, può aumentare traffico e tempo di risposta perchè il client instaura 2 connessioni HTTP per ogni richiesta, e a ogni richiesta si potrebbero avere più redirection.

---

## Scheduling basato su DNS

In questo caso lo scheduling viene effettuato nella fase di lookup della risorsa:

- il client chiede l’indirizzo IP corrispondente al nome del sito
- riceve uno specifico indirizzo IP, che al momento è il migliore fra i possibili, e un opportuno TTL. Il TTL indica per quanto tempo è valida la scelta di quello specifico server

La difficoltà è il `caching` dell’indirizzo IP nei DNS intermedi per tutto il TTL.

## TTL dei record

- `TTL costante`: una possibilità è settare TTL con valori molto bassi, per avere pieno controllo dello scheduling da parte del DNS. Il problema è che alcuni name server potrebbero non collaborare e si potrebbe sovraccaricare il name server autorità del sito.

- `TTL adattativo`: si modifica dinamicamente il valore in base al carico sui server e la frequenza con cui vengono fatte le richieste su un certo dominio

## Difficoltà nell’approccio

A causa del caching, i DNS controllano solo una parte del traffico destinato ad un certo sito. Per affontare il problema si cerca di diminuire il valore del TTL ma se viene ridotto troppo potrebbe non avere effetto sulla cache dei browser e alcuni DNS non cooperativi potrebbero ignorare TTL molto piccoli.

---

## IP anycast

Nel caso si fosse in scala geografica e si volesse utlizzare un solo indirizzo IP allora si usa il meccanismo di `IP-anycast`, che consiste nell’annunciare l’indirizzo IP contenente una replica del servizio web da diversi AS. 

Il BGP di ogni AS in internet sceglie l’annuncio che corrisponde alla metrica migliore (per esempio l’as-path più breve), quindi si ha che il client invierà le richieste alla replica più vicina.

L’indirizzamento dei server può avvenire solo per nome o solo per indirizzo IP.

---

## Difficoltà dello scheduling

Una buona allocazione del client al server tiene conto del carico del server e la prossimità tra client e server. Il carico del server è funzione di giorno e ora, fusi orari e distribuzione geografica degli utenti.

## Algoritmi di scheduling

Si deve trovare un modo per scegliere quale server risponderà alle richieste del client:

- `selezione possibile`: si usa HTTP redirect oppure DNS scheduling
- `selezione non possibile`: si usano i siti mirror perchè il server stesso viene selezionato dall’utente oppure si usa IP anycast dove il server è implicitamente scelto dalla posizione del client nella rete.

Basandosi anche sulle difficoltà si ottengono 2 tipi di algoritmi:

- `statici`: round robin o funzione hash
- `dinamici`: si basano sulla conoscenza di informazioni sul client (prossimità client-server), conoscenza dello stato del server (server meno carico) oppure entrambi

## Scheduling gerarchico

Consiste nel far uso di più meccanismi di scheduling in successione, esistono 2 tipi:

- `scheduling a due livelli`:
    - il primo livello basato su DNS considerando per esempio la posizione del client
    - il secondo livello è basato su HTTP redirect
- `scheduling a tre livelli`:
    - il primo livello è basato su anycast, partizionando i client per continente di appartenenza
    - il secondo livello è basato su DNS scheduling
    - il terzo livello è basato su HTTP redirect

---

## Content delivery networks

I `content provider` distribuiscono contenuti a milioni di utenti tramite le `content delivery networks` mandando contenuti agli utenti da multipli server geograficamente distribuiti situati sulla frontiera della rete.

Akamai è la rete più estesa e distribuita al mondo; quello che fa è mettere tutti i customer sulla stessa infrastruttura di distribuzione.

## Strategia di Akamai

La strategia è quella di realizzare un servizio di distribuzione globale basato su un’unica rete centrato su cluster, dove questi cluster possono essere collocati all’interno dei provider points of presence oppure sui points of presence di akamai. Akamai permette anche di standardizzare i requisiti dei content provider classificando i contenuti statici e dinamici.

## Standardizzazione del content provider

I server Akamai memorizzano permanentemente i contenuti statici, mentre i contenuti dinamici sono rilevati dinamicamente sul sito originale del distributore di contenuti.

## Misura dello stato della rete

Akamai misura costantemente lo stato della rete fra i points of presence. I valori che sono collezionati sono utilizzati per scegliere quale è la replica giusta per distribuire i contenuti e anche per identificare nella rete i cammini che sono a più alta velocità e sfruttarli.