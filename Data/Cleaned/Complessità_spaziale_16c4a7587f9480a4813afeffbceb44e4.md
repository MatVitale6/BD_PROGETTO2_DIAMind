# Complessità spaziale

Argomenti: Teorema di Savitch
.: No

## Tempo di computazione

- `lemma`: se una MT decide un linguaggio usando spazio $s(n)$, con $s(n)\ge n$, allora le sue computazioni terminano in tempo $2^{O(s(n))}$
- `dimostrazione`: si considera il comportamento della MT $M$ sulla stringa $x$ con $|x|=n$. Siano $c_1,c_2,..,c_t$ le configurazioni attraversate da $M$, con $c_i$ configurazione al tempo $i$ e $t$ tempo di calcolo di $M$ su $x$.

Nella sequenza di $c_1,c_2,..,c_t$ non possono esserci due $c_i$ uguali altrimenti $M$ ciclerebbe. Il numero di possibili configurazioni attraversate è quindi al più il prodotto tra: il numero di stati, il numero di possibili posizioni della testina sul nastro, il numero di possibili contenuti delle celle.

$$
O(1)\cdot s(n)\cdot |\Sigma|^{s(n)}=2^{O(s(n)+log(s(n)))}=2^{O(s(n))}
$$

Dato che $M$ non può passare per una configurazione 2 volte durante la computazione, la computazione deve finire in $2^{O(s(n))}$ passi.

---

## $\text{SAT}\in \text{DSPACE(n)}$

- `teorema`: $SAT$ appartiene a $\text{DSPACE(n)}$
- `dimostrazione`: sia $n$ la lunghezza dell’input, le variabili sono quindi al più $n$

Si genera sul nastro, in interazioni successive, tutte le possibili assegnazioni vero/falso delle variabili. in ogni iterazione si valuta se la formula è vera e si cancella sul nastro, per riusarlo nell’iterazione successiva. L’unica informazione da mantenere sul nastro è il valore corrente vero/falso delle variabili.

---

## Relazioni elementari tra classi di complessità

- `teorema`: per ogni $f:N\to N$ con $f(n)\ge n$:
    
    $$
    \text{DTIME(f(n))}\subseteq \text{NTIME(f(n))} \\
    DSPACE(f(n))\subseteq NSPACE(f(n))
    $$
    
    - `dimostrazione`: una $\text{MT}$ è una $\text{MTND}$
- `teorema`: per ogni $f:N\to N$ con $f(n)\ge n$:
    
    $$
    \text{DTIME(f(n))}\subseteq \text{DSPACE(f(n))} \\
    NTIME(f(n))\subseteq NSPACE(f(n))
    $$
    
    - in $t$ passi di computazione una $MT$ può usare al più $t$ celle di nastro

---

## Tempo e spazio deterministici

- `lemma`: se una $MT$ decide un linguaggio usando spazio $s(n)$, con $s(n)\ge n$, allora le sue computazioni terminano in tempo $2^{O(s(n))}$
- `dimostrazione`: si considera il comportamento della $MT$ $M$ sulla stringa $x$ con$|x|=n$, siano $c_1, c_2,...,c_t$ le configurazioni attraversate da $M$ con $c_i$ configurazione al tempo $i$ e $t$ tempo di calcolo di $M$ su $x$. Nella sequenza $c_1,c_2,...,c_t$ non possono esserci 2 $c_i$ uguali, altrimenti $M$ ciclerebbe.

Il numero di possibili configurazioni attraversate è quindi al più il prodotto tra: il numero di stati, il numero di possibili posizioni della testina sul nastro, il numero di possibili contenuti delle celle.

- Tale numero è: $O(1)\cdot s(n)\cdot |\Sigma|^{s(n)}=2^{O(s(n))+log(s(n))}=2^{O(s(n))}$
- infatti: $O(1)\cdot s(n)=O(s(n))=2^{log(O(s(n)))}=2^{O(log(s(n)))}$
- inoltre per una qualche costante $p$, $|\Sigma|=2^P$, quindi $|\Sigma|^{(s(n))}=2^{p\cdot s(n)}=2^{O(s(n))}$

Dato che $M$ non può passare per una configurazione 2 volte durante la computazione, la computazione deve finire in $2^{O(s(n))}$ passi.

---

## Teorema di Savitch

- `teorema`: per ogni $s:N\to N$  con $s(n)\ge n$, si ha:
    
    $$
    NSPACE(s(n))\subseteq DSPACE(s^2(n))
    $$
    
- `dimostrazione`: si simula deterministicamente la MTND che usa spazio $s(n)$. Si studia lo yieldability problem.

Siano 2 configurazioni $c_1$ e $c_2$ di una MTND $N$ ed un numero $T$, si vuole verificare se $N$ può raggiungere $c_2$ da $c_1$ in al più $T$ passi. Lo yieldability problem può essere risolto da una MT deterministica. Cioè si prova con ogni configurazione intermedia $c_m$ e si verifica ricorsivamente se da $c_1$ si può raggiungere $c_m$ e da $c_m$ si può raggiungere $c_2$, in entrambi i casi con al più $T/2$ passi, dove il secondo test può riusare lo spazio del primo.

Ogni livello della ricorsione richiede spazio $O(s(n))$ per memorizzare la configurazione. La profondità della ricorsione è $log(T)$ dove $T$ è il tempo impiegato dalla computazione più profonda della MTND. SI ha che $T=2^{O(s(n))}$ da cui $log(T)=O(s(n))$, si ha quindi che la computazione deterministica usa spazio $O(s^2(n))$.