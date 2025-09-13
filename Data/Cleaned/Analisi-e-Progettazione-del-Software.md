---
author:
- "*Giacomo Sturm*"
date: |
  *Dipartimento di Ingegneria Civile, Informatica e delle Tecnologie Aeronautiche  
  Università degli Studi “Roma Tre"*
title: |
  **Analisi e Progettazione del Software**  
  Appunti delle Lezioni di Analisi e Progettazione del Software  
  *Anno Accademico: 2024/25*
---

\providecommand{\labelText}[2]{#1}

# Introduzione all’Analisi ed alla Progettazione

Una buona conoscenza di linguaggi di programmazione, orientati agli oggetti, non è sufficiente a sviluppare software di qualità, bisogna necessariamente sviluppare capacità di analisi e progettazione del software, orientate agli oggetti, in questo corso. Sviluppare software di qualità è complesso e richiede una approccio ingegneristico. Il punto critico si basa sui ragionamenti non sui linguaggi di programmazione usati, poiché permette di ottenere competenze trasversali. Sono richieste quindi competenze di programmazione, ma non si tratterà di programmazione, o almeno non prevalentemente in questo corso.

Un sistema software deve implementare un insieme di funzionalità e fornire anche delle qualità, deve essere realizzato in modo da resistere a guasti o errori, poiché un software con funzionalità eccellenti, ma senza qualità è un software scadente. Di analisi e progettazione delle qualità se ne parlerà in corsi futuri. Ci si concentra sul minimo indispensabile, l’analisi e progettazione delle funzionalità. Le problematiche dello sviluppo software dipendono, in parte, dal paradigma di programmazione utilizzato, per un software orientato agli oggetti, le problematiche da analizzare e risolvere riguardano principalmente oggetti e le loro definizioni, descrizioni, responsabilità, funzioni, etc. L’analisi e la progettazione del software non sostituiscono la programmazione, ma forniscono indicazioni buone per realizzare un software di qualità. Nell’ingegneria del software non ci sono teoremi, solo esperienze passate, affinché non si commettano gli stessi errori. In generale bisogna prima effettuare un’analisi dei requisiti indipendente dal paradigma, poi un’analisi orientata agli oggetti OOA, *Object Oriented Analysis*, ed infine la progettazione orientata agli oggetti OOD, *Object Oriented Design*. Prima bisogna comprendere il problema, poi formalizzarlo in modo da essere utile per attività successive, ed infine nella progettazione si considerano gli elementi del linguaggio orientato agli oggetti per impostare l’attività. Seguite queste fasi di analisi e progettazione è possibile effettivamente implementare il software, diminuendo via via il livello di astrazione per arrivare alla fase di programmazione con nozioni utili per realizzare un software di qualità. Queste attività altamente creative e possono essere studiate per apprendere i fondamenti della progettazione.

Un’attività fondamentale è la modellazione, un modello è una semplificazione della realtà, descrivendo tutte e sole le caratteristiche di interesse. Esistono tanti tipi di modelli con finalità diverse, è utile applicarne tanti per produrre del buon software. In questo corso la modellazione sarà una parte centrale sia dell’analisi che della progettazione. La modellazione favorisce il ragionamento e la comunicazione tra progettisti in modo efficace. È necessario comunicare non solo con altri progettisti, ma anche con noi stessi a distanza di tempo. L’importanza dei modelli è l’idea che rappresentano, e la differenza tra i modelli è il modo in cui questa idea viene comunicata.

Per realizzare modelli si utilizzerà la notazione visuale standard UML, *Unified Modelling Language*, sopratutto per modelli relativi a software OO. Ci interessa ragionare in termini di OO, e la modellazione aiuta e facilita questi ragionamenti in termini di concetti di OO. Una buona notazione semplifica il lavoro ed i ragionamenti alla comunicazione, questo è lo scopo di UML, riuscire a pensare in termini di oggetti. UML rappresenta uno strumento, non può aiutare nel caso non si abbiano basi di analisi e progettazione, fornisce una buona notazione per descrivere gli elementi principali in termini OO e favorisce la comprensione e la comunicazione, come scopo primario.

Nella programmazione orientata agli oggetti bisogna scrivere classi, definire le informazioni ed i metodi di istanza per le classi, i problemi dello sviluppo OO consistono nell’individuare questi elementi. Il problema principale è comprendere quali sono gli oggetti e come collaborano tra di loro, in generale può essere basata sull’allocazione della responsabilità tra gli oggetti. Per la progettazione si seguirà l’approccio della progettazione guidata dalla responsabilità e queste verranno assegnate in base a pattern, un pattern è una soluzione esemplare ad un problema ricorrente, come GRASP o GoF.

Se quello che viene effettuato nell’analisi e progettazione del software non fornisce alcun suggerimento utile per la scrittura del codice, allora non è una buon’analisi. Queste attività preliminari devono fornire informazioni utili su come scrivere il software. L’analisi non è interessata alla soluzione del problema, quindi non si parla di software durante l’analisi, può essere stabilito come deve essere utilizzato, ma per discutere come deve essere il software bisogna trattare la progettazione. La progettazione riguarda come si può realizzare una soluzione concettuale soddisfando i requisiti per il sistema, senza trattare direttamente la sua implementazione. Tuttavia se si tratta di come può essere risolto il problema e come è realizzato il software non si considera l’implementazione, assegnata alla programmazione.

Ci sono diversi modi in cui l’analisi e la progettazione possono essere effettuate, in questo corso si tratteranno nell’ambito di OO. L’analisi OOA si basa principalmente sull’identificazione dei concetti del problema, simile all’analisi concettuale trattata in basi di dati. Nella progettazione OOD si tratta di software e gli elementi sono indirettamente collegati alla realtà ma non rappresentano direttamente gli elementi trattati nell’analisi. Nella programmazione OOP si implementano gli elementi descritti durante la OOD. Nell’analisi si può individuare una classe concettuale, un insieme di oggetti del mondo reale, nella progettazione si può decidere di utilizzare una classe software per rappresentarlo, mentre si può implementare alla programmazione. Anche se si tratta di elementi diversi sono tra di loro correlati. Ci si muove dal dominio di interesse dove non è presente il software al software dove bisogna rappresentare in modo adeguato il dominio di interesse.

Nell’analisi si definisce un modello di domino per rappresentare i concetti e le loro associazioni, e gli eventuali attributi significativi. Nella progettazione si utilizza un diagramma di interazione tra oggetti software ispirati agli elementi di individuati nell’analisi, ed un diagramma delle classi per descrivere la struttura delle classi software ed i loro elementi.

UML è un linguaggio standard di modellazione, e sarà molto usato, ma non si tratta dell’argomento principale del corso, l’enfasi è sulla sua applicazione. In UML vengono definiti 14 tipi di diagrammi, la notazione è la stessa ma viene analizzata da diversi punti di vista: dal punto di vista concettuale, dove rappresentano elementi del mondo reale o del dominio di interesse, mentre dal punto di vista software possono rappresentare astrazioni o componenti software. Una classe può essere concettuale o software, rappresentata in entrambi i casi da un rettangolo, ma l’applicazione è diversa. Un diagramma UML può essere applicato in modi diversi, può essere talmente dettagliato da poter generare automaticamente il software, quindi trattando UML come un linguaggio di programmazione, può essere analizzato come un progetto, oppure come un abbozzo. Per imparare ad utilizzare UML come abbozzo bisogna prima studiare il suo funzionamento come progetto.

Nei casi complessi è molto più facile ragionare in modo visuale con dei diagrammi bidimensionali, che con una notazione testuale.

## Sviluppo Iterativo ed Evolutivo

Una delle tematiche importanti nell’ingegneria del software sono i processi ed i metodi per lo sviluppo, ovvero approcci per realizzare, rilasciare e mantenere il software in modo da essere utilizzato. Di processi software ne esistono molti, diversi tra di loro. Diversi processi software differiscono per quando vengono svolte le diverse attività del processo. Le attività principali sono le generalmente le stesse tra i diversi processi, cambia come vengono gestite ed in che modo e quando seguirle da altre attività.

### Attività di Processi Software

Attività comuni nei processi sono software:

- Specifica dei Requisiti

- Analisi

- Progettazione

- Implementazione

- Validazione e Verifica

- Rilascio o Installazione

- Manutenzione ed Evoluzione

- Gestione del Progetto

La prima attività consiste nell’analisi e nella specifica dei requisiti per determinare lo scopo del sistema e le sue caratteristiche, viene realizzata in modo informale. L’analisi successiva deve formalizzare i requisiti precedentemente individuati, affinché possano essere meglio utilizzati nelle attività successive, come modellazione dei dati. La progettazione concettuale dei dati infatti si dovrebbe chiamare analisi progettuale dei dati. L’attività di progettazione determina gli elementi che costituiscono il sistema. Segue l’implementazione e la scrittura del codice. Le attività logicamente successive sono di validazione, tramite test automatizzati o manuali, mentre la verifica viene effettuata normalmente da chi scrive il codice per verificare che il codice che è stato scritto sia conforme ai requisiti stabiliti. Chi realizza il software generalmente non è chi lo vende o lo richiede, durante l’analisi dei requisiti con interviste si stabiliscono i requisiti dai committenti, la validazione ha lo scopo di verificare che il sistema è conforme ai veri bisogni dei clienti e dei committenti, poiché i requisiti potrebbero non esprimere i loro veri bisogni per fraintendimenti da ambo le parti. Quindi l’attività di validazione richiede una presenza significativa di una parte dei clienti o committenti o loro rappresentanti. Dopo aver realizzato il software questo deve essere rilasciato o installato per essere utilizzato dagli utenti finali. Dopo aver rilasciato il software bisogna anche mantenerlo, molto probabilmente infatti verranno individuati errori dopo il rilascio, mentre la manutenzione evolutiva consiste nell’introduzione di nuove attività. Normalmente il costo di manutenzione ci si aspetta sia almeno pari al costo di realizzazione del sistema. Un altro aspetto importante è la gestione del progetto, la gestione delle persone e dei lavoratori impegnati nella realizzazione del sistema.

### Tipi di Processi Software ed UP

I diversi processi software non si differenziano per le attività, i metodi dovrebbero essere comuni a tutti i processi e possono essere trasversali tra diversi, così come i ruoli che per le stesse attività vengono assegnati alle stesse persone.

Si differenziano sopratutto per l’organizzazione temporale delle attività, nell’ordine delle attività e nel tempo dedicato alle singole attività ed alle successive. I processi sono pensati per essere utilizzati da persone competenti.

UP, *Unified Process* è un processo iterativo per lo sviluppo si software OO. Per comprendere i processi iterativi si bisogna comprendere le loro origini, il processo a cascata, definito negli anni ’60/’70 ma ancora molto diffuso, è un processo dove le attività vengono svolte temporalmente in modo sequenziale. L’ordine logico diventa l’ordine fisico temporale, senza considerare la gestione del progetto che viene effettuata in modo trasversale. Dei piccoli ritorni di tipo correttivo sono comunque necessari. Com’è stato definito questo processo, non può funzionare per la realizzazione di software. Ciascuna attività produce dei documenti dettagliati e per procedere alla successiva attività questi devono essere convalidati. Inoltre le diverse attività spesso sono svolte da team differenti. Non è detto quindi che tutti siano in grado di comprendere allo stesso modo ed allo stesso livello il software. Questo processo software nasce in base alle tecniche usate in altre attività, come le ingegnerie dure, ma il software è morbido quindi i principi che valgono nelle ingegnerie classiche non valgono nell’ingegneria del software, questo ancora non era chiaro agli albori. In pochi casi è il modo migliore di procedere, e nella maggior parte dei casi non può funzionare. Più tempo passa da quando viene implementato l’errore a quando viene corretto, più costa la sua correzione. Poiché la verifica e la validazione viene effettuata solamente dopo aver realizzato l’intero software, il costo per correggere gli errori cresce enormemente, effettuando delle correzioni a cascata. Non consente una gestione efficace dei rischi, trattati tardi nel ciclo di vita. Il processo a cascata funziona bene se la raccolta iniziale dei requisiti, l’analisi e la progettazione è realizzata in modo corretto. Non è un’ipotesi realistica che l’analisi o le altre attività iniziale vengano svolte correttamente e concordi alle successive attività. La percentuale di cambiamenti dei requisiti di un progetto dipende sia dalle dimensione che dalla sua complessità, quindi è possibile che durante lo sviluppo si possano scartare fino alla metà dei requisiti individuati nelle fasi iniziali, non possono essere analizzati a cascata. Questo è una della cause più comuni del fallimento del software. Se vengono implementati tutti i requisiti iniziali, la maggior parte di questi non vengono utilizzati o poco raramente. Quindi almeno la metà del tempo di sviluppo del codice è tempo sprecato, poiché le funzionalità realizzate in quel periodo non sono utilizzate. Nel processo a cascata sono presenti dei correttivi per affrontare questi due problemi, ma non sono in grado di risolverli. È quindi necessario un modo differente di procedere per evitare questi disastrosi problemi.

La risposta ai processi a cascata è lo sviluppo evolutivo, iterativo ed incrementale. Nello sviluppo evolutivo si crea un’implementazione iniziale del sistema, la si espone agli utenti o agli sviluppatori stessi per ottenere una valutazione e sulla base di questo l’implementazione iniziale viene raffinata. Sulla base di questo modo di procedere il sistema migliora ed evolve verso la sua versione finale. La versione iniziale anche nella sua imperfezione è utile per ottenere il suo feedback e migliorare, poiché fornisce quello che vogliono veramente gli utenti. Lo sviluppo evolutivo è basato su dei cicli, una sua forma è lo sviluppo iterativo dove si lavora in iterazione di lunghezza temporale fissata, un paio di settima. Questi mini progetti vengono chiamati iterazioni e dopo aver ottenuto il feedback di un’iterazione si può passare alla successiva migliorando la qualità. In ogni iterazione vengono svolte tutte le attività in modo da poter aumentare la qualità e raffinare il software all’iterazione successiva. Il feedback dello sviluppo iterativo è legato all’utilizzo del software che è stato realizzato, nello sviluppo evolutivo in generale potrebbe essere legato ad elementi non eseguibili. Questo sviluppo è incrementale, aumentando da iterazione ad iterazione ed è evolutivo, aumentando la qualità in base al feedback.

In ciascuna iterazione si anticipano alcune attività su una parte dei requisiti e si posticipano su altri requisiti, si effettua uno scambio temporalmente. Nello sviluppo del software iterativo si accetta il cambiamento e l’adattamento. I cambiamenti più significativi dovrebbero essere effettuati durante le iterazioni iniziali. Il riscontro per un’iterazione proviene sia dalle attività di sviluppo che da test, dai clienti o committenti, etc.

Ad ogni iterazione si lavora solo su un sottoinsieme dei requisiti quindi sarebbe meglio ottenere una visione d’insieme del progetto per capire come realizzare quei requisiti. Utilizzando questo metodo la probabilità di fallimento è minore, il cliente può vedere ad ogni iterazione lo stato del software senza aspettare la sua realizzazione completa e permette di avere un percorso evolutivo. I rischi di questa progettazione consistono nella scelta errata dei requisti e della loro realizzazione in ordine sbagliato, e nell’adottare un pensiero a cascata. Un buon compresso chiamato *timeboxing* consiste nell’avere una durata prefissata per le iterazioni che permette di avere un feedback continuo in un *timebox* di qualità per migliorare il software. In questo modo ad ogni iterazioni deve essere prodotto un sistema eseguibile, per realizzarlo è possibile ridurre i requisiti dell’iterazione.

Nello sviluppo iterativo il codice viene continuamente modificato, deve essere organizzato in modo tale da essere facilmente modificabile, altrimenti non sarebbe possibile questo sviluppo. A questo fine il codice deve essere facilmente comprensibile. La struttura del software deve essere flessibile in modo che gli eventuali cambiamenti siano di facile implementazione. Si possono ottenere queste qualità applicando principi ed utilizzando strumenti opportuni.

Nel corso delle iterazioni si vuole comprendere quanti e quali requisti devono essere assegnati alle singole iterazioni, di iterazione in iterazione bisogna chiedersi quali di questi sono davvero importanti, a questa domanda devono rispondere il cliente o il committente. I requisiti più importanti devono essere realizzati all’inizio. Negli ultimi giorni di ogni iterazione bisogna determinare quello che deve essere realizzato nella successiva iterazione. Nelle prime iterazioni l’analisi richiede pochi giorni, lo sforzo maggiore è impiegato alla scrittura del codice, utilizzando lo sviluppo guidato dai test, per validare e verificare il software. L’analisi dei requisti o in generale tutti gli incontri con il committente e gli utenti si concentrano negli ultimi giorni di ogni iterazione. A metà dell’iterazione si confronta ciò che è stato realizzato nella metà precedente con quello che si era proposto all’inizio dell’iterazione. Ci sono tre possibilità, o si è in tempo, o in ritardo o in anticipo. In caso di ritardo si possono scartare uno o più requisiti dall’iterazione corrente poiché è importante finire almeno una parte di quello che si era prestabilito in modo corretto. In caso si è in anticipo si possono aggiungere nuovi requisti da svolgere. Un’aspetto fondamentale dello sviluppo iterativo è la pianificazione iterativa, spesso pianificare all’inizio ogni iterazione è lavoro perso, ma all’inizio può essere utile imporre delle date limite per certe attività e requisiti. Dopo le prime iterazioni si vuole aver analizzato e raffinato la gran parte dei requisiti, lasciando una piccola parte meno importante da raffinare lungo le restanti iterazioni. Nella pianificazione iterativa guidata dal cliente si vuole realizzare ciò che ha più valore al cliente prima, ad ognuno dei requisti viene assegnato un voto che può essere alto medio o basso. Analogamente nella pianificazione guidata dal rischio, le attività più rischiose vengono realizzata all’inizio per avere il più tempo possibile per correggerle, viene quindi assegnato un voto allo stesso modo ad ogni requisito. Sulla base della somma dei voti i requisiti vengono ordinati e si tende ad effettuare nell’iterazione successiva ciò che è più rischioso e più voluto dal cliente. Questo tipo di sviluppo è compatibile con lo sviluppo sull’architettura, dove le prime iterazioni sono concentrate nella costruzione, verifica e stabilizzazione del nucleo centrale dell’architettura.

Un’altra idea dello sviluppo iterativo è il backlog, o lavoro arretrato, per assegnare priorità ai requisiti rimasti indietro alla fine di un’iterazione. Questo backlog deve essere aggiornato ad ogni iterazione, contenente i problemi individuati o i requisiti scartati durante un’iterazione per mancanza di tempo. A ciascuna voce viene assegnata una priorità.

In un’iterazione i requisiti vengono bloccati e non possono essere cambiati durante quell’iterazione, poiché è troppo rischioso cambiarli lungo il percorso. Durante un’iterazione si lavora quindi a cascata, ma questo è accettabile su una porzione dei requisiti. La prima iterazione è speciale e spesso è centrata quasi esclusivamente dell’analisi dei requisiti.

Nel processo unificato entrambe queste iniziative nascono dalla collaborazione di diversi aziende e studiosi che hanno definito sia UML ed UP, per unificare processi esistenti in modo da essere migliore di questi esistenti. In UP le iterazioni vengono etichettate in fasi, la prima di ideazione è molto breve è orientata sopratutto all’identificazione dei primi requisiti, seguita dall’elaborazione dove si realizza un primo nucleo del software di grande valore, nella seguente fase di costruzione si costruisce il resto dei requisiti di minore importanza, e di rischio minore. L’analisi e la progettazione hanno valore sopratutto nella prima manciata delle iterazioni.

Le attività del processo iterativo sono organizzate in discipline e ciascuna produce un elaborato. Tra di queste sono di interesse in questo corso, la disciplina dei requisiti, di modellazione del business e della progettazione, enfatizzate in questo corso durante la fase di elaborazione. Fasi e discipline dove vengono applicati principalmente l’analisi dei requisiti, OOA, OOD, i pattern ed UML. Queste ed altre discipline sono sempre incluse nel lavoro di ogni iterazione, ciò che cambia è l’enfasi di ciascuna e l’impegno, che variano nel tempo. Gli elaborati di interesse vengono definiti all’interno dello scenario di sviluppo, elaborato nella disciplina di infrastruttura.

### Metodi Agili

I processi agili, che vengono chiamati metodi agili, per agilità si intende una forma di sviluppo iterativo che è in grado di rispondere in modo rapido e flessibile ai cambiamenti. In certi casi in modi davvero estremi, come per Google dove sono presenti anche decine di migliaia di aggiornamenti al giorno. Bisogna essere veloci nel capire cosa deve essere modificato e cambiarlo in breve periodo. Questo deve essere effettuato con iterazioni da poche settimane, meno del processo UP. Questo promuove rilasci e consegne incrementali. Sostengono i valori agili, della comunicazione tra persone ed il loro valore. Esiste un manifesto dei principi agili, è importante poter rispondere al cambiamento più che avere un piano definito dei requisiti. Nel modello agile favorisce la comunicazione piuttosto che creare una documentazione dettagliata, questa è comune per uno sviluppo a cascata. Il metodo più diffuso per lo sviluppo agile è *scrum*, mischia, dove solo i giocatori, il team di sviluppo, che deve effettuare decisioni in autonomia. Questo metodo agile che consente di concentrarsi nella realizzazione del più alto valore di business nel minor tempo possibile, lavorando us iterazioni brevi. In questo modo è possibile ispezionare il software funzionante in poche settimane e ripetutamente. Si auto-organizza le priorità più alte per determinare il modo migliore di procedere. Chiunque dopo ogni iterazione puà vedere il software funzionante e decidere se rilasciarlo o continuare a migliorarlo per un altro *sprint*, il termine di scrum per iterazione. Un elemento centrale è il backlog. Ogni iterazione produce un incremento del prodotto software possibilmente rilasciabile.

# Analisi dei Requisiti

Nel libro di testo ci si riferisce a studi di caso prima di analizzare le iterazioni.

Il primo studio di caso è un sistema software da usare nei punti vendita dei supermercati, chiamato POS NextGen. L’obiettivo è quello di realizzare un sistema da poter utilizzare in qualsiasi supermercato.

Il secondo studio di caso permette di realizzare una simulazione del gioco Monopoly.

Sicuramente si farà riferimento al sistema ERedit per realizzare in metodo interattivo diagrammi ER.

## Iterazione Zero

La prima iterazione, generalmente quella dedicata all’analisi dei requisiti appartiene sia all’UP, chiamata ideazione, che a Scrum, dove si chiama envisioning. Comprende l’inizio dell’analisi dei requisiti, solo i più importanti. Si effettua una valutazione economica del progetto che si intende realizzare, quest’analisi è un’approssimazione poiché manca di precisione all’inizio del progetto, e può essere effettuata nuovamente dopo un certo numero di iterazioni per aumentare la precisione di queste valutazioni.

I requisiti corrispondono ad una descrizione informale del sistema in discussione, e normalmente deve risolvere dei problemi per soddisfare dei bisogni che hanno dei clienti. Le parti interessate sono delle persone o gruppi di persone che hanno interessi nel sistema da realizzare. Si comincia cercando di capire chi sono queste persone.

Un’intera branca dell’ingegneria del software è interamente dedicata all’analisi dei requisiti, poiché questa è una problematica molto complessa, e necessita di un approccio ingegneristico. Si può definire come il processo di ricerca, analisi, organizzazione, documentazione, verifica e tracciatura dei requisiti, in mutamento.

I requisiti rappresentano una descrizione del problema che deve essere risolto, comprende un insieme di funzionalità, spesso devono poter gestire alcuni tipi di dati; inoltre il sistema deve avere delle proprietà di qualità. Le qualità del sistema sono caratteristiche come prestazioni, scalabilità, sicurezza, altrimenti il sistema non è particolarmente utile. L’analisi e la progettazione per le qualità è un argomento per corsi successivi, si tratterà principalmente delle funzionalità.

Il valore dei requisiti per le parti interessate è importante per realizzare un software utile. Nei casi d’uso l’obiettivo dei requisiti viene espresso esplicitamente, questo permette di comprendere il motivo del requisito specifico.

I requisi sono di due tipi, funzionali, che riguardano le funzionalità che il sistema deve fornire, e le informazioni che il sistema deve gestire. I requisi non funzionali vengono anche chiamati requisiti di qualità poiché interessano le proprietà di qualità del sistema.

Chi deve realizzare il software probabilmente non conosce il sistema di cui deve realizzare il software. Per cui è necessario documentare ed organizzare i requisiti, in modo da favorire le attività successive. La tracciatura dei requisiti comprende non solo tracciare i cambiamenti tra i requisiti per avere relazioni tra versioni diverse dei requisiti. Poiché i requisiti cambiano è necessario effettuare un approccio iterativo per poter apprendere questi cambiamenti, piuttosto che un approccio a cascata.

Normalmente l’analisi dei requisiti comincia da interviste per cercare, scoprire e validare i requisiti, generalmente si assegnano un paio di giornate per effettuare queste interviste alle parti interessate. Il cliente ed il committente provano ad esprimere le funzionalità richieste dal sistema, e l’analista prova a rappresentarle utilizzando un qualche formalismo per i requisiti, questo è sicuramente sbagliato ed è necessario convalidarli. Per validare questi requisiti nel metodo interattivo, si ottiene il feedback dal cliente dopo l’iterazione. Una parte importante consiste nel realizzare un linguaggio comune tra le due parti, una che sviluppa software e una che richiede il software. In questo modo è possibile comunicare in modo efficiente ed efficace tra le due parti. Questo processo di comunicazione è spesso accidentato, per questo è necessari formalizzarlo.

I requisiti non funzionali vengono anche chiamati attributi di qualità, per qualità si intende, in questo contesto, una misura delle caratteristiche di un prodotto in relazione all’impiego che si vuole fare di quel prodotto.

Nel processo unificato vengono prodotti degli elaborati da ciascuna disciplina per la disciplina dei requisiti i principali sono il modello dei casi d’uso per rappresentare i requisiti funzionali del sistema, le specifiche supplementari, di cui non verrà parlato quasi per niente per descrivere i requisiti di qualità del sistema, il glossario per definire le parole utilizzate e favorire la comunicazione, le regole di business o di dominio, la visione, un documento sintetico per descrivere i principali requisiti del sistema.

Nella Scrum gli elaborati vengono riportati nel Product Backlog, la lista di tutte le funzionalità ed altri requisiti che devono essere ancora realizzati e nelle storie utente.

## Casi d’Uso

I casi d’uso sono un formalismo per i requisiti, insieme alle regole di dominio, i formalismi usati nei testi d’esame. Sono un formalismo adatto allo sviluppo iterativo, applicato anche al di fuori dell’UP. Sono dei racconti pensati per essere scritti, a differenza delle storie utente, per descrivere in che modo può e deve essere utilizzato il sistema che verrà sviluppato. I casi d’uso sono importanti per la documentazione fornita agli utenti, in forma di manuali d’uso del sistema e del prodotto. Sono importanti anche nella verifica del sistema, dove vengono effettuati dei test in corrispondenza dei singoli casi d’uso.

Un esempio di caso d’uso, relativo ad un sistema di vendita utilizzando il sistema POS è il seguente:

> **Elabora Vendita**:  
> Un cliente arriva alla cassa con alcuni articoli da acquistare. Il cassiere utilizza il sistema POS per registrare ogni articolo acquistato. Il sistema mostra il totale ed i dettagli per ogni articolo. Il cassiere inserisce informazioni sul pagamento, che il sistema convalida e registra. Il sistema aggiorna l’inventario. Il cliente riceve dal sistema una ricevuta e poi se ne va con gli articoli acquistati.

Un caso d’uso racconta una storia su come gli utenti o attori del sistema possono raggiungere i loro obiettivi, usando il sistema. Per attore si intende qualcosa o qualcuno dotato di comportamento per interagire con il sistema in discussione. Potrebbero essere persone con un ruolo, sistemi informatici o organizzazioni. Si differenzia tra uno scenario, istanza di caso d’uso, ed il caso d’uso, l’insieme delle possibili istanze. Uno scenario è una sequenza specifica di azioni e interazioni tra il sistema e gli attori, possono essere di successo o di fallimento rispetto all’attore primario. Un caso d’uso è l’insieme di tutti gli scenari correlati che usa un attore per raggiungere un obiettivo. I casi d’uso possono essere scritti a diverso livello di dettaglio, il primo consiste in una semplice riga con una descrizione molto sintetica dell’obiettivo che vuole raggiungere l’attore. Il secondo formato consiste in una breve storia scritta di poche righe con pochi dettagli. Il formato successivo è il formato informale che normalmente richiede scrivere una pagina, dov’è presente uno senario particolare, principale, di successo, seguito da una serie di scenari alternativi, con la possibilità di fallimento. In questo caso il caso d’uso d’esempio precedente riguardante il sistema POS potrebbe contenere scenari alternativi riguardanti l’inserimento manuale degli articoli per errori del sistema, oppure la rimozione di articoli su richiesta del cliente, oppure il fallimento della transazione monetaria con il sistema POS.

Lo scenario è una sequenza di azioni, ma normalmente le possibilità sono tante e non vengono descritte per esteso, ma con variazioni locali, con l’idea che nell’esecuzione di un caso d’uso si potrebbero attraversare diversi scenari alternativi. Procedendo in questo modo con un numero limitato di variazioni si possono rappresentare un numero esponenziale di scenari. Il risultato di un’istanza dovrebbe essere un valore osservabile da un attore, in modo da assegnare priorità ai requisiti.

Nel processo unificato un elaborato chiamato modello dei casi d’uso comprende una descrizione testuale dei casi d’uso, che prevede questi testi. I diagrammi di casi d’uso rappresentano un ovale contenente il nome del caso d’uso, informazioni minimali, può essere usato come un indice visuale per i casi d’uso descritti nel modello dei casi d’uso. Questi infatti non sostituiscono i casi d’uso, ma possono essere aggiunte per comunicare in modo visuale informazioni riguardanti questi. Non possono essere sempre applicabili, sono adatti a sistemi interattivi.

Sono presenti diversi tipi di attori, l’attore primario utilizza direttamente il sistema per raggiungere gli obiettivi; l’attore finale è quello che vuole raggiungere degli obiettivi, può non usare direttamente il sistema. In alcuni sistemi questi due attori coincidono. L’attore di supporto fornisce servizi al sistema in discussione, in generale un sistema informatico. Gli attori fuori scena non compaiono nel caso d’uso, ma i loro interessi nel comportamento del sistema devono essere rappresentati nel caso d’uso.

I casi d’uso possono essere scritti in vari formati: breve, informale e dettagliato, che può richiedere una decina di pagine. I primi due sono stati già trattati, mentre un caso d’uso in formato dettagliato è un documento strutturato in più pagine che comprende varie sezioni, la parte più importante è lo scenario principale di successo. La sezione più ampia sono le estensioni, gli scenari alternativi. Viene preceduto da un preambolo, contenente il nome, la portate il livello, la descrizione degli attori, primari e le parti interessate. Queste sono seguite dalle precondizioni e la garanzia di successo. Lo scenario principale viene seguito dalle estensioni e da altre sezioni opzionali, come i requisiti speciali, un elenco delle tecnologie e dei dati, la frequenza di ripetizione ed altre voci non standard.

Nel preambolo una sezione che è utile analizzare separatamente sono le parti interessate e gli interessi, che descrive gli interessi di tutti gli attori coinvolti considerando anche quelli fuori scena. È utile per definire i limiti imposti al sistema, cattura tutti e soli i comportamenti relativi agli interessi delle parti interessate, descritti nel caso d’uso.

Lo scenario principale di successo è strutturato in passi, singole azioni, ed è utile numerarli. Questa sequenza di passi può contenere istruzioni di controllo per realizzare ripetizioni. Questo non contiene istruzioni condizionali, gestite nelle estensioni. Si esprimono in maiuscolo i nomi degli attori presenti nel caso d’uso. Convenzionalmente nel primo passo e nell’ultimo passo non si parla dell’uso del sistema, ma dell’obiettivo del caso d’uso. L’interfaccia utente non viene descritta ma è utile considerarla per le interazioni con il sistema da parte degli attori.

In generale i passi sono di tre tipi, azioni, interazioni, validazioni e cambiamenti di stato. Nelle interazioni l’attore comunica informazioni al sistema. Enfatizzando le interazioni possono essere date per scontate le azioni effettuate dal sistema. Di solito il primi passo, ed a volte anche l’ultimo, non ricadono in queste tipologie, ma indicano l’evento che scaturisce l’esecuzione del caso d’uso. Se inizia con un login, il caso d’uso contiene una validazione.

La sezione successiva più lunga contiene le estensioni, scenari alternativi, deviazioni temporanee rispetto allo scenario principale di successo. Questo modo di scrivere requisiti è utile poiché con $n$ estensioni è possibile scrivere $2^n$ scenari diversi. Nella prima parte dell’estensione è presente una condizione, e nella parte successiva viene descritta come viene gestita, sono gli attori che vogliono gestire il caso d’uso diversamente, può avvenire in qualunque momento, dopo aver eseguito l’estensione il controllo ritorna allo scenario principale. Ci sono tre tipi di estensioni, il primo descrive metodi alternativi in cui l’attore primario vuole procedere rispetto a quanto descritto nello scenario principale. Il secondo tipo riguarda la gestione di errori, o in generale la gestione di qualcosa che viene si verifica durante l’esecuzione dello scenario principale, e quindi si procede in modo diverso. Generalmente è il sistema che si accorge dell’errore durante azioni normali o validazioni. Il terzo tipo di estensioni rappresenta un modo concreto di eseguire un’azione astratta descritta in un passo dello scenario principale.

Una singola estensione può comprendere diverse azioni da svolgere per correggere lo stesso errore. L’utilizzo delle estensioni fornisce modi diversi per poter effettuare la stessa azione. Estensioni possono essere a loro volta parte di estensioni, per avere molta flessibilità negli scenari disponibili. Il caso d’uso non sono i veri requisiti, i veri requisiti possono essere compresi solo dopo che questi verranno implementati, e dopo aver ottenuto il feedback del cliente. Questo è solo un punto di partenza.

Nel formato dei RUP, il primo passo non viene scritto nello scenario principale di successo, ma in un’altra sezione chiamata trigger, che contiene le azioni che avviano il caso d’uso. Il formato due colonne prevedere di separare quello che fa il sistema da quello che fanno gli altri attori.

Nell’analisi dei requisiti si scrivono i casi d’uso in uno stile essenziale, ignorando l’interfaccia utente, e si considerano le azioni degli utenti e alle responsabilità del sistema, non ad azioni correlate. Bisogna scrivere in modo conciso, chiaro e completo, senza scrivere troppi dettagli. Bisogna specificare in modo chiaro il soggetto, il verbo e frasi coordinate. I casi d’uso sono una scatola nera, non viene descritto come viene effettuata un’azione del sistema, infatti l’analisi del come appartiene alla progettazione. Descrive le responsabilità del sistema e le interazioni con gli attori.

L’analista deve capire indicativamente quali sono i tutti i casi d’uso, il modo per trovarli normalmente è chiedersi chi sono le persone che dovranno normalmente usare il sistema. Questi saranno gli attori principali. Mentre chiedersi se ci sono altre persone che hanno interesse nell’uso del sistema, aiuta ad individuare gli attori finali. Dopo aver individuato questi attori bisogna capire gli obiettivi degli attori per cui utilizzano il sistema.

I casi d’uso centrali in UP individuati in un’iterazione verranno analizzati alla successiva, cercando di espandere casi d’uso in vari formati cercando quelli più importanti, avendo una visione in ampiezza che mano mano che avanzano le iterazioni aumenta di profondità.

Normalmente l’esecuzione di un caso d’uso richiede pochi minuti, raramente ore, certamente non giorni. Nel processo unificato ci stanno diversi elaborati per i requisiti, le specifiche supplementari analizzano i requisiti non funzionali e quindi non è di interesse in questo corso. Il glossario è importante poiché definisce i termini e le definizioni importanti. Le regole di dominio anch’esse sono normalmente importanti.

## Storie Utente

Nel contesto dei metodi agili, i casi d’uso i sono ritenuti troppo formali, in questi metodi più che documentare è importante capire. Nei metodi agili invece di scrivere i requisiti in modo formale si preferisce parlare per comunicare e comprendere i requisiti. La comprensione dei requisiti dettagliata deve essere effettuata prima della fase di analisi e progettazione dei requisiti. Una storia utente descrive in modo semplice una funzionalità o requisiti di intesse per un utente del sistema. La relazione fra storia utente e caso d’uso non è banale e non verrà trattata. Rappresenta il valore per un utente del sistema, o per il suo acquirente. Di solito vengono scritte su schede volutamente piccole. Contiene una descrizione minimale, utile come promemoria di comunicazioni future per comprendere gli aspetti della storia, una conversazione, dato che per i metodi agili la comunicazione è la parte più importante, e dei test di accettazione scritti sul retro della carta.

## Iterazione 1

Nell’iterazione uno si progetta la base di dati e l’interfaccia utente, che non verranno analizzate in questa iterazione. L’obiettivo didattico di questa iterazione è ottenere capacità di base per l’analisi e la progettazione, anche se nella realtà non verranno effettuate solamente queste operazioni.

I casi d’uso vengono spesso realizzati in modo incrementale, le varie caratteristiche e scenari vengono realizzati su diverse iterazioni, conservando l’elaborato corrispondente di ogni iterazione.

### Esempio Monopoly: Requisiti

Per l’iterazione uno si definisce uno scenario di base del caso d’uso del gioco di una partita di Monopoly, si considera che tutti i giocatori si spostino sulle caselle del tabellone. Possono giocare da due ad otto giocatori. Si definisce un caso d’uso di avviamento. Ogni partita viene rappresentata come una serie di giri, in ogni giro si ogni giocatore effettua un turno, in ogni turno un giocatore tira i dadi ed avanza il numero di caselle complessivo e sposta il suo segnalino sulla casella corrispondente, la partita viene terminata dopo venti giri. Sono presenti solo queste componenti di base del movimento nel gioco del Monopoly.

## Architettura del Software

Prima bisogna scegliere come è realizzato il sistema, ed in seguito si può decidere quale tipo di analisi e progettazione è più pertinente. Normalmente riguarda delle scelte sugli elementi principali del sistema, per implementare le qualità essenziali del sistema. Questa scelta è difficile da cambiare. Un modo molto comune per organizzare il software è l’architettura a strati, composto da elementi a grana grande, chiamati package. Gli strati alti sono una pila di elementi verticali che possono effettuare chiamata agli strati più bassi, ma ciò non è possibile in senso opposto. Gli strati sono composti da questi package. L’utente interagisce con un’interfaccia utente, nello strato più alto del sistema.

Un divisione comune degli strati è composta da tre strati, la presentazione con l’interfaccia utente, la logica applicativa e lo strato dei servizi tecnici e l’accesso alla base di dati. Uno dei principi di progettazione fondamentali è il principio di separazione degli interessi, afferma che non vanno mischiati elementi diversi, e bisogna raggrupparli per scopi, interessi e responsabilità.

Ci si occupa principalmente dell’analisi e progettazione dello strato della logica applicativa, largamente indipendente dalle tecnologie. La scelta in modo in cui è organizzato questo strato ha un impatto profondo sul codice del software. In generale questo strato si occupa di gestire dati ed implementare funzionalità. La strategia per lo strato della logica applicativa provoca un impatto profondo sul codice, ed anche su come viene svolta l’analisi e la progettazione. Nell’approccio transazionale, per la logica applicativa, i dati sono presenti solo su una base di dati, e le funzionalità vengono effettuate accedendo alla base di dati, sistema adottato da software della Oracle. L’approccio procedurale consiste in una distribuzione in oggetti per rappresentare i dati ed informazioni, gestiti in memoria principale, e le funzionalità vengono realizzate da oggetti e servizi che accedono a queste strutture. Questo strato viene anche chiamato di dominio. Questo corso si riferisce all’approccio procedurale, la strategia *Domain Model*.

L’approccio di modello di dominio viene utilizzato quando si utilizzano metodologie ad oggetti, dove il codice è diviso in classi ed ogni classe si occupa sia di dati che di operazioni, si incapsulano i dati nelle classi relative a quel tipo di informazioni, e le funzioni di una classe sono relative solamente ai dati gestiti da quella classe. Spesso questo si chiama strato di dominio.

Le applicazioni possono essere realizzate in modo stand-alone, ovvero autonome per ogni utente. Le operazioni sono esclusive ai dati di quello specifico utente, non sono condivise con altri utenti o altri dispositivi. Se ci sono più osservatori che utilizzano questo tipo di applicazione, ognuno vede la propria applicazione. Le applicazioni client-server operano su dati condivisi, potenzialmente tutti gli utenti dell’applicazione possono accedere agli stessi dati, e possono contribuire a questi dati. Richiede un accesso in rete o nel web.

L’analisi e la progettazione per le applicazioni stand-alone si realizza considerando un solo utente ed una sola istanza dell’applicazione. Nel caso della progettazione di applicazione client-server, è più complesso. L’applicazione non si deve limitare a gestire i dati condivisi dagli utenti, ma deve gestire anche i dati di ogni singolo utente. Ci sono molti più osservatori, che cambiano nel tempo. Per ogni utente bisogna saperlo identificare univocamente ed associare i dati relativi a quello specifico utente. Deve gestire sia dati condivisi da tutti gli utenti che i dati utilizzati in un certo momento da ogni utente. Questo va effettuato per ciascuna sessione, o conversazione, di utilizzo del client-server. I dati della sessione non sono persistenti, ma sono memorizzati solo per la durata della sessione, mentre i dati condivisi son persistenti.

In generale ogni applicazione client-server deve gestire dati condivisi su una base di dati condivisa e dati relativi allo stato delle sessioni, da gestire separatamente utente per utente e sessione per sessione, ed in genere questi sono transienti, fino a quando non vengono salvati.

La soluzione comune consiste nell’introdurre un nuovo strato per applicazioni tra quello di presentazione e quello di logica, realizzando in questo strato gli oggetti sessione contenenti i dati di sessione per ciascun utente, normalmente sono dei collegamenti verso oggetti presenti nello strato di dominio. Il modo migliore per ragionare consiste nell’avere due strati diversi, ma collegati che rappresentano lo strato della logica applicativa. Il libro di testo mischia questi due strati. Nell’analisi e progettazione si dovranno separare questi due livelli e quindi effettuare ragionamenti separati, per la gestione dei dati condivisi e la gestione delle sessioni. Inoltre nella programmazione si dovranno utilizzare tecnologie opportune e si dovranno considerare in modo diverso questi due aspetti.

# Progettazione Concettuale

L’analisi enfatizza l’investigazione di un problema e dei suoi requisiti, enfatizzando cosa interessa al sistema, non è interessata ad individuare una soluzione al problema. Uno di questi modi è l’analisi orientata agli oggetti OOA, si basa principalmente sull’identificazione dei concetti del dominio ed una loro rappresentazione ad oggetti.

I principi che guidano l’analisi del software sono principi generali e valgono in tutti i metodi di analisi e si deve concentrare sulle informazioni che il sistema deve gestire, le funzioni che dovrà svolgere ed il comportamento sistema. Il sistema software da realizzare deve rappresentare delle informazioni, non ci si concentra sui dati, ma sulle tipologie di informazione che dovrà rappresentare, questo rappresenta il domino del sistema. Sulla base di queste informazioni possono essere invocate funzioni o operazioni del sistema, trattato come una scatola nera, quindi non si sa come questo esegue l’operazione. Ma è possibile osservare il comportamento del sistema dopo l’esecuzione di una di queste operazioni.

L’analisi e la progettazione hanno lo scopo di individuare le interazioni rivolte verso il sistema che rappresentano le operazioni in funzione del cambiamento di informazioni nel mondo reale, il comportamento consiste nelle operazioni svolte dal sistema in caso di una di queste interazioni, con le relative modifiche ai dati del sistema.

L’OOA comprende il modello di dominio, che descrive i concetti del dominio informatico del problema; le operazioni o funzioni di sistema, mediante diagrammi di sequenza di sistema, che il sistema è chiamato a svolgere; i contratti delle operazioni, ovvero una descrizione del comportamento del sistema a queste operazioni.

L’analisi e la progettazione sono iterative ed incrementali ed hanno lo scopo di comprendere e favorire la comunicazione.

## Progettazione Concettuale e Modellazione di Dominio

Dove in Basi di Dati si parlava di realtà di interessa, qua si parla di dominio di sistema. La progettazione concettuale di una base di dati ha lo scopo di rappresentare le specifiche informali della realtà di interesse ed offrire una descrizione formale e completa, indipendente dalle tecnologie ed i criteri di rappresentazione. Quindi rappresenta un’attività di analisi, e non di progettazione e sarebbe opportuno chiamarla “analisi concettuale”. La modellazione di dominio descrive le informazioni della realtà di interesse secondo una rappresentazione concettuale ed a oggetti. La modellazione di dominio è simile alla progettazione concettuale, ed è un modo particolare di effettuare OOA.

La notazione utilizzata non è più il diagramma ad oggetti, ma un modello ad oggetti come UML. Nella base di dati i diagrammi si chiamano schemi, nell’ingegneria del software i diagrammi si chiamano modelli, mentre i formalismi nelle basi di dati si chiamano modelli, ed in ingegneria del software si parla di linguaggi. Uno schema concettuale viene chiamato un modello di dominio. Un diagramma di modello concettuale ER viene espresso nell’ingegneria del software come un diagramma delle classi di UML, utilizzato dal punto di vista concettuale.

Nella progettazione concettuale di basi di dati le entità rappresentano oggetti che hanno proprietà comuni ed esistenza autonoma, così come nel modello di domino. Se un concetto ha proprietà significative ed esistenza autonoma, allora è opportuno rappresentarlo come un’entità o oggetto, se ha una struttura semplice si rappresenta come attributo di una entità o relazione, in base di dati, e solamente di oggetto per il modello di domino. Se date due classi concettuali c’è un concetto che le associa, allora può essere rappresentato come una relationship, o associazione.

Entità e classi concettuali quindi sono simili, un’entità rappresenta una classe di oggetti con proprietà comuni, le cui istanze sono chiamate appunto istanze, o occorrenze. Mentre una classe concettuale in UML rappresenta un insieme di elementi o concetti con caratteristiche simili, le cui istanze sono chiamate istanze o oggetti. Un entità viene rappresentata da un rettangolo contenente solo il nome, mentre una classe concettuale può essere separata in due compartimenti, il primo con il nome, ed il secondo dove sono espresse informazioni contenute dalla classe concettuale.

Gli attributi sono proprietà elementari di entità o relazioni, rappresentati all’esterno da un pallino collegato all’oggetto. Mentre in UML possono essere solo proprietà elementari degli oggetti di una classe, e sono interne ad esse, rappresentate nello scompartimento sotto al nome della classe.

Una relazione in ER rappresenta un legame logico tra due o più entità e si indica con un rombo, contenente il suo nome, può anche avere attributi. Mentre in UML un’associazione rappresenta una connessione significativa tra classi, viene rappresentata graficamente da una riga che unisce le due classi. Un’istanza di associazione si chiama collegamento. In ER le relazioni possono essere binari o $N$-arie, in UML sono generalmente binarie, e sono possibili $N$-arie anche se poco comuni. In UML non possono avere attributi e generalmente il nome è un verbo che indica una relazione, mentre in ER il nome di una relazione è un sostantivo.

In ER per ogni entità va specificato almeno un identificatore, mentre in UML non è comune la pratica, anche se è possibile.

Un cambiamento significativo riguarda la cardinalità e molteplicità. Mentre nei diagrammi ER la cardinalità di una relazione indica la partecipazione minima e massima di un’entità ad una relazione, la cardinalità in UML di un’associazione indica quante istanze di una classe possono essere associate ad un’istanza dell’altra classe. Effettivamente ha un significato opposto, le posizioni sono quindi invertite, anche se alcuni dialetti di ER utilizzano la stessa posizione del linguaggio UML. Di seguito come viene mostrata la cardinalità e la rispettiva molteplicità tra i due diagrammi:

<div class="center">

|   ER    |  UML   |
|:-------:|:------:|
| $(a,b)$ | $a..b$ |
| $(a,a)$ |  $a$   |
| $(0,N)$ |  $*$   |
| $(1,N)$ | $1..*$ |

</div>

Le generalizzazioni sono presenti sia in ER che in UML, ma i loro formalismi sono differenti, e nel loro uso pratico può essere molto diverso. Verranno quindi omesse per ora.

In ER in un diagramma bisogna rappresentare solamente le informazioni persistenti, le entità rappresentano una classe di istanze, sia l’insieme, in genera nessuna entità ha una sola istanza. Le entità rappresentano informazioni, ed hanno in genere almeno un attributo. In UML invece non bisogna rappresentare solo le informazioni persistenti, ma anche quelle transienti. Una classe non rappresenta il relativo insieme. Le classi possono avere anche un solo oggetto, istanza, e possono non avere attributi, e possono essere presenti classi che rappresentano solo un comportamento.

Strategia di realizzazione di progettazione concettuali sono utili anche per la modellazione di domini, quali la rappresentazione delle informazioni, senza considerare la loro implementazione; l’enfasi su ciò che è rilevante ai fine della descrizione del dominio del problema.

Se un concetto ha proprietà significative e o descrive una classe di oggetti con esistenza autonoma, allora bisognerebbe rappresentarlo come una classe concettuale. Se un concetto ha una struttura semplice e si può pensare con un tipo primitivo, allora si potrebbe rappresentare come un attributo, associato alla classe concettuale a cui si riferisce. Se sono state associate due classi concettuali e c’è un concetto che le associa, può essere rappresentato come un’associazione. Le strategie di progettazione di modelli concettuali sono top-down, bottom-up, ma generalmente si utilizzerà un modello a macchia d’olio.

Nella modellazione di dominio è utile avere altri diagrammi che rappresentano oggetti, collegamenti e valori, istanze degli attributi. Questo diagramma si chiama diagramma degli oggetti di dominio, dove i nodi del grafo rappresentano oggetti, e ciascun oggetto è decorato con valori corrispondenti ad attributi. Per capire se un diagramma corrisponde ad un diagramma delle classi o degli oggetti bisogna controllare il nome dei nodi, ogni volta che viene usato per un oggetto è necessario usare “:”, può essere omesso il nome simbolico ed il nome della classe. Ma nel diagramma delle classi è vietato l’uso di “:”. Normalmente il risultato dell’analisi è il diagramma delle classi, ma viene usato il diagramma degli oggetti per risolvere i dubbi. Si tratta di un modo per comprendere e comunicare.

## Modellazione di Domino

La modellazione di dominio riguarda l’analisi delle informazioni, per comprendere il dominio di interesse e le informazioni da rappresentare. Questo modello delle informazioni di dominio contiene queste informazioni che il sistema deve gestire.

È un modello concettuale ad oggetti, è anche un dizionario visuale del linguaggio di dominio, poiché il suo scopo principale è la comunicazione, e viene sviluppato in modo iterativo ed incrementale, dai requisiti dell’iterazione corrente.

Le classi gli attributi e le associazioni hanno dei nomi, la scelta dei nomi è di cruciale importante per la chiarezza e la pulizia del codice.

Il modello di dominio è utile a rappresentare i concetti del domino di interesse, da un modello di analisi, concettuale, degli oggetti di dominio o degli oggetti di dominio. Può essere rappresentato in pratica usando UML, in particolare come un diagramma delle classi senza operazioni, e soprattutto dal punto di vista concettuale. Nei diagrammi delle classi compaiono in modo particolare nomi delle classi ed attributi ed associazioni.

I diagrammi delle classi si possono rappresentare sotto il punto di vista concettuale e dal punto di vista software, che comprende più informazioni, riguardante il pezzo di codice che descrive l’elemento del dominio di interesse della data classe concettuale.

In un modello di domino si usano classi concettuali, un concetto nel dominio di interesse; associazioni concettuali, una relazione tra gli oggetti di due classi e le loro istanze vengono chiamate collegamenti; ed attributi concettuali, rappresentano una proprietà elementare degli oggetti di una classe. Gli attributi sono solo di classi e non di relazioni.

Il modello di domino definisce la struttura del linguaggio usato dagli sviluppatori ed usato per comunicare con le parti interessate. Questa metodologia di modellazione è tornata di moda, con la progettazione guidata dal dominio.

Un altro tipo di dizionario visuale è l’atlante ed è utile realizzarlo, ma questi dizionari visuali si riferiscono principalmente al mondo reale, con i rispettivi oggetti fisici.

Quando si parla del modello di dominio bisogna evitare di parlare di operazioni o di usare elementi software, poiché non mostra oggetti del mondo software. Un modello di dominio non è un modello di dati, si riferisce solamente ai dati persistenti. Un dato si definisce persistente se al termine dell’esecuzione del caso d’uso, quel dato deve essere ricordato. Deve gestire anche dati transienti, generato nei primi passi di un caso d’uso e deve essere ricordato in passi successivi, ma sempre nello stesso caso d’uso. Non descrive invece dati locali, che vengono ricordati in un solo passo dell’esecuzione di un caso d’uso.

Nella pratica si parla di modello di dominio in due contesti, sia in UP nel modello concettuale di dominio, e sia nel software nello strato della logica applicativa, chiamato strato di domino, ma viene chiamato modello di dominio nella pratica. Questi due sono strettamente collegati e danno uno la forma all’altro, uno è lo strato principale dal lato software, mentre l’altro permette di dare la forma a questo strato di dominio, il principale elemento architetturale della struttura software.

Nell’analisi si crea un modello di dominio per comprendere il dominio del sistema ed il suo vocabolario e per definire il linguaggio; inoltre si usa per la progettazione per ispirare la progettazione dello strato di dominio.

Si usa il principio del salto rappresentazionale, la distanza tra come è scritto il codice e come si pensa nel dominio del problema, e vuole mantenerlo basso. Questo principio afferma che potrebbe essere utile sceglier classi software che rispecchiano gli elementi nel modello di dominio. Si vuole abbassare, non eliminare, poiché nell’analisi si ignora in larga misura tutto ciò che riguarda l’implementazione. In un modello di dominio gli oggetti sono astrazioni di oggetti reali, questo permette di selezionare caratteristiche tra un insieme di oggetti per stabilire se sono tra di loro simili o diversi, per rappresentarli con la stessa o diverse classi.

### Classi

In un modello di dominio le classi concettuali sono astrazioni di oggetti reali, un’astrazione è un processo che permette di selezionare solamente alcune caratteristiche e proprietà di un insieme di oggetti, escludendo caratteristiche non rilevanti.

L’astrazione più usata nel modello di dominio è quella di classificazione per definire un concetto e poter rappresentare molti oggetti del mondo reale come una singola classe, caratterizzati da proprietà comuni. L’astrazione giusta da applicare dipende dal dominio, bisogna sapere i casi d’uso; non si può modellare senza considerare il suo contesto di dominio.

Un’astrazione è applicata correttamente se le proprietà enfatizzate sono rilevanti nel dominio di interesse; se le proprietà non enfatizzate sono irrilevanti nel domino. Inoltre un’astrazione corretta può essere non corretta in un dominio simile, ma diverso.

La modellazione di dominio va effettuata nell’ambito di un dominio ben preciso, che ne definisce il contesto.

Ogni classe concettuale serve a rappresentare un concetto del dominio, oppure è un concetto, la differenza tra l’essere ed il rappresentare dal punto di vista concettuale è bassa. Rappresenta un idea, un concetto o un oggetto. Può essere rappresentata da un simbolo, nel diagramma, un intensione, nel glossario, o un estensione. Il nome può essere volutamente sintetico, l’intensione rappresenta il significato dell’oggetto vero, come verrebbe descritto in un glossario, si chiama anche intensione del concetto. È utile ragionare sull’estensione del concetto, ovvero su tutte le istanze di un oggetto.

### Sintassi UML: Classi, Associazioni ed Attributi

Una classe in UML è un descrittore di oggetti che possiedono le stesse caratteristiche, se viene utilizzato per realizzare un modello di analisi, allora una classe concettuale, rappresenta un concetto del mondo reale.

Nel primo compartimento di una classe viene inserito il nome, nei seguenti attributi. Le istanze di una classe vengono chiamate oggetti mentre istanze di classi concettuali vengono chiamate classi concettuali. Un’istanza di una classe, un oggetto, può essere rappresentata graficamente mediante un diagramma degli oggetti di dominio, per mostrare un pezzo di realtà di interesse di esempio. I due punti “:” nel nome di una classe identificano la sua istanza, quindi non vanno inseriti nel modello di dominio. L’estensione di una classe concettuale, si può rappresentare mediante un grafo, un diagramma degli oggetti di dominio che rappresenta i modo visuale un insieme di oggetti del mondo reale nel contesto del dominio di interesse.

Un’associazione concettuale è una relazione tra classi concettuali, rappresentata come una connessione, le sue estremità individuano la “cardinalità” dell’associazione. Dal punto di vista concettuale questi collegamenti sono bidirezionali. Una linea rappresenta un collegamento e quindi ogni istanza di un collegamento è un’associazione.

In un diagramma degli oggetti di domino sono presenti collegamenti tra tutti gli oggetti collegati, che nel modello di dominio hanno un’associazione che li collega. Quindi nel modello di domino è possibile esista un’unica stessa associazione tra due classi concettuali, mentre in un diagramma degli oggetti di domino è normale siano presenti molti collegamenti relativi alla stessa associazione, questi collegamenti contengono solo il nome e non hanno le cardinalità dell’associazione corrispondente.

Un attributo concettuale associa a ciascun oggetto un valore. In termini matematici è una funzione che associa a ciascun oggetto un valore. Gli attributi vengono assegnati a dei valori nel diagramma degli oggetti. Un diagramma degli oggetti di dominio rappresenta in modo visuale una piccola porzione d’esempio del dominio di interesse. Quando si hanno dei dubbi su quali classi associazioni ed attributi da utilizzare, realizzare un diagramma degli oggetti può aiutare.

Un diagramma degli oggetti di dominio rappresenta in modo visuale un insieme di oggetti di esempio del mondo reale, nel contesto del dominio del problema. Viene rappresentato come un grafo etichettato che mostra oggetti, collegamenti tra oggetti e valori di attributi degli oggetti. Viene usato per rappresentare e comunicare una piccola parte del dominio di interesse. Sono uno strumento utile per validare e scoprire porzioni del modello di dominio.

## Creare un Modello di Dominio

Rimanendo vincolati ai requisiti scelti per l’iterazione corrente, per creare un modello di dominio, evitando la “paralisi da analisi”. Dopo aver individuato un certo numero di classi si individuano le associazioni ed attributi. Un altro modo di procedere, sempre vincolati dai requisiti correnti, si identificano una alla volta le astrazioni di interesse e si decide come rappresentarle e si disegnano nel modello di domino.

Per creare un modello di dominio bisogna essere sempre vincolati dai requisiti scelti all’iterazione corrente. Gli unici strumenti disponibili nella modellazione di dominio sono classi, associazioni ed attributi.

Per trovare le classi concettuali, bisogna individuare prima le classi candidate, dopo aver creato questo elenco bisogna determinare quali di questi candidati è opportuno rappresentare come una classe. Meglio sovra-specificare il dominio che sotto-specificare, quindi si tende a cominciare con molte classi concettuali a grana piccola. Non si interessa un elenco corretto delle classi concettuali, ma di avere un elenco di classi utili. Bisogna essere ispirati nella scelta delle classi software. Nella progettazione software avere informazioni non persistenti è utile, quindi non vanno escluse da quest’analisi. Inoltre è possibile avere classi la cui estensione contiene un solo oggetto, oppure senza attributi, o con un solo comportamento, ma queste due da usare con cautela.

Per trovare le classi concettuali si possono usare le strategie usate nel contesto della progettazione concettuale di basi di dati. Si possono utilizzare pattern di analisi, riusando o modificando modelli esistenti.

I pattern di analisi sono soprattutto molto utili, ma in questo corso non verranno analizzati.

Conviene evidenziare i nomi e le locuzioni nominali nel testo di caso d’uso, poiché su questi si bisogna riferirsi per scegliere i nomi degli elementi del modello di dominio. Questi potranno essere nomi di classi concettuali candidate, oppure potrebbe essere opportuno rappresentarli come attributi o associazioni.

Questa tecnica è utile soprattutto all’inizio per identificare i concetti candidati, ma oltre a questo non offre molto, quindi presenta diversi inconvenienti. Potrebbe infatti non riconoscere concetti lasciati impliciti nella comunicazione, o potrebbe enfatizzare concetti poco importanti. Inoltre soffre delle ambiguità del linguaggio naturale. Se si scopre un uso improprio di alcuni termini, con connotazione ambigua, oltre a migliorare i casi d’uso si potrebbero creare modelli in parallelo in base alla diversa interpretazione.

## Individuare Classi Concettuali

Una tecnica migliore consiste nell’uso di un elenco di categorie comuni di classi concettuali. Questo contiene le categoria di classi che bisogna prendere in considerazione per identificare un insieme di classi concettuali candidate.

Il linguaggio parlato è ricco di ambiguità, quindi la strategia migliore per trovare le classi concettuali candidati è dall’elenco di categorie di classi concettuali, per cercare all’interno del dominio classi appartenenti a queste categorie.

Il valore di una classe dipende dal valore assegnatoli dall’utente o dal committente, o dalle parti interessate al sistema.

Il libro propone una quindicina di categorie di classi concettuali.

<div class="center">

|                     Categoria di Classe Concettuale                      |                              Esempi                               |
|:------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
|                         Transazioni commerciali                          |                 Vendita, pagamento, prenotazione                  |
|                     Elementi o righe di transazioni                      |                   Riga di vendita per articolo                    |
|       Prodotti o servizi correlati a transazioni e o loro elementi       |                   Articolo, volo, posto, pasto                    |
|                    Dove è registrata la transazione?                     |              Registro, libro mastro, piano dei voli               |
|   Ruoli di persone o organizzazioni correlate alle transazioni, attori   |  Cassiere, cliente, negozio, giocatore, passeggero, linea aerea   |
|               Luogo della transazione o luogo del servizio               |                  Negozio, aeroporto, volo, posto                  |
|       Eventi significativi, spesso con tempo o luogo da ricordare        |                     Vendita, pagamento, volo                      |
|                              Oggetti fisici                              |     Articolo, registro, segnalino, tabellone, dado aeroplano      |
|                          Descrizioni di oggetti                          |              Descrizione prodotto, descrizione volo               |
|                                Cataloghi                                 |                 Catalogo prodotti, catalogo volo                  |
|              Contenitori di oggetti, fisici o informazioni               |              Negozio, scaffale, tabellone, aeroplano              |
|                          Oggetti in contenitori                          |                   Articolo, casella, passeggero                   |
|                      Altri sistemi che collaborano                       | Sistema di autorizzazione di credito controllo del traffico aereo |
| Registrazioni di questioni finanziarie, di lavoro, contrattuali e legali |           Ricevuta, libro mastro, giornate manutenzioni           |
|                           Strumenti finanziari                           |                Contante, assegno, linea di credito                |
|                        Piani, manuali, documenti                         | Elenco variazioni di prezzo giornaliere, piano delle riparazioni  |

</div>

Se il dominio è un dominio di business, è importante cercare all’inizio classi inerenti a transazioni commerciali. Alcune transazioni sono atomiche, ma la maggior parte non lo sono quindi si possono rappresentare con righe, voci o elementi di transazioni per rappresentare i vari passi delle transazioni. Normalmente le transazioni sono correlate a dei prodotti o servizi, associati alla transazione. Si modella utilizzando classi differenti per prodotti o servii collegati alle transazioni.

In Italia le vendite vanno registrate in un libro mastro, quindi bisogna rappresentare questo oggetto mediante una sua classe. Un’altra classe consiste negli attori del dominio, il ruolo delle persone e organizzazioni correlate alle transazioni, sia dipendenti, attori primari del caso d’uso, che i negozi o compagnie dove lavorano, che possono essere rappresentate dalla categoria dei luoghi della transazione o del servizio. Tra gli attori ci potrebbe essere l’osservatore.

Inoltre vanno rappresentati eventi significativi, come la vendita ed il pagamento di beni o servizi, da ricordare sia nel tempo che nel luogo dove sono effettuati. Alcuni eventi sono istantanei, altri occupano un lasso di tempo, occupano un certo periodo. Un’altra categoria consiste negli oggetti fisici, con cui gli attori interagiscono per effettuare certe azioni, possono essere sia i beni offerti che altri oggetti di aiuto agli attori.

Le classi descrizioni sono delle classi le cui istanze servono a descrivere istanze di altri oggetti di un’altra classe. Può essere utile avere una descrizione dei beni offerti, per descrivere le caratteristiche di un prodotto offerto dal sistema, disponibile in una determinata quantità. In un ristorante il meno è composto da descrizione di piatti, non rappresentano il piatto in sé, ma è una sua descrizione che può essere ordinata per ottenere il piatto in sé.

Un’altra categoria collegata sono i cataloghi, di beni o servizi offerti, come un menu nell’esempio precedente. Dopo aver trovato gli oggetti può essere utile chiedersi dove si trovano spazialmente, quindi è utile rappresentare gli oggetti contenitori di oggetti utilizzando altre classi, analogamente si possono rappresentare oggetti in contenitori, questi oggetti possono essere fisici oppure informazioni.

Nelle azioni si possono utilizzare sistemi ausiliari per controllare il pagamento, sistemi di autorizzazione che vanno modellati con opportune classi. Per registrare eventi finanziari si usano delle classi per il libro mastro, il registro, giornale di manutenzioni. Classi collegate sono i sistemi finanziari, per eseguire la transazione, come contanti, assegni, ed altri metodi di pagamento.

Considerando il sistema POS e questo elenco di categoria di classi concettuali, si possono individuare candidate quali: vendita, pagamento in contanti, riga di vendita per l’articolo, che rappresenta una linea in uno scontrino, l’articolo, il registratore di cassa, il cassiere, il cliente, il negozio, la descrizione prodotto, il catalogo prodotti, il libro mastro. Quest’ultima tuttavia non è di interesse nel caso d’uso per il sistema POS, quindi oltre a questa si hanno le restanti classi concettuali.

### Osservazioni

Se si vuole effettuare il modello di dominio per pochi casi d’uso è utile individuare il singolo concetto più importante in questi singoli casi d’uso. Spesso nel titolo di un caso d’uso appare il nome del concetto più importante. L’importanza deriva principalmente dal valore monetario, quindi è opportuno cominciare dalla categoria delle transazioni commerciali. Ma se non sono coinvolti né il commercio né i soldi, ma ad alcuni concetti può essere comunque associato un valore, da parte dell’utente o da parti interessate.

Inoltre è quasi indispensabile utilizzare una classe singleton che rappresenta l’intero dominio e fornisce il contesto alle altre classi, associazioni ed attributi. Nel caso d’uso del sistema POS è il caso della classe `Store`, il negozio.

Nei sistemi client-server è utile rappresentare una classe che individua un punto di accesso al sistema per gli utenti di quel sistema. Un oggetto può rappresentare un punto di accesso fisico o virtuale per il sistema in discussione, e non si chiama mai sistema, poiché il sistema è il tutto. Effettuando una decomposizione di dominio non si ha una classe che rappresenta il sistema per intero. Spesso si chiama portale, nel caso del Sistema POS, si tratta del registratore di cassa `Register`.

Nella modellazione di dominio è utile mostrate gli attori coinvolti negli scenari descritti, con classi che ne rappresentano i loro ruoli. Si discuterà se è utile avere delle super-classi per i ruoli. Di solito invece non è opportuno inserire classi che modellano i casi d’uso o i singoli passi del caso d’uso.

Si possono utilizzare documenti fisici come ricevute di transazioni per poter rappresentare una porzione del dominio, una ricevuta fornisce informazioni sulla vendita, sul negozio, sui prodotti, le righe di vendita per articolo relative a descrizioni dei prodotti. Ci sono informazioni riassuntive sulla vendita e sul pagamento, ed i registratori di cassa utilizzati per registrare la vendita, a volte anche il nome del cassiere. In questo modo si sono individuate molte delle classi concettuali che possono essere inserite nel modello di dominio.

Gli strumenti per UML sono difficili da usare, ed è importante imparare a pensare che ad usare strumenti di disegno UML. Ci stanno dei dubbi normalmente nella modellazione di dominio, ma lavorando in modo iterativo è possibile ed incentivato correggere eventuali errori di modellazione per creare, modificare o rimuovere classi dal modello.

Un’altra linea guida fondamentale è l’uso dei termini del dominio, ed escludere caratteristiche inutili o fuori dalla portata, questo dipende dal dominio. La scelta e l’assegnazione dei nomi agli elementi del modello è molto importante, classi associazioni ed attributi. Anche se non sarà necessario scrivere il glossario in questo corso, è necessario pensare come se bisognasse scriverlo per definire i nomi in modo significativo, evitando la disinformazione.

Quando si aggiunge un elemento bisogna chiedersi che cosa rappresenta, se si risponde con un nome diverso da quello scelto, probabilmente non è un nome adatto. I nomi delle classi sono sempre al singolare, poiché rappresentano una classe, se invece una classe la cui istanza rappresenta un insieme di oggetti, invece di usare un nome al plurale si può usare un termine, un nome collettivo per indicare quell’insieme di oggetti.

Nel modello di dominio non ci sono elementi che parlano del software, l’eccezione è quando il dominio che si sta rappresentando è puramente software.

Se sono presenti oggetti indistinguibili tra di loro, è utile utilizzare una classe descrizione per le stesse proprietà, a volte si chiamano tipologia invece di descrizione. È utile quando serve una descrizione indipendente dall’attuale esistenza di istanze di tali articoli o servizi. Si possono usare per ridurre ridondanze o ripetizioni di informazioni, per evitare anomali, di inserimento, aggiornamento e cancellazione. Sono utili anche nozioni riguardanti la normalizzazione per le basi di dati.

In particolare è importante aggiungere una classe descrizione per poter modellare istanze di articoli o servizi che non sono ancora presenti nel sistema, come articoli o servizi possibili, ma non ancora disponibili all’utente.

Una descrizione testuale di un altro oggetto, sarebbe meglio rappresentarla come un attributo dell’oggetto stesso. Inoltre dipende dal dominio in cui si sta lavorando, per valutare se una determinata classe descrizione è sensata.

## Individuare Associazioni

In UML un’associazione è una relazione tra classi o coppie di classi significativa, viene identificata da un nome e da altre proprietà come le molteplicità dell’associazione. Il criterio fondamentale per individuare associazioni concettuali, è dato dalla necessità di ricordare il legame fra delle coppie di oggetti, ma anche se non si dovesse ricordare potrebbe essere utile per altri motivi, quindi questo criterio non è sufficiente. La necessità di ricordare deve essere persistente o transiente. Questa memoria si riferisce ad una necessità effettiva; se c’è necessità di ricordare, allora bisogna utilizzare un’associazione, se non c’è necessità allora bisogna utilizzare un altro criterio per determinare se è opportuno rappresentare modellare l’associazione.

Un modello di dominio dovrebbe contenere associazioni che vanno ricordate, oppure se sono implicate dall’elenco delle categorie di associazioni comuni. Al contrario delle classi, è consigliabile utilizzare il numero minore di associazioni possibili, mentre è consigliato creare un numero superiore a quanto consigliato per le classi.

Nel software le associazioni sono rappresentate o da variabili riferimento o da collezioni riferimento, sono da un oggetto ad un altro, ma non implicano che il secondo oggetto vede il primo, nel modello di dominio non bisogna pensare alla loro direzionalità né in termini di puntatori o collezioni. Il nome delle associazioni segue lo schema secondo cui permettono di formare una frase di senso compiuto, e deve essere leggibile e significativa, formata dai nomi delle classi che mette in relazione. Sono quindi verbi o locuzioni verbali. Dove possibile vanno evitati nomi poco informativi, come verbi generici “fare”, “usare”, etc. Il nome deve essere in maiuscolo, e si legge da sinistra a destra e dall’alto verso il basso, oppure seguendo la freccia di lettura, una freccia posta accanto al nome dell’associazione che indica il verso.

Come per le classi nel libro di testo si utilizza un elenco di associazioni comuni, che fornisce coppie di classi concettuali tra le quali è comune avere una relazione. Associazioni comuni sono tra transazioni correlate tra di loro, tra una riga di una transazione alla transazione completa. Allo stesso modo un’associazione tra un bene o un servizio venduto o comprato per una transazione. Si usa un’associazione se un oggetto è contenuto in un altro, se è una descrizione di una classe, se è membro, se è un sottoinsieme, se usa gestisce o possiede un’altra classe.

Le più utili sono tra una parte fisica o logica ed il tutto, e tra elementi di una transazione e la transazione completa.

Le associazioni sono mostrate da un segmento, ed è utile rappresentare anche la loro molteplicità. Spesso quando si legge il nome di una transazione si legge all’occidentale, leggendo prima la classe di sinistra, poi il nome dell’associazione e poi la classe di destra. Si inserisce un triangolino, la freccia di lettura, accanto al nome dell’associazione per indicare qual è il verso in cui leggere l’associazione, anche se è semanticamente equivalente il verso in cui viene scritto il nome. Si tende a scegliere il più significativo tra le due orientazioni. In UML le estremità si chiamano ruoli, dalla versione 2 in poi si chiamano estremità di associazioni, le molteplicità infatti si rivolgono alle estremità e non alle associazioni. Questi ruoli possono avere molteplicità, nome e navigabilità.

### Molteplicità

La molteplicità indica quante istanze di una classe possono essere associate al minimo ed al massimo ad un’istanza dell’altra classe. Per indicare un qualsiasi numero di istanze si usa `*`. Il metodo per assegnare la molteplicità è al contrario di quanto studiato per i modelli ER. Per indicare un intervallo si usa la notazione `x..y`, per specificare un numero esatto di istanze, o una lista di numeri esatti si usa `x` o `x,y,z`.

Le molteplicità massime sono di solito molto più importanti delle minime, ed a volte può essere una perdita di tempo determinare la corretta molteplicità minima. Esistono quattro tipi diversi di associazioni in base alle molteplicità, uno a molti e molti ad uno, uno ad uno e molti a molti.

Le associazioni uno a uno, sono poco comuni con partecipazione obbligatoria ad entrambi i lati, mentre è più comune avere associazioni opzionali da un lato dell’associazione. Le molteplicità minime sono difficili da definire e non conviene definirle per associazioni a molti, invece sono necessarie per associazioni con molteplicità massima pari ad uno. Normalmente decidere se la molteplicità minima è zero o uno è irrilevante, a volte sono sottili da definire e non conviene impiegare più tempo per capirlo. A volte la molteplicità minima dipende dal determinato momento che si analizza e quali casi d’uso si stanno considerando.

Non vuol dire che tra due classi è presente una singola associazione, è possibile ci siano un gran numero di associazioni diverse, per questo bisogna identificarle da un nome. Le estremità di un’associazione si chiamano estremità o ruoli, accanto ad un’estremità può essere talvolta utile inserire il nome del ruolo della classe in quell’associazione. Se il nome è significativo può essere utile, per esempio se il modello di domino è anche un dizionario dei termini.

Sono possibili associazioni riflessive o ricorsive che collegano una classe con sé stessa.

Un’associazione può essere derivata come composizione da altre associazioni. Sono delle relazioni binari tra una coppia di classi, fra queste relazioni esiste un’operazione di composizione, un’associazione derivata viene indicata con un `/` davanti al suo nome.

In certi casi non è utile mostrarle, se la regola di derivazione è ovvia. In altri casi è utile mostrarla nel modello di dominio, se il nome di quell’associazione non compare da nessun’altra parte nel modello di dominio allora è meglio inserirla, analogamente se il nome è già presente allora non conviene inserirla. Si ricorda che si vuole inserire un numero lineare di associazioni nel modello di dominio per mantenerlo leggibile. Questo criterio linguistico è il più importante. Un modello di dominio non deve essere perfetto, deve essere adeguato, dato che la modellazione è mirata alla comunicazione.

In UML una classe che rappresenta un insieme di oggetti non si rappresenta con una classe come negli schemi Entity-Relationship, ma con un’associazione sulla classe di cui rappresenta l’insieme. Se quest’insieme ha un nome, allora bisogna aggiungere una classe con quel nome, altrimenti va collegata a qualche altra classe, senza crearne di nuove. Essendo un dizionario visuale dei termini del dominio bisogna inserire solo ciò che rappresenta termini utili.

Talvolta è utile inserire associazioni e nomi per comprendere e comunicare, solo se sono significativi o favoriscono la comprensione del dominio, ma questi concetti non devono essere gestiti direttamente dal sistema.

### Aggregazione e Composizione

Alcune associazioni hanno significati particolari, ci possono essere fino a 18 tipi diversi di associazioni, tra questi i più importanti per ora sono aggregazione e composizione. Un’aggregazione è un’associazione che indica in modo approssimativo una relazione tra una parte dell’intero e quest’ultimo. Se il nome suggerisce questo tipo di relazione allora si tratta di un’aggregazione. Le aggregazioni sono utili poiché alcune operazioni applicate sull’intero si applicano anche alle parti. Le composizioni sono una forma forte di aggregazione, dove valgono delle regole aggiuntive, in questa le istanze delle parti devono sempre appartenere ad un composto, ogni parte appartiene solo ad un composto alla volta, ed il composto è realizzabile dalla creazione o eliminazione delle sue parti. Le istanze della parte vengono sempre create dopo l’intero, ed al più insieme, ma non prima.

Gli estremi di una composizione presentano un rombo sulla classe che rappresenta l’intero.

Generalmente non si mostrano aggregazioni, mentre le composizioni si rappresentano solo se vengono identificati motivi validi, quando si è in dubbio è meglio utilizzare un’associazione semplice. Dal punto di vista software le composizioni sono diverse, poiché oggi software che non appartengono a composizioni nel modello di dominio, possono seguire le regole delle composizioni dal punto di vista software, quindi è possibile identificarle come composizioni software.

## Individuare Attributi

Gli attributi sono delle funzioni, dagli oggetti della classe al tipo degli attributi, sono mostrati nel secondo comparto della classe. Gli attributi derivati si indicano allo stesso modo delle associazioni derivate. Oltre al nome può essere inserito anche il tipo, ma normalmente nella modellazione di dominio si inserisce solo in casi particolari. Si indicano solo attributi di classi e non di associazioni. Derivano dalla necessità di ricordare alcuni dati, per ogni dato che si deve ricordare va rappresentato un attributo di una classe. Il tipo di un attributo intuitivamente deve essere primitivo, non deve essere un concetto complesso del dominio. Se nel mondo reale il valore di un attributo non si pensa come semplice allora è opportuno rappresentarlo come una classe. È sconsigliato usare chiavi esterne, per mostrare un collegamento verso classi esterne, questo metodo infatti impedisce i ragionamenti e la comunicazione.

In casi particolari come l’indirizzo non è chiaro come va rappresentato se con un attributo o una classe. In queste situazioni conviene utilizzare classi tipo di dato, servono per rappresentare valori strutturati o con delle regole non banali. Classi tipo di dato mostrano delle nozioni e concetti poco significativi. Non si mostra la classe ma si indicano a parte quali sono le classi tipi di dato, senza specificarne gli attributi. Quantità numeriche sono spesso rappresentate da classi tipo di dato, poiché necessitano anche di un’unità di misura.

Anche per gli attributi esiste la nozione di attributo derivato, calcolato con qualche formula a partire da un oggetto o altri attributi. Ogni attributo deve appartenere ad una classe, se avendo trovato tutte le classi un attributo non ha una collocazione naturale in nessuna delle classi, forse manca una classe.

Quantità numeriche vengono spesso rappresentate mediante classi di tipo di dato o con il pattern “Quantity”.

## Modelli Concettuali

Nello sviluppo software è comune utilizzare modelli concettuali, e se ne usano di molti tipi, i più comuni sono modelli di dati, che rappresentano informazioni persistenti che deve gestire il sistema. Un secondo tipo di modello concettuale delle informazioni, chiamato modello dei tipi di business, viene utilizzato per rappresentare tutti e soli i dati persistenti e transienti che il sistema deve gestire. Un altro tipo di modello concettuale chiamato modello concettuale di business, che oltre a rappresentare le precedenti, può contenere e mostrare altri concetti importanti. Informazioni che non riguardano dati che il sistema deve gestire direttamente ma possono essere utili per la comprensione del dominio.

Nelle attività successive di analisi e progettazione, avere un modello di dominio che parla solo dei dati che il sistema deve gestire direttamente è più utile; quindi è preferibile avere due varianti, una contenente le informazioni che deve gestire direttamente ed una contenente anche informazioni aggiuntive per favorire la comprensione.

Si può procedere in modo iterativo anche quando si effettua il modello di dominio, un buon modo di procedere è sviluppare il modello di dominio solo su uno dei casi d’uso, e dopo aver finito il modello aggiungere classi, associazioni ed attributi per i successivi caso d’uso. In un progetto iterativo, l’analisi e la modellazione del dominio non dovrebbe richiedere più di un paio d’ore.

## Analisi delle Funzioni

L’analisi delle funzioni ha lo scopo di capire quali sono le interazioni che vengono effettuate nei confronti del sistema. L’effetto di queste azioni non è di interesse in funzione delle analisi delle interazioni. Queste vengono chiamate operazioni di sistema. Può essere utile mostrarle insieme al loro ordine nei diagrammai di sequenza di sistema. In particolare un diagramma di sequenza in UML descrive alcuni oggetti che interagiscono tra di loro, possono essere oggetti software che interagiscono.

Questo diagramma è composto da oggetti con una linea tratteggiata lungo l’asse verticale, questo è l’asse temporale, su cui sono presenti piccoli rettangoli che rappresentano l’attivazione dell’oggetto, dall’invocazione alla terminazione della funzione.

Nei diagrammai di sequenza di sistema questi oggetti non rappresentano oggetti software, è presente un oggetto sistema, analizzato come fosse una scatola nera ed un attore principale di un caso d’uso. Si analizza un caso d’uso alla volta. Si analizza quello che succede durante l’esecuzione del caso d’uso. Le frecce verso il sistema sono piene, mentre frecce tratteggiate sono interazioni dal sistema verso l’attore. Non si mostrano le azioni svolte dal sistema, si modellano solo le funzioni e non il comportamento. Queste frecce uniscono le due linee temporali del sistema e dell’attore principale, ed il loro ordine rappresenta l’ordine in cui vengono chiamate durante un caso d’uso.

Lo scopo di un caso d’uso è descrivere le interazioni tra gli attori ed il sistema in discussione, il sistema esegue delle azioni solo quando viene richiesto da parte dell’attore, queste azioni sono operazioni di sistema, operazioni che il sistema può essere chiamato ad eseguire. Un evento di sistema è una richiesta generata dall’utente per eseguire una certa operazione di sistema, sono eventi di input del sistema, mentre un’operazione di sistema è una trasformazione o interrogazione che il sistema può essere chiamato ad eseguire. Non si cercano direttamente le operazioni di sistema, ma si cercano indirettamente individuando gli eventi di sistema. In UML un evento è definito come un elemento importante o degno di nota che avviene durante l’esecuzione del sistema, ed un’operazione rappresenta ciò che un componente o l’intero sistema vengono chiamati ad eseguire. Esistono due tipi di operazioni di sistema, interrogazioni e trasformazioni; un’interrogazione è un’operazione che restituisce dei valori, senza modificare lo stato del sistema, mentre una trasformazione modifica lo stato del sistema.

### Diagramma di Sequenza di Sistema

Un diagramma di sequenza di sistema SSD, *System Sequence Diagram*, serve a mostrare per uno specifico scenario di caso d’uso, modificato sulla base di qualche estensione ben definita, in riferimento allo scenario principale di successo.

Bisogna definire in modo dettagliato quali sono questi eventi di sistema, poiché sono quelli che è il sistema è tenuto a gestire, sono presenti tre tipi principali di questi eventi ìm eventi esterni da parte di attori, analizzati mediante SSD, eventi temporali e guasti ed eccezioni. Questi eventi definiscono le operazioni di sistema, il loro insieme rappresenta l’interfaccia del sistema, che dovrà essere progettato nel OOD.

Un SSD può essere generato per ispezione dallo scenario di riferimento del caso d’uso. Bisogna fissare il caso d’uso, impostando il sistema e gli attori principali. Ogni passo del caso d’uso viene analizzato e ne viene determinata l’interazione con il sistema o dal sistema e viene rappresentata come una freccia, le azioni del sistema non vengono mostrate. Se dei passi vengono ripetuti si può includere un rettangolo che indica il loop, che racchiude le opportune interazioni ripetute. Questi freme di interazione sono etichettati da una parola chiave, per effettuare un ciclo si ha “loop”, ma è possibile realizzare istruzioni condizionali ed altri tipi di interazioni specifiche. Interazioni che non coinvolgono il sistema non vengono rappresentate. Le operazioni di sistema vengono implicitamente definite per ogni evento di sistema, e bisogna assegnare un nome a queste azioni, dopo averle definite. Il modo in cui vengono definite nei due versi è diverso. Il nome di un azione del sistema deve essere scritta come se si trattasse di un metodo o funzione, in camel case. In UML un’operazione è un termine astratto e l’implementazione di un’operazione si chiama metodo. Queste operazioni possono avere dei parametri che vanno indicati nelle azioni generate.

Le risposte di interazioni vengono scritte in modo informale come un insieme di valori restituiti, generati da azioni interne al sistema. Gli eventi e le operazioni di sistema vanno descritte al livello dell’intento non dell’azione causata. Bisogna determinare perché si vuole effettuare quell’evento. Per istruzioni ripetitive un rettangolo racchiude le interazioni, ed un’etichetta ne descrive il tipo di ripetizione. In UML le condizioni vengono racchiuse un parentesi quadre e vengono messe sulla linea tratteggiata che valuta la condizione. I nomi negli SSD sono sintetici, ed è opportuno inserirli in un glossario per definirli. Un SSD può definire anche interazioni tra il sistema ed altri sistemi esterni, ma se ne parlerà più avanti, anche per la realizzazione di diagrammi di comunicazione.

Può essere che un’operazione di sistema ossa essere rappresentata esattamente da un passo, talvolta sono spezzate su più passi e talvolta un passo contiene più operazioni di sistema. Un’operazione di sistema è di solito relativa ad un’interazione a grana media tra l’attore ed il sistema. Non bisogna usare oggetti e riferimento come parametri di sistema. Non bisogna considerare le risposte come oggetti software. La prima parte del nome di un’operazione dovrebbe essere un verbo, ed il nome deve essere relativo all’intento dell’operazione e non del caso d’uso. I passi iniziali e finali potrebbero non rappresentare operazioni di sistema. Spesso un’operazione di sistema è relativa a più parametri, e non è comune ed a volte un errore separare vari parametri in più operazioni di sistema, sopratutto se questo avviene in uno stesso passo del caso d’uso. Inoltre è utile considerare passi concreti e non astratti dello scenario del caso d’uso, questo infatti può astrarre dei concetti reali, ma è utile concretizzarli per distinguerli da eventuali operazioni simili derivate dalla stessa astrazione. Si considera l’esecuzione di un caso d’uso durante una singola sessione di un sistema client-server, ma ciò non è garantito quindi procedendo con la progettazione potrebbe essere utile considerare parametri per distinguere le varie sessioni tra di loro. Per ora non è utile rappresentarli, dato che si tratta di semplice analisi.

L’identificazione delle operazioni di sistema va effettuata per ogni caso d’uso del sistema, ma vanno realizzati SSD solamente per gli scenari più complessi, essendo parte del modello dei casi d’uso. Sono una visualizzazione delle operazioni implicite nei casi d’uso, possono essere utilizzate per realizzare delle stime di costo, ma non sono elaborati ufficiali di UP.

### Contratti delle Operazioni

Nell’analisi può essere utile definire in modo preciso il comportamento delle operazioni di sistema questo si realizza tramite i contratti. I contratti delle operazioni di sistema descrivono l’effetto prodotto dalla loro esecuzione, in termini di cambiamenti di stato del sistema. Questo si basa su una rappresentazione astratta dello stato del sistema basata sul modello di dominio.

Un contratto contiene il prototipo dell’operazione, con il nome ed i suoi parametri, i riferimenti ai casi d’uso dove può verificarsi, le pre e post-condizioni. La prima identifica le ipotesi circa lo stato del sistema prima dell’esecuzione, descrivono lo stato di avanzamento del caso d’uso; mentre la seconda descrive i cambiamenti di stato dopo l’esecuzione dell’operazione.

I contratti descrivono il cambiamento dello stato del sistema, descrivendo lo stato prima e dopo la sua esecuzione, senza descrivere come viene effettuato. Solamente le trasformazioni generano un cambiamento di stato del sistema, quindi la parte di trasformazione è molto più interessante della parte di interrogazione. Quindi generalmente si possono escludere le operazioni di sistema che rappresentano semplici interrogazioni dall’analisi dei contratti. L’analisi del comportamento delle operazioni di sistema, è analisi solo delle trasformazioni. Una stessa operazione di sistema potrebbe comparire in più casi d’uso.

Quando si è parlato di modellazione di domino non si è parlato né di funzioni né di comportamento, l’analisi del comportamento ricongiunge queste due argomenti. Le due analisi possono essere svolte indipendentemente. Il cambiamento di stato non viene descritto in base alla metodologia in cui il sistema conserva i dati, ma sulla base delle interazioni descritte nel modello di dominio, indipendente dall’implementazione. Si immagina che il sistema gestisca in memoria un grafo che rappresenta gli oggetti del dominio del sistema. Un contratto è relativo ad una singola operazione di sistema. Il modello di dominio di riferimento per scrivere questo contratto è relativo alle sole informazioni che il sistema deve gestire direttamente in quel momento. L’effetto delle operazioni di sistema viene analizzato nell’analisi del comportamento. Questo cambiamento di stato viene espresso in modo astratto espresso in termini del modello di dominio.

Il cuore del contratto sono la pre-condizione e la post-condizione. Le prime sezioni sono l’operazione ed i riferimenti ai casi d’uso in cui si può verificare. Le pre-condizioni sono delle condizioni prima di chiedere l’operazioni di sistema, ipotesi, assunzioni circa lo stato del sistema, subito prima che viene richiesta. Sono espresse in modo abbastanza informale per descrivere a quale punto dell’esecuzione del caso d’uso ci si trova. Le post-condizioni descrivono i cambiamenti di stato dopo l’esecuzione dell’operazione nel modello di dominio. Non si parla mai del durante, non viene descritto cosa accade durante l’esecuzione dell’operazione del sistema, poiché si tratta di progettazione.

Le post-condizioni descrivono cambiamenti di stato, non operazioni, dopo l’esecuzione, e quindi vanno scritte al passato. I cambiamenti di stato nelle post-condizioni possono essere solo di tre tipi:

- Creazione o cancellazione di un oggetto

- Formazione o rotture di un collegamento

- Cambiamento del valore di un attributo

Le post-condizioni descrivono in modo parametrico rispetto ai parametri dell’operazione di sistema.

Per trovare le post-condizioni ci si chiede se vanno creati o cancellati degli oggetti, se vengono formati o rotti dei collegamenti, sono cambiati valori di attributi. Per indicare gli oggetti ed attributi si indica sempre il nome, il tipo e la classe. Per i collegamenti bisogna individuare gli oggetti, questi possono essere direttamente noti al sistema, indicati nelle pre-condizioni o creati durante l’esecuzione, oppure intuitivamente bisogna effettuare una ricerca. In questo caso bisogna indicare che si sta scegliendo un oggetto tra tanti ed il criterio ed i parametri con cui si è effettuata la ricerca. Le pre-condizioni hanno lo scopo di descrivere in modo sintetico lo stato di avanzamento del caso d’uso, inoltre indica gli oggetti noti, di interesse a quel punto del caso d’uso.

Nell’analisi si utilizza il punto di vista concettuale, può avere tante sfumature. Nella modellazione di dominio, si chiede cosa esiste nel dominio. Non è l’approccio giusto nella scrittura dei contratti, poiché si vuole conoscere le informazioni circa il mondo reale che il sistema conosce. È comune adattare una prospettiva dell’esistenza, nei contratti invece si parla di conoscenza, ovvero il sistema viene a conoscenza dal punto di vista concettuale di qualcosa. Se viene creata una nuova istanza di una classe, oppure se viene formato un collegamento, il sistema diventa a conoscenza di queste nuove informazioni, non si interessa infatti dell’esistenza per sé di questi nuovi elementi, ma solamente della loro conoscenza da parte del sistema. In una post-condizione è lecito dire che è stata creata un’istanza di una classe, se il sistema non ne era già a conoscenza.

Per scrivere i contratti si considerano solo le operazioni che è più difficile capire, tra quelle definite nell’SSD del caso d’uso corrente. Le pre-condizioni sono normalmente implicate dell’esecuzione di operazioni di sistema precedenti.

Per i sistemi client-server bisogna scrivere i contratti dal punto di vista del punto di accesso al sistema, poiché rappresenta il tramite degli input degli attori che lo utilizzano. Quando nei contratti si parla del punto di accesso direttamente, nella formazione dei collegamenti si indica quello specifico che sta effettuando le operazioni richieste dall’attore, quindi non è necessario effettuare la ricerca di questo oggetto, dato che in questo modo è già noto al sistema.

Quando si scrivono contratti per interrogazioni, le post-condizioni sono sempre vuote. Non si prendono in considerazione in questa analisi, ma si considerano nel modello di dominio per capire quale informazioni il sistema deve gestire direttamente. Dato che le trasformazioni sono operazioni molto più complesse, sono centrali nell’analisi delle funzioni per dedicare uno sforzo maggiore alla loro comprensione. Non sempre è facile distinguere tra interrogazioni e trasformazioni.

Può essere utile ragionare su un’intera esecuzione del caso d’uso, per realizzare i contratti, in questo modo si analizzano complessivamente le post-condizioni e bisogna dividerle tra le post-condizioni delle singole operazioni di sistema. Le post-condizioni delle singole operazioni inoltre sono interessate anche ad i cambiamenti transienti.

Collegamenti transienti non sono permanenti, spesso riguardano oggetti correnti per questo caso d’uso o per quel specifico passo del caso d’uso. Sono transienti se vengono utilizzati solamente nel caso d’uso o in un suo passo, e non più dopo la sua terminazione. In questi casi non bisogna creare un collegamento permanente, ma un collegamento transiente, sempre verso l’oggetto che rappresenta il punto d’accesso al sistema, in sistemi client-server.

Il mondo, il modello di dominio, va guardato dall’istanza dell’oggetto che rappresenta il punto d’accesso primario dell’attore del caso d’uso.

Si possono inserire commenti, ma non devono violare la forma del contratto.

Rappresenta un errore indicare la formazione di collegamenti già noti al sistema, se sono presenti più di un collegamento tra due oggetti, allora è opportuno identificarli tramite il loro nome nel contratto; altrimenti non è necessario, poiché si tratta dell’unico collegamento tra quei due oggetti.

I contratti e l’SSD per un caso d’uso devono essere mutualmente coerenti, quindi se si modifica uno o l’altro, in seguito a miglioramenti o dopo aver trovato degli errori, è necessario cambiarli entrambi per renderli coerenti tra di loro. Durante la scrittura dei contratti infatti è possibile identificare informazioni transienti che il sistema deve gestire, da rappresentare nel modello di dominio, dato che la sua analisi è mirata solo alle informazioni persistenti. Generalmente quindi questi due modelli vengono realizzati in parallelo, il modello di dominio e l’analisi delle funzioni, per aggiornarsi a vicenda, poiché analizzano due aspetti diversi della stessa realtà di interesse.

Al termine dell’esecuzione di un caso d’uso si può assumere che tutte le informazioni transienti precedenti, come i collegamenti formati vengano implicitamente cancellate, quindi non è necessario descriverle esplicitamente nelle post-condizioni dell’ultima operazione del caso d’uso.

Anche se non sempre è necessario scrivere contratti, è sempre utile pensare i contratti, appunto per analizza il sistema dal punto di vista di informazioni transienti.

# Progettazione

La progettazione ha lo scopo di trovare la struttura di una soluzione software del problema in esame, capire quali sono gli strumenti software, precedentemente considerati a scatola nera nell’analisi, ora completamente di interesse. La progettazione orientata agli oggetti OOD si basa sullo specificare una comunità di oggetti e classi software che collaborano per soddisfare requisiti. Queste classi scelte in OOD, verranno poi implementate in OOP.

Un possibile approccio consiste in un progettista che esegue progettazione, visuale, ma non implementa in codice il software. Un altro consiste nel sovrapporre il ruolo di progettista e programmatore. Durante un’iterazione nelle prime giornate lavora come progettista per poi lavorare come programmatore scrivendo codice sulla base delle decisioni di progetto che ha preso, strategia “disegna e poi codifica”. Un altro modo ulteriore di procedere consiste nel non passare per UML.

Una pratica della modellazione agile è il disegno leggero, dove si inseriscono solamente i dettagli importanti, utili a comprendere e comunicare nei disegni UML. Alcune pratiche consistono nel modellare in gruppo, e creare diversi modelli in parallelo, ed iterare ad un altro modello, tra analisi e progettazione. Al disegno leggero vengono dedicate poche ore all’inizio dell’iterazione, passando rapidamente all’implementazione ed ai test, con progettazione durante la codifica.

Vengono usati due tipi di diagrammi, diagrammi delle classi e diagrammi delle partizioni, due tipi diversi di diagrammi, analizzati sempre dal punto di vista software, questi rappresentano modelli statici e dinamici. Si hanno quindi due tipi di progettazione, statica e dinamica, di cui la dinamica è più importante e su questa bisogna soffermarsi. La progettazione a oggetti dinamica consiste più che all’individuazione dei metodi, alla progettazione delle interazioni tra oggetti. Le uniche interazioni ammesse fra oggetti che si considerano sono la creazione di oggetti e l’invocazione di metodi. Inoltre per progettare si considerano pattern GRASP e la progettazione guidata dalla responsabilità.

In seguito si effettua la modellazione ad oggetti statica, utile per determinare quali classi e come scriverle. Normalmente non si svolge un approccio a cascata, ma si creano i modelli in parallelo. L’importante in OOD è comprendere e comunicare, sapendo assegnare in modo abile le responsabilità agli oggetti software, sulla base di principi e design pattern. Verranno esposti questi principi e pattern durante questa sezione, strada facendo.

Progettare per un ingegnerie non vuol dire capire il problema, ma determinare tra tutte le soluzioni la migliore che soddisfano certi criteri.

La valutazione è simile, ma il modo di lavorare è molto diverso rispetto all’analisi, poiché in analisi si lavora dal punto di vista concettuale, mentre in progettazione si lavora dal punto di vista software.

## Architettura Logica

Vengono rielaborate le nozioni relative all’introduzione all’architettura. Si parla dell’architettura a strati, dove il codice deve essere scritto e strutturato in macro elementi. Uno strato di presentazione, uno della logica applicativa ed uno dei servizi tecnici. La struttura può essere descritta da un diagramma package di UML, a loro volta possono contenere altri package. La notazione per un package è un rettangolo con un’etichetta dove viene inserito il nome. Le frecce di collegamenti tra i vari package vengono chiamate dipendenze, nell’architettura a strati sono dall’alto verso il basso, e rappresentano interazioni tra porzioni di codice.

Una scelta molto comune e minimale degli strati per sistemi informatici è questa a tre strati, in questo corso ci si concentra soprattutto sullo sviluppo dello strato della logica applicativa e sulla comunicazione tra i vari strati. La separazione di interessi impone che macro-attività separate siano su package separati.

Lo strato della logica applicativa non dipende dalle implementazioni dello strato di presentazione e dei servizi tecnici, è indipendente dalle tecnologie che si vogliono utilizzare. È basata su due principi fondamentali, il principio di separazione degli interessi, responsabilità diverse devono essere mantenute in strati strati diversi, ed il principio di modularità o coesione e accoppiamento. L’interesse più importante è quello della logica applicativo, separato sia dall’interesse di presentazione che dall’interesse dei servizi tecnici. Il principio di modularità afferma che il codice deve essere organizzato in moduli, internamente coesi e debolmente accoppiati tra di loro. Questi sono i due principi di progettazione più importanti.

I nomi delle classi nel modello di dominio sono ispirati dal nome delle classi concettuali. Per cui lo strato della logica applicativa può essere organizzato come uno strato del dominio, in base al principio del salto rappresentazionale basso, anche se è uno dei principi di progettazione peggiore. In questo modello gli oggetti incapsulano dati ed operazioni.

DDD, *Domain-Driven Design*, propone un’architettura a quattro strati, dov’è presente uno strato di dominio ed uno di applicazione, in quest’ultimo è presenta una sola classe che gestisce tutte le informazioni transienti, tutte quelle permanenti sono presenti nello strato di dominio, che rappresenta il modello di dominio, sulla base del salto rappresentazionale basso.

Il principio di separazione Modello-Vista, dove per modello si intende lo strato di dominio e per vista si intende lo strato di presentazione, afferma che gli oggetti non di presentazione, ovvero quelli di modello non devono parlare direttamente con gli oggetti della presentazione. La comunicazione indiretta è possibile, ma se ne parlerà più avanti; inoltre nella vista non ci deve essere logica applicativa. Questo rappresenta un caso particolare del principio di separazione degli interessi.

Nella progettazione bisogna individuare il codice per effettuare questa interazione, diviso tra gli strati di presentazione e dominio, con opportune chiamate di metodi. I diagrammi di sequenza di sistema definiscono nomi di operazioni che devono essere definite all’interno di oggetti con gli opportuni parametri. Un SSD descrive l’interfaccia, parziale, dello strato di dominio, individuando le operazioni di sistema relativa ai metodi di classi dello strato di dominio.

## Diagrammi delle Classi

Il diagramma delle classi in UP si chiama diagramma delle classi di progetto DCD, *Design Class Diagram*, controparte del modello di dominio, entrambi diagrammi delle classi, ma con finalità diverse.

Si sono già usati diagrammi delle classi di UML, si parla più in generale dei diagrammi delle classi in riferimento dal punto di vista software, sono utili nella progettazione statica, possono essere classi, interfacce o associazioni. Una classe rappresenta un pezzo di codice che a seconda dei casi, o è già stato scritto o si sta decidendo di scrivere. Descrive le caratteristiche di queste classi. Una classe è rappresentata da un rettangolo, diviso in tre compartimenti. Nel compartimento più in alto si trova il nome della classe, nel compartimento in mezzo si trovano gli attributi, andranno poi implementati come variabili di istanza. Queste classi software sono un tipo di classificatore in UML; ovvero un elemento di un modello che descrive caratteristiche comportamentali, metodi e funzioni, e strutturali, variabili. Il terzo compartimento non è delle variabili di istanza, poiché alcune vengono rappresentate tramite associazioni, può implicare che in una delle due classi coinvolte vada definita una variabile di istanza di tipo riferimento ad oggetto.

Normalmente si assume che le variabili di istanza siano private, la notazione di UML è `+` per pubbliche, `-` per private e `#` per protected, alcune sottolineate sono variabili statiche o variabili di classe, per tutti gli oggetti della classe è presente una sola copia di questa variabile. L’ultimo compartimento contiene le operazioni, nomi di metodi, nella programmazione nella classe si dovrà scrivere anche il corpo di questi metodi. La notazione generale è del tipo:

        visibilità nome : tipo molteplicità = default { stringa-proprietà }

In UML quasi tutto è opzionale, anche solo una classe contenente il nome è un diagramma delle classi valido.

La linea che finisce con un triangolo rappresenta un’estensione, inoltre le interfacce sono mostrate con un rettangolo, ma accanto al nome della classe viene scritto `<<Interface>>`. La freccia tratteggiata che finisce con un triangolo indica che la classe da cui parte implementa la classe che punta. Le interfacce hanno solo il compartimento delle operazioni, in questo caso sono metodi poiché le interfacce non contengono le loro implementazioni.

Un elemento nuovo sono le frecce di navigabilità, mostrate solo su alcune associazioni indicano che la classe puntata viene memorizzata come riferimento dalla classe che punta. Saranno rappresentate da variabili di istanza di tipo riferimento. Le dipendenze sono delle frecce tratteggiate che finiscono con la punta di una freccia, ma non con un triangolo pieno, quindi ha una notazione simile all’implementazione delle interfacce, la classe che punta dipende in qualche modo dalla classe puntata. Le associazioni non hanno nomi, invece sono indicati i nomo e le molteplicità solamente sul ruolo puntato dalla freccia, ed indica il nome della variabile d’istanza di riferimento che utilizza l’oggetto da cui parte la freccia. La molteplicità inoltre si può inserire solo sul lato navigabile.

Un ultimo elemento sono le note, dei diagrammi con orecchietta, che vanno interpretati come dei commenti con una linea tratteggiata che finisce con un pallino che indicano a quale classe si riferiscono.

Possono essere rappresentate anche da estremità di associazione, dell’associazione non viene detto il nome, di molteplicità viene riportata una sola accanto alla freccia di navigabilità, la maggior parte delle associazioni sono navigabili in un solo verso, ed è possibile che associazioni bidirezionali vengano rappresentate con due associazioni. Vicino alla molteplicità viene scritto il nome del ruolo. Viene implementato come un riferimento dal punto di vista software verso l’oggetto navigabile, e non è possibile percorrerle in verso opposto, ovvero dal lato software è impossibile conoscere le istanze a cui è collegato se non è navigabile. Se si vogliono conoscere le informazioni da ambo i lati si utilizzano frecce bidirezionali, ma si preferisce avere due frecce unidirezionali, inoltre non va mostrato il nome delle associazioni.

In UML è permesso, ma viene considerato un errore in questo corso, mostrare un’associazione mediante un attributo. Un’associazione è più importante di un attributo. UML ha un proprio sistema di tipi e nei diagrammi delle classi si può usare il sistema dei tipi di UML ed in parte si utilizzerà per le collezioni, oppure si può utilizzare il sistema di tipi di Java. Per indicare che un’associazione è ordinata si specifica tra parentesi graffe `{ordered}`, o utilizzando le collezioni `{List}`. Si utilizzano collezioni quando la molteplicità del ruolo navigabile è maggiore di uno.

In questo corso di collezioni si utilizzano solo liste e mappe, normalmente non è utile utilizzare insiemi. Per mostrare una collezione di riferimento, si potrebbe utilizzare una notazione degli attributi ripetuti, da non usare in questo corso. In UML elementi delle collezioni sono indicati da una notazione che ricorda l’accesso di elementi degli array in Java, `[]`. Si possono utilizzare attributi per indicare in modo testuale un’associazione a molti.

Le collezioni sono oggetti, una collezione non memorizza le istanze degli oggetti ma riferimenti a questi oggetti. Generalmente non si userà la notazione che mostra un oggetto a sé per rappresentare le collezioni, per semplicità viene quindi lasciato implicito, ma il suo uso è consentito anche nei diagrammi degli oggetti software.

Il rettangolo con orecchietta normalmente si chiama nota, per esprimere commenti, possono essere utilizzati per esprimere dei vincoli, per anticipare l’implementazione scritto in un linguaggio di programmazione o pseudo-codice.

L’operazione rappresenta il metodo, ma il metodo non è solo un’operazione. Un’operazione in UML è la dichiarazione, descrizione, specifica di una trasformazione o interrogazione che un oggetto può essere chiamato ad eseguire. Questo rappresenta un prototipo, e può includere eventuali vincoli quali pre e post-condizioni del metodo. Un diagramma di classi UML mostra solo le operazioni, se si vogliono mostrare metodi, si può aggiungere in una nota. Elementi come la visibilità, la lista dei parametri ed il tipo di ritorno sono opzionali. La notazione testuale di un’operazione è la seguente:

        visibilità nome ( lista-parametri ) : tipo-ritorno { stringa-proprietà }

Nel codice di una classe, iin corrispondenza all’operazione `create` possono essere inseriti costruttori usando lo stereotipo `<<constructor>>`, inoltre classi getter e setter se si decide di implementarle non è necessario inserirle nel diagramma di classi di oggetti.

IN UML parole chiavi sono annotazioni per classificare un elemento, vengono contenute tra due parentesi francesi `<<...>>`, mentre un vincolo è una condizione semantica o restrizione, contenuta tra parentesi graffe.

Si usa il simbolo della generalizzazione per indicare l’ereditarietà tra le classi, la notazione si può usare anche nella modellazione di dominio, in cui ha un significato completamente diverso, ma se ne parlerà più in dettaglio in sezioni successive.

Le dipendenze indicano che un elemento conosce un altro elemento in modo forte, si discuterà la loro utilità in OOD. Una dipendenza in UML sono mostrate da frecce tratteggiate con una punta aperta, in alcuni linguaggi di programmazione se una variabile ha un certo tipo il compilatore se ci sono modifiche nella classe dove viene definito il tipo ricompila sia questa classe che le classi che dipendono, ovvero che hanno variabili di quel tipo, questa si chiama dipendenza di compilazione. Tenere traccia di queste dipendenze è importante. Con le estensioni di classi, la sottoclasse dipende dalla superclasse, la superclasse in generale non dipende dalle sottoclassi. Tutte le frecce nei diagrammi di classe indicano dipendenze, quindi se c’è già una dipendenza tra due classi non è necessario aggiungere una freccia tratteggiata. Non è utile mostrare dipendenze già implicate da altri elementi, invece è utile mostrare dipendenze di uso per visibilità globale, per parametro, locale, o per metodo statico, ed eventuali dipendenze di creazione. Le dipendenze possono essere etichettate con un tipo, può essere una chiamata `<<call>>`, oppure può richiedere la creazione di un oggetto con `<<create>>`.

Si un oggetto richiedere un interfaccia si realizza con una linea che finisce con un semicerchio, dove viene scritto il nome dell’interfaccia richiesta dalla classe. Se un’interfaccia collabora con un oggetto ed è una dipendenza di un altro, si utilizza sempre una linea tratteggiata, ma questa termina in una linea che finisce su un pallino che parte dall’oggetto su cui collabora l’interfaccia, con scritto sopra il nome dell’interfaccia. Questa notazione si chiama a lollipop. Se un oggetto implementa un’interfaccia si utilizza una linea tratteggiata che termina per un triangolo. La notazione a lollipop indica che un oggetto implementa una certa interfaccia, può essere unita con la notazione a semicerchio quando un altro oggetto richiede questa interfaccia quando viene implementata da quell’oggetto.

Anche dal punto di vista software ha senso parlare di aggregazioni e composizioni, sono navigabili dall’intero verso la parte e non viceversa. Nel software possono essere utilizzate con un significato diverso rispetto al modello di dominio, ma mantengono la stessa notazione in UML, semplicemente aggiungendo una freccia all’estremo terminante nella parte. Nel software si potrebbe usare una composizione per indicare che l’oggetto parte non è condiviso da altri oggetti. Dal punto di vista software indica che si rappresentano come oggetti diversi tra le varie istanze della classe intero.

I vincoli sono condizioni espresse tra parentesi graffe, all’interno di un elemento o all’interno di una nota, come condizione astratta o porzione di codice.

Per indicare classi singleton si inserisce un nome in alto a destra nel rettangolo del nome dell’oggetto, questi hanno un significato diverso rispetto al modello di dominio. Si indica che verrà creata una singola istanza di questa classe. Inoltre per indicare attributi o metodi statici si indicano con una sottolineatura.

La progettazione è guidata dalle responsabilità, queste vengono assegnate nei modelli dinamici e sintetizzate nei modelli statici, quindi è necessario nelle pratiche agili lavorare su questi diagrammi in parallelo. Le classi definite nei diagrammi di interazione vengono definite nei diagrammi delle classi, mentre i messaggi nei diagrammi di interazione indicano metodi nelle classi.

## Diagramma di Interazione

I diagrammi di interazione di UML permettono di descrivere oggetti che si scambiano messaggi, permette una modellazione dinamica, dal punto di vista software. Questa è un’attività fondamentale della OOD.

Per interazione si intende una specifica di come alcuni oggetti si scambiano oggetti nel tempo per eseguire un certo compito in un contesto. Un diagramma di interazione mostra la collaborazione id un gruppo di oggetti che vuole realizzare lo stesso compito. Gli oggetti si chiamano partecipanti, il compito è dato da un messaggio trovato e l’interazione tra i partecipanti è basata sullo scambio di messaggi.

Ci sono due tipi di diagrammi di interazione, i diagrammi si sequenza ed i diagrammi di comunicazione. Nei diagrammi di comunicazione sono presenti i partecipanti e si scambiano informazioni mandandosi messaggi. Per indicare un messaggio la notazione prevedere un’espressione messaggio e poi una freccia, un altro elemento grafico è una linea di collegamento. L’espressione del messaggio indica sempre un’invocazione di metodi anche quando non si usano le parentesi. Collegamenti e frecce sono elementi grafici distinti, le linee puntate sono solo nei diagrammi delle classi ed indicano associazioni navigabili, invece nei diagrammi di interazione le frecce rappresentano messaggi, invocazioni di metodi.

Il primo messaggio non viene numerato, gli altri messaggi sono numerati, e le risposte vengono numerate con numerazione gerarchica o decimale: il messaggio $X.x$ viene inviato in risposta al messaggio $X$, inviato durante la gestione del messaggio $X$. Si può inserire questa numerazione anche non solo su uno stesso collegamento. Per i messaggi del primo oggetto si utilizza la numerazione $X$, $Y$.

Per indicare gli oggetti si usa il nome della loro istanza seguito da `:` ed il nome della classe di appartenenza. Vanno mostrati anche oggetti collezioni allo stesso modo, specificando nel tipo il nome della collezione con il tipo degli oggetti contenuti in `<>`. Il tipo può essere anche un’interfaccia o una classe astratta. Per indicare un elemento della collezione si indica accanto al nome dell’istanza con un `[i]`, come per l’indicizzazione di un array.

Per interagire con le collezioni, si può usare la notazione che indica l’oggetto collezione, ed in questo caso le uniche operazioni sono quelle definite dall’oggetto. Non bisogna mostrare messaggi uscenti dalle collezioni. Per iterare su una collezione la notazione prevede di usare il destinatario del messaggio non l’oggetto collezione, ma un generico elemento $i$-esimo della collezione e si indica con notazione iterativa come iterare sugli elementi. Quando si lavora su una collezione, e si itera sugli elementi della collezione normalmente si itera su tutti gli elementi. Non verrà mai mostrato il funzionamento di una collezione, oggetti predefiniti. Per interagire con le collezioni si devono usare solo metodi generici come `add`, `find`, `remove`, etc. Alternativamente si può utilizzare la notazione specifica del JCF.

Ad una oggetto è possibile chiedere solo operazioni predefinite della sua classe. Per dire che un oggetto esegue un’operazione si usa una linea collegata a sé stesso. La creazione di oggetti non si mostra con la linea tratteggiata, la notazione è uguale a quella di creare un metodo, e per indicare che si tratta di creazione si usa lo stereotipo `«create»` oppure il messaggio speciale `create`, inoltre si può inserire all’interno del nome dell’oggetto creato `{new}`, per indicare che si tratta di un oggetto nuovo.

La formazione dei collegamenti è particolarmente importante, per formare un collegamento ad uno, si inserisce nel parametro del messaggio inviato all’oggetto un riferimento simbolico ad un oggetto, e bisogna esplicitare un vincolo indicando quel parametro a cosa corrisponde. `{X = x}`, dove $X$ è la variabile locale ed $x$ è il riferimento simbolo all’oggetto. Se non si usa questa convenzione non è possibile capire che si sta formando un collegamento tra due oggetti. Questo è un tipo di numerazione annidata.

I frame di interazione non sono presenti nei diagrammi di comunicazione, per mostrare le istruzioni condizionali e ripetitive si usa un altro approccio, si mette davanti al nome del messaggio una condizione fra parentesi quadre`[...]`. Per messaggi condizionali consecutivi si indicano percorsi condizionali mutualmente esclusivi, numerati con una lettera a seguito del numero `X`$\alpha$, ulteriori messaggi nella catena vengono segnati con `X`$\alpha$`.x`, in notazione gerarchica. Per le istruzioni iterative bisogna usare l’asterisco e la notazione precedente per indicare con una notazione informale quante volte eseguire l’iterazione.

Un oggetto potrebbe invocare un metodo su una classe astratta, essendo un messaggio polimorfo, senza sapere quale è il tipo concerto del messaggio. Se l’esecuzione del metodo è diverso per i vari tipi concreti si ferma l’esecuzione del diagramma e si ricomincia mostrando i vari casi dell’esecuzione per ciascun metodo concreto. Di solito è un errore creare oggetti di classi astratti o interfacce, ma c’è un’eccezione, quando si vogliono creare delle collezioni, il tipo che si utilizza è un’interfaccia.

Un messaggio è rappresentato da un’espressione scritta accanto ad una linea di collegamento che indica la direzione del messaggio, e definisce quale è il mittente ed il destinatario. Il collegamento ed il messaggio sono due elementi distinti.

Se si disegna a mano i diagrammi di comunicazione sono più efficaci, se si usa un buon strumento i diagrammi di sequenza possono essere più efficaci, essendo più espressivi e leggibili.

## Visibilità tra Oggetti

Un oggetto può inviare un messaggio ad un altro oggetto solamente se il mittente ha visibilità del destinatario, quindi conosce un riferimento al destinatario del messaggio. La visibilità deve essere progettata, il progetto non solo deve contenere tutti i messaggi, ma deve garantire che in termini di visibilità siano sensati.

Esistono quattro modi comuni per avere visibilità da un oggetto $A$ ad un oggetto $B$. La prima è la visibilità per attributo o per variabile di istanza, dove l’oggetto $B$ è attributo di $A$. La visibilità per parametro indica che $B$ è stato passato ad $A$ come parametro di un metodo. La visibilità locale indica che $B$ è stato creato in un metodo di $A$. La visibilità globale è possibile e pericolosa poiché induce un accoppiamento alto, dove $B$ è visible in modo globale all’interno del progetto, e quindi non solo dall’oggetto $A$.

La visibilità descritta nell’esempio POS tra il registratore ed il catalogo prodotti è per attributo, dove nel caso d’uso d’avviamento viene inizializzata questa variabile nel suo costruttore. La visibilità per parametro avviene nel passaggio della descrizione tra il registratore, la vendita e la riga di vendita.

Si può trasformare la visibilità che ha un oggetto rispetto ad altri oggetti, memorizzando in variabili di istanza dal parametro di un metodo. Si può passare da visibilità locale a visibilità per attributo, memorizzando il riferimento, o per parametro, passandolo ad altri oggetti.

Un progetto deve garantire la visibilità tra gli oggetti necessarie per consentire l’interazione corretta tra di loro. La visibilità per attributo è la forma comunemente a più lunga durata, sopravvive a diverse esecuzioni di operazioni durante lo svolgimento di un caso d’uso, quindi è quella che deve essere progettata con più cura.

Un errore comune nell’ambito della visibilità è mostrare un messaggio dove il mittente non ha visibilità dell’oggetto destinatario, se è veramente importante in quel contesto inviare il messaggio allora bisogna determinare in che modo il mittente possa avere visibilità del destinatario, e si progetta per ottenere questa forma di visibilità. Altrimenti potrebbe essere opportuno che sia un altro oggetto a collaborare con il destinatario, quindi bisogna applicare information expert, e valutare le alternative con low coupling e high cohesion.

## Pattern GRASP

Nel software una responsabilità è un’astrazione di ciò che esegue o rappresenta quel componente. Le responsabilità vengono assegnate durante la fase di progettazione. Le responsabilità degli oggetti sono o di fare, di eseguire un’istruzione di dichiarare un oggetto di coordinare un gruppo di oggetti che devono svolgere un compito, etc.; o di conoscere, conoscere oggetti collegati, dati derivati, o dati appartenenti ad oggetti. Tutte queste sono tipologie di responsabilità. Le responsabilità di fare vengono espresse nei contratti o nei diagrammi di sequenza di sistema, e si trovano scritte informalmente nel testo del caso d’uso. L’idea di responsabilità è un’astrazione, non ’cè niente che corrisponde direttamente ad una responsabilità nel codice, viene rappresentata da una variabile di istanza o da un metodo, istruzione o classe, nei casi più semplici; nei casi più complessi è rappresentata da vari variabili di istanza e metodi, in diverse classi. Non è presente una relazione uno ad uno tra la responsabilità e gli elementi del software. Le responsabilità possono essere a grana grossa o fine.

Un oggetto a cui viene assegnata una responsabilità deve poi soddisfarla, può agire da solo o collaborare con altri oggetti. La soddisfazione di una responsabilità deve portare ad una collaborazione. La progettazione orientata agli oggetti infatti è la progettazione di interazioni e collaborazioni. Si pensa ad un progetto OO come una comunità di oggetti software con responsabilità che collaborano.

Per realizzare la progettazione guidata dalla responsabilità RDD, *Responsibility Driven Development*, bisogna identificare in modo iterativo la responsabilità e chiedersi a quale oggetto bisogna assegnarla e poi bisogna chiedersi come quell’oggetto possa soddisfare quella responsabili, questo porta ad individuare molte sotto-responsabilità. Per assegnare una responsabilità bisogna ricorsivamente assegnare sotto-responsabilità.

I pattern GRASP, *General Responsibility Assignment Software Patterns* sono principi fondamentali per la progettazione, utilizzati al fine didattico. I pattern sono soluzioni esemplari a problemi ricorrenti. Si utilizzano i pattern per capire in che modo assegnare responsabilità. I pattern GRASP sono nove, in questa parte del corso si mostrano i cinque pattern GRASP principali, nella seconda parte del corso si parlerà dei pattern GRASP avanzati che parlano del polimorfismo. Questi pattern GRASP di base suggeriscono di assegnare responsabilità ad oggetti software ispirati al modello di dominio, mentre i pattern polimorfi non si ispirano al modello di dominio. In un modello sano normalmente sono presenti classi software sia ispirate che non ispirate al modello di dominio.

Normalmente si prendono decisioni di progetto quando vengono assegnate le responsabilità, vanno mostrate dentro diagrammi di UML, come assegnazioni di metodi o parametri in classi. Questi diagrammi devono essere realizzati come conseguenze di scelte di progetto, non il contrario.

Gli oggetti software mostrati nella soluzione possono essere ispirati da oggetti del modello di dominio. I primi cinque pattern GRASP guidano l’assegnazione di responsabilità a oggetti software ispirate al modello di dominio. Questo approccio diminuisce il salto rappresentazionale LRG, *Low Representational Gap*, anche se questo è il peggiore dei principi di progettazione. È normalmente un bene che sia presente un salto rappresentazionale, è bene avere lo strato del dominio che è in corrispondenza del modello di dominio, ma dove questi due modelli danno ciascuno forma all’altro, ma sono due oggetti distinti. Questo approccio infatti non garantisce di poter gestire facilmente la complessità del sistema. Inoltre si deve mirare ad un salto rappresentazionale basso, non nullo, altrimenti non si avrebbe spazio di modificare il sistema.

I pattern sono soluzioni esemplari a soluzioni ricorrenti, e possono essere descritti in modo strutturato, nome, problema e soluzione. Sono delle coppie problemi-soluzione, derivano dall’esperienza, a posteriori si individuano problemi e soluzioni simili associate, raggruppate in un solo pattern.

Il ragionamento di base di RDD consiste nel chiedersi qual è la prossima responsabilità da assegnare, dopo averla individuata si cerca un pattern per assegnarla, dopo averlo individuato si ricerca la classe o oggetto a cui assegnarla. Dopo averlo assegnata ad un oggetto ci si chiede se può soddisfarla autonomamente, altrimenti si cercano altre sotto-responsabilità, e si ricomincia il ciclo del ragionamento.

Un pattern è una coppia di un problema ed una soluzione esemplare, con un nome. Questo nome facilita la comprensione, memorizzazione e comunicazione. Le soluzioni proposte dai pattern sono già stati dimostrati corretti in varie situazioni, non affermano quindi nuove idee.

### Creator

Il primo pattern Creator, descrive il problema di chi crea un oggetto, la soluzione semplificata è di assegnare la responsabilità di creare un’istanza dell’oggetto ad una classe ulteriore, che generalmente deve anche mantenere il riferimento a quell’oggetto.

In base ai criteri definiti per questo pattern si possono individuare varie scelte possibili, nei casi più semplici si sceglie in base al peso dei criteri. Altrimenti si sceglie in base a low coupling e high cohesion. In molti casi dopo aver trovato la classe creatore, bisogna chiedersi qual è l’oggetto da creare. Normalmente si deve scegliere come creatore chi è utile abbia un riferimento all’oggetto creato, chi lo registra o chi lo deve usare. Sono criteri che derivano dal chiedersi per chi sono utili queste informazioni. Questo aumenta la coesione e riduce l’accoppiamento, diminuendo il numero di oggetti che lavorano per la creazione di un altro oggetto.

In alcuni casi i suggerimenti forniti da questo pattern sono inadeguati, in termini di coesione o accoppiamento, si discuteranno questi durante l’analisi del pattern *Pure Fabrication*. Non sempre questi pattern quindi forniscono suggerimenti adeguati, possono essere conformi al progetto attuale oppure possono peggiorare lo stato del progetto.

### Information Expert

Il secondo pattern *Information Expert* è il pattern più generale tra questi cinque, affronta il problema software molto ricorrente, ovvero il principio di base per assegnare responsabilità agli oggetti. La soluzione, semplificata, a questo problema consiste nell’assegnare la responsabilità all’oggetto che probabilmente è in grado di soddisfarla.

Gli oggetti hanno una parte strutturale ed una comportamentale, queste due parti devono essere collegate, le operazioni di una classe devono essere relative ai dati memorizzati e viceversa, i dati memorizzati aiutano a svolgere le operazioni dell’oggetto. Se questo è vero la classe è coesa, ha uno scopo coerente. Sostanzialmente questo pattern fornisce suggerimenti che sostengono l’alta coesione. Quando il pattern suggerisce più di un oggetto, allora si parla di più esperti, si dicono parziali se contengono solo parte delle informazioni necessarie per compiere la responsabilità. Dati più esperti parziali bisogna scegliere uno di questi per elevarlo ad esperto dominante, che direttamente o indirettamente è in grado di ottenere le informazioni restanti. Bisogna capire come questo oggetto è in grado di collaborare con gli altri oggetti parziali per recuperare le informazioni necessarie.

Si utilizza per tutte le responsabilità che non rappresentano gestione di oggetti o gestione di operazioni di sistema.

Information expert si basa su un’intuizione, ma questa non è intuizione non è intuitiva. L’utilizzo di questo pattern porta ad oggetti software che hanno responsabilità normalmente non assegnate ad oggetti del mondo reale, ovvero effettuano azioni che gli oggetti che rappresentano nel mondo reale subiscono. Quindi chi nel mondo reale effettua certe azioni, nella rappresentazione software non è più responsabile di queste.

Talvolta le soluzioni fornite da questo pattern potrebbero essere cattivi suggerimenti, non compatibili con low coupling o high cohesion. I vantaggi porta a distribuire il comportamento in più classi, rendendo il codice più facilmente comprensibile e modificabile.

### Accoppiamento e Coesione

Il principio di modularità suggerisce di realizzare un progetto ad alta coesione e basso accoppiamento, è una misura di quanto fortemente due elementi sono tra di loro dipendenti. Normalmente si vuole che l’accoppiamento sia basso, poiché al cambiare di una delle sue dipendenze bisogna modificare tutti gli altri elementi che dipendono da esso. Questo non dipende solamente dal numero delle dipendenze uscenti da un oggetto, ma anche dalla forza della dipendenza, l’accoppiamento viene pesato in base a queste dipendenze. Questo principio è migliore del principio di salto rappresentazionale basso. Avere un accoppiamento basso permette di ridurre l’impatto dei cambiamenti. Si divide il codice in moduli caratterizzati da una forte coesione interna ed un basso accoppiamento esterno, questi due sotto-principi sono rappresentati da due pattern GRASP, si potrebbero utilizzare solamente questi due, ma questi pattern sono valutativi, richiedono di prendere in considerazioni progetti alternativi e prendere il migliore e scartare il peggiore. Per ogni decisione di progetto sono presenti molte alternative che si combinano in modo esponenziale, lasciando molti progetti alternativi possibili. I pattern si sostengono e si abilitano a vicenda. Creator sostiene information expert ed abilita low coupling, information expert e controller sostengono sia low coupling e high cohesion.

L’accoppiamento è una misura di quanto un elemento è fortemente collegato ad altri elementi, tendenzialmente si cerca un’accoppiamento basso, non necessariamente sono tanti elementi potrebbero essere pochi a cui è connesso in modo forte. Mentre la coesione rappresenta quanto siano connesse le responsabilità di un elemento software, e generalmente si cerca una coesione alta. La misura è un numero che dipende dal codice, esistono degli analizzatori che formalizzano questa misura e restituiscono un numero, questo valore da solo non ha un significato, solamente se confrontato con i valori di altri progetti può avere valore. Si preferiscono valori di accoppiamento minori e valori di coesione maggiori. È una misura relativa che può essere effettivamente calcolata dal codice, solo stimata durante la progettazione. Dagli anni ’70 si è capito che i sistemi più facilmente modificabili sono quelli con accoppiamento basso e coesione alta. Questi garantiscono la modificabilità poiché se è coeso un singolo elemento contiene pochi metodi, mentre per accoppiamento basso la probabilità che andranno effettuate modifiche ad altri elementi è anch’essa bassa. Un progetto è coeso se i metodi d’istanza operano sulle variabili di istanza, e queste supportano i metodi d’istanza. Inoltre è anche una misura di quanto lavora compia un certo elemento software, se una classe esegue poco lavoro la sua coesione probabilmente è minima, mentre se compie tanto lavoro la sua coesione è alta.

Entrambe le misure rappresentano la forza delle relazioni fra le singole classi ed i metodi della classe. Si può ragionare anche a grana più grande parlando di pacchetti e dipendenze. L’accoppiamento parla di relazioni tra elementi di classe esterne, mentre la coesione parla di relazioni tra elementi interni a classi o moduli. Questi danno luogo ai principi più importanti, il principio di separazione di interessi ed il principio di modularità. Il principio di modularità indica che il sistema debba essere composto da moduli che sono fortemente coesi e debolmente accoppiati. Questa misura può essere effettuata tramite algoritmi applicati al codice e confrontando le varie possibili soluzioni.

La coesione alta indica di tenere insieme ciò che devono cambiare insieme, mentre l’accoppiamento basso indica di tenere lontani gli elementi non correlati, che devono cambiare separatamente.

Modificabilità e comprensibilità sono entrambe relative a coesione e accoppiamento, supponendo di dover modificare un pezzo di codice, modificare una porzione di una classe, se il codice è altamente accoppiato, altre classi potrebbero dipendere da questa appena modificata, e quindi bisognerebbe modificare anche tutte le altre classi dipendenti, propagando la modifica. Il tempo di una modifica dipende dal tempo per il cambiamento totale, inoltre è più facile cambiare una porzione di codice piccola in un’elemento piccolo, che in un elemento di grande dimensione. Se si tengono le classi piccole e coese, è quindi più facile modificarle, e favorisce anche la modifica di codice all’interno di quella classe. La presenza di una dipendenza, è solamente una possibilità che si debbano modificare anche altre classi, l’accoppiamento quindi è una misura della probabilità che al cambiamento di una classe bisogna modificare classi ulteriori. Per facilitare il cambiamento di una classe si tiene la coesione alta, e per evitare la propagazione dei cambiamenti si tiene l’accoppiamento basso.

Esistono diverse forme di coesione, in base a diversi criteri, quali per pura coincidenza, una forma non utile. Altri tipi di coesione sono la coesione temporale, per alcuni elementi è una buona forma, mantiene insieme elementi che devono essere usati nello stesso tempo. Normalmente avere tutti gli elementi appartenenti ad un caso d’uso in un singolo modulo può essere un buon approccio, ma negli altri elementi del dominio questo non è un buon criterio, poiché porta ad un cattivo accoppiamento e coesione, va bene solo per i controller. La coesione funzionale indica di avere funzioni in un elemento che possono svolgere una singola operazione. La coesione dei dati applica lo stesso concetto della coesione funzionale riguardo i dati.

### Low Coupling

Il terzo pattern GRASP riguarda l’accoppiamento tra elementi software, si chiama *Low Coupling*, e vuole risolvere il problema di ridurre l’impatto di cambiamenti. Assegna le responsabilità in modo da mantenere l’accoppiamento basso. La soluzione è assegnare la responsabilità in modo che l’accoppiamento non necessario rimanga basso. Si utilizza questo principio per valutare e confrontare diverse soluzioni.

Permette di avere un impatto ai cambiamenti basso, localizzato, risolve il problema di sostenere dipendenze basse. Questo principio valutativo permette di avere un accoppiamento basso, analizzando e comparando alternative di assegnazione di responsabilità scegliendo quella con accoppiamento minore. Si può determinare determinare da diagrammi di interazione o diagrammi di classi di progetto se sono presenti dipendenze o collegamenti che non sembrano riflettere le responsabilità degli oggetti coinvolti. Questo è un principio di base che va considerato sempre e comunque, il suo obiettivo specifico è quello di avere classi indipendenti che possono cambiare in modo separato tra di loro.

Nei linguaggi orientati agli oggetti, le forme più comuni di accoppiamento tra due oggetti $A$ e $B$ sono:

- Se la classe $A$ presenta attributi di $B$ o referenzia un’istanza o collezioni di $B$

- Se un oggetto $A$ richiama metodi dell’oggetto $B$

- Se un oggetto $A$ crea un oggetto $B$

- Se la classe $A$ referenzia in un suo metodo un oggetto $B$, come un parametro, variabile locale o tipo restituito

- Se la classe $A$ è sottoclasse diretta o indiretta di $B$, oppure se implementa l’interfaccia $B$

I vari tipi di accoppiamento riguardano le dipendenze tra elementi, e ci sono più forme. Alcune sono necessarie altre sono superflue, poiché si vuole una accoppiamento basso e non nullo. Un accoppiamento non utile è l’accoppiamento per dati interni, ovvero utilizzare direttamente le variabili di istanza di una modulo, quindi al minimo cambiamento di queste bisogna anche cambiare tutte le dipendenze ad altri moduli. Analogamente l’accoppiamento per dati globali, ovvero mettere a disposizione per l’intero progetto dei dati, non dipendenti da una singola classe. Un’altra forma di accoppiamento forte che può mal gestito è per sottoclasse, la sua utilità dipende dall’uso corretto del polimorfismo. Le ultime forme trattate sono comuni e tendenzialmente necessarie. L’accoppiamento per associazione indica che una classe gestisce dati che sono istanze di altri classi, l’accoppiamento per uso utilizza tramite interfaccia l’esecuzione di operazioni da altre classi, e l’accoppiamento mediante parametri indica che un’operazione di una classe utilizza istanze di altre classi, come parametri dell’operazione.

L’accoppiamento con elementi stabili di per sé non rappresenta un problema, determinare quando un elemento è stabile è anch’esso un problema da risolvere. L’accoppiamento dovuto a composizione generalmente non rappresenta un problema. In generale l’accoppiamento per associazione è inerentemente più forte, per cui non è opportuno utilizzare mappe dove sia la chiave che il valore sono classi software. Infatti si sono sempre utilizzate chiavi di tipo primitivo, non classi di dominio, normalmente rappresenta una violazione di low coupling.

La relazione tra accoppiamento e coesione non rimane tale anche agli estremi, se si cerca un accoppiamento troppo basso, la coesione diminuisce, analogamente per una coesione troppo alta. Una forma subdola di accoppiamento consiste nella duplicatone del codice, poiché se il codice è duplicato e bisogna modificare una porzione di codice, allora bisognerà modificare anche gli altri codici duplicati. La duplicazione del codice è infatti un anti-pattern.

### Controller

Il quarto principio di progettazione affronta il problema di determinare quale oggetto del dominio gestisce le richieste dell’utente, si chiama *Controller*. Il pattern GRASP controller, risolve questo problema, il controller è l’oggetto del dominio che accetta la richiesta dell’utente, e può gestire anche la logica del dominio, anche se questo tipo di ragionamento è molto sconsigliato. Se si utilizza una struttura dove lo strato di dominio è unito allo strato application, questo pattern si riferisce al primo oggetto dello strato del dominio, dello strato application, che riceve queste richieste. Il pattern fornisce due soluzioni, una prima consiste nell’utilizzare un oggetto che rappresenta il sistema complessivo, *facade controller*, oppure un’istanza del caso d’uso in cui si verifica l’operazione, *session controller*. Possono o rappresentare l’intero sistema, oppure possono rappresentare un punto d’accesso al sistema. In questo corso si tratterà solo il facade controller, questo oggetto è un *singleton*, per le applicazioni standalone viene scelto un oggetto il cui nome della classe ricorda il nome del sistema. Mentre per i sistemi client-server si vuole utilizzare un oggetto che rappresenta un punto di accesso al sistema, ovvero un portale.

Il controller è il primo oggetto oltre lo strato UI che è responsabile di ricevere o gestire un messaggio per un’operazione di sistema. Al termine controller vengono applicati diversi significati. Quello che viene utilizzato solamente nel corso sono facade controller, può rappresentare il sistema complessivo, un oggetto radice, un punto d’accesso al sistema o un sottoinsieme principale.

Le operazioni di sistema identificate vengono assegnate ad una classe concettuale sistema che è un’astrazione del’intero software. Viene quindi utilizzato solamente nell’analisi, per la progettazione non è opportuno utilizzare una classe software sistema con significato analogo, ma queste responsabilità vengono attribuite al controller.

L’utilizzo di un facade controller impone di utilizzare metodi per tutti i casi d’uso, altri tipi di controller sono dedicati ai singoli casi d’uso e quindi diminuiscono l’accoppiamento. Questi “Use-Case Controller” sono una altro tipo di controller che non verrà trattato in questo corso.

I sistemi ricevono eventi di input dall’esterno ed un modo comune per controllarli è il pattern controller, l’utilizzo del termine controller è una collisione con altri elementi MVC, dove viene chiamato “Controller GRASP”. Questi controller possono delegare ad altri oggetti le operazione richieste dallo strato di presentazione, che a loro volta hanno delegato queste operazioni al controller. Il controller relativamente delega il lavoro, quindi non esegue molto lavoro, semplicemente lo delega ad altri oggetti, coordinando e controllando le attività, ma senza eseguirle lui stesso.

Assegnare troppe responsabilità ad un controller è un errore, poiché potrebbe generare un blob. Può essere utile avere un controller per ogni caso d’uso, normalmente le responsabilità della gestione transiente sdi un caso d’uso vengono assegnate ad un controller, e si dice che le responsabilità dello stato della sessione o stato della conversione e quelle transienti sono coese. Sono possibili diverse architetture a strati, si potrebbe avere uno strato application come strato intermediario tra domino ed interfaccia utente, questo contiene tutti e soli i controller.

Le richieste che arrivano al controller, devono essere interpretazioni delle azioni dell’utente, questi elementi nello strato di interfaccia utente che gestiscono gli input dell’utente sono chiamati controller MVC che chiamano le operazioni dei controller GRASP. Questi due tipi di controller sono correlati ma hanno responsabilità diverse. I controller MVC dipendono dalla tecnologia usata, mentre il controller GRASP è in qualche modo indipendente dalla tecnologia.

Se i casi d’uso sono pochi allora si sceglie un facade controller, se sono molti o molto diversi, allora potrebbe essere utile utilizzare dei case-use controller. Un’altra soluzione consiste nell’utilizzare un’interfaccia di sistema che contiene tutte le operazioni di quel caso d’uso e vengono implementate da una classe software. Se si usa un use-case controller questi implementano una sola interfaccia, mentre se si usa un facade controller, questo implementa più interfacce.

Nella realtà si può effettuare una scelta intermedia, utilizzando un facade controller per ogni attore diverso nel sistema. Per ogni attore si può realizzare un’applicazione web diversa, e nell’implementazione si immagina che questi controller siano separati e abbiano responsabilità diverse.

Se l’applicazione è standalone tendenzialmente si utilizza un facade controller che rappresenta l’intero sistema, mentre se il sistema è client-server, allora il controller rappresenta un punto d’accesso. Per facilitare la progettazione si suppone che un solo cliente alla volta possa utilizzare il punto d’accesso, mentre nella realtà questo non è sempre verificato. Questo problema viene risolto nello strato di presentazione utilizzando diverse tecnologie, permettendo di aumentare il numero di clienti contemporanei, senza modificare lo strato di dominio.

### High Cohesion

Il pattern *High Cohesion* è correlato a low coupling, e risolve il problema di mantenere gli oggetti focalizzati, comprensibili e gestibili, un effetto collaterale di low coupling, sostiene lo stesso low coupling. L’obiettivo di high cohesion è di creare classi facili da comprendere, meno codice è presente in una classe, più facile è da comprendere. Ogni classe dovrebbe avere un’unica funzione o responsabilità.

La coesione è una metrica ed è utile pensare a diversi livelli qualitativi di coesione funzionale. Normalmente per il principio di separazione degli interessi responsabilità tecniche e quelle non tecniche vanno separate tra di loro. Le tre responsabilità di dominio, gestione dei dati persistenti ed interazione utente devono rimanere separate. La coesione è l’altra caratteristica importante del principio di modularità, è una misura di quanto sono correlate le responsabilità o operazioni di un elemento software. Può essere una misura di quanto lavoro viene svolto da un elemento software. Tra le due possibilità proposte, un principio fondamentale della progettazione favorisce quella a coesione più alta. Generalmente migliorando la coesione migliora anche l’accoppiamento e viceversa. Aumentare la coesione favorisce la comprensione in isolamento. Nello sviluppo iterativo, il codice deve essere facilmente modificabile ed anche facilmente comprensibile. Il caso estremo di coesione alta è quando in ogni classe è presente una sola istruzione, ma sia questo caso che quelle di accoppiamento estremamente basso non favorisce la comprensione.

Ci sono casi dove il livello di coesione basso è giustificabile, per esempio se favorisce il lavoro e quindi la collaborazione con altri non specializzati con il sistema o le tecnologie in questione. Elementi con coesione bassa sono generalmente difficili da mantenere, poco comprensibili e difficilmente modificabili.

Ci sono diversi tipi di coesione:

- Coesione dei dati, una classe implementa un tipo di dati

- Coesione funzionale, gli elementi di una classe svolgono una sola funzione

- Coesione temporale, gli elementi sono raggruppati, perché usati nello stesso tempo

- Coesione per pura coincidenza, gli elementi sono raggruppati per caratteristiche del loro nome, o non inerenti alla loro funzione

La duplicazione di codice o ripetizione non necessaria è un anti-pattern, peggiora la coesione introducendo metodi e responsabilità in più ad elementi, che altrimenti potrebbero non averle. Porta a del codice difficile da comprendere e da modificare, per migliorare si può astrarre questo codice comune in una nuova classe. Questa è una tecnica di refactoring.

### SOLID

I pattern SOLID danno gli stessi principi dei pattern GRASP, ma a volte la loro applicazione può essere più semplice.

Un altro anti-pattern è il “blob”, o classe dio, un oggetto che è responsabile dello svolgimento di un compito complesso, e tutte le altre classi che le stanno attorno sono anemiche, utilizzate solo come contenitori di dati, o che svolgono solo compiti semplici e piccoli. In questi casi va utilizzato information expert per riassegnare meglio le responsabilità.

## Realizzazione di Casi D’uso

La progettazione nell’UP si chiama realizzazione dei casi d’uso, enfatizza la relazione forte tra la progettazione ad oggetti e l’implementazione dei casi d’uso. Il modo migliore di lavorare è affrontare tutte le operazioni di un caso d’uso in una singola seduta di progettazione. È utile ragionare oltre che alle operazioni, anche sulle risposte del sistema.

Ci si concentrerà principalmente sulla parte di trasformazione delle operazioni, potranno essere realizzati diagrammi per alcune risposte del sistema, ed in parallelo verrà realizzato un diagramma delle scelte strutturali del progetto. Per ogni operazione di sistema si realizzerà un diagramma di interazione. Nella realizzazione di un caso d’uso si userà il testo dei casi d’uso, e sopratutto i contratti delle operazioni, essendo scritti in modo abbastanza formale, anche se dal punto di vista concettuale.

Generalmente è sempre presente un caso d’uso d’avviamento che inizializza tutti gli oggetti ed i dati che verranno usati nei casi d’uso successivi. Se si progetta nell’ipotesi di non avere dati persistenti, bisogna o stravolgere l’intero progetto per interagire con la base di dati, oppure si possono applicare piccole modifiche. Si suppone che i dati siano caricati in memoria e sempre disponibili, per introdurre la persistenza dei dati bisogna effettuare modifiche semplici al progetto. Basta infatti modificare le operazioni relative al caso d’uso d’avviamento, dove questi dati vengono caricati in memoria.

Durante la realizzazione di un caso d’uso, la prima attività consiste nell’individuare una classe controller, indirettamente collegato a tutti gli altri oggetti, si può immaginare che questo oggetto singleton rappresenta la radice di un albero, da cui è possibile raggiungere ogni altro oggetto del progetto. Normalmente per i sistemi client-server si utilizza un oggetto che rappresenta un punto di accesso al sistema. L’oggetto che riceve la richiesta dell’utente, deve avere un’operazione dello stesso nome dell’operazione richiesta dall’utente. Normalmente la creazione dell’oggetto controller viene effettuata nel caso d’uso d’avviamento, quindi non c’è bisogno di creare questo oggetto quando viene richiesta un’operazione di sistema.

Il controller ha due responsabilità ricevere, coordinare e controllare le operazioni di sistema, e gestire i dati transienti. Se il controller crea un’istanza di un oggetto, generalmente è il controller a mantenere questo riferimento realizzando un collegamento unidirezionale. Una regola sempre valida è che se deve essere creato un collegamento, il responsabile è sempre l’oggetto da cui parte il collegamento. Nel DCD si mostra questa relazione navigabile ad uno, e si scrive solamente il nome del ruolo accanto all’estremità navigabile. Bisogna mostrare la formazione dei collegamenti in modo esplicito, mentre non bisogna mostrare le assegnazione degli attributi, sono di interesse solo i collegamenti.

Per poter memorizzare i collegamenti verso degli elementi di una collezione, bisogna creare un oggetto collezione, questo viene realizzato nell’operazione di sistema che utilizzerà questa collezione. Bisogna creare la collezione inizialmente vuota, da una variabile di istanza privata della classe che userà la collezione, nel suo costruttore. I nomi che compaiono nei diagrammi di interazione potrebbero essere collegati ai nomi dei ruoli dei collegamenti. Bisogna mostrare in modo esplicito tutti gli oggetti, anche gli oggetti collezione.

### Realizzazione di Casi d’Uso: Sistema POS, Elabora Vendita

Si considera il caso d’uso del sistema POS che determina l’acquisto da parte di un cliente di una serie di articoli: “Elabora Vendita”. Il cliente arriva alla cassa POS con ciò che vuole acquistare, articoli o servizi, quindi il cassiere inizia una nuova vendita. Per ogni articolo viene registrata una nuova riga di vendita con la corrispondente quantità per stesso articolo, mostrando le informazioni relative per ogni nuova riga di vendita. Dopo che il cassiere ha inserito tutti gli articoli, il sistema mostra il prezzo totale con le imposte, questo viene riferito al cliente che sceglie un metodo di pagamento. Il sistema gestisce il pagamento effettuato dal cliente, e registra la vendita completata, inviando le informazioni necessarie ai sistemi di contabilità e di inventario del negozio. Genera infine la ricevuta, ed il cliente può andare via con i suoi articoli acquistati.

Per facilitare l’individuazione di operazioni di sistema si può realizzare un SSD relativo a questo caso d’uso. Si considera la prima operazione di sistema, quella chiamata dal cassiere per creare una nuova vendita. Questa operazione viene chiamata `makeNewSale`, per creator e controller questa è un’operazione di `Register`, controller del caso d’uso, e si occupa di creare e memorizzare il riferimento a sale. Nel costruttore della vendita si ha la creazione della collezione `lineItems` di tipo `List<SalesLineItem>`. Analizzando il contratto di questa operazione, bisogna creare un oggetto vendita, formare il collegamento tra questo ed il controller, ed inizializzare i suoi attribuiti. Nel costruttore della classe vendita vengono inizializzati i suoi attributi, invocato da `Register`, che ne mantiene un riferimento. Questo deve essere esplicitato nel corrispondente diagramma di interazione.

L’operazione successiva `enterItem` corrisponde ai passi 3 e 4 del caso d’uso, dal punto di vista concettuale è utile avere riferimenti alle linee di vendita. Nelle post-condizioni si crea la linea di vendita `sli`, viene collegata alla vendita corrente `s`, e si associa alla descrizione prodotto a cui si riferisce. Si aggiornano infine gli attributi della linea di vendita `sli`. Normalmente se ne è responsabile, nello sue post-condizioni, un’operazione di sistema effettua per prima la creazione di un’istanza di un oggetto. Bisogna determinare il controller per `enterItem`, essendo il controller dell’intero caso d’uso lo stesso si sceglie sempre la `Register`. Si disegna quindi il diagramma di interazione con `Register` che riceve il messaggio dell’operazione. La responsabilità della creazione dell’oggetto software `SalesLineItem` si determina dal pattern creator, quindi il primo candidato è la vendita di cui è composizione. L’altro candidato è chi registra o memorizza i riferimenti alle righe di vendita, e questo è il registratore di cassa. Chi è che deve usare strettamente gli oggetti di tipo righe di vendita, sono gli oggetti che devono stampare il totale, ovvero la quantità per il prezzo unitario prodotto. La quarta possibilità è chi possiede i dati necessari all’inizializzazione, ovvero chi conosce la quantità e può passarla come argomento al costruttore di righe di vendita per l’articolo, non è detto che il cassiere software rappresenta pienamente il cassiere nella vita reale, quindi l’unico oggetto software che conosce la quantità è il registratore poiché gli viene passato per messaggio.

Se questi due candidati fossero di pari livello allora bisognerebbe creare due progetti software e valutarli in base a coesione ed accoppiamento. Ma in questo caso si considera solamente `Sale` come classe che crea e mantiene un riferimento alla riga di vendita. Ma sono presenti tanti oggetti vendita, a quale di questi allora va assegnata la responsabilità di mantenere un riferimento alla riga di vendita? La vendita corrente ha la responsabilità di creare e memorizzare questa riga di vendita. La prossima responsabilità è determinare chi deve chiedere alla vendita corrente di creare il nuovo oggetto riga di vendita per prodotto. Il pattern da applicare per questa responsabilità potrebbe essere low coupling, oppure information expert, quest’ultimo indica che la responsabilità va assegnata all’oggetto che conosce la vendita corrente, e questa responsabilità è stata assegnata al controller. Quindi per il pattern information expert è il controller che richiede di creare una nuova riga di vendita per prodotto a vendita corrente. Quindi il controller invia un messaggio di tipo `makeLineItem` e prende come parametro la descrizione e la quantità del prodotto di cui creare la riga di vendita, questo non crea l’oggetto, ma indica all’oggetto ricevente di creare un oggetto, solo con lo stereotipo `create` si indica che il messaggio sta creando un oggetto. La riga di vendita è un oggetto della collezione `linesItem`, quindi bisogna aggiungerla alla collezione, dopo averla creata. Per il pattern information expert l’oggetto vendita ha questa responsabilità, invia quindi il messaggio di numero 2.2 `add(sli)`. Per poter usare la collezione bisogna crearla, quindi la vendita corrente `s` dovrebbe creare l’oggetto collezione se esso non esiste, ma questo già esiste essendo stato creato nel costruttore di vendita.

A questo punto bisogna associare la riga di vendita alla descrizione prodotto corrispondente. Questo è necessario perché per stampare lo scontrino è necessario conoscere la descrizione prodotto. Se l’associazione fosse navigabile solo dalla descrizione alla riga di vendita, allora per stampare la descrizione bisognerebbe controllare tutte le descrizioni prodotto cercando quale ha un riferimento a questa descrizione. Quindi la navigabilità è invertita, dalla riga di vendita alla descrizione prodotto. In riga di vendita bisogna inserire un riferimento all’articolo, prima di poter effettuare il collegamento. Si deve effettuare una ricerca, quindi bisogna determinare a chi assegnare la responsabilità per trovare la descrizione prodotto relativa all’articolo di codice `itemID`. Per il pattern information expert deve essere un oggetto che sicuramente conosce tutte le descrizioni prodotto, in questo caso è il catalogo prodotti, che serve a rappresentare appunto tutte le descrizioni prodotto.

Nel diagramma di interazione sarà presente un oggetto catalogo prodotti con un riferimento alla mappa chiamata `descriptions` di tipo `Map<ProductDescription>`. Quindi il catalogo deve ricevere un messaggio per effettuare questa ricerca che si può chiamare `getProductDescription(id)`, questa cercherà nella mappa l’oggetto con `get(id)`. Normalmente un oggetto che contiene una mappa fornisce delle operazioni di ricerca e di aggiunta alla mappa; mentre se si indicasse al plurale `getProductDescriptions` restituirebbe l’intera mappa, e non è l’operazione richiesta. Essendo l’operazione di inserimento la più importante bisogna diminuire l’overhead dell’operazione. Se ogni volta bisognasse effettuare un doppio salto dal registratore al negozio e dal negozio al catalogo prodotto si aumenterebbe notevolmente l’overhead; quindi nel modello di progetto si suppone che il registratore conosca direttamente il catalogo prodotti. Si suppone che all’inizio della giornata venga assegnato il riferimento al catalogo prodotti. Questo approccio è sicuramente migliore di aggiungere il riferimento di catalogo prodotto alla vendita, o riga di vendita per articolo, poiché sono di ordine di grandezza molto superiore e si sprecherebbero risorse per memorizzare legami superflui. Il registratore allora deve richiedere al catalogo prodotti la descrizione e la salva nella variabile `desc`. Questa rappresenta la prima operazione, poiché la creazione della riga di vendita ha bisogno della descrizione `desc` come parametro, questo messaggio viene numerato uno, mentre la creazione della riga di vendita è il messaggio due.

Questo pattern viene chiamato *IDs to Objects*, che consiste nell’assegnazione della responsabilità di chi deve individuare un riferimento ad un oggetto dato un identificatore. Il messaggio iniziale al registratore di cassa contiene l’identificatore, poiché processi diversi non condividono puntatori e quindi riferimenti agli oggetti, e non sarebbe quindi possibile passare direttamente la descrizione prodotto anche se si volesse.

Bisogna determinare ora chi associa il nuovo oggetto riga di vendita per articolo alla descrizione prodotto, questo può avvenire all’interno del costruttore. Anche se nel costruttore sono presenti due argomenti, uno di questi è un attributo che non va rappresentato, mentre va rappresentata la formazione del collegamento, in un’etichetta indicando esplicitamente il vincolo: `{description = desc}`.

Il registratore è connesso verso la vendita ed il catalogo prodotti, e il collegamento tra il catalogo e la descrizione prodotto devono essere già presenti, e si suppone che in passi precedenti del caso d’uso o in casi d’uso diversi siano stati creati. I collegamenti generati dal caso d’uso tra la vendita e la riga di vendita, e tra la riga di vendita e la descrizione prodotto, sono creati in questo caso d’uso e potrebbero essere utili in altri casi d’uso, altrimenti non sarebbero stati creati se non fossero utili. Ma lo stesso collegamento può essere usato anche nello stesso caso d’uso di creazione. Sono inoltre presenti dipendenze tra il registratore e la vendita verso la descrizione prodotto.

Avendo ora il progetto completo per il caso d’uso `enterItem`, si può espandere il diagramma delle classi, avendo più diagrammi di interazione che forniscono informazioni per ogni operazione. Dal registratore, il controller, prima di questa operazione erano già presenti il legame con la vendita corrente ed il catalogo prodotti, e tra il catalogo prodotti e la descrizione prodotto, sulla base della sua mappa. In seguito a questa operazione vengono formati il collegamenti tra la vendita e la riga di vendita per articolo, e tra questa e la descrizione prodotto. Inoltre sono presenti due dipendenze dal registratore e la vendita verso la descrizione prodotto.

L’operazione di sistema successiva è `endItemEntry` per terminare l’inserimento di nuovi articoli, dal contratto si ha che questa è un’interrogazione, ed essendo un’operazione di sistema bisogna realizzare il suo diagramma di interazione. Il controller è sempre il registratore di cassa, e si inserisce un commento specificando che non bisogna effettuare niente all’arrivo di quest’operazione. In realtà quando si avrà una base di dati quest’operazione avrà un effetto, per questo viene inserito questo metodo nel controller, senza inserire alcune logica.

L’operazione seguente è `getTotal`. Lo strato di dominio è responsabile di calcolare i dati da mostrare, non per mostrarli, questo infatti è compito dello stato di presentazione che richiede questi dati tramite interrogazioni. Per progettare un’interrogazione bisogna partire enunciando la responsabilità dell’interrogazione, in questo caso si vuole mostrare il totale della vendita dopo aver inserito tutti gli articoli. Il pattern più utile per le informazioni è l’information expert, ed indica di assegnare questa responsabilità a chi possiede i dati per soddisfare questa responsabilità.

Per calcolare il totale della vendita si sommano i totali parziali delle righe di vendita per articolo, e ciascuna di esse sono quantità per prezzo unitario per articolo. Nel modello di dominio, e anche nel diagramma delle classi di progetto, queste informazioni sono contenute in tre classi, la vendita, la riga di vendita e la descrizione prodotto. Tuttavia le responsabilità devono essere assegnate ad un unico oggetto. Quando ci stanno esperti parziali delle informazioni bisogna individuare l’esperto dominante ed assegnare a lui la responsabilità. L’esperto dominante è quell’oggetto o uno degli oggetti che direttamente o indirettamente conosce tutte le informazioni che servono, questo oggetto è la vendita.

Quindi si inizia un diagramma di interazione dove l’interrogazione non è un’operazione di sistema. La classe vendita deve richiedere le informazioni per poter calcolare i totali parziali per riga di vendita dei vari articoli, applicando nuovamente information expert si ha che i responsabili per trovare ciascun totale parziale sono le righe di vendita per articolo. Quindi deve iterare su ogni riga di vendita per articolo con un ciclo e richiedere a tutte queste il totale parziale. Si mostra quindi nell’interazione tra le due il ciclo che viene effettuato, si inserisce davanti al messaggio l’asterisco per indicare che si sta iterando su ogni elemento della collezione, si indica inoltre un elemento generico della collezione.

Poiché la riga di vendita per articolo non conosce il prezzo unitario deve richiederlo alla classe che lo conosce ovvero la descrizione prodotto. Ogni riga di vendita per articolo chiede alla propria descrizione prodotto il prezzo, quindi il primo messaggio tra la vendita e le varie righe di vendita è un ciclo, mentre tra la singola riga di vendita generica viene mandato un solo messaggio alla sua descrizione prodotto. Dato che per ogni riga di vendita viene richiesto una singola volta il prezzo dalla sua descrizione prodotto.

Per soddisfare queste responsabilità nel diagramma delle classi di progetto bisogna soddisfare la navigabilità per tutte le operazioni individuate. Deve essere navigabile da vendita a righe di vendita per articolo, tramite la sua mappa, mentre da riga di vendita per articolo a descrizione prodotto.

L’operazione `getTotal` è una risposta del sistema quindi non bisogna partire dal controller, la progettazione per le interrogazioni è importante poiché può guidare la progettazione per i cambiamenti di stato. Se in un sistema non ci fossero alcune interrogazione non sarebbe necessario progettare. Spesso le interrogazioni si possono calcolare “ad occhio”, per ispezione delle navigabilità, scegliendo quelle che soddisfano i requisiti. Se in un altro caso d’uso queste navigabilità non fossero sufficienti, bisognerebbe formare altri collegamenti.

Nella progettazione quando si deve implementare un dato derivato si hanno due possibilità, si può indicare la virtualizzazione o la materializzazione. Nella prima non si rappresenta come una variabile di istanza, ma con un’interrogazione, ovvero con un metodo. Un dato è materializzato se è presente in una classe e per ottenerlo bisogna richiederlo. Il diagramma di interazione cambia se il dato è virtualizzato o materializzato. Se è virtualizzato il diagramma di interazione è complicato, mentre se un dato è materializzato il diagramma di interazione per richiederlo è più semplice, ma gli altri diagrammi di interazione possono essere più complicati per accedere a questo dato.

Tra le due operazioni precedenti `endItemEntry` e `getTotal` è presente una relazione, poiché dopo aver richiesto la prima operazione, il sistema deve eseguire la seconda. Alcune possibili implementazioni di questa relazione verranno trattate in sezioni successive.

Si considera l’operazione di sistema `makeCashPayment`, il controller per questa operazione è sempre il registratore di cassa, richiede come parametro l’importo versato per indicare il pagamento effettuato dal cliente. Si considera la navigabilità dal pagamento al pagamento in contanti, quindi ogni pagamento conosce il suo pagamento in contanti, allora bisogna assegnare la responsabilità della creazione del nuovo oggetto pagamento in contanti. Per il pattern creator il controller può essere il registratore di cassa oppure la vendita che richiede dal pagamento le informazioni per poter in seguito calcolare il resto. Avendo due esperti parziali si devono creare più soluzioni e confrontarle in termini di coesione ed accoppiamento.

Nella prima soluzione il registratore crea il pagamento in contanti e la vendita deve ottiene le informazioni sul pagamento da parte del registratore, mentre nella seconda soluzione è la vendita che deve creare il pagamento in contanti, quindi il registratore invoca un il metodo alla vendita. Nella prima soluzione il registratore è collegato con una dipendenza di creazione con il pagamento in contanti, nel secondo progetto invece il registratore non dipende in alcun modo dal pagamento in contanti. La differenza di accoppiamento tra i due progetti nel primo è presente un’associazione in più, quindi è peggiore rispetto al secondo, dove sono presenti solo associazioni necessarie. Questa differenza, tuttavia piccolissima, va presa in considerazione in questo caso. Per valutare i due progetti in termini di coesione si considera quanto codice bisogna scrivere nelle classi. Nel primo progetto è definito un metodo per settare il pagamento, dato che il pagamento in contanti non viene creato direttamente, ma nel secondo progetto è presente un metodo per creare il pagamento in contanti dalla classe vendita, quindi sono presenti lo stesso numero di metodi. Normalmente il controller deve delegare alle altri classi l’esecuzione di metodi, quindi deve avere il meno codice possibile, e nel primo progetto il controller deve creare il pagamento in contanti e deve impostare il pagamento in contanti per la vendita, passando il riferimento. Il codice è quindi leggermente peggiore per il controller nel primo caso, ed è sicuramente più semplice nel secondo caso, dove deve solo invocare un metodo della vendita. Il codice per la classe vendita è sostanzialmente uguale tra i due casi, quindi in termini di accoppiamento è peggiore il primo progetto. Anche se nel secondo progetto deve effettuare due operazioni, queste due sono molto coese.

L’altra responsabilità da assegnare è memorizzare la vendita completata. Si ipotizza che possa essere necessario un libro mastro dove tenere traccia di tutte le vendita. Si analizzano quindi le due soluzioni in termini di coesione, una solamente con la classe negozio, con la responsabilità di memorizzare le vendita, e un’altra che necessita di una nuova classe libro mastro. Per ora si sceglie la soluzione più semplice, ma in futuro si potrebbe decidere di cambiare l’approccio poiché la classe negozio potrebbe avere troppe responsabilità. Non si sceglie invece la classe registratore poiché deve solamente memorizzare i dati transienti, altrimenti non sarebbe coeso come controller.

Un’ulteriore interrogazione `getBalance` deve restituire il resto dovuto al cliente, dopo il pagamento in contanti. La responsabilità cade alla classe vendita conoscendo tutte le informazioni necessarie, indirettamente. Questa chiede prima al suo pagamento il totale pagato, ed invoca il suo stesso metodo `getTotal` per effettuare la differenza e restituire il risultato.

Nel diagramma delle classi di progetto aggiornato dopo aver realizzato questi diagrammi di interazione, la classe negozio conosce le vendite completate e tra le due c’è una navigabilità doppia, nelle operazioni viste fin’ora non c’è una necessità per la navigabilità dalla lista al negozio, questa verrà giustificata in seguito.

Il prossimo problema da analizzare è come collegare l’interfaccia utente al dominio. Quando l’utente preme il pulsante di inserimento, qualche oggetto dello strato UI chiede ad un oggetto dello strato di dominio di eseguire l’operazione. Deve essere presente nello strato di presentazione una visibilità verso il controller, questa deve essere creata nel caso d’uso d’avviamento. Un’opzione peggiore consiste nel passare riferimenti ad altri oggetti dello strato di domino allo strato dell’interfaccia utente. Per effettuare interrogazioni lo strato di presentazione chiede al registratore il riferimento agli oggetti da che deve interrogare, in questo caso solamente vendita, dove sono definite le uniche due interrogazioni `getBalance` e `getTotal`.

Il caso d’uso d’avviamento generalmente viene rappresentato da un’operazione chiamata `starUP`, la prima ad essere eseguita dal sistema. Durante il caso d’uso d’avviamento devono essere create tutte le descrizioni prodotti, il catalogo a loro associate, deve essere creato il controller, il negozio e la lista delle vendite registrate.

Si potrebbe ragionare in termini dei pattern GRASP per progettare il caso d’uso d’avviamento, un pattern progettuale comune consiste nell’usare un oggetto di dominio iniziale, che direttamente o indirettamente crea tutti gli oggetti di questo caso d’uso. Questo oggetto viene scelto da quelli vicini alla radice del progetto.

Un metodo di scrivere il codice consiste di creare una classe main principale, con un singolo metodo statico che gestisce l’avviamento, Inoltre bisogna creare l’oggetto radice dell’interfaccia utente. L’oggetto iniziale è il negozio e da questo vengono creati gli altri oggetti di dominio e viene passato in questo metodo il controller all’interfaccia utente. Quindi la navigabilità tra il negozio ed il registratore è bidirezionale e motivata da questa necessità.

Oltre agli oggetti precedentemente elencati da essere creati in questo caso d’uso, devono essere formati tutti i collegamenti necessari tra questi oggetti, poiché sono richiesti dalle operazioni. I collegamenti sono formati dagli oggetti da cui il collegamento parte. Il negozio lo crea il metodo iniziale, il registratore lo crea il negozio, il catalogo prodotti è creato anch’esso dal negozio, e questo crea la mappa vuota della descrizione prodotto ed in qualche modo crea tutte le descrizioni prodotto e le aggiunge a questa mappa, inoltre il negozio crea la lista inizialmente vuota delle vendite effettuate. Questo rappresenta un modo per realizzare il caso d’uso d’avviamento. Si può quindi realizzare un diagramma di interazione per quest’operazione, e modificare il DCD per garantire le navigabilità richieste.

Nonostante tutto sono stati volutamente commessi degli errori sia in questo progetto, sia nel progetto Monopoly, questi verranno analizzati e corretti in sezioni successive, per permettere di comprendere a pieno le loro motivazioni.

## Trasformare il Progetto in Codice

In UP per implementare il progetto si utilizza l’elaborato “Modello di Implementazione”, che contiene diverse informazioni, non solo il codice sorgente. Gli elaborati di progetto come DCD e diagrammi di interazione rappresentano l’input per la scrittura del codice. La fase di progettazione può avvenire anche parallelamente alla codifica del progetto.

Nelle fasi precedenti di OOA/D si sono individuati elementi e decisa la struttura del progetto, e l’interazione tra gli elementi contenuti. Per implementare il progetto, bisogna scrivere in codice classi ed interfacce, facendosi guidare dal progetto e quindi dagli elaborati prodotti nelle fasi precedenti. Per il principio di salto rappresentazionale basso, si può rappresentare ogni classe del DCD come una classe software a sé, successivamente si discuterà la possibilità di creare classi non attribuibili al modello di dominio. Analizzando il DCD gli attributi delle classi diventano variabili d’istanza, i collegamenti diventano riferimenti e collezioni, ed i metodi devono essere implementati, non si trattano più a scatola nera. Le prime due trasformazioni sono semplici ed immediate, mentre per implementare i metodi correttamente, bisogna consultare i diagrammi di interazioni corrispondenti. Se una proprietà strutturale è un’associazione a molti non bisogna usare una variabile riferimento semplice, ma una variabile collezione. Il tipo di una variabile collezione normalmente è un’interfaccia, ma quando bisogna utilizzarla bisogna scegliere un’implementazione, questo dettaglio deve essere considerato nella scrittura del codice non nella progettazione, poiché non vengono presi in considerazione tutti i dettagli del codice. Si guarda ad un’oggetto ed i corrispondenti messaggi entranti ed uscenti, in relazione ai messaggi entranti si scrive un metodo, ed in relazione ad ogni messaggio uscente si scrive un metodo ed un’invocazione di un metodo, per la classe corrispondete all’oggetto a cui è diretto il messaggio. Per definire un metodo si guarda il diagramma di interazione del metodo, isolando le varie parti, per capire quali sono le operazioni che deve effettuare quel metodo in particolare, e non metodi invocati da altri oggetti. Solamente considerando ogni messaggio ricevuto ed inviato da tutti gli oggetti si può scrivere la maggior parte del codice. Si utilizzano gli stessi nomi per i metodi e per i parametri, le uniche informazioni non contenute nei diagrammi di interazioni sono per le variabili locali dei metodi, diverse da riferimenti ad oggetti, ma essendo di tipo primitivo, le operazioni e quindi il codice da scrivere relativo a questi, è semplice.

Considerando il sistema POS, si analizzano uno ad uno tutti i diagrammi di interazione ed il DCD. Partendo dal controller bisogna inserire tutti i metodi eseguiti, ed invocati da altri oggetti, e tutti i riferimenti (collegamenti) ad altri oggetti. Essendo un facade controller, contiene tutti e quattro i metodi relativi alle operazioni di sistema:

``` java
    public class Register{
        private ProductCatalog catalog;
        private Sale currentSale;

        public Register() {}
        public void makeNewSale() {}
        public void enterItem(...) {}
        public void endItemEntry() {}
        public void makeCashPayment(Money cashTendered) {}
    }
```

La prima operazione di sistema è relativa al metodo `makeNewSale`, in questa il controller crea un nuovo oggetto `Sale` e lo memorizza nella sua variabile d’istanza per la vendita corrente. Il costruttore di vendita quando viene creato l’oggetto deve creare la collezione di linee di vendita per articolo.

``` java
    public class Sale{
        private List<SalesLineItem> lineItems;  

        public Sale(){
            lineItems = new ArrayList<>();
        }
    }
```

Si suppone che nel caso d’uso d’avviamento, e quindi nel costruttore di `Register` venga assegnato il catalogo prodotti, è l’oggetto radice della del modello di dominio a creare tutti gli oggetti usati dai casi d’uso. Passando all’operazione successiva, si può scrivere il corpo del metodo, guardando al diagramma di interazione:

``` java
    public void enterItem(long id, int qty){
        ProductDescription desc = catalog.getProductDescription(id);
        currentSale.makeLineItem(desc, qty);
    }
```

A questo punto bisogna implementare i metodi invocati del catalogo prodotti e di vendita. Quest’ultima crea un nuovo oggetto linea di vendita per articolo. Questa classe ha due proprietà strutturali, la descrizione prodotto e la quantità, di quest’ultima non si tratta poiché non è una formazione di un collegamento, essendo l’aspetto degli attributi completamente ignorato nella progettazione.

Nel codice bisogna anche occuparsi della gestione delle eccezioni, ma per ora viene ignorata.

Si potrebbe seguire l’ordine in cui gli oggetti appaiono nei diagrammi di interazione, ma questo non è consigliato, poiché ad ogni nuovo diagramma bisognerebbe aggiungere e modificare ciò che è già stato scritto. Si potrebbero implementare prima classi che non dipendono da altre, e poi si aggiungono le altre, ma se si effettua lo sviluppo guidato dai test, il modo di procedere è diverso. In quel caso si comincia dalla classe controller, verrà trattato successivamente.

Nel costruttore del catalogo prodotto viene creata la mappa, dichiarata nella classe, e carica nella mappa tutte le descrizioni prodotto in base al loro codice. Questo metodo crea delle descrizioni prodotto e le aggiunge alla mappa. Una soluzione minimale più flessibile indica di avere queste informazioni in file di tipo CSV e questo metodo legge le linee da questo file e crea in questo modo le descrizioni prodotto.

Nella classe vendite ci sono tre variabili strutturali e sei operazioni, individuate dal DCD. Per il calcolo del totale dato che non si usano tipi primitivi, bisogna utilizzare il metodo della classe `Money.add` per aggiungere tra di loro due elementi di questa classe, invece di utilizzare semplicemente l’operatore `+`.

Si è bisogno anche della classe `main` per creare il registratore ed il negozio e creare l’interfaccia utente, passando come riferimento il controller. L’oggetto negozio creato in questo metodo è la radice del gerarchia degli oggetti nel modello di dominio, quindi deve creare tutti gli altri oggetti. Essendo un’operazione complessa, si può realizzare un suo diagramma di interazione.

## Retrospettiva sull’Iterazione 1

Ancora non si è finita l’iterazione uno, ma si sono viste le idee essenziali. In Scrum alla fine di ogni iterazione si svolgono due meeting, il primo consiste nel dimostrare il lavoro svolto sul sistema, mentre una riunione privata per il team di sviluppo è dedicata all’analisi dell’applicazione di Scrum per controllare se si è applicato correttamente lo sviluppo iterativo.

Nelle precedenti analisi si sono utilizzati degli elaborati per assistere nella progettazione. I concetti presenti nei casi d’uso vanno rappresentati nel modello di dominio, le interazioni fra gli attori vanno rappresentai nei diagrammi di sistema, inoltre anche in contratti sono utili a formalizzare le informazioni presenti nel testo dei casi d’uso. Inoltre i casi d’uso si utilizzano anche durante la progettazione. Un altro elaborato importante è il modello di dominio, utilizzato per rappresentare i concetti espressi nel testo del caso d’uso, anche se i termini sono espressi meglio nel glossario, sono presenti nomi sintetici per le classi, ed è utile scrivere la definizione delle classi. Inoltre le condizioni dei contratti si riferiscono al cambiamento di stato relativo a questo caso d’uso. Nella progettazione il modello di dominio può fornire uno spunto per la scelta delle classi e dei nomi delle classi.

Le operazioni di sistema sono definite dal testo dello scenario del caso d’uso, per ogni operazione va scritto il relativo contratto, e nella progettazione per ogni operazione si scrive un diagramma di interazione, che descrive l’interazione per gestire quell’operazione. I contratti sono scritti per le operazioni di sistema, in modo più formale descrivono le loro responsabilità. Sono importanti anche nella progettazione, non solo essendo ispirati ai nomi delle classi, anche alcune responsabilità sono motivate dalle post-condizioni dei contratti delle operazioni. I requisiti non funzionali sono definiti da specifiche aggiuntive, hanno un impatto soprattutto sull’architettura del sistema, ma si è deciso di progettare sopratutto per lo strato del dominio, utilizzando un’architettura a tre strati. Il modello di progetto è formato dal diagramma delle classi di progetto ed i diagrammi di interazione per ogni operazione di sistema.

Questi elaborati influenzano il codice, è opportuno che le classi e le interfacce presenti nel codice si rappresentano da classi nel modello di dominio; le proprietà strutturali si rappresentano da variabili di istanza nel codice; le operazioni nei diagrammi di classi di progetto vanno rappresentate come metodi; ed i messaggi studiati nei diagrammi di interazione contribuiscono sia all’identificazione delle operazioni e dei metodi delle classi, sia all’identificazione delle istruzioni dei singoli metodi.

Nella progettazione si è lavorato per operazione di sistema, partendo da una operazione per chiedersi cosa succede al loro interno, nel codice questo viene inserito in più classi, poiché il codice eseguito chiamato appartiene a più classi. Se non si lavorasse in questo modo, si creerebbe una singola funzione per ogni operazione di sistema, avendo una corrispondenza diretta tra le operazioni ed i metodi. Anche se sarebbe comodo inserire tutte le istruzioni di un’operazione di sistema in una singola funzione, se si separa in più metodi si crea codice caratterizzato da una buona coesione e buon accoppiamento, quindi più facilmente comprensibile e modificabile. Consente di effettuare ragionamenti complessivi nei diagrammi visuali ed in seguito permette di scrivere codice caratterizzato da alta coesione e basso accoppiamento. I ragionamenti complessivi sono anche utili, poiché per modificare un’operazione di sistema si modica il progetto, e dal progetto si capisce in quali classi vanno effettuate delle modifiche. La progettazione modulare è una tecnica che produce codice caratterizzato da alta coesione interna e basso accoppiamento esterno, e facilmente comprensibile e modificabile.

## Esempio: Sistema Monopoly

Si considerano i requisiti per il Monopoly Game System, si considera la progettazione del caso d’uso d’avviamento in modo differente rispetto allo studio di caso POS, come dovrebbe essere realizzato.

Per il salto rappresentazionale basso si considerano le stesse classi del modello di dominio. Si sceglie un facade controller come un oggetto radice, di nome "Monopoly Game".

Le operazioni di sistema per lo studio di caso sono `initialize` corrispondente al caso d’uso d’avviamento, e `playGame` l’operazione che simula una partita di monopoly. La simulazione della partita viene realizzata considerando tutti i giocatori a turno per 20 turni, consentiti a lanciare i dadi e muovere il loro segnalino sul tabellone. Si definisce un turno un giocatore che tira i dadi e muove il segnalino, mentre si completa un giro quando tutti i giocatori hanno effettuato il loro turno. Probabilmente bisogna memorizzare dati storici sulla partita, ma queste informazioni sono di interesse solamente durante la progettazione. Bisogna conoscere il numero di giocatori ed il giro corrente, tra le classi del dominio si considera quale possa conoscere entrambi queste informazioni. Probabilmente per eseguire i due cicli più esterni della simulazione si considera il controller. Delle metriche dell’ingegneria del software sulla coesione e l’accoppiamento è suggerito che avere un doppio ciclo è più complesso rispetto ad un unico ciclo, quindi è consigliabile separare i due cicli in due metodi differenti. Nel metodo `playGame` è presente il primo ciclo che invoca sé stesso per giocare un giro, invocando il metodo `playRound`, in questo è presente l’esecuzione del turno di ogni giocatore.

Si considera chi è responsabile di effettuare un turno per il giocatore, se questi giocatori fossero reali sarebbe sbagliato poiché il comportamento del giocatore è contenuto nel controller. Poiché si tratta di giocatori virtuali, è lecito assegnare la responsabilità alla classe giocatore. Per information expert si considerano le informazioni necessarie per effettuare un turno; il giocatore o il segnalino conoscono la posizione corrente nel tabellone del giocatore. Il tabellone conosce la posizione delle seguenti caselle, dove si dovrà muovere il segnalino. Essendo presenti tre esperti parziali, si assegna la responsabilità all’esperto dominante.

Quando ci sono delle scelte di progetto alternative bisogna valutare il loro impatto su coesione ed accoppiamento. Se si assegnano al controller, si assegnerebbero tutte le responsabilità per la simulazione al controller, ma questo non è accettabile in termine di coesione ed accoppiamento, quindi si esclude il controller. Considerando i requisiti futuri, le informazioni gestite dal giocatore dovranno essere prese in considerazione per effettuare il turno di gioco, quindi si scarta il tabellone e si assegna la responsabilità di effettuare un turno al giocatore. Se il giocatore non fosse reale, non sarebbe questa la scelta. I turni vanno effettuati in ordine quindi probabilmente si ha un riferimento ad una lista di giocatori nel controller, su cui viene invocato il metodo `takeTurn`.

Un giocatore per effettuare un turno deve tirare i dati, calcolare la nuova posizione del segnalino e spostarlo sulla nuova casella. Per muovere il segnalino il giocatore deve passare la nuova posizione al segnalino. Per conoscere la nuova posizione bisogna comunicare con il tabellone, mentre per tirare i dadi bisogna conoscere i dadi. Una possibilità è che il giocatore invochi il controller per tirare i dadi, aumentando l’accoppiamento, mentre alternativamente si potrebbe avere un riferimento diretto tra il giocatore ed i dadi ed il tabellone. Entrambe queste soluzioni aumentano l’accoppiamento. Queste associazioni non erano presenti nel modello di dominio, ma non si è vincolati a mantenere le stesse associazioni del modello di dominio. Si considera quest’ultima soluzione, si considerano inoltre visibilità per attributo ottenute nel caso d’uso d’avviamento oppure durante all’esecuzione del metodo.

Per il principio della separazione tra il comando e l’interrogazione si dividono le operazioni per chiedere al dado di generare un numero casuale `roll` e di richiedere la faccia attuale del dado `getFaceValue`. Nel gioco alcune operazioni richiedono di accedere più volte alle informazioni sul lancio del dado, quindi se non si memorizzassero non sarebbe possibile ottenerle dopo il lancio. Quindi si utilizza una variabile interna `faceValue` per memorizzare questa faccia corrente. Questo principio di programmazione indica che ogni metodo o operazione dovrebbe essere un comando, che esegue azioni senza restituire dati, ed un’interrogazione che calcola e restituisce un valore.

Nella progettazione si utilizza UML come bozzo, quindi non si dovrebbero realizzare diagrammi di interazione per metodi invocati durante l’esecuzione di un metodo. Si considera il metodo `getSquare` per conoscere la nuova casella dove dovrebbe muoversi il segnalino. Questo finisce il progetto per il caso d’uso di simulazione di una partita, invece per il caso d’uso d’avviamento bisogna creare tutti questi oggetti e formare dei collegamenti. Per ogni classe bisogna capire l’oggetto che crea quella classe. L’oggetto di dominio iniziale è un oggetto radice e potrebbe essere “Monopoly Game”, questo crea il tabellone, il giocatore, mentre per i dadi, si potrebbe scegliere sia il giocatore che il controller, ma dovendo esserci solamente due dadi, ogni nuova creazione di un giocatore creerebbe una nuova coppia di dadi, quindi si assegna questa responsabilità al controller. Il giocatore crea il suo segnalino, mentre il tabellone crea le sue caselle.

Si parte dalle classe meno accoppiate alle classi più accoppiate. Si considera quindi il dado:

``` java
    public class Die{
        public static final int MAX = 6;
        private int faceValue;

        public Die(){
            roll();
        }

        public void roll(){
            faceValue = (int) (Math.random() * MAX + 1);
        }

        public int getFaceValue(){
            return faceValue
        }
    }
```

Si considera la classe casella:

``` java
    public class Square{
        private String name;
        private int index;

        public Square(String name, int index){
            this.name = name;
            this.index = index;
        }
    }
```

Si implementa ora il tabellone, dato che si è realizzata la classe casella da cui dipende:

``` java
    public class Board{
        private static final int SIZE = 40;

        private List<Square> squares;

        public Board(){
            squares = new ArrayList<>(SIZE);
            this.buildSquares();
        }

        private void buildSquares(){
            for (int i = 0; i < SIZE; i++){
                Square s = new Square("Square")
                squares.add(s)
            }
        }

        public Square getStartSquare(){
            return squares.get(0);
        }

        public Square getSquare(Square start, int distance){
            int endIndex = (start.getIndex() + distance) % SIZE;
            return squares.get(endIndex);
        }
    }
```

Si passa ora alla classe segnalino:

``` java
    public class Piece{
        private Square location;

        public Piece(Square location){
            this.location = location;
        }

        public Square getLocation() { 
            return location; 
        }
        
        public void setLocation(Square location) { 
            this.location = location; 
        } 
    }
```

Per ultima si implementa la classe giocatore, la più accoppiata in questo progetto:

``` java
    public class Player{
        private String name;
        private Piece piece;
        private Board board;
        private Die[] dice;

        public Player(String name, Die[] dice, Board board){
            this.name = name;
            this.dice = dice;
            this.board = board;
            this.piece = new Piece(board.getStartSquare());
        }

        public void takeTurn(){
            int rollTotale = 0;
            for (int i = 0;  i < dice.length; i++){
                dice[i].roll();
                rollTotale += dice[i].getFaceValue();
            }
            Square oldLoc = piece.getLocation();
            Square newLoc = board.getSquare(oldLoc, rollTotal);
            piece.setLocation(newLoc);
        }
    }
```

# Iterazioni Successive

## Sviluppo Guidato dai Test e Refactoring

Queste tecniche cominciano a prendere piene dal ’99, quando venne pubblicato il primo libro commentato sulla metodologia agile “Extreme Programming”, tra queste pratiche le più diffuse e radicate in tutti i metodi agili sono lo sviluppo guidato dai test ed il refactoring. Lo sviluppo guidato dai test è una pratica di progettazione, dove una pratica importante è capire in che ordine bisogna scrivere i test, altrimenti sarebbe una pratica solamente di programmazione. Esistono diversi tipi di test di cui si parla, oltre ai test unitari, test di integrazione, test di componenti, test end-to-end, etc., che verificano la correttezza di porzioni o dell’inerita del software.

Il ciclo del TDD, si scrive prima un test unitario che fallisce, poiché il codice o non è stato scritto oppure non è corretto, in seguito si scrive il codice che permette di passare il test, ed in seguito si applica il refactoring. Poiché prima di passare al test successivo bisogna ripulire il codice per avere una situazione il più semplice possibile. Ad oggi lo sviluppo automatizzato è considerato una pratica fondamentale dello sviluppo iterativo. La mancanza di implementare test automatizzati viene considerato un debito tecnologico.

Il refactoring può essere definito in vari modi, come un metodo strutturato e disciplinato per riscrivere ristrutturare codice esistente senza modificarne il comportamento, applicando piccoli passi di trasformazione in combinazione con la ripetizione di test dopo ciascun passo, poiché non si cambia il comportamento. Questo permette di migliorare il codice per renderlo più accettabile per il miglioramento successivo.

Si utilizza il refactoring per semplificare l’introduzione dei cambiamenti, che potrebbero richiedere una modifica dell’assegnazione delle responsabilità. Se non si vuole ripulire il codice, lo sviluppo iterativo fallisce, poiché bisogna modificarlo continuamente.

Si considera il metodo `takeTurn` del giocatore, che non è molto coeso:

``` java
    public class Player{
        private String name;
        private Piece piece;
        private Board board;
        private Die[] dice;

        public Player(String name, Die[] dice, Board board){
            this.name = name;
            this.dice = dice;
            this.board = board;
            this.piece = new Piece(board.getStartSquare());
        }

        public void takeTurn(){
            int rollTotale = 0;
            for (int i = 0;  i < dice.length; i++){
                dice[i].roll();
                rollTotale += dice[i].getFaceValue();
            }
            Square oldLoc = piece.getLocation();
            Square newLoc = board.getSquare(oldLoc, rollTotal);
            piece.setLocation(newLoc);
        }
    }
```

Un buon metodo contiene 3 o 4 linee di codice, compresa intestazione e commenti. Questo metodo non è coeso perché si occupa di più di un’operazione. Deve tirare i dati, calcolare la nuova posizione ed assegnare la nuova posizione al segnalino. In molti IDE esiste un’opzione “extract method” per effettuare quest’operazione, selezionando la porzione di codice che si vuole trasformare nel suo suo stesso codice:

``` java
    public class Player{
        private String name;
        private Piece piece;
        private Board board;
        private Die[] dice;
        
        public Player(String name, Die[] dice, Board board){
            this.name = name;
            this.dice = dice;
            this.board = board;
            this.piece = new Piece(board.getStartSquare());
        }

        public void takeTurn(){
            int rollTotal = rollDice();
            Square oldLoc = piece.getLocation();
            Square newLoc = board.getSquare(oldLoc, rollTotal);
            piece.setLocation(newLoc);
        }

        private int rollDice(){
            int rollTotal = 0;
            for (int i=0; i<dice.length; i++){
                dice[i].roll();
                rollTotale += dice[i].getFaceValue();
            }
            return tolTotale;
        }
    }
```

## GRASP: Polimorfismo

Nella programmazione orientata agli oggetti, è necessario l’uso del polimorfismo, altrimenti si chiamerebbe programmazione ad oggetti; allo stesso modo per l’analisi, per la generalizzazione. Si comincia quindi in questa iterazione a trattare la progettazione e l’analisi orientata agli oggetti.

Per motivi didattici in quest’iterazione si considerano ancora casi semplici.

Sono stati già trattati i cinque pattern semplici, ma i pattern GRASP sono nove, i quattro che verranno introdotti in questa sezione sono:

- *Pure Fabrication*

- *Polymorphism*

- *Indirection*

- *Protected Variations*

I pattern GRASP di base normalmente scelgono le classi ispirandosi al modello di dominio e non viene preso in considerazione il polimorfismo, mentre questi quattro pattern avanzati permettono di introdurre classi software scollegate dal modello di dominio, con fabrication, e si può introdurre e capire come utilizzare il polimorfismo, inoltre analizzano trattano l’accoppiamento.

### Pure Fabrication

Quando sono stati introdotti i pattern, ogni tanto si diceva che i suggerimenti di questi pattern potevano essere sbagliati, delle controindicazioni. Bisogna capire come agire quando si verificano queste controindicazioni, e bisogna capire quando si applicano. Questo pattern parla di invenzione pura, qualcosa di inventato nel progetto, ma deve essere una scelta appropriata, “pura”. In particolare il problema affrontato da questo pattern consiste nel determinare a quale oggetto assegnare la responsabilità quando non si possono chiamare obiettivi di high cohesion e low coupling, ma le soluzioni suggerite da information expert o da altri pattern non sono appropriate. La soluzione è quella di assegnare ad una classe artificiale o di convenienza un insieme di responsabilità altamente coeso. Sicuramente si vuole garantire una coesione alta, a questa classe inventata appositamente per mantenere una coesione alta ed accoppiamento basso. Se tutte le soluzioni basata sul modello di dominio portano a peggiorare il progetto in termini di coesione ed accoppiamento, allora, solo in questo caso, bisogna applicare questo pattern.

Nel caso del sistema POS, l’oggetto indicato da information expert per memorizzare una vendita, è la vendita stessa, ma questo vuol dire che le istruzioni SQL per salvare i dati sulla base di dati si trovano dentro la classe vendita, ma questa è certamente una soluzione di bassa coesione. Sicuramente è una violazione del principio di separazione degli interessi, si assegnano sia interessi di dominio che tecnici alla classe vendita, quindi non è una soluzione adatta alla separazione del progetto a strati. Inoltre si starebbe accoppiando la classe vendita del modello di dominio ad una tecnologia specifica, quindi per modificare la tecnologia bisognerebbe cambiare anche questa specifica porzione di codice.

Invece per pure fabrication bisogna creare una nuova classe dedicata a salvare i dati della vendita, questa classe se viene implementato un progetto software su un sito con Spring, è una repository, un’interfaccia. Questo salvaguardia la coesione e l’accoppiamento. Nelle ultime iterazioni potrebbe essere il controller a parlare con la repository, oppure il ledger.

L’accoppiamento non si può eliminare, ma si può spostare dove da meno fastidio. Repository è un pattern per la persistenza degli oggetti, che verrà analizzato alla fine del corso. Incapsula l’accesso alla base di dati, nascondendolo e fornisce agli altri oggetti l’illusione di una collezione in memoria di oggetti di un certo tipo. Da l’illusione di una collezione in memoria, come se fosse presente una classe di vendite, o di altri elementi in memoria persistente. In questo modo si può modificare il progetto semplicemente per implementare la persistenza. Quindi verranno sostituite tutte le collezioni nel progetto con delle repository, si stanno solo cambiando localmente alcuni dettagli.

Questa soluzione salva coesione ed accoppiamento della vendita. Inoltre un’altra soluzione è quella di una classe più generale dedicata a salvare oggetti di qualunque tipo, non solo vendita, quindi non si tratta di una repository, questo è molto generale ed è facilmente riutilizzabile.

Nel Monopoly la classe che lancia i dadi nel progetto attuale è il giocatore, poi chiede il risultato e li somma. In questa soluzione il giocatore è fortemente accoppiato con le regole dell’uso dei dadi, non è un accoppiamento elevato, ma certamente rilevante. Nella versione corrente del monopoly sono presenti tre dadi, di cui uno opzionale, e ci sono delle regole speciali per capire come gestire il risultato del terzo dado. Quindi considerando questi requisiti la classe giocatore sarebbe ancora più accoppiata e meno coesa, quindi questo progetto sicuramente non è ideale per problemi di coesione ed accoppiamento del giocatore nei confronti dei dadi. Una soluzione migliore è quella di introdurre una classe che il li libro chiama `Cup`, ci sono dei giochi che contengono nella confezione un bicchiere, il bussolotto, in cui si mettono i dadi per lanciarli. Quindi nei modelli di dominio relativi a questi giochi, è presente una classe relativa al bussolotto. Poiché in Monopoly non c’è questa diventa un’applicazione di pure fabrication. Questa soluzione semplifica la classe giocatore, le responsabilità legate a gestire i dati vengono assegnate a questa nuova classe, spostando questa parte di codice. Poiché la classe bussolotto gestisce le regole dei dadi è giusto che sia fortemente accoppiata con essi.

Le pure fabrication possono essere scelte ispirandosi ad altri domini, come in questo caso, mentre altre applicazioni non prendono da altri modelli di dominio.

Due tipi di classi nel DCD, alcune ispirate al modello di dominio, ed altre non ispirate, le prime classi a volte vengono chiamate classi oggetti scelti per disposizioni rappresentazionali. Le classi create da pure fabrication vengono chiamate classi oggetti scelti per decomposizioni comportamentali.

Nei progetti reali c’è un buon bilanciamento tra questi due tipi di classi, è difficile che non ci sia pure fabrication, ed usare classi solo ispirate al modello di dominio non è consigliato. L’esperienza detta quando un progetto è bilanciato rispetto a questi due tipi di classi. Le classi oggetti scelti per disposizioni rappresentazionali hanno diversi nomi, tra questi, in particolare in DDD, ci si interesse dei servizi. Un servizio rappresenta un insieme di funzioni o funzionalità correlate che non trovano posto in nessun’altra classe singola del dominio, rappresentano comportamenti.

Se si usa un use-case controller anche questo non trova corrispondenze nel dominio, quindi si tratta di pure fabrication. Non bisogna abusare di pure fabrication, non bisogna inserire classi artificiali costantemente, anche questo pattern presenta delle controindicazioni. Le responsabilità dovrebbero essere assegnate in primo luogo da information expert, per avere un salto rappresentazionale basso. Abusando di pure fabrication, aumenta il salto rappresentazionale, aumentando la complessità del progetto.

ALcuni errori comuni di pure fabrication consistono di assegnare ad un oggetto ratificale responsabilità, senza risolvere il problema di coesione ed accoppiamento. Siccome le pure fabrication rappresentano algoritmi. Nel sistema POS la soluzione per il calcolo del totale della vendita è esemplare, introdurre una classe artificiale per questa responsabilità peggiora l’accoppiamento. Nel Monopoly assegnare la responsabilità di creare le caselle ad una classe Dog peggiore l’accoppiamento, assegnando responsabilità a classi che non sono appropriate per quel modello di dominio.

### Polymorphism

Intuitivamente la soluzione proposta da questo pattern è di usare il polimorfismo, la soluzione in realtà è molto più specifica, usare il polimorfismo per assegnare una responsabilità seguendo una specifica linea guida. Inoltre bisogna capire qual è il problema, non è dovuto ad una generalizzazione nel modello di dominio.

I problemi sono in realtà una coppia di problemi, tra loro correlati. Il primo tipo di problema in cui è utile utilizzare il polimorfismo è quando nel sistema bisogna gestire alternative basate sul tipo. Un esempio nel sistema Monopoly consiste nelle varie alternative dovute al tipo di casella dove atterra il giocatore. Per gestire le alternative si possono usare le istruzioni condizionali, ma questa soluzione aumenta l’accoppiamento e non è facilmente modificabile. L’esperienza detta che un progetto di questo tipo è difficile da gestire rispetto a nuove alternative. Quando si gestiscono queste alternative sulla base di istruzioni condizionali, queste non sono su un metodo solo, ma con la stessa struttura sono in metodi diversi della stessa classe, o peggio ancora in metodi di classi diverse. Quindi bisognerebbe modiche in modo coordinate tutti questi gruppi di codice. Utilizzando il polimorfismo per gestire un nuovo caso è sufficiente aggiungere una nuova classe, questo rappresenta una soluzione certamente migliore.

Implementare operazioni dipendenti dal tipo con istruzioni condizionali è una cattiva pratica, non è facilmente comprensibile e non è facilmente modificabile.

Il secondo problema è come creare componenti software inseribili, ovvero si vuole avere oggetti in una relazione di tipo client-server, quando uno di questi ha bisogno di effettuare un’azione questo chiede ad un altro, quello che chiama l’operazione ha il ruolo di client quello che la riceve ha il ruolo di server. Considerando questi oggetti in una relazione client-server, si vuole utilizzare nuovi server, nuove implementazioni del servizio, senza dover cambiare il client.

Le sottoclassi sono accoppiate alle superclassi, questo accoppiamento deve essere tenuto basso, se si usasse il polimorfismo per risolvere altri problemi, si potrebbe aumentare questo accoppiamento, rendendo il codice più difficile da modificare.

Quando le alternative oppure i comportamenti correlati variano con il tipo di qualche oggetto, allora assegna le responsabilità del comportamento che varia ai tipi per i quali il comportamento varia, utilizzando operazioni polimorfe; non ai tipi di cui varia il comportamento. Tra questi due è presente una profonda differenza.

Non è obbligatorio l’uso dell’ereditarietà per implementare il polimorfismo, per cui in molti linguaggi di programmazione è possibile utilizzare il polimorfismo senza ereditarietà, per esempio Python dove gli oggetti non sono tipati. Per eseguire alternative che variano in base al tipo non bisogna usare logica condizionale, e non bisogna testare il tipo di un oggetto, solo in casi estremamente specifici. Solo in alcuni casi è utile, altrimenti per gestire questi tipi di alternative bisogna utilizzare il polimorfismo. Tuttavia non vanno evitate le istruzioni condizionali da tutto il codice, queste sono necessarie, non per testare il tipo degli oggetti.

Si vuole risolvere il problema del comportamento del giocatore in base al tipo di casella su cui si trova. Nel progetto corrente si utilizza uno switch, un’istruzione che simula una cascata di if per implementare questo comportamento. Questo è il modo in cui non bisogna procedere, solo nel caso in cui si è sicuri di non essere in questo caso, avendo una sola istruzione condizionale in tutto il codice. Quando ce ne possono essere più di una bisogna utilizzare un altro metodo.

Il comportamento che varia è quello del giocatore, quindi bisogna usare il polimorfismo sulla classe casella, non va usato sui tipi di cui varia, ma sui tipi per cui varia il comportamento. Questo varia in base al tipo di casella su cui è arrivato. Per cui varia il comportamento sulla casella. Le classi software di caselle dovranno avere una qualche operazione polimorfa. Ma se il polimorfismo è sulle caselle, come si può cambiare il comportamento nel giocatore. Bisogna utilizzare un qualche metodo che permette di variare il comportamento. Questo metodo deve avere qualche visibilità del giocatore di cui deve variare il comportamento. Questa visibilità può essere per attributo, parametro o locale, una buona soluzione in questo caso è utilizzare una visibilità per parametro, avere nella classe casella un’operazione polimorfa, parametrica rispetto a giocatore. Questa operazione dirà al giocatore come si deve comportare. Nel progetto viene usata un’operazione `landedOn` polimorfa rispetto al giocatore, a cui viene passato il riferimento del giocatore. Questo metodo viene chiamato dalla casella su cui si trova il giocatore. Questa operazione è astratta nella superclasse `Square`, ma è concreta nella sue sottoclassi. Si crea una gerarchia di classi software che rispecchia la gerarchia di classi concettuali nel progetto del Monopoly. Nel modello di dominio si hanno introdotto queste sottoclassi poiché implicavano un comportamento diverso, normalmente su queste classi si applica il polimorfismo.

Il polimorfismo non ha a che fare con le proprietà strutturali. Nel modello di dominio si ha il giocatore, la casella ed il segnalino. Si modifica il modello poiché è il giocatore che si trova sulla casella, e possiede il segnalino. Casualmente il segnalino è su quella casella, ma l’informazione importante è che il segnalino si trova su quella casella. Nel progetto la classe segnalino viene sostanzialmente eliminata, ed il giocatore conosce direttamente la posizione in cui si trova. Questo aumenta la coesione e l’accoppiamento, perché il giocatore sa direttamente dove si trova e per cambiare posizione deve cambiare una sua propria variabile di istanza. Il giocatore chiede direttamente al tabellone dove deve andare passando il suo parametro posizione, aggiornandolo. Non si è cambiato il comportamento del progetto dall’iterazione uno, ma questo refactoring permette di gestire meglio operazioni successive. A questo punto è il giocatore che ha il controllo, ma non conosce il comportamento richiesto da quel tipo di casella. Usa il polimorfismo, invocando l’operazione polimorfa della casella su cui si trova, passando un riferimento a sé stesso come parametro. In seguito la casella delega il comportamento al giocatore, non lo effettua la casella stessa. Il metodo del giocatore che verrà eseguito dipende dal tipo specifico della casella, che il giocatore non può conoscere.

Quando si rappresenta una chiamata polimorfa in un diagramma di interazione, si rappresenta fino all’invocazione polimorfa, ed in seguito si crea un diagramma diverso per ogni tipo di casella che implementa questo metodo polimorfo. Le sottoclassi di casella al momento sono quattro, quindi bisogna mostrare quattro diagrammi di interazione.

La forza di questo pattern consiste di avere il codice di due tipi di casella diverse, in due classi diverse. In questo modo dopo l’aggiunta di una nuova sottoclasse di casella, non è necessario testare quello che non è stato cambiato, ovvero gli altri tipi di casella. Questo invece andrebbe fatto se si utilizzasse una cascata di istruzioni condizionali. Questo è il vero valore del pattern polimorfismo. Per implementare questo polimorfismo potrebbe essere necessario aggiungere metodi alla classe di cui cambia il comportamento, per essere invocato dalla classe per cui il comportamento cambia, questi sono metodi assolutamente coesi.

Il polimorfismo si applica anche per i componenti software inseribili, si considerano le interazioni con il sistema esterno della contabilità per il sistema POS. L’azienda del sistema POS vende solo il sistema POS, e permette di utilizzare qualsiasi sistema di contabilità, poiché è la scelta più flessibili che permette di vendere il più possibile il sistema di contabilità. Il sistema POS quindi deve poter interagire su qualsiasi sistema di contabilità sul mercato. Si suppone che esistano diversi sistemi di contabilità, ed ogni negozio ne usa uno solo, ma a priori non si può sapere quale venga utilizzato, e si vuole realizzare un sistema POS indipendente dal tipo di sistema di contabilità utilizzato.

I sistemi di contabilità hanno un comportamento molto simile, ma hanno un API diversa, ed a parità di tecnologia usate, l’interfaccia usata è sicuramente diversa. Per gestire l’interazione con questi sistemi, si suppone che sia la classe register che completata la vendita parla con il sistema di contabilità. La prima possibilità consiste nell’usare un’istruzione condizionale, ma questa non facilita la comprensione e la modificabilità in futuro, in caso di cambiamento a questi sistemi esterni. Il motivo per cui questa soluzione è la peggiore è che il codice per interagire con un certo sistema di contabilità, che non è nel modello di dominio, si trova all’interno di una classe.

Il suggerimento del polimorfismo è simile a quello descritto nel sistema Monopoly, si vuole inserire questi pezzi di codice in classi diverse, ed a questi pezzi di codice si vuole dare lo stesso nome, si vuole usare una superclasse astratta che contiene questo nome unico, in modo che il registratore possa parlare con un qualsiasi sistema di contabilità mediante ad una chiamata ad una classe astratta. Poiché il comportamento varia con il tipo, come si parla con il sistema esterno. Come si parla con il sistema esterno si chiama adattamento, esiste infatti un pattern chiamato adattatore che risolve nello specifico questo problema. Bisogna assegnare la responsabilità al tipo di adattamento che varia a tipi diversi concreti che corrispondono al sistema esterno con cui si sta parlando. Queste classi sono delle pure fabrication, non sono classi di dominio, poiché non hanno quasi nessun collegamento al dominio. Qui si introducono nuovi tipi, mentre per le caselle si utilizzavano i tipi che già si avevano. Il registratore userà il polimorfismo in base a questa variabile. La spiegazione del progetto è basata sul polimorfismo, e per chi varia in base al tipo di comportamento esterno per cui vengono definite nuove classi che non sono di dominio.

Si utilizza la nomenclatura con una `I` davanti al nome per indicare che si tratta di un’interfaccia. L’operazione di questa interfaccia è proprio quella che si è messa nel diagramma di sistema `postSale`, questa si potrebbe chiamare in modi diversi, si chiama nel modo preferito. Inoltre si ha una classe concreta per ogni tipologia di sistema esterno, che implementa il metodo `postSale` in base alla tecnologia di ognuno dei sistemi esterni. L’accoppiamento è ridotto poiché ognuna di queste classi è un unico tipo di sistema. Se viene introdotto sul mercato un nuovo sistema di contabilità allora è sufficiente creare un nuovo tipo di interfaccia.

L’adattatore deve adattare la chiamata e adattare i parametri, l’operazione di invocare del sistema esterno, probabilmente non si chiama `postSale`, ma in qualche altro modo. Inoltre l’adattatore, data una vendita di tipo `Sale` del tipo del sistema POS, mentre il parametro del sistema di contabilità è di un altro tipo, quindi bisogna costruire questo oggetto comparabile alla vendita nel sistema POS, e poi chiamare il metodo specifico per questo sistema di contabilità.

Il modo migliore di cambiare le cose è non cambiarle, ma aggiungere nuove classi al limite del possibile per mantenere il comportamento invariato, contenti comportamenti aggiuntivi.

Il polimorfismo non è opportuno in sistemi molto semplici, è molto costoso, la prima volta che viene applicato, sopratutto se ci sono tanti tipi di variazioni e tanti comportamenti diversi. Se i tipi o variazioni sono sempre due, potrebbe essere più semplice utilizzare istruzioni condizionali. È di solito un errore assegnare la responsabilità di un comportamento ai tipi di cui varia il comportamento.

In certi casi il comportamento di un oggetto non varia in base al tipo, ma in base a qualche parametro.

### Indirection

Questo è un pattern tipico per ridurre l’accoppiamento, l’indirezione affronta il problema di assegnare la responsabilità per diminuire l’accoppiamento diretto tra due oggetti. Utilizzando la classe vendita per accedere la base di dati si aumenta notevolmente l’accoppiamento diretto tra questi due. La soluzione è spostare questo codice in un’altra classe, facendone un intermediario per la comunicazione precedentemente diretta. La soluzione assegna la responsabilità ad un oggetto intermediario per diminuire l’accoppiamento diretto indesiderato. L’accoppiamento indiretto non è più un problema, poiché è alterante coesa per pure fabrication. Spesso questa nuova classe è un’indirezione.

Allo stesso modo per il giocatore ed i dadi, attraverso il bussolotto. Il giocatore deve sapere meno cose del bussolotto rispetto a quante ne doveva sapere prima sui dadi. L’indirezione riduce l’accoppiamento. Molte problematiche dell’informatica sono risolte dall’indirezione. Ma producono problemi di prestazione, ma non sono di interesse in questo caso.

Molti dei design pattern sono basati sul polimorfismo e rappresentano delle pure fabrication che usano indirezioni.

### GoF: Template Methode

Il problema affrontato da questo pattern GoF, è di progettare algoritmi ricorrenti, ma nella sua ipotesi i diversi algoritmi sono una variante l’uno dell’altro, al contrario del pattern strategy.

La soluzione di questo pattern indica di introdurre le parti comuni in una superclasse astratta ed inserire nelle sottoclassi solo le parti varianti.

### GoF: Observer

Nei sistemi software di successo le interazioni con sistemi esterni sono effettuati da invocazione remota, o tramite ascoltatori. Questo pattern *Observer* o *Publisher-Subscriber*, descrive questo secondo modo di operare, e risolve lo stesso problema dell’invocazione remota, ovvero la comunicazione con sistemi esterni.

In questi sistemi, gli oggetti informano altri oggetti che è avvenuto qualcosa, si usano avvenimenti di dominio, ed è l’oggetto che ascolta gli eventi che dal tipo di evento verificato decide quale dei suoi metodi eseguire per gestire questo evento. Questo avviene in modo asincrono, mentre in invocazione remota avviene in modo sincrono, l’oggetto invocante aspetta la fine dell’esecuzione del metodo invocato. Inoltre ci sono diversi tipi di oggetti *subscriber*, “abbonati”, che ascoltano gli eventi di dominio, mentre diversi oggetti *publisher* generano gli eventi di dominio. Inoltre si vuole un accoppiamento basso tra publisher e subscriber. Questo è un problema estremamente comune, la soluzione è inserire un ascoltatore intermediario tramite interfaccia, in realtà molti ascoltatori che implementano l’interfaccia. Un altro aspetto è che la relazione di abbonamento è dinamica, è sufficiente aggiunte un elemento alla collezione di abbonati all’interfaccia ascoltatore.

Si utilizza questo sistema per gestire la visualizzazione dei dati, poiché è proibito che gli oggetti modello comunichino direttamente con gli oggetti vista, in questo modo possono comunicare indirettamente. L’interfaccia utente è un abbonato, e la logica di business è un publisher di eventi che viene ascoltato dall’interfaccia utente che può rappresentare il dato.

Per le operazioni `endItemEntry`, utilizzando questo pattern si può comunicare un evento per permettere il calcolo dei totali da associare alla vendita, pubblicando l’evento relativo al nuovo totale della vendita.

## Rapido Aggiornamento dell’Analisi

Considerando il sistema POS dal punto di vista dei casi d’uso non ci sono cambiamenti. Mentre dal punto dei vista dei requisiti, bisogna considerare che i dati delle transazioni devono essere registrati nel sistema di contabilità, già esistente. Questo viene mostrato nei diagrammi di sequenza di sistema, avendo più partecipanti. Bisogna considerare anche gli attori di supporto, fra ci si concentra sul sistema di contabilità.

Questo sistema di contabilità è a scatola nera e si interagisce passando le informazioni con metodi `postSale`. Le imposte calcolate alla vendita vengono calcolate da un altro sistema, inoltre per effettuare una transazione con carta di credito si deve ricevere una conferma.

Nel calcolo parziale di una vendita, sono stati commessi degli errori nelle analisi precedenti. Se il prezzo di un prodotto cambia dopo la conclusione di una vendita, questo viene calcolato in base al prezzo attuale, non in base a quanto sono stati venduti, quindi il totale di una vendita potrebbe essere sbagliato. Inoltre si suppone di essere interessati a tutti i dettagli di una vendita, quindi anche dei prezzi dei singoli articoli nella vendita. Il problema si potrebbe risolvere memorizzando lo storico dei prezzi, ma questo non è un buon approccio. Si considera invece che il parametro contenuto nella descrizione di un articolo, si riferisca al prezzo corrente, mentre nella classe linea di vendita per articolo si introduce un nuovo attributo che corrisponde al prezzo di vendita con cui è stato venduto.

Devono essere modificati i diagrammi di sequenza di sistema, aggiungendo i metodi e le interazioni necessarie per richiedere alla descrizione articolo il prezzo corrente.

Per il monopoly si inseriscono caselle di vario tipo, inserendo una gerarchia di classi, ma queste generalizzazioni verranno descritte successivamente.

Nel sistema POS cambiano i requisiti relativa ai pagamenti, quindi nel modello di dominio bisogna utilizzare nuovi concetti, alcuni dei quali non si conosce come rappresentarli. Probabilmente una carta di credito è una classe, e servizi di autorizzazioni del pagamento. Per realizzare diverse classi per i pagamenti, si considerano le classi di pagamento in contanti, con carta o con assegno, delle specializzazioni della generalizzazione pagamento.

In UML ci sono due notazioni per le gerarchie, una dove ogni classe ha una sua freccia, un’altra dove tutte le frecce delle sottoclassi convergono, la differenza quindi è solamente grafica.

Bisogna capire quando è lecito ed utile mostrare una relazione di generalizzazione specializzazione tra classi. Per comprendere se una relazione può essere realizzata in questo modo bisogna considerare tre criteri, il primo indica che la definizione di una superclasse deve essere più generale della definizione di una sottoclasse, altrimenti sarebbe errato utilizzare questo simbolo. Il secondo criterio non riguarda l’intenzione, ovvero la definizione, ma l’estensione, l’insieme degli elementi della classe; tutti i membri dell’estensione della sottoclasse devono essere membri dell’estensione della superclasse, altrimenti non sarebbe una sottoclasse.

Poiché ogni istanza della sottoclasse è anche un’istanza della superclasse, deve passare il test linguistico secondo cui una sottoclasse è un superclasse, sulla base dei loro nomi. Questa regola delle conformità delle estensioni si può effettuare ragionando sulle estensioni oppure applicando questa regola linguistica.

Il terzo criterio riguarda le proprietà strutturali delle classi, attributi e partecipazione ad associazioni. Tutte le caratteristiche strutturali di una superclasse si devono poter applicare allo stesso modo a ciascuna delle sottoclassi.

Affinché sia lecito utilizzare il simbolo, devono essere verificate tutte e tre queste condizioni. L’introduzione di una classe concettuale, può essere suggerita dall’identificazione di una partizione di una classe concettuale identificata in precedenza. Bisogna mostrare altre classi disgiunta dalla sottoclasse che formano insieme una partizione della superclasse. È utile mostrare solamente partizioni, non sottoclassi singole. Aggiungere una sottoclasse è utile quando presenta delle proprietà strutturali aggiuntive rispetto alla superclasse, ha quindi attributi o associazioni aggiuntive di interesse. È utile introdurre una sottoclasse quando il suo comportamento è diverso da quello della superclasse o dalle altre sottoclassi, secondo modalità di interesse.

Nell’esempio del monopoly si considera se i vari tipi di caselle è utile rappresentarli come delle sottoclassi, questo è verificato poiché il loro comportamento è differente tra di loro e dalla superclasse. Ognuno di questi tipi di casella implica un comportamento diverso. Queste sottoclassi da sole non formano una partizione, quindi si aggiunge una sottoclasse che rappresenta tutte le caselle rimanenti, avente nessun comportamento, l’assenza di comportamento è anch’essa un comportamento, diverso da quello delle altre sottoclassi.

Alla fine di tutte le iterazioni, questa gerarchia sarà più grande.

Un errore comune nell’utilizzo delle generalizzazione consiste nell’utilizzare sottoclassi quando nel modello di dominio per avere una gerarchia completa il numero di sottoclassi non sia stabile, ovvero quando le regole di dominio cambiano frequentemente.

L’introduzione di una superclasse è utile quando le sottoclassi rappresentano variazioni di un concetto simile, quando le sottoclassi sono conformi alle diverse regole prima elencate.

### Classi Astratte

Una classe concettuale è astratta se ciascun membro della classe deve essere anche membro delle sottoclassi. Le classi astratte in Java non possono essere istanziate. Se le sottoclassi partizionano le superclassi, allora questa è astratta, ma se è possibile creare un’istanza non appartenente alle sottoclassi, la superclasse non è astratta. Seguendo le linee guida descritte precedentemente tutte le superclassi sono astratte.

In UML si utilizza una notazione o scrivendo il nome in corsivo, oppure scrivendo `{abstract}` accanto al nome. Se la superclasse fosse astratta ogni possibile istanza richiederebbe di una sottoclasse, anche se avesse una singola istanza. Per il sistema POS con il riferimento ai requisiti correnti, il pagamento è una superclasse, partizionata dai vari tipi di pagamenti.

Per rappresentare un diagramma degli oggetti in presenza di classi astratte si considerano solo le istanze delle sottoclassi, senza rappresentare la generalizzazione.

La classificazione degli oggetti indica quali sono le classi di cui un oggetto è istanza. In UML sono possibili diverse opzioni per gestire questa classificazione. Per classificazione singola si indica che un oggetto appartiene direttamente ad una sola classe, che è la classe più specifica di un oggetto. Mentre nella classificazione multipla un oggetto può appartenere direttamente a più classi. Queste potrebbero essere collegate in una gerarchia di classi. Nella classificazione statica il tipo di un oggetto è immutabile, mentre nella classificazione dinamica, uno stesso oggetto potrebbe appartenere in tempi diversi a classi diverse.

Nei modelli ER si ha una classificazione multipla e dinamica, in UML invece hanno una classificazione singola e statica, questi due hanno una semantica completamente diversa. In molti linguaggi di programmazione ad oggetti si usa la classificazione singola e statica, quindi nella modellazione di dominio per mantenere il salto rappresentazionale basso si utilizza la stessa classificazione.

### Stati Dinamici

In alcuni casi gli oggetti si possono trovare in stati diversi, normalmente lo stato degli oggetti è pensato per cambiare nel corso del tempo, il loro tipo no. Per esempio un’ordinazione in un ristorante può essere registrata, in preparazione o consegnata, etc. Questo non si rappresenta tramite delle sottoclassi, poiché si utilizza una rappresentazione singola e statica, quindi lo stato non può essere realizzato mediante lo stato, dato che il tipo è immutabile.

Per rappresentare i diversi tipi di stati si associa l’oggetto ad una gerarchia di oggetti che rappresentano i vari stati. Si usa una gerarchia di stati, ed il comportamento di un oggetto può variare in base allo stato tramite un meccanismo di delega, invocando uno di questi stati. Gli stati delle persone spesso si chiamano ruoli, che possono cambiare, quando si modellano persone quindi si considerano gerarchie di ruoli. Per cambiare ruoli e stati quindi si creano nuovi oggetti ruoli per quell’oggetto, e si formano collegamenti, o si rompono collegamenti con oggetti ruoli.

Il pattern “State” permette di gestire situazioni complesse, ma non bisogna abusarlo, soprattutto nei casi semplici. Si potrebbe utilizzare mediante un attributo o come i ruoli di un’associazione. In questi casi i diversi stati di un oggetto non cambiano considerevolmente il comportamento di un oggetto, oppure non esiste un insieme finito di stati che un oggetto può assumere.

I ruoli si possono rappresentare come associazioni, un oggetto può assumere ruoli diversi in base a quale associazione lo collega ad un altro oggetto. L’alternativa migliore dipende dal dominio, si potrebbe infatti rappresentare come classi diverse, invece di associazioni diverse per uno stesso oggetto. Tra le due soluzioni non cambia il numero di associazioni, solamente viene sdoppiata la classe che prima rappresentava contemporaneamente entrambi i ruoli.

### Ereditarietà

Nel software si parla di ereditarietà invece di generalizzazione, nel software dipende dalle caratteristiche software, quindi i criteri di utilizzo sono diversi.

L’errore sul prezzo dei prodotti che cambia nel sistema POS, può essere risolvo anche considerando una classe che tiene conto dello storico dei prezzi, dove ogni istanza h aun prezzo ed un intervallo di validità. È utile quando si vuole conoscere tutta la variazione dei prezzi nel corso del tempo, anche se non sono state effettuate vendite a quel prezzo.

Esiste un modo per aggiungere attributi ad un’associazione, chiamato classi di associazioni, che non andranno usate. Anche se nella modellazione di dominio è comodo, nella classe software non c’è niente di equivalente, con un salto rappresentazionale alto, quindi utilizzando il principio del salto rappresentazionale basso è meglio utilizzare una classe normale.

Associazioni qualificate permettono di rappresentare insiemi come le mappe.

Nell’iterazione tre nel sistema monopoly si aggiungono le proprietà che un giocatore può comprare, come sottoclassi delle caselle. Questa è una superclasse dei vari tipi di proprietà. Si utilizza una sottoclasse di casella, come superclasse dei vari tipi di caselle proprietà, utilizzando inoltre un’associazione con il giocatore con partecipazione opzionale per indicare che possono avere un proprietario. Per le caselle proprietà si può utilizzare una gerarchia, motivata da un comportamento diverso. Per esempio una casella proprietà senza proprietario può essere acquistata, per un certo prezzo, questo è quindi irrilevante dal tipo, mentre per pagare l’affitto quando questa casella ha la proprietà, dipende dal tipo di proprietà su cui si trova. Tra queste cambia l’algoritmo per il calcolo dell’affitto.

### Altre Operazioni di Sistema

Anche a parità di casi d’uso, per gli esempi proposti precedentemente, è possibile determinare nuove operazioni di sistema, analizzando le estensioni dei casi d’uso già analizzati

Nel sistema POS si possono analizzare le estensioni per i pagamenti, trovando le operazioni di sistema per effettuare il pagamento con carta di credito o contanti. È necessario identificare queste operazioni di sistema, ma non è obbligatorio mostrarle per tutti gli scenari. Normalmente ci si concentra su quelli più complessi. Nel rappresentare queste operazioni di sistema è utile trovare le interazioni con sistemi esterni, tramite un’attività di analisi. Per esempio i sistemi di contabilità quando viene salvata una vendita.

Per l’operazione `makeCashPayment` bisogna modificare il contratto, poiché sono state introdotte nuove forme di pagamento e quindi una generalizzazione, dividendo il pagamento in contanti, con assegno e con carta di credito. Nei contratti si può dire che è stata creata un’istanza di pagamento carta di credito o in contanti, mai rispetto la classe astratta pagamento. Inoltre non si può dire che il tipo dell’oggetto è cambiato. Le post-condizioni rimangono delle tre forme introdotte, ed il tipo di pagamento creato dipende da quale operazione viene chiamata.

## Sistema Monopoly

Si trattano cambiamenti dei requisiti dalla terza iterazione, nella terza iterazione se un giocatore si muove su una casella proprietà, se non è di nessuno la può comprare, altrimenti deve pagare l’affitto, in base al tipo di casella proprietà. Non si considerano le case o alberghi, o la regola del monopolista, ovvero se un giocatore ha tutte le caselle di un colore raddoppia l’affitto.

Per la gestione di questi requisiti bisogna rappresentare la casella proprietà, ed i tre tipi di caselle proprietà, terreno, stazione o società. Bisogna determinare se aggiungere una nuova classe per rappresentarle. Una motivazione per l’introduzione di una sottoclasse è la presenza di proprietà strutturali di interesse, come il prezzo d’acquisto ed il proprietario. Vanno prese d’analisi anche le differenze comportamentali, causate al giocatore. Tra i vari tip i di caselle proprietà non ci sono proprietà strutturali di interesse, ma proprietà comportamentali diverse da rappresentare. Poiché queste tre caselle condividono le loro proprietà strutturali si possono mettere a fattore comune per introdurre una superclasse. Ogni casella proprietà può avere un proprietario. In generale poiché queste tre classi partizionano la classe proprietà, questa è una classe astratta.

È utile avere tutte quattro queste classi come classi software, mentre l’associazione tra il giocatore alla casella proprietà si rappresenta come due collegamenti, poiché un giocatore deve conoscere quali sono le sue proprietà per calcolare in base al loro valore l’affitto, mentre data una casella proprietà bisogna sapere il proprietario per sapere se può essere comprata o se il giocatore che ci cade deve pagare l’affitto.

Per rappresentare le nuove caselle non è detto che sia sufficiente modificare il metodo `landedOn`. Supponendo che sia sufficiente modificare questa operazione, bisogna capire se bisogna modificare il codice delle classi concrete o della classe astratta. Quando un giocatore cade su una casella proprietà, può comprarla, pagare l’affitto, o non fare niente, questi comportamenti non dipendono dal tipo, quindi non si usa il polimorfismo, si usano quindi istruzioni condizionali. Se la casella non è di nessun giocatore, la casella invoca il metodo `attemptPurchase` del giocatore che vi è caduto, altrimenti chiama il metodo `payRent` passando il riferimento al giocatore corrente. Per tentare di acquistare una casella bisogna controllare se il giocatore ha abbastanza soldi, altrimenti non può comprarla, ed in seguito ad una transazione con successo viene assegnato il proprietario a questa casella. Per pagare l’affitto bisogna prima calcolare l’affitto da pagare, ed in seguito ridurre i soldi del giocatore che vi è caduto, ed aumentare dello stesso importo la quantità di denaro del proprietario. Per calcolare l’affitto bisogna utilizzare il polimorfismo, poiché dipende dal tipo di casella proprietà. Se è un terreno dipende dal numero della casella, se è una stazione dipende dal numero di stazioni, e se è una casella società dipende dal risultato del lancio dei dadi.

## Raffinamento dell’Architettura

Nell’architettura a strati bisogna distinguere tra collaborazioni tra l’alto verso il basso, di tipo richiesta e risposta, e collaborazioni all’alto nella forma di notifica di eventi.

La collaborazione verso l’alto può essere realizzata tramite observer, con ascoltatori e publisher di eventi. Oppure possono utilizzare facade, ma solo nei casi più semplici, altrimenti rappresenterebbe un anti-pattern.

Repository ed Entity sono dei design pattern di DDD, per accedere a base di dati. Per ogni tipo di oggetto persistente che richiede un accesso globale si utilizza un oggetto che fornisce l’illusione di una collezione in memoria di tutti gli oggetti di quel tipo, fino ad ora si è progettato con questa modica in mente. L’accesso avviene mediante un’interfaccia, le classi che implementano questa interfaccia prima venivano chiamati *Data Access Object*.

Un’entità è un oggetto caratterizzato da una sua identità e continuità in un periodo di tempo lungo, è un tipo di oggetto di tipo persistente gestito da una repository. Oggetti persistenti non esistono nel software, quindi bisogna capire come rappresentarli come oggetti software. È presente un’associazione uno ad uno tra informazioni persistenti ed oggetti software. Il repository gestisce l’interazione tra le informazioni dell’entità e le sue varie istanze software, ha la responsabilità di gestire il ciclo di vita della sua entità.

Nello strato di dominio si crea un nuovo oggetto solo in corrispondenza dei contratti, se si accede ad oggetti presenti nel repository, questa istanza software viene creata dal repository stesso e non dallo strato di dominio, la repository cerca nella tabella le informazioni per l’oggetto da creare, quindi la sua rappresentazione concettuale, una volte ottenute queste informazioni crea l’oggetto software concreto e lo restituire a chi l’ha invocato. All’esterno della repository la creazione di un’istanza software avviene in corrispondenza della creazione concettuale delle istanza della classe.

Gli aggregati sono un insieme di oggetti che devono essere acceduti insieme. Un aggregato è un’insieme oggetti valore e di un’entità di esistenza indipendente.
