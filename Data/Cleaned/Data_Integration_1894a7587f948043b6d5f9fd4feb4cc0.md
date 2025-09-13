# Data Integration

Tags: Data Fusion, Record Linkage, Schema Alignment
.: No

L’obiettivo del `data-integration` è il processo di combinare dati provenienti da fonti diverse per creare una visione unificata e coerente. Questo concetto è fondamentale per le aziende che lavorano con grandi voluymi di dati provenienti da sistemi diversi, come database, applicazioni, file o servizi cloud.

Le sfide del `data-integration` sono:

- `semantic-ambiguity`: quando si integrano dati da diverse fonti è necessario che la stessa informazione concettuale può essere modellata in modi diversi e che informazioni concettualmente diverse possono essere modellate in modo simile.
- `instance representation ambiguity`: Le stesse entità possono essere rappresentate in modi differenti
- `data-inconsistency`: quando si combinano dati da diverse fonti bisogna affrontare ambiguità e incoerenze a livello di istanza, queste discrepanze devono essere risolte per creare un set di dati unico, pulito e coerente.

## Schema Alignment

Se si considera un insieme di schemi sorgente relativi allo stesso dominio, dove schemi diversi possono descrivere il dominio in modi differenti, il processo di `schema-alignment` produce 3 risultati principali:

- `Mediated Schema`: questo schema fornisce una visione unificata delle diverse fonti e cattura gli aspetti più rilevanti del dominio considerato. In pratica lo schema mediato funge da modello centrale che riunisce tutte le informazioni principali, risolvendo le differenze tra gli schemi sorgente.
- `Attribute Matching`:  si tratta di un’operazione che associa gli attributi di ciascun schema sorgente agli attributi corrispondenti nello schema mediato.
- `Schema Mapping`:  qeusto processo specifica le relazioni semantiche tra il contenuto di ciascun schema sorgente e lo schema mediato. Queste mappature sono poi utilizzate per riformulare le query dell’utente.

Questo step è complesso per molte ragioni, perchè fonti diverse possono descrivere lo stesso dominio utilizzando schemi molto differenti rendendo difficile creare una visione unificata dei dati. Altri problemi sono che gli stessi concetti possono essere rappresentati con nomi diversi oppure lo stesso nome di un attributo può avere significati diversi a seconda del contesto.

## Record Linkage

Il `record-linkage` affonta il problema dell’ambiguità nella rappresentazione delle istanze e ha l’obiettivo di capire quali record rappresentano la stessa entità e distinguere quali record rappresentano entità diverse.

- `Blocking`: il matching e il clustering garantiscono la correttezza del record linkage ma possono essere molto inefficienti specialmente su grandi quantità di dati. Per rendere il processo computazionalmente fattibile si utilizza il `blocking` per rendere il record linkage più efficiente su grandi dataset. Si applica una funzione di blocking su uno o più attributi dei record, questa funzione suddivide i record in blocchi più piccoli, il matching a coppie viene eseguito solo tra record all’interno dello stesso blocco, riducendo il numero totale di confronti.
    
    Si utilizzano funzioni di blocking per evitare che alcuni record possano non essere inseriti nello stesso blocco, causando falsi negativi. Questo crea blocchi sovrapposti, aumentando la probabilità di trovare corrispondenze senza aumentare troppo i costi computazionali. L’obiettivo quindi è bilanciare il `recall` con il numero di confronti necessari.
    
- `Pairwise Matching`: è il confronto tra una coppia di record per valutare se corrispondono, ovvero se riferiscono alla stessa entità. Ci sono diversi diversi approcci per effettuare questo confronto:
    - `rule-based`: utilizzato nella pratica e si basa sulla conoscenza del dominio, si potrebbero definire regole come: se nome e data di nascita coincidono allora è lo stesso individuo
    - `classification-based`: si basa su dati di addestramento per costruire un modello che decide se 2 record corrispondono o meno, per esempio utilizzando il machine learning
    - `distance-based`: applica metriche di distanza per calcolare quanto siano diversi i valori degli attributi corrispondenti
- `Clustering`: Le decisioni locali di match o non match prese nel confronto tra le coppie di record possono non essere globalmente coerenti, per risolvere queste incoerenze si usa un passaggio di clustering che rende le decisioni di matching globalmente coerenti, raggruppa i record in partizioni dove ogni partizione rappresenta una singola entità garantendo che record diversi finiscano in partizioni separate.

## Data Fusion

Il `data-fusion` affronta il problema della qualità dei dati e ha l’obiettivo di determinare quale valore utilizzare nei dati integrati quando le diverse fonti forniscono valori in conflitto.