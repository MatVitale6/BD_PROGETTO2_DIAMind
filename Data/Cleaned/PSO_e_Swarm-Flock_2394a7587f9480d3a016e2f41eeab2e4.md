# PSO e Swarm-Flock

check: Yes

## Introduzione

Non tutti gli algoritmi di ottimizzazione si basano sulla biologia o sulla natura; molte tecniche sono sviluppate puramente sulla base di principi matematici e computazionali.

Le reti neurali sono ispirate alla struttura del cervello umano. Sono composte da unità di elaborazione chiamate neuroni che sono collegate tra loro in un pattern complesso. Questi neuroni lavorano insieme per apprendere dai dati e fare previsioni o decisioni.

## Particle Swarm Optimization

Il `PSO` è uno degli algoritmi bioispirati ed è un algoritmo semplice per la ricerca di una soluzione ottimale nello spazio delle soluzioni. Si basa su concetti tratti dall’osservazione del comportamento sociale di alcune specie animali, come i banchi di pesci o gli stormi di uccelli.

Si differenzia dagli altri algoritmi di ottimizzazione per il fatto che è necessaria solo la funzione obiettivo e non dipende dal gradiente o da qualsiasi forma differenziale dell’obiettivo. Inoltre ha pochissmi iperparametri. I sociobiologi ritengono che un banco di pesi o uno stormo di uccelli che si muovono in gruppo possano trarre profitto dall’esperienza di tutti gli altri membri.

Durante l’iterazione dell’algoritmo, le particelle aggiornano la loro velocità e posizione in base a 3 fattori principali:

- esperienza `personale`: la particella tiene traccia della migliore soluzione che ha incontrato finora.
- esperienza del `vicinato`: la particella è influenzata dalle migliori soluzioni incontrate dalle particelle del suo vicinato.
- `inerzia`: la particella mantiene parte dalla sua velocità precedente per mantenere la coerenza del movimento.

In sostanza l’aggiornamento della velocità e della posizione avviene iterativamente fino a raggiungere una condizione di terminazione. L’algoritmo sfrutta il concetto di collaborazione e condivisione di informazioni tra le particelle per guidare la ricerca dell’interno spazio delle soluzioni. Le equazioni di aggiornamento sono mostrati di seguito:

$$
x^{(i+1)}\gets x^{(i)}+v^{(i)} \\
v^{(i+1)}\gets wv^{(i)}+c_1r_1(
x^{(i)}_{best}-x^{(i)})+c_2r_2(x^{(i)}_{best}-x^{(i)})
$$

Dove $x^{(i)}_{best}$ è la miglior soluzione trovata fra tutte le particelle; $w$, $c_1$, $c_2$ sono parametri; $r_1$, $r_2$ sono numeri casuali estratti da $U(0, 1)$. Una strategia comune è permettere all’inerzia $w$ di decadere nel tempo.

Il parametro $w$ è chiamato costante d’inerzia compreso fra 0 ed 1 e determina quanto la particella dovrebbe continuare con la sua precedente velocità.

I parametri $c_1$ e $c_2$ sono chiamati rispettivamente coefficienti cognitivi e sociali. Questi controllano quanto peso dovrebbe essere dato nel bilanciare il miglioramento del risultati di ricerca della particella stessa e il riconoscimento del risultato di ricerca dello sciame.

Un valore alto di $w$ permette di avere maggiore capacità di ricerca `globale`, mentre un valore minore di $w$ permette di avere maggiore capacità di ricerca `locale`.

→ Questi parametri possono essere visti come controllo del compromesso tra esplorazione e sfruttamento

## Swarm-Flock