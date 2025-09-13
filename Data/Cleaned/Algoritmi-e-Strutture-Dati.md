---
author:
- "*Giacomo Sturm*"
date: |
  *Dipartimento di Ingegneria Civile, Informatica e delle Tecnologie Aeronautiche  
  Università degli Studi “Roma Tre"*
title: |
  **Algoritmi e Strutture di Dati**  
  Appunti delle Lezioni di Algoritmi e Strutture di Dati  
  *Anno Accademico: 2023/24*
---

\providecommand{\labelText}[2]{#1}

# Algoritmi

Un algoritmo viene definito come una serie di istruzioni eseguibili da una Random Access Machine, che, da un’insieme di input, produce un insieme di output. Un algoritmo è corretto, se la sua esecuzione termina, e restituisce un insieme di output corretto, ovvero una soluzione ad un problema computazionale. Una Random Access Machine è un modello astratto di un calcolatore, più semplice del modello di un computer ideato da John von Neumann. In questa macchina è presente un programma, ed è in grado di accedere ad una memoria composta da registri ad indirizzamento casuale (Random Access Memory), gli insieme di input e di output vengono forniti come sequenze di dati, ed ogni operazione del programma viene eseguita dalla macchina sequenzialmente, a costo unitario, costante.

Questo modello ideale non rappresenta calcolatori reali, poiché non pone limitazioni sulle  
grandezze in ingresso o in uscita, inoltre può modellare solo macchine mono-processori. Inoltre l’implementazione di algoritmi in linguaggio macchina, eseguibili dalla RAM, non è un’operazione efficiente. Per cui è utile fornire un’altra definizione di algoritmo, rispetto alla codifica in pseudocodice. Un algoritmo rappresenta una procedura di calcolo, esprimibile come in pseudocodice, che, da un’insieme di input, produce in insieme di output. Questa definizione è equivalente alla definizione tramite una Random Access Machine, e fornisce molti più vantaggi, poiché lo pseudocodice è un linguaggio di facile implementazione. Non rappresenta un linguaggio di programmazione, ma un intermedio tra il linguaggio naturale ed un linguaggio di programmazione, per poter definire le operazioni di un algoritmo. I dati su cui opera lo pseudocodice vengono salvati in oggetti ed array, il modo in cui si organizzano i dati in memoria rappresentano strutture di dati, usate per rendere più efficiente l’elaborazione dei dati salvati.

## Pseudocodifica

Lo pseudocodice rappresenta un linguaggio semplice, non deve essere compilato, o eseguito da alcuna macchina, per cui il suo unico scopo è avere una semantica comprensibile. Poiché rappresenta un linguaggio semplice, il tipo delle variabili rimane costante, e non è supportata l’algebra sui puntatori. Si possono effettuare una serie di operazioni elementari come l’assegnazione, ad una variabile, del valore di un’espressione:

``` c
    var = exp
```

La variabile `var` da inizializzare si trova sempre alla sinistra, mentre il valore o l’espressione `exp` da assegnare si trova sempre alla destra dell’operatore `=`.

É possibile utilizzare istruzioni condizionali del tipo `if-then-else`, anche se viene spesso omesso `then`:

``` c
    if condizione_1
        istruzione_1
    else
        istruzione_2
```

Inoltre è possibile concatenare più istruzioni condizionali:

``` c
    if condizione_1
        istruzione_1
    else if condizione_2
        istruzione_2
    //...
    else 
        istruzione_default
```

Sono possibili istruzioni ripetitive utilizzando `for-to`, `while-do ` e `repeat-until`:

``` c
    // istruzione for
    for i = var_1 to val_1
        istruzione_1
    
    // istruzione while
    while condizione_2 do
        istruzione_2
    
    // istruzione repeat
    repeat
        istruzione_3
    until condizione_3
```

Si possono definire oggetti, formati da variabili di tipi diversi, chiamati campi, accessibili usando l’operatore (`.`):

``` c
    // obj: un oggetto che presenta due attributi campo_1 e campo_2
    // si assegna al primo attributo dell'oggetto il valore della variabile var_1
    obj.campo_1 = var_1 
    
    // si assegna al secondo attributo dell'oggetto il valore della variabile var_2
    obj.campo_2 = var_2 
```

Una variabile che rappresenta un oggetto, `obj` nel caso precedente, viene trattata come un puntatore o riferimento all’oggetto. Si usa la costante `NULL ` per porre a zero un riferimento.

Si indica un array come `A`, un oggetto formato da un campo `A.length` che indica la lunghezza dell’array, ed un array di lunghezza `A.length`, ovvero va dall’indice `i = 0` fino all’indice  
`i = A.length-1`:

``` c
    len_A = A.length // lunghezza dell'array 
    var_i = A[i]     // si accede all'elemento i-esimo del'array 
```

Non sono presenti definizioni di tipo, per cui vengono usati commenti per indicare il tipo delle variabili; inoltre si suppone siano allocate in memoria nel momento della loro dichiarazione. Le variabili sono sempre interne alla procedura dove sono state dichiarate. Una singola procedura può non restituire alcun valore, ma quando restituisce un valore, ne può restituire solo uno, e deve sempre restituirne uno. Quando vengono passati parametri tra procedure, vengono passati per valore, in caso siano variabili, mentre viene passato il riferimento ad un oggetto, invece di riprodurre l’intero oggetto nella procedura di arrivo.

Il passaggio dallo pseudocodice ad un linguaggio di programmazione, in grado di eseguire il programma si chiama implementazione.

## Notazione Asintotica

Per analizzare l’evoluzione di una funzione, è utile rappresentare i limiti di questo andamento per valori sempre più grandi. Quest’analisi può fornire limiti superiori ed inferiori della funzione analizzata. Questi limiti si ottengono comparando la funzione analizzata con funzioni di andamento noto, per restringere l’intorno di evoluzione della funzione analizzata.

Si considerano per facilità funzioni nel domino dei naturali, facilmente estendibili sui reali.

Si definisce l’insieme delle funzioni limitate superiormente da $g(n)$, l’insieme contenente tutte le funzioni, dopo un valore note $n_0$, sono sempre minori o uguali alla funzione $g(n)$ scalata di un fattore $c$: $$O(g(n)):=\left\{f(n):\exists c,n_0\in\mathbb{N}\mbox{ t.c. }\forall n\geq n_0 \implies 0\leq  f(n)\leq c\cdot g(n)\right\}$$ Ogni funzione contenuta nell’insieme, presenta delle costanti $c,n_0$ specifiche. Le operazioni di scala $c$ non influenzano l’andamento asintotico della funzione $g(n)$, per cui è legittimo considerare la costante di scala $c$, nella comparazione tra la funzioni analizzate. Questo può essere effettuato solamente se si sta attuando una trattazione asintotica delle funzioni. Per cui la funzione $g(n)$ appartiene all’insieme delle funzioni limitate superiormente da $g(n)$: $$g(n)\leq c\cdot g(n)\land c\geq 1\implies g(n)\in O(g(n))$$ Per cui vale la proprietà riflessiva.

L’insieme è vuoto, se la funzione di comparazione $g(n)$ è negativa: $$O=\emptyset\iff g(n)<0$$

Si dimostra che un polinomio di grado $k$, appartiene all’insieme $O(n^k)$: $$\begin{gathered}
    c_1n^k-c_2n^{k-1},\;\;c_1,c_2>0
\end{gathered}$$ Si dimostra che esistono due costanti $c$ e $n_0$, tali che: $$\begin{gathered}
    0\leq c_1n^k-c_2n^{k-1}\leq cn^k\\
    0\leq c_1-\displaystyle\frac{c_2}{n}\leq c
\end{gathered}$$ Si pone $c=c_1$: $$\begin{gathered}
    c_1-\displaystyle\frac{c_2}{n}\leq c\,\mbox{per }n\geq0\\
    0\leq c_1-\displaystyle\frac{c_2}{n}\,\mbox{per }n\geq\frac{c_2}{c_1}
\end{gathered}$$ Per cui la costanti $c=c_1$ e $n=c_2/c_1$ verificano quest’ipotesi.

Si dimostra che vale la proprietà transitiva. Per ipotesi: $$\begin{gathered}
    f(n)\in O(h(n))\\
    h(n)\in O(g(n))
\end{gathered}$$ Esprimendole tramite la definizione: $$\begin{gathered}
    \exists c',n_0'>0\mbox{ t.c. }\forall n\geq n'_0,\,0\leq f(n)\leq c'\cdot h(n)\\
    \exists c'',n_0''>0\mbox{ t.c. }\forall n\geq n''_0,\,0\leq h(n)\leq c''\cdot g(n)
\end{gathered}$$ Combinandole si ottiene: $$\begin{gathered}
    0\leq f(n)\leq c'\cdot c'' g(n)
\end{gathered}$$ Per cui: $$\begin{gathered}
    \exists c'''=c'\cdot c''\land \exists n'''_0=\mbox{max}(n'_0,n''_0)\mbox{ t.c. }\forall n\geq n'''_0, \, 0\leq f(n)\leq c'''\cdot g(n)
\end{gathered}$$

Si dimostra la regola dei fattori costanti positivi. Se $d>0$: $$\begin{gathered}
    f(n)\in O(g(n))\iff d\cdot f(n)\in O(g(n))\\
    \exists c,n_0>0\mbox{ t.c. }\forall n\geq n_0,\,0\leq f(n)\leq c\cdot g(n)\\
    c'=c\cdot d\\
    \exists c',n_0>0\mbox{ t.c. }\forall n\geq n_0,\,0\leq f(n)\leq c'/d\cdot g(n)\\
    0\leq d\cdot f(n)\leq c'\cdot g(n)
\end{gathered}$$

Si dimostra la regola sella somma. $$\begin{gathered}
    h(n)\in O(g(n))\land\; k(n)\in O(g(n))\implies h(n)+k(n)\in O(g(n))\\
    \exists c',n_0'>0\mbox{ t.c. }\forall n\geq n'_0,\,0\leq h(n)\leq c'\cdot g(n)\\
    \exists c'',n_0''>0\mbox{ t.c. }\forall n\geq n''_0,\,0\leq k(n)\leq c''\cdot g(n)\\
    0\leq h(n)+k(n)\leq c'\cdot g(n)+c''\cdot g(n)\\
    \exists c'''=c'+ c''\land \exists n'''_0=\mbox{max}(n'_0,n''_0)\mbox{ t.c. }\forall n\geq n'''_0, \, 0\leq h(n)+k(n)\leq c'''\cdot g(n)
\end{gathered}$$

Si definisce l’insieme $\Omega$ delle funzioni limitate inferiormente da $g(n)$, l’insieme di tutte le funzioni scalate di un fattore $c$, sempre maggiori o uguali alla funzione $g$ dopo un valore $n_0$: $$\Omega(g(n)):=\{f(n):\exists c,n_0>0\mbox{ t.c. }\forall n\geq n_0\implies 0\leq c\cdot g(n)\leq f(n)\}$$

Per l’insieme $\Omega$ risulta questa proprietà: $$\begin{gathered}
    f(n)\in\Omega(g(n))\iff g(n)\in\Omega(f(n))\\
    \exists c',n_0'>0\mbox{ t.c. }\forall n\geq n'_0,\,0\leq c'\cdot g(n)\leq f(n)\\
    \exists c'',n_0''>0\mbox{ t.c. }\forall n\geq n''_0,\,0\leq c''\cdot f(n)\leq  g(n)\\
    c'\cdot c''\cdot f(n)\leq c'\cdot g(n)\leq f(n)\land c'\cdot c''\cdot g(n)\leq c''\cdot f(n)\leq g(n) 
\end{gathered}$$

I valori costanti $c$ positivi sono spesso minori di $1$, non necessariamente rappresentano un numero intero. Per cui si può esprimere la condizione di appartenenza ad uno di questi insiemi $f(n)\in\Omega(g(n))$ come: $$0\leq g(n)\leq c\cdot f(n)$$

Per questo insieme vale la proprietà riflessiva: $$\begin{gathered}
    c\cdot g(n)\leq  g(n)\land 0\leq c\leq 1\implies g(n)\in \Omega(g(n))
\end{gathered}$$

Per questo insieme valgono le proprietà analoghe all’insieme $O$. Vale la proprietà transitiva: $$\begin{gathered}
    f(n)\in \Omega(h(n))\\
    h(n)\in \Omega(g(n))\\
    \exists c',n_0'>0\mbox{ t.c. }\forall n\geq n'_0,\,0\leq  c'\cdot h(n)\leq f(n)\\
    \exists c'',n_0''>0\mbox{ t.c. }\forall n\geq n''_0,\,0\leq c''\cdot g(n)\leq  h(n)\\
    0\leq c'\cdot c''\cdot g(n)\leq f(n)\\
    \exists c'''=c'\cdot c'',n'''_0=\mbox{max}(n'_0,n''_0)>0\mbox{ t.c. }\forall n\geq n'''_0\,0\leq c'''\cdot g(n)\leq f(n)\\
    f(n)\in\Omega(g(n))
\end{gathered}$$ Vale la regola dei fattori costanti positivi: $$\begin{gathered}
    f(n)\in \Omega(g(n))\iff d\cdot f(n)\in \Omega(g(n))\\
    \exists c,n_0>0\mbox{ t.c. }\forall n\geq n_0,\,0\leq c\cdot g(n)\leq f(n)\\
    c'=c\cdot d\\
    \exists c',n_0>0\mbox{ t.c. }\forall n\geq n_0,\,0\leq c'/d\cdot g(n)\leq f(n) \\
    0\leq  c'\cdot g(n)\leq d\cdot f(n)\\
    d\cdot f(n)\in\Omega(g(n))
\end{gathered}$$ Vale la regola della somma: $$\begin{gathered}
    h(n)\in\Omega(g(n))\land\; k(n)\in\Omega(g(n))\implies h(n)+k(n)\in\Omega(g(n))\\
    \exists c',n_0'>0\mbox{ t.c. }\forall n\geq n'_0,\,0\leq  c'\cdot g(n)\leq h(n)\\
    \exists c'',n_0''>0\mbox{ t.c. }\forall n\geq n''_0,\,0\leq  c''\cdot g(n)\leq k(n)\\
    0\leq c'\cdot g(n)+c''\cdot g(n)\leq h(n)+k(n)\\
    \exists c'''=c'+ c''\land \exists n'''_0=\mbox{max}(n'_0,n''_0)\mbox{ t.c. }\forall n\geq n'''_0, \, 0\leq c'''\cdot g(n)\leq  h(n)+k(n)
\end{gathered}$$

Per entrambi gli insiemi $O$ e $\Omega$ esistono delle funzioni incommensurabili tra di loro, ovvero funzioni che non possono essere comparate tra di loro: $$\begin{gathered}
    f(n)\notin O/\Omega(g(n))\\
    g(n)\notin O/\Omega(f(n))
\end{gathered}$$

Si definisce l’insieme $\Theta$ delle funzioni limitate superiormente ed inferiormente da $g(n)$: $$\Theta(g(n)):=\{f(n):\exists c_1,c_2,n_0>0\mbox{ t.c. }\forall n\geq n_0\implies 0\leq c_1\cdot g(n)\leq f(n)\leq c_2\cdot g(n)\}$$ Da questa definizione è immediatamente deducibile che se una funzione appartiene a questo insieme, appartiene automaticamente all’insieme $O(g(n))$ e $\Omega(g(n))$: $$\begin{gathered}
    f(n)\in\Theta(g(n))\implies\begin{cases}
        f(n)\in O(g(n))\\
        f(n)\in\Omega(g(n))
    \end{cases}
\end{gathered}$$

Vale la proprietà riflessiva: $$\begin{gathered}
   \exists c',c''>0\mbox{ t.c. } c'\cdot g(n)\leq g(n)\leq c''\cdot g(n)\implies g(n)\in\Theta(g(n))
\end{gathered}$$ Inoltre per questo insieme valgono tutte le proprietà precedentemente analizzate per $O$ e $\Omega$.

## Complessità

Esistono molti algoritmi diversi per risolvere lo stesso problema computazionale. Per verificare quale di questi sia migliore rispetto agli altri, si definiscono grandezze che quantificano l’efficienza di un dato algoritmo. Ogni programma ha un costo associato alla sua esecuzione, questo costo può essere dovuto alla memoria necessaria per eseguirlo, il tempo che impiega la sua esecuzione, il traffico generato sulla rete, etc. Generalmente il tempo di calcolo di un programma rappresenta la sua caratteristica più importante. In generale il tempo di calcolo cresce all’aumentare del numero di input $n$, per cui si può misurare come una funzione dell’input in ingresso $T(n)$.

Il tempo di calcolo di un programma dipende per la maggior parte dall’algoritmo implementato, e di meno da altri fattori come l’hardware, il compilatore o il linguaggio utilizzato per implementarlo. Per cui si tende ad analizzare solamente il tempo rispetto all’algoritmo utilizzato. Poiché il costo di un programma dipende dal tempo di calcolo dell’algoritmo che utilizza, bisogna analizzare il suo comportamento a priori, senza eseguire il programma, per fornire una previsione del suo tempo di calcolo.

In generale il tempo di calcolo non è una funzione $T(n)$, poiché ad ogni esecuzione il tempo impiegato da un programma potrebbe variare dal valore fornito da questa funzione. Per cui si analizza asintoticamente il caso peggiore, il caso migliore, ed il caso medio, dell’esecuzione di un dato algoritmo. In generale si studia solamente il caso peggiore, poiché il caso medio è più vicino al caso peggiore, il caso migliore non garantisce un comportamento per un caso generico e il tempo di esecuzione nel caso medio è rilevante solamente se esegue lo stesso programma un numero elevato di volte. In generale si è definita ogni operazione dello pseudocodice a costo unitario, per cui il tempo di esecuzione di un algoritmo è direttamente proporzionale al numero di operazioni eseguite. Si può calcolare direttamente dallo pseudocodice, ed in seguito si analizza il suo comportamento asintotico. Altrimenti è più efficiente calcolare il comportamento asintotico di parti delle pseudocodice separatamente, per poi combinarle ed analizzare il comportamento asintotico di $T(n)$, senza analizzare esplicitamente il comportamento di $T(n)$.

Dato un algoritmo $A$ avente tempo di esecuzione nel caso peggiore $T(n)$, si dice che per un input di dimensione $n$ l’algoritmo ha complessità temporale $O(f(n))$ se: $$T(n)\in O(f(n))$$

Per cui al massimo il tempo di esecuzione dell’algoritmo $A$ è $f(n)$, rappresenta il tempo sufficiente all’esecuzione del dato algoritmo. Per le proprietà della notazione asintotica, ha complessità $g(n)$, per ogni funzione $g(n)$, tale che $f(n)\in O(g(n))$. Più la condizione è stringente più la complessità espressa dalla notazione $O(f(n))$ è significativa.

Analogamente può essere definito un limite inferiore per il tempo di esecuzione di un programma, corrispondente al tempo necessario per la sua esecuzione, in caso la funzione $T(n)$ sia tale che: $$T(n)\in \Omega(f(n))$$

Per cui se la funzione tempo di esecuzione al caso peggiore $T(n)$ è tale che: $$T(n)\in \Theta(f(n))$$ Allora $f(n)$ rappresenta il tempo necessario e sufficiente all’esecuzione dell’algoritmo.

Per la regola della somma, si può analizzare ogni sezione dello pseudocodice separatamente, sommando in seguito i loro comportamenti asintotici. Per cui è più efficiente sommare direttamente il costo asintotico di ogni riga dello pseudocodice.

Istruzioni semplici e sequenze finite di istruzioni semplici hanno costo costante: $$\Theta(1)$$ Sequenze di istruzioni non semplici ha costo pari alla somma del costo delle singole istruzioni.

Per un’istruzione condizionale si calcola separatamente $O$ e $\Omega$, poiché bisogna sapere se la condizione è stata verificata:

``` c
    if condizione_1
        istruzione_1
    else
        istruzione_2
```

Il limite superiore del tempo di esecuzione di una istruzione condizionale è dato dalla somma dal limite superiore del tempo di esecuzione della valutazione di `condizione_1` e il limite maggiore tra i tempi di esecuzione di `istruzione_1` e `istruzione_2`. Analogamente il limite inferiore si calcola come la somma tra il limite superiore del tempo di esecuzione di `condizione_1` ed il limite minore tra i limiti inferiori di `istruzione_1` e `istruzione_2`.

Per operazioni iterative bisogna calcolare il limite al numero di operazioni nel ciclo $\Theta(g(n))$, ed il limite al costo di ciascuna operazione ripetuta $\Theta(f(n))$. Per cui il costo complessivo di un’operazione iterativa è data da: $$\Theta(g(n))\cdot\Theta(f(n))=\Theta(g(n)\cdot f(n))$$

Quando viene chiamata una procedura, bisogna prima calcolare il tempo $T(n)$ della procedura chiamata, ed in seguito esprimerlo rispetto alla dimensione dell’insieme passato alla procedura $m$: $T(m)$, ed esprimere la sua relazione rispetto alla dimensione dell’input della procedura iniziale $n$.

Questo modello non rappresenta un analisi completa di ogni possibile algoritmo, poiché per tutti il linguaggi dove è presente un valore limite per i tipi, in caso gli input assumano valore maggiore, il tempo di esecuzione dipende anche da come vengono gestiti questi valori. Per cui è possibile che la dimensione dei singoli valori di input influenzi il costo delle operazioni. Inoltre è possibile esprimere l’input di una procedura rispetto al numero di bit che necessita, rappresentando quindi un andamento esponenziale: $$\begin{gathered}
    k=\lceil \log_2n\rceil\\
    \Theta(n)=\Theta\left(2^k\right)
\end{gathered}$$

In caso l’input sia di piccole dimensioni, il comportamento fornito dall’analisi asintotica potrebbe non coincidere al comportamento reale dell’algoritmo. Per cui non è possibile stabilire quale algoritmo sia più efficiente per dimensioni di input piccole sulla base di un’analisi asintotica.

Quest’analisi inoltre ignore l’effetto delle costanti moltiplicative, potrebbero essere sufficientemente elevate per cui anche un’operazione analizzata come a tempo costante $\Theta(1)$, potrebbe richiedere un tempo molto elevato per essere eseguita.

### Teorema dell’Esperto

Quando si implementa un’algoritmo tramite ricorsione, per determinare il tempo impiegato dall’esecuzione, bisogna distinguere due casi, il tempo di esecuzione del caso base, ed il tempo di esecuzione del caso induttivo: $$T(n)=\begin{cases}
        af(n) &0\leq n<n_0\\
        bT(g(n))+h(n)&n\geq n_0
    \end{cases}$$ Questo tipo di espressione vengono chiamate formule di ricorrenza, e non presentano sempre una soluzione semplice. Trattando complessità asintotiche, spesso i casi base vengono omessi.

Spesso quando si ha un insieme di input di dimensione piccola, la complessità è sempre costante $\Theta(1)$. Si considera la seguente equazione di ricorrenza: $$T(n)=\begin{cases}
        a&n=0\\
        T(n-1)+g(n)&n\geq0
    \end{cases}$$

Si dimostra per induzione che ammette come soluzione la seguente espressione: $$\begin{gathered}
    T(n)=a+\displaystyle\sum_{k=1}^ng(k)\tag{\stepcounter{equation}\theequation}\\
    T(0)=a+\displaystyle\cancelto{0}{\sum_{k=1}^0g(k)}=a\\
    T(n)=T(n-1)+g(n)=a+\displaystyle\sum_{k=1}^{n-1}g(k)+g(n)=a+\displaystyle\sum_{k=1}^ng(k)
\end{gathered}$$

Data una formula di ricorrenza: $$T(n)=\begin{cases}
        \Theta(1)&n=0\\
        a\cdot T\left(\displaystyle\frac{\strut{n}}{\strut{b}}\right)+\Theta(n^k)&n>0
    \end{cases}$$

$b$ rappresenta il numero di suddivisioni effettuate all’insieme di input ad ogni ricorsione. Per cui ad un passo ricorsivo $i$-esimo, la dimensione dell’insieme di input è stata ridotta fino a $n\cdot b^{-i}$ per ogni chiamata ricorsiva dello stesso livello. Mentre $a$ rappresenta quante chiamate vengono effettuate ad ogni passaggio ricorsivo. Per cui ad un passo $i$-esimo sono presenti $a^i$ chiamate della funzione per quel livello. Si può comporre così un albero delle chiamate ricorsive, di altezza $h=\log_bn$, ovvero le suddivisioni necessarie affinché la dimensione dell’input diventi $1$, dove ogni livello presenta $a^i$ nodi, ed un costo complessivo pari a $a^i\cdot n^k\cdot b^{-i\cdot k}$. Si sommano i costi per ogni livello e si ottiene la seguente espressione: $$\begin{gathered}
    T(n)=\displaystyle\sum_{i=0}^ha^i\left(\frac{n}{b^i}\right)^k=\sum_{i=0}^ha^i\frac{n^k}{b^{ik}}=n^k\sum_{i=0}^h\left(\frac{a}{b^k}\right)^i
\end{gathered}$$

La sommatoria rappresenta una serie geometrica di ragione $\rho=a\cdot b^{-k}$, se avesse una ragione minore di uno, allora convergerebbe ad un valore costante: $$\begin{gathered}
    \rho<1\to a<b^k\\
    T(n)=\displaystyle n^k\sum_{i=0}^h\rho^i=n^k\frac{1}{1-\rho}\in\Theta\left(n^k\right)
\end{gathered}$$

Per $a=b^k$, la complessità è uguale ad ogni livello, allora ha una ragione costante $\rho=1$: $$\begin{gathered}
    \rho=1\to a=b^k\\
    T(n)=\displaystyle n^k\sum_{i=0}^h1=n^k\cdot h=n^k\cdot\log_nb\in\Theta(n^k\cdot\log_nb)
\end{gathered}$$

Se avesse una ragione maggiore di uno, allora si avrebbe: $$\begin{gathered}
    \rho>1\to a>b^k\\
    T(n)=\displaystyle n^k\sum_{i=0}^h\rho^i=n^k\frac{\rho^h-1}{\rho-1}\in\Theta(n^k\cdot\rho^h)\\
    n^k\cdot\rho^h=\displaystyle n^k\frac{a^{\log_b n}}{b^{k\log_bn}}=\frac{n^k}{n^k}a^{\log_bn}\\
    T(n)=\Theta(a^{\log_bn})=\Theta(n^{\log_ba})
\end{gathered}$$

Quindi, per $a$ e $b$ strettamente maggiori di zero $a,b\geq1$, il teorema dell’esperto afferma che la soluzione di questa formula di ricorrenza è data da: $$T(n)=\begin{cases}
        \Theta(n^k)&a<b^k\\
        \Theta(n^k\cdot\log n)&a=b^k\\
        \Theta(n^{\log_ba})&a>b^k
    \end{cases}$$

### Complessità Intrinseca

# Problema dell’Ordinamento

Il problema dell’ordinamento costituisce un problema molto comune, dove una sequenza di valori in input deve essere permutata in modo tale che gli elementi rispettano una certa relazione d’ordine nella sequenza di output. In generale il problema dell’ordinamento si affronta su sequenze di numeri, in particolare interi, dove la relazione d’ordine rappresenta l’operatore minore-uguale $\leq$: $$\begin{gathered}
    (a_1,\cdots,a_n)\to(b_1,\cdots,b_n)\mbox{ t.c. }:b_1\leq b_2\leq\cdots\leq b_n
\end{gathered}$$

In generale la sequenza viene fornita come un array `A` con $n$ posti. Ma è possibile utilizzare una lista per memorizzare la stessa sequenza. Gli algoritmi d’ordinamento si possono dividere in due tipi, algoritmi di tipo *greedy* ed *incrementali*:

- La tecnica *greedy* consiste nell’eseguire sempre una scelta localmente ottima, ma ciò non comporta che sia anche globalmente ottima.

- Nella tecnica *incrementale*, la soluzione di un’istanza di dimensione minore, è utile per risolvere un’istanza di dimensione superiore.

Si definisce un algoritmo *in loco*, quando utilizza solamente la struttura dati dell’input per effettuare l’ordinamento, ovvero non salva i dati su strutture di dati aggiuntive durante la computazione. Si definisce *stabile* se non altera l’ordine di elementi che presentano lo stesso valore, nell’insieme di input. Questo può essere utile in caso gli elementi in input rappresentano delle chiavi, e la posizione reciproca dei dati a loro associati è significativa.

<div class="center">

|                  |     Caso Migliore      |  Caso Medio   | Caso Peggiore | *In loco* | *Stabile* |
|:----------------:|:----------------------:|:-------------:|:-------------:|:---------:|:---------:|
| *Selection Sort* |     $\Theta(n^2)$      |               |               |    Sì     |    Sì     |
| *Insertion Sort* |      $\Theta(n)$       | $\Theta(n^2)$ |               |    Sì     |    Sì     |
|   *Merge Sort*   | $\Theta(n\cdot\log n)$ |               |               |    No     |    Sì     |
|   *Heap Sort*    | $\Theta(n\cdot\log n)$ |               |               |    Sì     |    No     |
|   *Quick Sort*   | $\Theta(n\cdot\log n)$ |               | $\Theta(n^2)$ |    Sì     |    No     |
|   *Tree Sort*    | $\Theta(n\cdot\log n)$ |               |               |    No     |    No     |

</div>

## Selection Sort

Il *selection sort* è una tecnica di ordinamento che sceglie data una sequenza il valore minimo, e lo inserisce al primo posto della sequenza, dopo aver effettuato questo scambio esegue nuovamente la procedura, diminuendo di uno la dimensione dell’input, senza considerare il primo elemento. Continua fino a quando non rimane un unico elemento, che dovrà necessariamente essere il valore massimo della sequenza. In generale l’algoritmo itera su ogni elemento dell’array, considerandolo come il primo elemento, e cercando il minimo nella sotto-sequenza considerata, questo può essere effettuato utilizzando due operazioni iterative annidate, oppure richiamando la funzione di ordinamento ricorsivamente ogni volta che viene effettuato uno scambio. Poiché in linguaggio C l’array non contiene la sua lunghezza, bisogna definire un oggetto `array` che presenta queste caratteristiche, oppure passare il numero di elementi nell’array `A_length` alle procedure.

Per semplicità vengono definite due procedure `minimo ` e `scambio ` che trovano il minimo valore in un’array, la prima, e scambiano il valore contenuto in due indici di un array, la seconda: “‘c int minimo(int\* A, int A_length)

int j_min = 0; int j;

for(j = 1 ; j \< A_length ; j++) if(A\[j\] \< A\[j_min\]) j_min = j;

return j_min;

void scambio(int\* A_1, int\* A_2) int temp = \*A_1; \*A_1 = \*A_2; \*A_2 = temp;

La funzione `minimo ` ha un costo $\Theta(m)$. Mentre la funzione `scambio ` esegue in tempo costante $\Theta(1)$. L’algoritmo si implementa iterando su ogni elemento e chiamando la funzione di minimo: “‘c

void selection_sort_itr(int\* A, int A_length) int i; for(i = 0 ; i \< A_length - 1; i++) scambio(A + i, A + i + minimo(A + i, A_length - i)); “‘ L’algoritmo trova il minimo e scambia i valori $n$ volte, per cui presentano un limite superiore: $$O(n)\cdot (O(m)+O(1))=O(n\cdot m)$$ Dove $m$ rappresenta $n-i$, per cui si ha: $$O(n\cdot(n-i))=O(n^2)$$

Invece se si analizzasse il limite di tempo inferiore, effettua l’operazione di minimo $n-1$ volte, ogni volta diminuendo di $1$ la dimensione dell’input in ingresso: $$\begin{gathered}
    \Omega\left(\displaystyle\sum_{i=1}^{n-1}n-i\right)=\Omega\left(\frac{n\cdot(n-2)}{2}\right)=\Omega(n^2)
\end{gathered}$$ Per cui l’algoritmo di *selection sort* ha un costo: $$\Theta(n^2)$$

Si considera una sua implementazione ricorsiva: “‘c void selection_sort_ric(int\* A, int A_length) if(A_length \> 0) scambio(A, A + minimo(A, A_length)); selection_sort_ric(A + 1, A_length - 1);

“‘ Da questo è possibile scrivere questa formula di ricorrenza: $$\begin{gathered}
    T(n)=\begin{cases}
        \Theta(1)&n=1\\
        T(n-1)+\Theta(n)&n>1
    \end{cases}
\end{gathered}$$ Per cui considerando la sua soluzione si può esprimere la sua complessità come: $$\begin{gathered}
    T(n)=\Theta(1)+\displaystyle\sum_{k=1}^{n}\Theta(k)=\Theta(1)+\Theta(1)+\cdots+\Theta(n)\\
    \Theta(1)+\Theta(n)+[\Theta(n-1)+\Theta(1)]+\cdots+\left[\displaystyle\Theta\left(n-\left\lfloor\frac{n}{2}\right\rfloor\right)+\Theta\left(\left\lfloor\frac{n}{2}\right\rfloor\right)\right]=\frac{n}{2}\cdot\Theta(n)=\Theta(n^2)
\end{gathered}$$

Si è quindi verificata la complessità dell’algoritmo, usando un’implementazione ricorsiva.

Indipendentemente dall’input di ingresso, se la sequenza è già ordinata, impiega lo stesso numero di operazioni per fornire un output. Questo algoritmo opera *in loco*, per cui memoria utilizzata è costante $O(1)$, ed è *stabile*.

## Insertion Sort

L’algoritmo di *insertion sort* è un algoritmo di tipo incrementale, dove a partire da un insieme vuoto si inserisce un elemento alla volta, mantenendo il sotto-insieme così creato ordinato. Quando si inserisce un elemento per mantenerlo ordinato, si traslano gli elementi per mantenere l’ordinamento. Il problema è risolta quando tutti gli elementi sono stati inseriti in questo modo nell’insieme. Si considera la seguente implementazione in linguaggio C: “‘c

void insertion_sort(int\* A, int A_length) int i, j, temp; for(i = 1 ; i \< A_length ; i++) temp = A\[i\]; j = i - 1; while(j \> -1 && A\[j\] \> temp) A\[j + 1\] = A\[j\]; j = j - 1; A\[j + 1\] = temp; “‘

L’algoritmo è *stabile*, poiché aggiungendo un elemento da destro verso sinistra, se incontra un elemento dello stesso valore, lo inserisce alla sua destra, mantenendo la posizione originale di quei due elementi. Inoltre anch’esso opera *in loco*, avendo una memoria utilizzata costante $O(1)$.

Nel caso peggiore deve controllare ad ogni iterazione tutti gli elementi del sotto-insieme, ciò avviene quando è presente un insieme di input ordinato in modo decrescente. Per ripete per $n$ volte $n$ operazioni di confronto, ha quindi una complessità nel caso peggiore: $$\Theta(n\cdot n)=\Theta(n^2)$$

Nel caso migliore invece deve effettuare solo un’operazione di confronto per ogni elemento aggiunto, per cui quando l’insieme di input è già ordinato, l’algoritmo legge solamente tutti gli elementi dell’insieme, e li assegna alla loro stessa posizione, senza alterare la posizione reciproca tra di loro. Quindi ha una complessità temporale: $$\Theta(n)$$

Nel caso medio, vengono comunque effettuate $O(n)$ iterazioni sul ciclo esterno, in questo caso bisogna scorrere fino alla metà del sotto-insieme per inserire un nuovo elemento, ma questo comporta comunque una complessità temporale: $$\Theta\left(\displaystyle\sum_{i=1}^{n-1}\frac{n-i}{2}\right)=\Theta\left(\frac{n(n-2)}{4}\right)=\Theta\left(\frac{n^2}{4}\right)=\Theta(n^2)$$ Questo algoritmo è più efficiente per input di dimensione piccola, poiché ha una complessità media in questi casi di $\Theta(n^2/4)$. Si dice *adattivo* poiché è in grado di operare su un insieme già parzialmente ordinato, con una complessità temporale $O(n+d)$, dove $d$ è il numero delle sostituzioni effettuate, e $n$ la lunghezza dell’insieme parzialmente ordinato. Inoltre è un algoritmo *online*, poiché è in grado di elaborare un insieme di input dove i dati arrivano uno alla volta.

## Merge Sort

Il *merge sort* è un algoritmo che si basa sulla disciplina del *divide et impera*, ovvero sulla divisione di un problema computazionale in sotto-problemi di dimensione minore, più facilmente ed efficientemente gestibili, per poi combinare le soluzioni ottenute per ottenere la soluzione al problema originario. Venne ideato nel 1945 da John von Neumann, si basa sul concetto che due sequenze ordinate possono essere unite tra di loro, mantenendo l’ordinamento, molto facilmente. Questo algoritmo di ordinamento divide la sequenza in input in due sotto-sequenza di lunghezza uguale, in seguito vengono ordinate secondo lo stesso *merge sort*, ed in seguito vengono unite tra di loro, per ottenere così una sequenza in output ordinata. Viene quindi implementato ricorsivamente, rispetto ad un caso base dove è presente una sequenza contenente un singolo elemento.

“‘c void merge(int\* A, int p, int q, int r)

int len_l = q - p + 1; int len_r = r - q;

// creo le due sotto-sequenze sinistra e destra int\* left = (int\*) malloc((len_l + 1)\* sizeof(int)); int\* right = (int\*) malloc((len_r + 1)\* sizeof(int));

// inizializzo le due sotto-sequenze int i, j; for(i = 0 ; i \< len_l ; i++) left\[i\] = A\[p + i\];

for(j = 0 ; j \< len_r ; j++) right\[j\] = A\[q + 1 + j\];

/\* assegno all’ultimo elemento delle due sotto-sequenze il massimo valore assumibile da un intero \*/ left\[len_l\] = 2147483647; right\[len_r\] = 2147483647;

// confronto le due sotto-sequenze per unirle sull’array A i = 0; j = 0; int k; for(k = p ; k \< r + 1 ; k++) if(left\[i\] \<= right\[j\]) A\[k\] = left\[i\]; i++; else A\[k\] = right\[j\]; j++;

void merge_sort(int\* A, int A_length) merge_sort_ric(A, 0, A_length - 1);

void merge_sort_ric(int\* A, int p, int r) if(p \< r) int q = (r + p) / 2; merge_sort_ric(A, p, q); merge_sort_ric(A, q + 1, r); merge(A, p, q, r);

“‘

Il confronto `<=` effettuato tra le due sotto-sequenze mantiene la stabilità dell’algoritmo. Per calcolare la sua complessità, bisogna calcolare la complessità delle sue sotto-procedure. Il caso base è costante $\Theta(1)$, poiché non si applicano operazioni sull’insieme di input. L’operazione di divisione $D(n)$ ha costo costante $\Theta(1)$. L’ordinamento delle due sotto-sequenze ha un costo totale $2\cdot T(n/2)$, mentre il costo dell’unione tra le due sotto-sequenze è lineare $C(n)=\Theta(n)$. Per cui si ottiene la seguente formula di ricorrenza per l’algoritmo di *merge sort*: $$T(n)=\begin{cases}
        \Theta(1) & 0\leq n\leq1\\
        2\cdot T\left(\displaystyle\frac{\strut{n}}{\strut{2}}\right)+D(n)+C(n)=2\cdot T\left(\displaystyle\frac{\strut{n}}{\strut{2}}\right)+\Theta(n)&n>1
    \end{cases}$$

Per il teorema dell’esperto ammette come soluzione la seguente espressione: $$T(n)=\Theta\left(n\cdot\log n\right)$$

## Heap Sort

L’algoritmo *heap sort* si basa sulla struttura di dati *coda di priorità* descritta nella sezione . Si suppone di avere a disposizione un’implementazione di un heap, tramite le seguenti *operazioni*:

- `build_max_heap`: funzione che crea un nuovo heap dato un array;

- `max_heapify`: funzione che ri-ordina un heap, per mantenere le proprietà;

- `swap`: funzione che scambia il contenuto di due caselle di un array.

Data l’implementazione di un *min-heap* è possibile effettuare la stessa procedura. Per ordinare gli elementi in maniera crescente si trasforma l’array in un *max-heap*, in seguito iterando su ogni elemento dell’array dall’ultimo al primo, si estrae l’elemento a più alta priorità nel *max-heap* e si assegna alla casella corrente dell’array $i$. Si diminuisce la dimensione dell’heap e si trasforma nuovamente in un *max-heap*: “‘c void max_heap_sort(int\* A1, int len_A1) heap\* h = new_queue(len_A1); build_max_heap(h, A1, len_A1); int i; for(i = h-\>A_length - 1 ; i \> 0 ; i–) swap(A1, 0, i); h-\>size–; max_heapify(h, 0); “‘ La trasformazione dell’array in un heap avviene in tempo lineare $\Theta(n)$, mentre ogni chiamata alla procedura `max_heapify ` ha una complessità nel caso peggiore $\Theta(\log n)$. Per cui nel caso peggiore questo algoritmo ha un costo: $$T(n)=\Theta(n)+\Theta(n)\cdot\Theta(\log n)\in\Theta(n\cdot\log n)$$ Mentre nel caso migliore ogni chiamata a `max_heapify ` ha costo costante $\Theta(1)$, quindi l’algoritmo ha un costo: $$T(n)=\Theta(n)$$ Ciò avviene solo quando ogni elemento dell’array è lo stesso, altrimenti sarebbe impossibile che la funzione di trasformazione in un *max-heap* impieghi un tempo costante per ogni elemento. Inoltre si può dimostrare considerando un caso di due elementi uguali come questo algoritmo non è *stabile*. Quando si estrae un elemento a più alta priorità si posiziona in fondo all’array, quindi avendo solo due elementi uguali, viene scambiata la loro posizione reciproca nell’array in output. Questo algoritmo invece è *in loco*, poiché l’heap lavora sullo stesso array fornito in input all’algoritmo.

## Quick Sort

L’algoritmo di ordinamento *quick sort* venne ideato nel 1962 da Charles Antony Richard Hoare. Questo algoritmo si basa sulla strategia *divide et impera*. Nel caso peggiore ha un tempo di esecuzione $\Theta(n^2)$, mentre nel caso migliore ha un tempo di esecuzione $\Theta(n\cdot\log n)$, ed ha delle prestazioni tra le migliori di ogni algoritmo basato su confronti. Per cui le costanti moltiplicative della sua notazione asintotica sono tra le più piccole (nel caso migliore infatti il tempo esatto di esecuzione è $1.39 n\cdot\log n$).

Verrà trattata la variante dell’algoritmo introdotta da Nico Lomuto. Questo algoritmo divide un sotto-array compreso tra due indici $p$ e $r$ in due sotto-array compresi, il primo, tra $p$ e $q-1$ ed il secondo tra $q+1$ e $r$. Vengono divisi in modo che ogni elemento nel sotto-array sinistro contenga valori minori o uguali del valore all’indice $q$, mentre tutti gli elementi nel sotto-array di destra contengano valori maggiori. Questi due sotto-array vengono poi ri-ordinati ricorsivamente, fino a quando l’array non viene completamente ordinato. La scelta dell’indice $q$ è quindi di vitale importanza per un’efficiente implementazione dell’algoritmo. Questa scelta viene effettuata dalla procedura di partizione. Ogni variante di questo algoritmo presenta una procedura diversa per la scelta di questo indice, chiamato *pivot*. Viene quindi fornita una possibile implementazione in linguaggio C dell’algoritmo: “‘c void quick_sort(int\* A, int A_length) quick_sort_ric(A,0,A_length);

void quick_sort_ric(int\* A, int p, int r) if(p \< r) int q = partition(A, p, r); quick_sort_ric(A, p, q - 1); quick_sort_ric(A, q + 1, r); “‘ Per cui la complessità dell’algoritmo ricade nella funzione di partizione. Questo algoritmo di ordinamento è *in loco*, poiché in caso si abbia $p=r$ l’invocazione della procedura non ha alcun effetto sull’array, mentre per $p>r$, l’invocazione non ha effetto, poiché non rispetta la condizione base. Il valore ottenuto dalla procedura `partition ` deve essere compreso tra i due indici forniti $p\leq q\leq r$. Questa procedura considera l’indice $r$ il pivot, su cui vengono confrontati tutti gli elementi del sotto-array. Vengono quindi posti dall’indice $p$ in poi gli elementi minori o uguali del valore del pivot, tramite la procedura `swap`. Infine viene posto il pivot, ovvero il valore all’indice $r$, subito dopo il primo sotto-array e viene restituito questo indice: “‘c int partition(int\* A, int p, int r) int i = p; int j; for(j = p ; j \< r ; j++) if(A\[j\] \<= A\[r\]) scambio(A + i, A + j); i++; scambio(A + i, A + r); return i; “‘ Questa procedura ha sempre un tempo di esecuzione di complessità lineare $T_p(n)\in\Theta(n)$. Il caso peggiore corrisponde a quando viene ripetutamente scelto come *pivot* il valore massimo o minimo nell’array. I due sotto-array che genera non sono quindi bilanciati, uno non rispetta il caso base, mentre l’altro array corrisponde all’array iniziale a meno di una casella, questo risulta in una complessità: $$\begin{gathered}
    T(n)=\begin{cases}
        a&n=0\\
        T(n-1)+\Theta(n)&n>0
    \end{cases}
\end{gathered}$$ Questa formula di ricorrenza è risolta dalla seguente espressione: $$T(n)=\displaystyle\sum_{k=1}^n\Theta(k)=\Theta\left(\sum_{k=1}^nk\right)=\Theta(n^2)$$

Il caso migliore invece avviene quando elegge a pivot il valore medio dell’array, in questo modo crea due sotto-array bilanciati: $$T(n)=2\cdot T\left(\displaystyle\frac{n}{2}\right)+\Theta(n)$$ Per il teorema dell’esperto, per $a=2$, $b=2$, e $k=1$: $$T(n)\in\Theta(n\log n)$$

L’analisi del caso medio è molto più complessa. Vengono fornite solamente due considerazione che aiutano a giustificare la complessità nel caso medio di questo algoritmo $\Theta(n\cdot\log n)$. Si analizza il caso dove le ricorsione sono sbilanciate fino ad una certa soglia. Si suppone che i sotto-array creati abbiano sempre la stessa proporzione fissa rispetta all’array di partenza di $9:1$. La formula di ricorrenza ottenuta è quindi: $$\begin{gathered}
    T(n)\leq T\left(\displaystyle\frac{9n}{10}\right)+T\left(\frac{n}{10}\right)+c\cdot n
\end{gathered}$$ La complessità dipende in parte maggiore dal sotto-array sbilanciato, considerando che avvengono $\log_{10/9}n$ ricorsioni si ha una complessità totale: $$c\cdot n\cdot\log_{10/9}n+g(n)\in O(n\cdot\log n)$$ Dove $g(n)$ dipende dalle chiamate ricorsive che avvengono anche sul sotto-array minore.

Si suppone ora che nel $20\%$ dei casi la procedura divide i due sotto-array sbilanciati $9:1$, inoltre si suppone che una partizione sbilanciata venga sempre seguita da una bilanciata. In questo modo una partizione sbilanciata può essere assorbita dalla partizione successiva.

Si può modificare la procedura di partizione, assegnando come pivot un valore casuale compreso nell’intervallo del sotto-array, per impedire che i casi peggiori coincidano con disposizioni notevoli dell’array, come un array disposto in maniera crescente e decrescente: “‘c int random_partition(int\* A, int p, int r) srand(time(0)); scambio(A + rand() return partition(A, p, r);

void random_quick_sort(int\* A, int A_length) random_quick_sort_ric(A,0,A_length);

void random_quick_sort_ric(int\* A, int p, int r) if(p \< r) int q = random_partition(A, p, r); random_quick_sort_ric(A, p, q - 1); random_quick_sort_ric(A, q + 1, r); “‘

## Tree Sort

Supponendo di disporre di un’implementazione di un albero binario di ricerca, descritta da queste due operazioni:

- `new_abr`: funzione che restituisce il riferimento ad un nuovo albero binario di ricerca vuoto;

- `add_abr`: funzione che inserisce un nuovo nodo, contenente un valore dato, in un albero binario di ricerca.

Utilizzando la struttura dell’albero è possibile ordinare una sequenza di interi in input, aggiungendo ogni volta un nuovo nodo contenente il valore corrispondente nella sequenza ad un albero binario di ricerca, inizialmente vuoto. In questo modo quando viene visitato l’albero tramite una visita simmetrica, i valori sono disposti in maniera crescente, per cui si è così ordinata la sequenza.

Questa procedura corrisponde all’algoritmo di ordinamento `tree_sort ` di complessità lineare nel caso migliore, poiché ognuna delle $n$ aggiunte all’albero avvengono in tempo logaritmico $\Theta(\log n)$, così come nel caso medio, per un tempo di esecuzione dell’ordinamento di $\Theta(n\cdot\log n)$. Mentre nel caso peggiore ogni aggiunta impiega tempo lineare $\Theta(n)$, quindi l’ordinamento viene eseguito in $\Theta(n^2)$. Questo quando si utilizza un albero binario di ricerca, ma è possibile utilizzare altre strutture dati che mantengono l’albero bilanciato, come gli alberi rosso-neri, per diminuire il tempo di inserimento di un ogni elemento, fornendo quindi un tempo di inserimento sempre in tempo logaritmico $\Theta(\log n)$, e quindi un ordinamento nel caso peggiore di $\Theta(n\cdot\log n)$: “‘c void abr_sort(int\* a, int len) albero_bin\* t = new_tree_bin(); int i; for(i = 0 ; i \< len ; i++) add_abr(t, a\[i\]); i = 0; bin_to_array(\*t, a, &i); “‘ “‘c void bin_to_array(albero_bin t, int\* a, int \*i) if(t != NULL) if(t-\>left != NULL) bin_to_array(t-\>left, a, i); a\[\*i\] = t-\>info; (\*i)++; if(t-\>right != NULL) bin_to_array(t-\>right, a, i); “‘ Per trasferire l’array ordinato sull’array di output si effettua una visita simmetrica, in tempo lineare $\Theta(n)$.

Per rendere più efficiente questa procedura è possibile utilizzare un albero rosso-nero per mantenere il tempo di esecuzione di ogni inserimento logaritmico:

- `new_rb`: funzione che restituisce il riferimento ad un nuovo albero rosso-nero vuoto;

- `add_rb`: funzione che inserisce un nuovo nodo, contenente un valore dato, in un albero rosso-nero.

Questo quindi garantisce un tempo di esecuzione dell’algoritmo di $\Theta(n\cdot\log n)$ sia nel caso migliore che nel caso peggiore: “‘c void rb_to_array(nodo\* root, nodo\* null, int\* a, int \*i) if(root != null) if(root-\>left != null) rb_to_array(root-\>left, null, a, i); a\[\*i\] = info_rb(root); (\*i)++; if(root-\>right != null) rb_to_array(root-\>right, null, a, i);

void rb_sort(int\* A, int A_length) int i; albero_rb\* rb = new_tree_rb(); for(i = 0 ; i \< A_length ; i++) add_rb(rb, A\[i\]); i=0; rb_to_array(rb\[0\], rb\[1\], A, &i); “‘

Questo algoritmo non è *in loco* poiché deve allocare memoria per un’intero, ha quindi una complessità spaziale lineare $\Theta(n)$ rispetto alla dimensione dell’input. Non è neanche *stabile* poiché non garantisce che due nodi aventi lo stesso valore rimangano nella stessa posizione reciproca dopo una rotazione, per mantenere le proprietà di un albero rosso-nero. Inoltre in base all’implementazione adoperata, potrebbe non essere possibile gestire valori multipli nell’input, quindi non fornirebbe un’ordinamento completo dell’intera sequenza, poiché rifiuterebbe tutti gli inserimenti multipli

# Pile, Code e Liste

Un tipo astratto di dato ADT “Abstract Data Type”, rappresenta una struttura di dati indipendente dalla sua implementazione. Un ADT è costituito da un *dominio di interesse*, ed eventuali *domini di supporto*, un insieme di *costanti*, ed un insieme di *operazioni*.

Data la descrizione di un ADT, è possibile implementarlo in un linguaggio di programmazione utilizzando tipi concreti o strutture, interni al linguaggio di programmazione usato, per rappresentare i *domini* necessari dell’ADT. Si possono realizzare strutture per rappresentare le *costanti* dell’ADT, e funzioni che svolgono le *operazioni* definite sullo specifico tipo astratto di dato.

Uno stesso ADT può essere implementato rispettando specifiche diverse, anche nello stesso linguaggio di programmazione, per ottenere una rappresentazione nel dato linguaggio in grado di rispettare proprietà diverse.

Un ADT non presenta limitazioni nella sua descrizione, ma può essere limitato dal linguaggio in cui viene implementato. Per esempio i tipi e le strutture realizzate in un dato linguaggio possono essere limitati in dimensione, per cui può essere necessario restringere i *domini* per poter realizzare un ADT.

## Pile

La pila o stack, è un ADT che implementa la disciplina LIFO “Last In First Out” per la gestione dei dati, quindi l’ultimo elemento salvato rappresenta il primo elemento che può essere estratto dalla pila. Il tipo astratto di dato pila è formato da tre *domini*:

- L’insieme delle pile di interi $\mathbb{P}$;

- L’insieme di interi $\mathbb{Z}$;

- L’insieme di booleani $\mathbb{B}:=\big\{\mathrm{true }, \,\mathrm{false}\big\}$.

L’unica *costante* è la pila vuota. Mentre è possibile definire una serie di operazioni:

- `is_empty`: $\mathbb{P}\to\mathbb{B}$, funzione che controlla se una pila dall’insieme delle pile, è vuota. Restituisce quindi un booleano;

- `push`: $\mathbb{P}\times\mathbb{Z}\to\mathbb{P}$, inserisce un intero all’interno di una pila, restituisce la pila contenente il nuovo elemento;

- `pop`: $\mathbb{P}\to\mathbb{P}\times\mathbb{Z}$, rimuove l’ultimo elemento da una pila, e ne restituisce il suo valore;

- `top`: $\mathbb{P}\to\mathbb{Z}$, restituisce il valore dell’ultimo elemento inserito nella pila;

- `empty`: $\mathbb{P}\to\mathbb{P}$, svuota la pila, e restituisce la *costante* pila vuota;

- `size`: $\mathbb{P}\to\mathbb{Z}$, restituisce il numero di elementi nella pila.

Può essere realizzata utilizzando un oggetto formato da un array `A`, ed un riferimento `top` all’indice corrispondente all’ultimo elemento inserito nella pila `p`. Poiché gli indici dell’array sono interi positivi, incluso lo zero, quando la pila è vuota, il riferimento non rappresenta nessun indice valido, per cui ogni intero negativo potrebbe essere utilizzato, ma nelle seguenti implementazioni viene usato il valore $-1$. In caso la pila sia limitata, di dimensione massima `maxsize`, quando si tenta di inserire un elemento, restituisce invece un errore di *overflow*. Analogamente quando si tenta di rimuovere o visualizzare l’ultimo elemento inserito in una pila, e la pila è vuota, allora si verifica un errore di *underflow*, e l’operazione non restituisce alcun valore.

Si considera una pila implementata in linguaggio C, tramite una struttura contenente un array di interi, la lunghezza dell’array, e l’indice corrispondente all’ultima posizione disponibile nella pila: “‘c pila\* new_stack(int maxsize)

pila\* p = (pila\*) malloc(sizeof(pila));

p-\>A = (int\*) malloc(maxsize\*sizeof(int)); p-\>A_length = maxsize; p-\>top = -1;

return p;

int is_empty_stack(pila\* p) return p-\>top == -1; “‘ In caso la pila abbia una dimensione massima, si rifiuta un inserimento quando si tenta di inserire in una pila già piena:

``` c
void push(pila* p, int x){
    if(p->top == p->A_length - 1) printf("errore di overflow");
    else{   
        p->top++;
        p->A[p->top] = x;
    }
}    
```

“‘c int pop(pila\* p) if( p-\>top == -1) printf("error: underflow"); else int temp = p-\>A\[p-\>top\]; p-\>top–; return temp;

int top(pila\* p) if(p-\>top == -1) printf("errore di underflow"); else return p-\>A\[p-\>top\];

void empty_stack(pila\* p) p-\>top=-1;

int size_stack(pila\* p) return p-\>top + 1; “‘

Tutte queste operazioni vengono eseguite in tempo costante $\Theta(1)$, ma la pila ha una dimensione limitata. Per cui per utilizzare una pila di dimensione non definita, si implementa una gestione telescopica della memoria. Ovvero quando si tenta di inserire un elemento nella pila piena, allora viene raddoppiata la dimensione dell’array, per permettere l’inserimento di nuovi elementi: “‘c void push(pila\* p, int x)

// se la pila è piena ne viene raddoppiata la dimensione if(p-\>top == p-\>A_length-1) realloc_stack(p);

p-\>top++; p-\>A\[p-\>top\] = x;

“‘ Viene quindi definita la funzione che permette di raddoppiare la dimensione dell’array: “‘c void realloc_stack(pila\* p) p-\>A_length \*= 2; p-\>A = (int\*) realloc(p-\>A, p-\>A_length \* sizeof(int)); “‘

La funzione di copia dell’array esegue l’operazione in tempo lineare $\Theta(n)$, ma viene chiamata solamente quando la dimensione della pila coincide alla dimensione dell’array dove è contenuta, altrimenti l’operazione avviene in tempo costante $\Theta(1)$. Per cui nel caso peggiore ha una complessità lineare, mentre nel caso migliore ha complessità costante. Per una pila inizializzata ad una dimensione di array $n$, il costo di un inserimento è costante fino a quando la dimensione della pila non raggiunge $n$, per cui si può distribuire il costo dell’operazione nel caso peggiore su ognuna delle $n$ operazioni effettuate nel caso migliore. In questo modo si ottiene la complessità ammortizzata dell’algoritmo: $$\displaystyle\frac{\Theta(n)}{n}=\Theta(1)$$

In generale quando viene realizzata un implementazione di un ADT, per renderla disponibile ed utilizzabile, bisogna fornire una descrizione delle sue limitazioni, ed una lista delle operazioni supportate, insieme alla complessità asintotica e o ammortizzata di ognuna di esse.

## Code

Analogamente ad una pila, può essere realizzata una coda, che implementa la disciplina FIFO “First In First Out”. Ovvero il primo elemento inserito nella coda, è anche il primo elemento che viene estratto dalla coda. Viene definita tramite utilizzando i seguenti *domini*:

- L’insieme delle code di interi $\mathbb{Q}$;

- L’insieme di interi $\mathbb{Z}$;

- L’insieme di booleani $\mathbb{B}:=\big\{\mathrm{true }, \,\mathrm{false}\big\}$.

L’unica *costante* come per le pile, è la coda vuota. Vengono definite le seguenti operazioni sulle code:

- `is_empty`: $\mathbb{Q}\to\mathbb{B}$, funzione che controlla se una coda dall’insieme delle code, è vuota. Restituisce quindi un booleano;

- `enqueue`: $\mathbb{Q}\times\mathbb{Z}\to\mathbb{Q}$, inserisce un intero all’interno di una coda, restituisce la coda contenente il nuovo elemento;

- `dequeue`: $\mathbb{Q}\to\mathbb{Q}\times\mathbb{Z}$, rimuove l’elemento più vecchio da una coda, e ne restituisce il suo valore;

- `front`: $\mathbb{Q}\to\mathbb{Z}$, restituisce il valore del primo elemento inserito nella coda;

- `empty`: $\mathbb{Q}\to\mathbb{Q}$, svuota la pila, e restituisce la *costante* pila vuota;

- `size`: $\mathbb{Q}\to\mathbb{Z}$, restituisce il numero di elementi nella pila.

Analogamente ad una pila, se tenta di inserire un elemento all’interno di una coda piena si verifica un errore di *overflow*. Invece se tenta di rimuovere un elemento oppure visualizzare il primo elemento da una coda vuota, si verifica un errore di *underflow*.

Può essere implementato in linguaggio C utilizzando un array, salvando in una struttura la lunghezza dell’array, l’indice del primo elemento, e del primo elemento disponibile nell’array, corrispondente all’indice successivo della coda.

L’array viene gestito circolarmente, quindi può accadere che l’indice relativo all’ultimo elemento in coda sia inferiore all’indice relativo al primo elemento in coda. La coda è vuota quando entrambi gli indici puntano alla stessa posizione nell’array. Secondo questa implementazione si possono inserire al massimo $n-1$ elementi nell’array associato, altrimenti si può associare l’indice associato al primo elemento disponibile ad un valore non valido, come un intero negativo.

Analogamente ad una pila, è possibile raddoppiare la dimensione dell’array associato alla coda in caso si arrivi alla dimensione massima. In questo modo è possibile gestire l’array in modo telescopico, avendo una complessità ammortizzata costante $\Theta(1)$ per l’inserimento in coda. Si considera la seguente implementazione per le operazioni su una coda: “‘c coda\* new_queue(int maxsize)

coda\* c = (coda\*) malloc(sizeof(coda));

c-\>A_length = maxsize; c-\>A = (int\*) malloc(maxsize\*sizeof(int)); c-\>head = 0; c-\>tail = 0;

return c;

int is_empty_queue(coda\* c) return c-\>head == c-\>tail;

void enqueue(coda\*c, int x)

// se la coda è piena, viene raddoppiata la sua dimensione if(c-\>tail + 1 == c-\>head \|\| (c-\>tail == c-\>A_length - 1 && c-\>head == 0)) realloc_queue(c);

c-\>A\[c-\>tail\] = x; c-\>tail = (c-\>tail + 1)

int dequeue(coda\* c) if(c-\>head == c-\>tail) printf("errore di underflow"); else int temp = c-\>A\[c-\>head\]; c-\>head = (c-\>head + 1) return temp;

int front(coda\* c) if(c-\>head == c-\>tail) printf("errore di underflow"); else return c-\>A\[c-\>head\];

void empty_queue(coda\* c) c-\>head = c-\>tail;

int size_queue(coda\*c) return (c-\>tail - c-\>head) \* (c-\>tail - c-\>head \>= 0) + (c-\>tail - c-\>head + c-\>A_length) \* (c-\>tail - c-\>head \< 0);

void realloc_queue(coda\* c)

c-\>A_length \*= 2; c-\>A = (int\*) realloc(c-\>A, c-\>A_length \* sizeof(int));

if(c-\>tail \< c-\>head) int i; for(i = 0 ; i \< c-\>tail ; i++) c-\>A\[c-\>A_length / 2 + i\] = c-\>A\[i\]; c-\>tail = c-\>A_length / 2 + i;

“‘

Come per una pila tutte le operazioni, avvengono in tempo costante $\Theta(1)$, mentre l’inserimento è lineare nel caso peggiore $\Theta(n)$, ed ammortizzato a tempo costante $\Theta(1)$.

### Uso di Pile e Code

Supponendo di avere a disposizione l’implementazione di una coda o di una pila, e le loro operazioni di *costante*, di inserimento e di rimozione, nella disciplina corrispondente, allora è possibile implementare l’ADT opposto utilizzando due pile o due code. La creazione avviene in tempo costante. In base a come vengono implementate le code o le pile su cui si basa questa struttura dati, avrà una dimensione massima, oppure una gestione della memoria telescopia: “‘c coda_2\* new_queue_2(int maxsize)

coda_2\* c = (coda_2\*) malloc(sizeof(coda_2));

c-\>p1 = new_stack(maxsize); c-\>p2 = new_stack(maxsize);

return c;

“‘ “‘c pila_2\* new_stack_2(int maxsize)

pila_2\* p = (pila_2\*) malloc(sizeof(pila_2));

p-\>c1 = new_queue(maxsize); p-\>c2 = new_queue(maxsize);

return p;

“‘ Le rispettive operazioni di inserimento vengono realizzate in tempo costante, se sono implementate con una dimensione limite, altrimenti se gestiscono la memoria in modo telescopico, allora hanno complessità lineari nel caso peggiore $\Theta(n)$, ed ammortizzati a tempo costante $\Theta(1)$: “‘c void enqueue_2(coda_2\* c, int x) push(c-\>p1, x); “‘ “‘c void push_2(pila_2\* p, int x) enqueue(p-\>c1, x); “‘ Per effettuare una rimozione, si copia una delle due strutture interne, fino al suo penultimo valore, all’altra, utilizzando le rispettive operazioni. In questo modo se si applica la disciplina FIFO, l’elemento rimasto nella prima struttura rappresenta l’elemento da rimuovere per implementare la disciplina LIFO. Viceversa per la disciplina LIFO. Quindi si rimuove l’elemento rimasto, e si salva su una variabile temporanea. Successivamente si copia per intero la seconda struttura sulla prima, ora senza un elemento, e si restituisce il valore di quest’ultimo così rimosso: “‘c int dequeue_2(coda_2\* c) while(size_stack(c-\>p1)\>1) push(c-\>p2, pop(c-\>p1)); int temp = pop(c-\>p1); while(!is_empty_stack(c-\>p2)) push(c-\>p1, pop(c-\>p2)); return temp; “‘ “‘c int pop_2(pila_2\* p) while(size_queue(p-\>c1)\>1) enqueue(p-\>c2, dequeue(p-\>c1)); coda\* temp = p-\>c2; p-\>c2 = p-\>c1; p-\>c1 = temp; return dequeue(p-\>c2); “‘ Quest’operazione avviene in tempo lineare $\Theta(n)$, poiché deve iterare su ogni elemento, per trasferirlo da una struttura interna ad un’altra. Una pila realizzata da due code non può rimuovere un elemento in tempo minore, mentre è possibile migliorare quest’implementazione per una coda realizzata da due pile. Considerando una coda realizzata in questo modo, per evitare di iterare ogni rimozione su entrambe le pile, si può assegnare una delle due pile come la pila di aggiunta, e l’altra di rimozione. In questo modo al termine della prima rimozione non viene iterata di nuovo sulla pila di rimozione per copiarla sulla pila di aggiunta, per cui ad una rimozione subito seguente non è necessario iterare nuovamente su tutti gli elementi ed è possibile rimuovere in tempo costante $\Theta(1)$ l’elemento. Solo quando è necessario effettuare un’operazione inversa bisogna iterare sull’altra pila, analogamente per l’aggiunta, se la pila di aggiunta è vuota si copia quella di rimozione all’interno della pila di aggiunta, per poi mantenere invariata la posizione della pila attiva: “‘c void enqueue_3(coda_2\* c, int x) if(is_empty_stack(c-\>p1)) while(!is_empty_stack(c-\>p2)) push(c-\>p1, pop(c-\>p2)); push(c-\>p1, x);

int dequeue_3(coda_2\* c) if(is_empty_stack(c-\>p2)) while(!is_empty_stack(c-\>p1)) push(c-\>p2, pop(c-\>p1)); pop(c-\>p2); “‘ Nel caso peggiore quindi l’operazione di rimozione e di aggiunta hanno tempo lineare $\Theta(n)$, mentre impiegano tempo ammortizzato costante $\Theta(1)$ nel caso migliore, poiché si può distribuire il costo lineare di una prima operazione di aggiunta o rimozione sulla successione di operazioni dello stesso tipo. Il caso medio dipende dalla frequenza delle operazioni, ed la loro inversione.

## Liste

Le liste sono una struttura dati dove gli elementi sono memorizzati linearmente, ed ogni elemento fornisce informazioni sulla posizione in memoria del successivo, e o del precedente. Per cui si possono distinguere in liste singolarmente e doppiamente concatenate. Per cui è utile utilizzare un iteratore per scorrere sugli elementi della lista, per identificare la loro posizione all’interno della lista.

Questo ADT è definito dai seguenti *domini*:

- L’insieme delle liste di interi $\mathbb{L}$;

- L’insieme di supporto degli iteratori, utilizzati per identificare le posizioni $\mathbb{I}$;

- L’insieme di interi $\mathbb{Z}$;

- L’insieme di booleani $\mathbb{B}$.

Le *costanti* sono la lista vuota, e l’iteratore non valido, in genere assume un valore definito a priori. La funzione `new_list ` chiamata per creare la lista restituisce la *costante* lista vuota, esegue l’*operazione* in tempo costante $\Theta(1)$.

Vengono definite le seguenti *operazioni* per aggiornare la lista:

- `add_head`: $\mathbb{L}\times\mathbb{Z}\to\mathbb{L}$, inserisce un intero in testa alla lista;

- `add_tail`: $\mathbb{L}\times\mathbb{Z}\to\mathbb{L}$, inserisce un intero in coda alla lista;

- `add_before`: $\mathbb{L}\times\mathbb{I}\times\mathbb{Z}\to\mathbb{L}$, inserisce un intero prima di uno specifico iteratore;

- `add_after`: $\mathbb{L}\times\mathbb{I}\times\mathbb{Z}\to\mathbb{L}$, inserisce un intero dopo di uno specifico iteratore;

- `delete_index`: $\mathbb{L}\times\mathbb{I}\to\mathbb{L}$, elimina un elemento da una lista, dato il suo iteratore;

- `delete_value`: $\mathbb{L}\times\mathbb{I}\to\mathbb{L}$, elimina il primo elemento da una lista, di valore dato;

- `empty`: $\mathbb{L}\to\mathbb{L}$, svuota una lista di interi.

Inoltre vengono definite una serie di *operazioni* per utilizzare la lista, ovvero per visualizzare e leggere gli elementi memorizzati:

- `head`: $\mathbb{L}\to\mathbb{I}$, restituisce l’iteratore corrispondente al primo elemento memorizzato sulla lista, oppure l’iteratore non valido in caso la lista sia vuota;

- `next`: $\mathbb{L}\times\mathbb{I}\to\mathbb{I}$, restituisce l’iteratore corrispondente all’elemento successivo, dato un iteratore, oppure l’iteratore non valido se è l’ultimo elemento;

- `prev`: $\mathbb{L}\times\mathbb{I}\to\mathbb{I}$, restituisce l’iteratore corrispondente all’elemento precedente, dato un iteratore, oppure l’iteratore non valido se è il primo elemento;

- `info`: $\mathbb{L}\times\mathbb{I}\to\mathbb{Z}$, restituisce il contenuto di un elemento dato il suo iteratore, genera un errore se viene fornito l’iteratore non valido;

- `search`: $\mathbb{L}\times\mathbb{Z}\to\mathbb{I}$, restituisce l’iteratore corrispondente all’elemento contenente un valore specifico, altrimenti l’iteratore non valido se non è presente nella lista;

- `tail`: $\mathbb{L}\to\mathbb{I}$, restituisce l’iteratore corrispondente all’ultimo elemento salvato sulla lista, oppure l’iteratore non valido se la lista è vuota;

- `is_empty`: $\mathbb{L}\to\mathbb{B}$, verifica se una lista è vuota;

- `size`: $\mathbb{L}\to\mathbb{Z}$, restituisce la dimensione della lista.

Una lista può essere implementata seguendo diverse strategie, in base a quale operazioni bisogna effettuare efficientemente sulla lista:

- *Concatenata*: ogni elemento fornisce un riferimento all’elemento successivo, per cui consente uno scorrimento efficiente in avanti;

- *Doppiamente Concatenata*: ogni elemento fornisce un riferimento all’elemento precedente e successivo, per cui permette uno scorrimento efficiente in avanti ed indietro;

- *Accesso agli Estremi*: fornisce un riferimento al primo, ed all’ultimo elemento salvato sulla lista, per una consultazione efficiente.

In genere una lista contiene il riferimento al primo elemento, quindi l’accesso a questo elemento avviene in tempo costante $\Theta(1)$. Se la lista è (semplicemente) concatenata, è possibile accedere all’elemento successivo in tempo costante $\Theta(1)$, mentre per accedere al precedente bisogna scorrere l’intera lista fino a raggiungerlo, per cui impiega un tempo lineare, nel caso peggiore $\Theta(n)$, dove $n$ è la lunghezza della lista. Se è doppiamente concatenata, invece è possibile effettuare quest’operazione in tempo costante $\Theta(1)$. Mentre se fornisce un riferimento all’ultimo elemento è possibile consultarlo in tempo costante $\Theta(1)$, invece di scorrere l’intera lista in tempo lineare $\Theta(n)$.

Una lista può essere implementata utilizzando due strategie diverse:

- *Array*;

- *Oggetti e Riferimenti*.

### Liste Tramite Array

Un array è un tipo di dato capace di contenere una sequenza di valori. Si può utilizzare un array per contenere la sequenza di valori memorizzati nella lista, ma bisogna fornire un modo per poter distinguere quale indice dell’array corrisponde ad elementi memorizzati in lista, e quali identifichino caselle libere nell’array. Sono possibili due strategie per attuare questo processo. Un primo metodo più semplice ed intuitivo consiste nel creare due array della stessa dimensione, che contengono il valore dell’indice precedente, il primo, e successivo, il secondo, dell’intero contenuto ad un dato indice $i$, nella lista contenente la sequenza. Quindi si lavora su tre array:

- `info`: contiene la sequenza di interi memorizzata sulla lista;

- `next`: contiene gli indici degli elementi successivi;

- `prev`: contiene gli indici degli elementi precedenti (se *doppiamente concatenata*).

Questi tre array vengono salvati nella struttura lista `l`. L’iteratore è quindi un intero, e rappresenta l’indice di un array $i$:

``` c
    l->info[i]  // valore contenuto all'indice i
    l->next[i]  // indice dell'elemento successivo in lista
    l->prev[i]  // indice dell'elemento precedente in lista
```

L’iteratore non valido quindi viene rappresentato da un indice non valido, in questo caso si sceglie il valore $-1$. Poiché per salvare una lista non sono necessari tutti gli indici dell’array, è possibile memorizzare su uno stesso array più di una lista, poiché non interferiscono l’una con l’altra, utilizzando due opportuni riferimenti (indici) ai primi elementi delle due liste:

``` c
    l_1->head   // testa della prima lista 
    l_2->head   // testa della seconda lista
```

Per cui è possibile utilizzare due liste per memorizzare le posizione disponibili nell’array. Una prima lista che salva gli interi nella lista, ed una seconda lista contenente tutte le celle non utilizzate nell’array. In questo modo quando viene inserito un nuovo elemento nella lista, viene rimosso un elemento dalla lista `free` contenente le posizioni disponibili, analogamente quando viene rimosso un elemento dalla lista, viene aggiunto alla lista `free`.

Una lista viene quindi inizializzata assegnando al riferimento alla testa (ed alla coda) l’iteratore non valido, mentre si assegna tutto l’array alla lista `free` degli elementi disponibili: “‘c lista_3a\* new_lista_3a(int maxsize)

lista_3a\* l = (lista_3a\*) malloc(sizeof(lista_3a)); l-\>info = (int\*) malloc(maxsize \* sizeof(int)); l-\>prev = (int\*) malloc(maxsize \* sizeof(int)); l-\>next = (int\*) malloc(maxsize \* sizeof(int));

// si inizializzano gli array degli indici int i; for(i = 0 ; i \< maxsize ; i++) l-\>next\[i\] = i + 1; l-\>prev\[i\] = i - 1; l-\>next\[maxsize - 1\] = -1;

l-\>head = -1; l-\>tail = -1; l-\>free = 0;

return l;

“‘ Questa lista ha quindi una dimensione massima, ma può essere gestita come per le pile e le code, raddoppiando la dimensione degli array una volta raggiunto il limite: “‘c void realloc_lista_3a(lista_3a\* l)

int n = size_lista_3a(l); // si ri-allocano i 3 array di dimensione doppia l-\>info = (int\*) realloc(l-\>info, 2 \* n \* sizeof(int)); l-\>next = (int\*) realloc(l-\>next, 2 \* n \* sizeof(int)); l-\>prev = (int\*) realloc(l-\>prev, 2 \* n \* sizeof(int));

// si inizializza la seconda metà dei nuovi array int i; for(i = n ; i \< 2 \* n ; i++) l-\>info\[i\] = 0; l-\>next\[i\] = i + 1; l-\>prev\[i\] = i - 1; l-\>next\[ 2 \* (n - 1)\] = -1; l-\>prev\[n\] = -1;

/\* assegna come primo valore disponibile il primo valore della seconda metà dei nuovi array \*/ l-\>free = n;

“‘ Se la lista non comprende una gestione telescopia della memoria, quando si tenta di inserire un nuovo elemento genera un errore di *overflow*. Per aggiungere un nuovo elemento, chiama la funzione `allocate_column`, che rimuove un elemento dalla lista `free`, e ne restituisce l’indice. Analogamente, la funzione `free_column ` aggiunge un elemento di indice $i$ alla lista `free`: “‘c int allocate_column_lista_3a(lista_3a\* l)

if(l-\>free == -1) realloc_lista_3a(l);

int nuovo = l-\>free; l-\>free = l-\>next\[l-\>free\]; if(l-\>free != -1) l-\>prev\[l-\>free\] = -1;

return nuovo;

void free_column_lista_3a(lista_3a\* l, int i) if(i != -1) l-\>prev\[i\] = -1; l-\>next\[i\] = l-\>free; if(l-\>free != -1) l-\>prev\[l-\>free\] = i; l-\>free = i; “‘ Queste operazioni avvengono in tempo costante $\Theta(1)$. Per cui anche l’aggiunta e la rimozione per indice di un elemento avviene in tempo costante $\Theta(1)$: “‘c void add_head_lista_3a(lista_3a\* l ,int x)

// se l’indice libero è valido, si può aggiungere il nuovo elemento alla lista int i = allocate_column_lista_3a(l); l-\>info\[i\] = x;

l-\>prev\[i\] = -1; // si rende il nuovo elemento il primo della lista l-\>next\[i\] = l-\>head; // si collega alla vecchia testa

if(l-\>head != -1) // in caso la lista non è vuota l-\>prev\[l-\>head\] = i; // si collega la vecchia testa alla nuova testa else l-\>tail = i; // se la lista è vuota, diventa anche la coda l-\>head = i; // la nuova testa diventa l’indice allocato

void add_tail_lista_3a(lista_3a\* l, int x)

// se l’indice libero è valido, si può aggiungere il nuovo elemento alla lista int i=allocate_column_lista_3a(l); l-\>info\[i\] = x;

l-\>next\[i\] = -1; // si rende il nuovo elemento, l’ultimo della lista l-\>prev\[i\] = l-\>tail; // si collega alla vecchia coda

if(l-\>tail != -1) // se la lista non è vuota l-\>next\[l-\>tail\] = i; // si collega la vecchia coda alla nuova coda else l-\>head = i; // se la lista è vuota, diventa anche la testa l-\>tail = i; // la nuova coda diventa l’indice allocato

void delete_index_lista_3a(lista_3a\* l, int i) if(i == -1) return ; // controlla se non è un indice valido else if(i == l-\>head) // se è la testa, si scollega l-\>head = l-\>next\[l-\>head\]; if(l-\>head != -1) // se la lista non è vuota, si scollega l-\>prev\[l-\>head\] = -1; else if(i == l-\>tail) // se è la coda, si scollega l-\>tail = l-\>prev\[l-\>tail\]; if(l-\>tail != -1) // se la lista non vuota, si scollega l-\>next\[l-\>tail\] = -1; else l-\>next\[l-\>prev\[i\]\]=l-\>next\[i\]; l-\>prev\[l-\>next\[i\]\]=l-\>prev\[i\]; free_column_lista_3a(l,i);// si aggiunge alla lista degli indici liberi “‘ Mentre la rimozione per valore avviene in tempo costante nel caso migliore $\Theta(1)$, tempo lineare nel caso peggiore $\Theta(n)$, e nel caso medio $\Theta(n/2)=\Theta(n)$, poiché deve iterare sulla lista fino a quando non trova il valore dell’elemento: “‘c void delete_value_lista_3a(lista_3a\*l, int k) delete_index_lista_3a(l, search_lista_3a(l, k)); “‘ “‘c int search_lista_3a(lista_3a\* l, int k) int i = -1; int scorri = l-\>head; // scorre fino a trovare il primo elemento contenente k while(scorri != -1) if(l-\>info\[scorri\] == k) i = scorri; break; // quando trova l’elemento, ferma il loop scorri = l-\>next\[scorri\]; return i; // restituisce l’indice corrispondente “‘ Mentre altre operazioni come il calcolo della dimensione della lista avvengono sempre in tempo lineare $\Theta(n)$: “‘c int size_lista_3a(lista_3a\* l) int i = 0; int scorri = l-\>head; // scorre su tutti gli elementi della lista while(scorri != -1) i++; scorri = l-\>next\[scorri\]; return i; “‘

Invece di utilizzare tre array, è possibile utilizzare un singolo array di dimensione tripla rispetto agli array precedenti, dove gli interi sono accoppiati a gruppi di tre. Il primo rappresenta il valore contenuto nell’elemento, il secondo contiene l’indice del successivo, ed il terzo rappresenta l’indice del precedente. Dato un elemento identificato dal iteratore $i$, si ha quindi:

``` c
    l->all[i]       // valore contenuto in i
    l->all[i + 1]   // indice del successivo
    l->all[i + 2]   // indice del precedente 
```

Si può implementare su questo singolo array la gestione delle celle disponibili come: “‘c int allocate_object_lista_1a(lista_1a\* l) if(l-\>free == -1) realloc_lista_1a(l); int nuovo = l-\>free; l-\>free = l-\>all\[l-\>free + 1\]; if(l-\>free != -1) l-\>all\[l-\>free + 2\] = -1; return nuovo;

void free_object_lista_1a(lista_1a\* l, int i) if(i != -1) l-\>all\[i + 2\] = -1; l-\>all\[i + 1\] = l-\>free; if(l-\>free != -1) l-\>all\[l-\>free + 2\] = i; l-\>free = i;

int lowest_free_object_lista_1a(lista_1a\*l) int lowest = l-\>free; int scorri = l-\>free; while(scorri != -1) if(l-\>all\[scorri\] \< lowest) lowest = l-\>all\[scorri\]; scorri = l-\>all\[scorri + 2\]; return lowest; “‘ Le prime due funzioni avvengono in tempo costante $\Theta(1)$, mentre l’ultima avviene in tempo lineare $\Theta(n)$. L’aggiunta di un elemento in testa alla lista è analogo all’aggiunta di un elemento alla lista `free`. L’array può essere gestito in maniera telescopia anche con questa lista: “‘c void realloc_lista_1a(lista_1a\*l)

int n = size_lista_1a(l); l-\>all = (int\*) realloc(l-\>all, 6 \* n \* sizeof(int));

int i; for(i = n ; i \< 2 \* n ; i++) l-\>all\[3 \* i + 1\] = 3 \* (i + 1); // successivo l-\>all\[3 \* i + 2\] = 3 \* (i - 1); // precedente l-\>all\[3 \* n + 1\] = -1; l-\>all\[6 \* n - 1\] = -1;

l-\>free = 3 \* n;

“‘ “‘c int size_lista_1a(lista_1a\*l) int i = 0; int j; for(j = l-\>head ; j != -1 ; j = l-\>all\[j + 1\]) i++; return i; “‘

Su queste implementazioni è utile definire delle funzioni di supporto per estrarre le informazioni volute da un dato elemento, poiché è possibile l’array ulteriormente, in modo da rappresentare una lista di elementi eterogenei. In questo caso è presente un’altra casella che indica il numero di interi salvati per quell’indice. Per cui per un iteratore $i$ si ha:

``` c
    l->all[i]                   // numero di elementi
    l->all[i + 1]               // primo elemento salvato
    //...
    l->all[i + l->all[i]]       // ultimo elemento salvato
    l->all[i + l->all[i] + 1]   // elemento successivo
    l->all[i + l->all[i] + 2]   // elemento precedente
```

Quindi si possono definire le seguenti funzioni, per semplificare lo scorrimento in lista, e la visualizzazione dei sui contenuti: “‘c int next_lista_1b(lista_1b\* l, int i) return l-\>all\[i + l-\>all\[i\] + 1\];

int prev_lista_1b(lista_1b\* l, int i) return l-\>all\[i + l-\>all\[i\] + 2\];

int\* info_lista_1b(lista_1b\* l, int i) int\* info = (int\*) malloc(l-\>all\[i\] \* sizeof(int)); int j; for(j = 0 ; j \< l-\>all\[i\] ; j++) info\[j\] = l-\>all\[i + 1 + j\]; return info; “‘ Le prime due vengono eseguite in tempo costante $\Theta(1)$, mentre la funzione di visualizzazione ha complessità lineare $\Theta(m)$, dove $m$ è il numero di elementi salvati. L’inserimento di un elemento e la gestione della memoria avviene quindi come: “‘c int allocate_object_size_lista_1b(lista_1b\* l, int n) int j = l-\>free; for(j = 0 ; j != -1 ; j = next_lista_1b(l, j)) if(l-\>all\[j\] = n) break; return j;

void free_object_lista_1b(lista_1b\* l, int i) if(i != -1) l-\>all\[i + 2 + l-\>all\[i\]\] = -1; l-\>all\[i + 1 + l-\>all\[i\]\] = l-\>free; if(l-\>free != -1) l-\>all\[l-\>free + 2 + l-\>all\[i\]\] = i; l-\>free = i;

void add_head_lista_1b(lista_1b\* l, int\* A, int A_length) int i = allocate_object_size_lista_1b(l, A_length); if(i != -1) int j; for(j = 0 ; j \< A_length ; j++) l-\>all\[i + 1 + j\] = A\[j\]; l-\>all\[j\] = l-\>head; // successivo l-\>all\[j + 1\] = -1; // precedente if(l-\>head != -1) l-\>all\[l-\>head + l-\>all\[l-\>head\] + 2\]; l-\>head = i; “‘ La rimozione avviene in tempo costante $\Theta(1)$, mentre la ricerca di un elemento delle dimensioni necessarie avviene nel caso migliore in tempo costante $\Theta(1)$, mentre nel caso medio e nel caso peggiore in tempo lineare $\Theta(n)$. La funzione di aggiunta nel caso migliore impiega $\Theta(m)$, dove $m$ è la dimensione dell’array. Mentre nel caso peggiore impiega $\Theta(n+m)$, dove $n$ è la dimensione della lista. Nel caso medio impiega $\Theta(n/2+m)$.

Inoltre è possibile includere un altro intero che indica se l’elemento è stato rimosso o meno, invece di eseguire ad ogni rimozione la funzione di aggiunta alla lista `free`:

``` c
    l->all[i]                   // numero di elementi
    l->all[i + 1]               // elemento rimosso
    l->all[i + 2]               // primo elemento salvato
    //...
    l->all[i + l->all[i] + 1]   // ultimo elemento salvato
    l->all[i + l->all[i] + 2]   // elemento successivo
    l->all[i + l->all[i] + 3]   // elemento precedente
```

In questo modo si può eseguire una funzione apposita che assegna tutti gli elementi segnati come rimossi alla lista `free`: “‘c void delete_lista_1c(lista_1c\* l, int i) l-\>all\[i + 1\] = 0;

void free_object_lista_1c(lista_1c\* l, int i) if(i != -1) l-\>all\[i + 3 + l-\>all\[i\]\] = -1; l-\>all\[i + 2 + l-\>all\[i\]\] = l-\>free; if(l-\>free != -1) l-\>all\[l-\>free + 3 + l-\>all\[i\]\] = i; l-\>free = i;

void garbage_collection(lista_1c\* l) int i; for(i = l-\>head ; i!= -1 ; i = next_lista_1b((lista_1b\*) l, i) + 1) if(!l-\>all\[i + 1\]) free_object_lista_1c(l, i); “‘

### Liste Tramite Oggetti

In caso il linguaggio di programmazione dove si vuole implementare l’ADT supporta la creazione di oggetti e l’uso di riferimenti ad oggetto, è possibile utilizzarli per realizzare l’ADT in modo più naturale, e soprattutto leggibile. Lo pseudocodice, così come il linguaggio C, è uno di questi linguaggi adatti. Si implementa quindi il tipo astratto lista, *singolarmente* o *doppiamente concatenata* utilizzando oggetti e riferimenti. Da considerare che si possono implementare pile e code, come casi particolari di liste, per cui anche questi ADT possono essere realizzati con oggetti e riferimenti. L’utilizzo di oggetti e riferimenti è più efficiente in termini di memoria, poiché non viene limitato dalla dimensione dell’array, stabilita priori. Inoltre permette un inserimento sempre costante, poiché la creazione di un nuovo oggetto avviene in tempo costante $\Theta(1)$. Mentre per per un ADT implementato su un array, ciò può essere solo ammortizzato a tempo costante $\Theta(1)$, se viene permesso di aumentare la dimensione dell’array. Inoltre utilizzare un array comporta uno spreco di memoria, se non viene fornito a priori il numero di elementi che verranno salvati su di esso, molto probabilmente verrà allocato spazio all’array che non verrà poi utilizzato per memorizzare alcun dato. Quindi quando si lavora su insiemi di dimensione molto elevata, è preferibile l’uso di oggetti e riferimenti.

Viene quindi definita la struttura `nodo`, che rappresenta un elemento salvato nella lista. Questo oggetto contiene il valore contenuto dall’elemento, in questo caso un intero, il riferimento all’oggetto successivo, ed in caso sia doppiamente concatenata il riferimento all’oggetto precedente. Questo permette un accesso in tempo costante $\Theta(1)$ in avanti e all’indietro. La lista è quindi un riferimento al primo nodo salvato, mentre se è implementata con accesso agli estremi, può essere realizzata come un array che presenta all’indice $0$ il riferimento al primo nodo della lista, e all’indice seguente $1$ il riferimento all’ultimo nodo della lista. L’iteratore è quindi rappresentato da un riferimento a nodo `nodo*`, e l’iteratore non valido viene descritto dal puntatore a `NULL`: “‘c lista_d\* new_lista_d() lista_d\* l = (lista_d\*) malloc(sizeof(lista_d)); \*l = NULL; return l; “‘ “‘c nodo_d\* new_nodo_d(int z, nodo_d\* i, nodo_d\* j) nodo_d\* nuovo = (nodo_d\*) malloc(sizeof(nodo_d)); nuovo-\>info = z; nuovo-\>next = i; nuovo-\>prev = j; return nuovo; “‘ In questa implementazione il dato salvato dentro al nodo è un intero, ma può essere utilizzato un riferimento ad un oggetto esterno, per memorizzare il tipo di dato richiesto dall’utilizzo della lista.

Per consultare la lista si utilizza l’operazione `i->next` che restituisce l’iteratore corrispondente all’elemento successivo salvato in lista, oppure `i->prev`.

Gli inserimenti e le eliminazioni vengono implementati secondo la stessa logica. Bisogna modificare i campi `next` e `prev` dei nodi considerati, ed eventualmente il riferimento al primo nodo della lista, analogamente alle *operazioni* implementate su array. A differenza dell’array bisogna anche de-allocare i nodi eliminati. Valgono le stesse considerazioni generali effettuate per il tipo astratto di dato lista, sulla complessità di queste operazioni: “‘c void add_head_lista_d(lista_d\* l, int z) nodo_d\* nuovo = new_nodo_d(z, \*l, NULL); if(\*l != NULL) (\*l)-\>prev = nuovo; \*l = nuovo; “‘ “‘c void add_tail_lista_d(lista_d\* l, int z)

if(\*l == NULL) add_head_lista_d(l, z); else

nodo_d\* scorri = \*l; while(scorri-\>next != NULL) scorri = scorri-\>next;

scorri-\>next = new_nodo_d(z, NULL, scorri);

“‘ “‘c void delete_node_lista_d(lista_d\* l, nodo_d\* i) if(i == NULL) return; if(i-\>prev != NULL) i-\>prev-\>next = i-\>next; if(i-\>next != NULL) i-\>next-\>prev = i-\>prev; if(\*l == i) \*l = i-\>next; free(i); “‘ Una lista realizzata come riferimento alla testa avrà un’accesso in tempo lineare alla coda $\Theta(n)$, se fosse implementate come un array di riferimenti a nodi, sarebbe possibile aggiungere ed eliminare un elemento in coda in tempo costante $\Theta(1)$.

In questo modo è possibile realizzare delle pile e delle code senza limitazioni sulla loro dimensione utilizzando oggetti e riferimenti e liste doppiamente concatenate. “‘c pila_lista\* new_stack_list() return new_lista_d();

int is_empty_stack_list(pila_lista\* p) return \*p==NULL;

void push_list(pila_lista\* p, int z) add_head_lista_d(p,z);

int pop_list(pila_lista\* p) if(\*p==NULL) printf("errore di underflow"); else int temp=(\*p)-\>info; delete_head_lista_d(p); return temp; “‘ “‘c coda_lista\* new_queue_list() lista_d\* c=(lista_d\*)malloc(2\*sizeof(lista_d)); \*c=NULL; \*(c+1)=NULL; return c;

int is_empty_queue_list(coda_lista\* c) return c\[0\]==NULL;

void enqueue_list(coda_lista\* c, int z) if(c\[0\]!=NULL) add_head_lista_d(c,z); else c\[0\]=new_nodo_d(z,NULL,NULL); c\[1\]=c\[0\];

int dequeue_list(coda_lista\* c) if(c\[0\]==NULL) printf("errore di underflow"); else int temp=c\[1\]-\>info; nodo_d\* temp_d=c\[1\]; c\[1\]=c\[1\]-\>prev; delete_node_lista_d(c,temp_d); return temp; “‘ In questo modo si ottengono delle operazioni di aggiunta e rimozione in tempo costante $\Theta(1)$.

Data una lista implementata con oggetti e riferimenti, è possibile invertire la lista in tempo lineare $\Theta(n)$. Un altro pregio di queste liste implementate con oggetti e riferimenti è la possibilità di unire due liste insieme, senza la necessità di copiare entrambe le strutture su di un’altra, risparmiando così spazio in memoria e tempo di compilazione. In questo modo si possono accodare due liste in tempo lineare $\Theta(n)$, oppure se sono implementate con *accesso agli estremi* in tempo costante $\Theta(1)$. Un’altra caratteristica delle liste consiste nella possibilità di implementare il *merge sort* senza allocare memoria aggiuntiva per salvare i dati. Questo viene ottenuto, iterando su ogni elemento della lista e collegandolo ad una nuova lista, solamente modificando gli attributi `next` e `prev` del nodo. La fusione di due liste si svolge come per gli array in tempo lineare $\Theta(n)$. Per cui la complessità temporale del *merge sort* per una lista è $\Theta(n\cdot\log n)$, mentre la sua occupazione in memoria consiste solamente delle chiamate ricorsive sullo *stack* quindi consiste in $\Theta(\log n)$.

Inoltre quest’implementazione fornisce un’ulteriore vantaggio, la possibilità di creare un nodo fittizio o sentinella, come iteratore non valido, invece del riferimento non valido. In questo modo effettivamente si crea una lista circolare, se la lista è doppiamente concatenata, la sentinella fornisce così un accesso agli estremi, poiché alla lista si accede tramite l’iteratore non valido. In questa implementazione molte procedure, come l’aggiunta e la rimozione di un nodo generico, risultano notevolmente semplificate, per non dover controllare la validità del riferimento, poiché la sentinelle rappresenta una zona di memoria accessibile, al contrario di `NULL. ` La lista vuota quindi coincide alla sola sentinella, che presenta nei campi precedente e successivo il riferimento a sé stessa: “‘c lista_c\* new_lista_c() lista_c\* l = (lista_c\*)malloc(sizeof(lista_c)); nodo_d\* null = (nodo_d\*)malloc(sizeof(nodo_d)); null-\>next = null; null-\>prev = null; \*l = null; return l; “‘ “‘c void add_head_lista_c(lista_c\* l, int z) if(\*l == (\*l)-\>next) (\*l)-\>next = new_nodo_d(z,\*l,\*l); (\*l)-\>prev = (\*l)-\>next; else nodo_d\* nuovo = new_nodo_d(z,(\*l)-\>next, \*l); (\*l)-\>next-\>prev = nuovo; (\*l)-\>next = nuovo;

void delete_node_lista_c(lista_c\* l, nodo_d\* i) if(i == \*l) return; nodo_d\* del = i; i-\>prev-\>next = i-\>next; i-\>next-\>prev = i-\>prev; free(del); “‘ L’operazione di eliminazione di un nodo in coda è analoga all’eliminazione in testa. La complessità è sempre costante $\Theta(1)$, ma il codice è molto più leggibile.

# Alberi Radicati

Il tipo astratto di dato *albero radicato* è una struttura di dati che utilizza una serie di oggetti chiamati nodi, per conservare le informazioni. Questo ADT è quindi un insieme di questi nodi, dove viene definita la relazione binaria “è figlio di”, invertendo i due input si ottiene la relazione equivalente “è genitore di”. Questa relazione deve rispettare due condizioni, per ogni nodo dell’insieme:

- Ogni nodo ha un solo genitore, tranne il nodo *radice* che non ha genitori;

- Da qualsiasi nodo è possibile raggiungere la radice, tramite un *cammino*, per cui si dice che l’albero è connesso.

Data la *radice* è possibile costruire un albero radicato, aggiungendo ogni volta un nuovo nodo, come figlio di un altro nodo preesistente. Due nodi si dicono *fratelli* se condividono lo stesso genitore. Si definisce il *grado* di un nodo, il numero dei suoi figli. I nodi che non presentano figli, ovvero, nodi di grado zero, vengono definite *foglie* dell’albero. Mentre un nodo di grado superiore o uguale ad uno si dice nodo interno all’albero.

Sulla base di queste considerazioni si possono realizzare due tipi diversi di alberi:

- *Alberi Binari*: sono alberi dove ogni nodo può essere al massimo di grado due;

- *Alberi di Grado Arbitrario*: sono alberi dove ogni nodo può avere un numero qualsiasi di figli.

Quindi in un *albero binario* ogni nodo viene caratterizzato da un figlio sinistro ed un figlio destro, per cui la posizione reciproca tra i nodi è rilevante. E si l’avere un singolo figlio sinistro o destro. Mentre in un *albero di grado arbitrario* non si distinguono i figli, per cui la loro posizione reciproca non è rilevante.

Viene definito *cammino* di un albero il percorso che attraversa una sequenza di nodi, dove ogni nodo è il genitore del successivo. Ogni connessione tra due nodi viene identificata da un *arco*. Il numero di archi su un cammino rappresenta la *lunghezza* di quest’ultimo. La lunghezza del cammino di un nodo qualsiasi dalla radice si definisce la *profondità* del nodo. Mentre la lunghezza del cammino più lungo tra la radice ad una foglia viene chiamata *altezza* dell’albero, rappresenta la profondità del nodo più profondo. Un nodo si dice *antenato* di un altro, se è presente nel cammino che collega quest’ultimo alla radice. Mentre il nodo da cui parte il cammino si dice *discendente* di ogni nodo sul suo cammino fino alla radice. L’insieme dei nodi costituito da un nodo, e da tutti i suoi discendenti rappresenta un *sotto-albero* dell’albero originario, radicato nel nodo stesso. Se l’ordine dei figli è significativo si indica come albero *ordinato*

L’ADT albero viene definito dai seguenti *insiemi*:

- L’insieme degli alberi di interi $\mathbb{T}$;

- L’insieme dei riferimenti ai nodi $\mathbb{R}$, che identificano le posizioni nell’albero;

- L’insieme degli interi $\mathbb{Z}$;

- L’insieme dei booleani $\mathbb{B}$.

La *costante* è l’albero vuoto, restituito dall’*operazione* `new_tree`.

Le *operazioni* di aggiunta, rimozione e consultazione per riferimento avvengono in tempo costante $\Theta(1)$:

- `root`: $\mathbb{T}\to\mathbb{R}$, restituisce il riferimento alla radice dell’albero;

- `left`; `right`: $\mathbb{T}\times\mathbb{R}\to\mathbb{R}$, restituisce il riferimento al figlio sinistro o destro;

- `is_empty`: $\mathbb{T}\to\mathbb{B}$, verifica se l’albero è vuoto;

- `add_root`: $\mathbb{T}\times\mathbb{Z}\to\mathbb{T}$, inserisce la radice in un albero vuoto;

- `add_left`; `add_right`: $\mathbb{T}\times\mathbb{R}\times\mathbb{Z}\to\mathbb{T}$, inserisce un figlio sinistro o destro ad un nodo;

- `delete_leaf`: $\mathbb{T}\times{\mathbb{R}}\to\mathbb{T}$, rimuove una foglia dall’albero;

- `empty`: $\mathbb{T}\to\mathbb{T}$, svuota l’albero.

Per gli alberi di grado arbitrario invece delle *operazioni* di aggiunta sinistra o destra, si definiscono *operazioni* di aggiunta di un fratello sinistro o destro, insieme con delle *operazioni* di consultazione:

- `first_sibling`: $\mathbb{T}\times\mathbb{R}\to\mathbb{R}$, restituisce il riferimento al primo figlio di un nodo;

- `last_sibling`: $\mathbb{T}\times\mathbb{R}\to\mathbb{R}$, restituisce il riferimento all’ultimo figlio di un nodo;

- `add_left_sibling`: $\mathbb{T}\times\mathbb{R}\times\mathbb{Z}\to\mathbb{T}$, inserisce un fratello sinistro ad un nodo;

- `add_right_sibling`: $\mathbb{T}\times\mathbb{R}\times\mathbb{Z}\to\mathbb{T}$, inserisce un fratello destro ad un nodo;

Queste funzioni hanno complessità costante $\Theta(1)$, eccetto la funzione di ricerca dell’ultimo fratello di complessità lineare $\Theta(m)$, dove $m$ è il numero dei fratelli. Le *operazioni* di ricerca di un elemento specifico, di conteggio del numero dei nodi o delle foglie, il calcolo dell’altezza dell’albero, e la ricerca di massimo e minimo, avvengono in tempo lineare $\Theta(n)$, dove $n$ rappresenta il numero di nodi nell’albero:

- `size`: $\mathbb{T}\to\mathbb{Z}$, restituisce il numero di nodi nell’albero;

- `height`: $\mathbb{T}\to\mathbb{Z}$, restituisce l’altezza dell’albero;

- `leaves`: $\mathbb{T}\to\mathbb{Z}$, restituisce il numero di foglie dell’albero;

- `search`: $\mathbb{T}\times\mathbb{Z}\to\mathbb{R}$, restituisce il riferimento ad un nodo contenete un certo valore, oppure il riferimento non valido in caso non esista;

- `max`; `min`: $\mathbb{T}\to\mathbb{Z}$, restituisce il valore massimo o minimo contenuto nell’albero.

Utilizzando implementazioni diverse di albero è possibile diminuire la complessità di queste operazioni. Ciò viene ottenuto applicando restrizioni sull’aggiunta di elementi all’albero, per renderlo bilanciato, e favorire la ricerca di elementi per valore.

Le procedure di complessità lineare $\Theta(n)$, devono attraversare l’intero albero, ma non essendo una struttura dati lineare, non è banale il metodo in cui bisogna procedere. Sono possibili due principali strategie per attraversare ricorsivamente un albero, inoltre se rappresenta un albero binario è possibile adoperare una strategia intermedia tra le due:

- *Visita in Pre-Ordine* “Pre-Order Traversal”: si effettuano le operazioni sul nodo, prima di passare ai figli;

- *Visita in Post-Ordine* “Post-Order Traversal”: si effettuano le operazioni ai figli, prima di passare al nodo.

Queste due strategie sono quindi una l’opposto dell’altra, nella prima le operazioni vengono effettuate dall’alto verso il basso, mentre nella seconda dal basso verso l’alto e permettono di visitare l’intero albero con relativa semplicità. Se l’albero è un albero binario è possibile applicare una *visita simmetrica* “In-Order Traversal”, processando prima il figlio sinistro, poi il nodo ed infine il figlio destro.

Nella visita in pre-ordine, si suppone di possedere il risultato della procedura sul genitore, così quando si arriva al nodo corrente, si effettuano le operazioni conoscendo questi parametri, e viene chiamata ricorsivamente la procedura sui figlia, passando i parametri così calcolati. Nella visita in post-ordine, si chiama ricorsivamente la procedura sui suoi figli, così quando si arriva al nodo corrente, si effettuano le operazioni conoscendo questi parametri e la fornisce dei parametri alla procedura lanciata dal genitore.

Nella visita simmetrica, quando si arriva ad un nodo generico si chiama la procedura sul figlio sinistro, poi processa i dati ottenuti da questa chiamata, insieme ai parametri del nodo, ed ai parametri forniti dal genitore, in seguito chiama ricorsivamente la procedura sul figlio destro, fornendo eventuali parametri, ed alla fine fornisce un risultato alla procedura chiamata dal genitore.

## Alberi Binari

Un albero binario è un tipo di albero ordinato dove ogni nodo può avere al massimo due figli. Si dice *completo* quando ogni nodo, eccetto le foglie, è di grado due. Per cui dato un albero binario completo è possibile mettere in relazione l’altezza, il numero dei nodi, ed il numero delle foglie. Poiché ogni nodo ha due figli, quando è completo, il numero di nodi dell’albero $n$ può essere ottenuto data la sua altezza $h$ come: $$n=2^{h+1}-1$$ Il numero di foglie invece corrisponde al numero di nodi sull’ultimo livello dell’albero, per cui si ha: $$n_f=2^h\iff h=\log_2n_f$$ Quindi il numero dei nodi interni si può esprimere come: $$n_i=n-n_f=2^{h+1}-1-2^h=2\cdot2^h-2^h-1=2^h-1$$

Come le liste, possono essere realizzati con oggetti e riferimenti, dove ogni nodo dell’albero binario presenta quattro campi. I riferimenti vengono inizializzati a `NULL ` e permettono di definire l’albero come un riferimento al nodo radice dell’albero: L’albero è quindi vuoto quando il riferimento della radice corrisponde al puntatore non valido. Vengono descritte ora le funzioni di aggiunta e di ricerca: “‘c nodo\* new_nodo_bin(int z, nodo\* parent, nodo\* left, nodo\* right) nodo\* nuovo=(nodo\*)malloc(sizeof(nodo)); nuovo-\>info=z; nuovo-\>parent=parent; nuovo-\>left=left; nuovo-\>right=right; return nuovo;

void add_root_bin(albero_bin\* t, int z) \*t = new_nodo_bin(z, NULL, NULL, NULL); “‘ “‘c void add_left_bin(nodo\* n, int z) n-\>left = new_nodo_bin(z, n, NULL, NULL);

void add_right_bin(nodo\* n, int z) n-\>right = new_nodo_bin(z, n, NULL, NULL); “‘ “‘c nodo\* search_bin(albero_bin\* t, int z) if(\*t == NULL \|\| (\*t)-\>info == z) return \*t; else nodo\* temp = search_bin(&(\*t)-\>left, z); if(temp != NULL) return temp; else return search_bin(&(\*t)-\>right, z); “‘ Non si descrive l’operazione di eliminazione di un nodo, poiché richiede specifiche su come ri-ordinare l’albero dopo la rimozione. Verrà trattata nello specifico per alberi binari di ricerca, dove la posizione dei nodi è significativa.

Per effettuare operazioni che richiedono la visita sull’intero albero, si possono realizzare semplicemente applicando una visita in pre-ordine, post-ordine o simmetrica: “‘c int greater(int a, int b) if (a\>b) return a; return b;

int height_bin(albero_bin\* t) if(\*t==NULL) return -1; return 1 + greater(height_bin(&((\*t)-\>left)), height_bin(&((\*t)-\>right)));

int leaves_bin(albero_bin\* t) if(\*t == NULL) return 0; return ((\*t)-\>left == NULL && (\*t)-\>right == NULL) + leaves_bin(&((\*t)-\>left)) + leaves_bin(&((\*t)-\>right)); “‘ “‘c int nodes_bin(albero_bin\* t) if(\*t == NULL) return 0; return 1 + nodes_bin(&((\*t)-\>left)) + nodes_bin(&((\*t)-\>right)); “‘ Inoltre si possono calcolare attraverso una singola visita invece di attraversa più volte l’albero, anche se presentano la stessa complessità asintotica $\Theta(n)$, per piccoli input è preferibile operare attraverso una singola visita, per diminuire il tempo necessario alla procedura.

## Alberi di Grado Arbitrario

Per realizzare alberi di grado arbitrario, bisogna fornire ad ogni nodo un modo efficiente per accedere ai loro fratelli, oppure accedere ai loro figli, senza sapere a priori il loro numero. Sono quindi possibili due realizzazioni, una prima implementazione utilizza liste di riferimenti a nodo, che rappresentano i figli di un nodo. Per cui in questa prima implementazione tramite liste ogni nodo contiene un campo che rappresenta una lista, contenente i riferimenti a tutti i suoi figli. Se il nodo è una foglia, questa lista è vuota. Questa strategia di implementazione prevede molte operazioni aggiuntive per la gestione della lista, non dispendiose in termini di tempo, ma diminuiscono la leggibilità del codice, per invece di questa implementazione, si favorisce la strategia chiamata “figlio-sinistro-fratello-destro”.

In questa implementazione vengono usati solo nodi, senza definire altri oggetti. L’oggetto nodo utilizzato corrisponde al nodo definito per gli alberi binari, presenta quindi gli stessi campi, ma in questo caso l’attributo `right` invece che al figlio destro, è un riferimento al fratello destro:

``` c
/* nodo di un albero di grado arbitrario implementato 
   secondo la strategia ``figlio-sinistro-fratello-destro'' */
typedef struct Nodo{
    struct Nodo* left;      // riferimento al primo figlio a sinistra
    struct Nodo* right;     // riferimento al primo fratello a destra
    int info;               // dato contenuto nel nodo
    struct Nodo* parent;    // riferimento al genitore
}nodo;

// albero di grado arbitrario definito come un riferimento della radice dell'albero 
typedef nodo* albero_a;
```

In questo modo si può diminuire di gran lunga la complessità di realizzazione delle operazioni su alberi di grado arbitrario, aumentando la leggibilità del codice. Le *operazioni* di creazione della *costante*, di aggiunta della radice e di un fratello a destra avvengo in tempo costante $\Theta(1)$. “‘c albero_a\* new_tree_a() albero_a\* t = (albero_a\*) malloc(sizeof(albero_a)); \*t = NULL; return t;

nodo\* new_nodo_a(int z, nodo\* left, nodo\* right, nodo\* parent) nodo\* nuovo = (nodo\*) malloc(sizeof(nodo)); nuovo-\>parent = parent; nuovo-\>left = left; nuovo-\>right = right; nuovo-\>info = z; return nuovo;

void add_root_a(albero_a\* t, int z) \*t = new_nodo_a(z, NULL, NULL, NULL); “‘ “‘c void add_right_sibling_a(albero_a\* t, nodo\* n, int z) if(\*t == n) return ; nodo\* nuovo = new_nodo_a(z, NULL, n-\>right, n-\>parent); n-\>right = nuovo; “‘ L’aggiunta di un fratello a sinistra prevede lo scorrimento su tutti i figli fino a raggiungere il fratello a sinistra, per poter cambiare il suo campo `right`, quindi ha una complessità lineare $\Theta(m)$, dove $m$ è il numero dei suoi fratelli: “‘c nodo\* left_sibling_a(albero_a\* t, nodo\* n)

if(n == NULL \|\| n-\>parent == NULL \|\| n-\>parent-\>left == n) return NULL; nodo\* scorri = n-\>parent-\>left; while(scorri-\>right != n) scorri = scorri-\>right; return scorri;

void add_left_sibling_a(albero_a\* t, nodo\* n, int z) if(\*t==n) return ; nodo\* nuovo = new_nodo_a(z, NULL, n, n-\>parent); nodo\* temp = left_sibling_a(t, n); if(temp!=NULL) temp-\>right = nuovo; else n-\>parent-\>left = nuovo; “‘ Mentre la ricerca di un nodo contenente un valore specifico ha complessità lineare $\Theta(n)$, dove $n$ è il numero dei nodi nell’albero: “‘c nodo\* search_a(albero_a\* t, int k) if(\*t == NULL \|\| (\*t)-\>info == k) return \*t; nodo\* temp = search_a(&((\*t)-\>left),k); if(temp != NULL) return temp; return search_a(&((\*t)-\>right),k); “‘

Inoltre è utile definire un’*operazione* per controllare se l’albero di grado arbitrario è anche un albero binario, cià viene effettuato semplicemente applicando una visita in pre-ordine o post-ordine sull’albero, e controllando che ogni nodo abbia al massimo due figli, in tempo lineare $\Theta(n)$.

## Heap

Una coda di priorità è una struttura di dati dove ogni elemento viene associato ad un valore di priorità, su cui viene definito un ordinamento. Su questa struttura dati si vogliono eseguire due *operazioni* principali efficientemente, l’inserimento di un nuovo elemento, con valore arbitrario di priorità, e la rimozione dell’elemento a più alta priorità.

Questa struttura di dati può essere utilizzata per allocare processi a risorse condivise, associando ogni richiesta di un processo per una specifica risorsa, ad un valore di priorità generato durante l’esecuzione. In questo modo viene assegnata la risorsa al processo di più alta priorità. Oppure possono essere utilizzate per rappresentare un sistema complesso dove la coda è formata da eventi e la loro priorità è il tempo in cui si devono verificare. La coda simula quindi l’evoluzione temporale del sistema, ed ogni estrazione dalla coda rappresenta un accadimento di un evento, e può comprendere l’inserimento in coda di altri eventi distanziati temporalmente.

La struttura di dati coda di priorità può essere realizzata considerando l’elemento a più alta priorità o a più bassa priorità. In generale una coda di priorità viene definito dai seguenti *domini*:

- L’insieme delle code di priorità $\mathbb{Q}$;

- L’insieme degli interi $\mathbb{Z}$;

- L’insieme dei booleani $\mathbb{B}$.

La *costante* è la coda vuota, fornita dalla procedura `new_queue`. Si definiscono ora le *operazioni* della coda di priorità:

- `insert`: $\mathbb{Q}\times\mathbb{Z}\to\mathbb{Q}$, inserisce un elemento, di priorità arbitraria, nella cosa;

- `maximum`, oppure `minimum`: $\mathbb{Q}\to\mathbb{Z}$, restituisce l’elemento a più alta (o più bassa) priorità;

- `extract_max`, oppure `extract_min`: $\mathbb{Q}\to\mathbb{Q}\times\mathbb{Z}$, estrae e restituisce l’elemento a più alta (o più bassa) priorità dalla coda;

- `is_empty`: $\mathbb{Q}\to\mathbb{B}$, verifica se la coda è vuota.

Una coda di priorità si può realizzare utilizzando una struttura dati lineare come una lista, ma presenta delle limitazioni intrinseche. La rimozione dell’elemento a più alta priorità avverrebbe in tempo costante $\Theta(1)$, ma l’inserimento di un nuovo elemento richiederebbe tempo lineare $\Theta(n)$. Altrimenti in caso si usasse una lista non ordinata, l’inserimento avverrebbe in tempo costante $\Theta(1)$, ma non essendo ordinata, sarebbe necessario cercare su tutta la lista l’elemento a più alta priorità, risultando quindi in un’operazione in tempo lineare $\Theta(n)$.

Queste due realizzazioni sono inefficienti, poiché almeno una delle operazioni avviene in tempo lineare. Quindi si cerca una struttura di dati in cui sia la rimozione che l’inserimento avvengono in tempo logaritmico $\Theta(\log n)$. Ciò viene realizzato tramite la struttura dati *heap*, può essere sia un *max-heap* che un *min-heap*, ma verrà analizzata solamente la `max_heap`, è un array dove la posizione degli elementi è in relazione con il loro valore. Possono essere rappresentati come degli alberi binari *quasi completi*, ovvero alberi che possono essere incompleti nella loro parte destra. L’heap codifica un albero binario quasi completo ad ogni livello, su un array `A`, di lunghezza `A_length`. La radice dell’albero si trova all’indice $0$, mentre per un generico nodo $i$, i suoi figli si trovano alla posizione $2i+1$ e $2i+2$, mentre il suo genitore si trova all’indice $\lfloor(i-1)/2\rfloor$. Per semplificare la leggibilità del codice è possibile implementare semplici funzioni di consultazione: “‘c int parent(int i) return (i - 1)/2;

int left(int i) return 2\*i + 1;

int right(int i) return 2\*i + 2;

“‘ Inoltre si suppone che la coda comprenda solo valori fino ad un indice `size` nell’array. Per cui l’heap è costituito da tre campi, la lunghezza della coda di priorità, la lunghezza dell’array e il riferimento al primo elemento dell’array.

In un *max-heap* il valore contenuto in un nodo $i$ è maggiore uguale del valore contenuto in tutti i suoi discendenti, ed il valore massimo viene memorizzato all’indice $0$. Mentre in un *min-heap* ogni nodo $i$ contiene un valore minore o uguale dei suoi discendenti.

Si dimostra che se un heap rappresenta un albero binario quasi completo di dimensione $n$, allora sono presenti $\lfloor n/2\rfloor$ nodi interni, corrispondenti agli indici da $0$ a $\lfloor n/2\rfloor-1$. Si considera un albero binario completo di altezza $h$, per cui ha $2^h-1$ nodi interni e $2^{h+1}-1$ nodi, quindi è verificata la relazione: $$\displaystyle\left\lfloor\frac{n}{2}\right\rfloor=\left\lfloor \frac{2^{h+1}-1}{2} \right\rfloor=2^h-\left\lfloor\frac{1}{2}\right\rfloor=2^h-1$$ Ora si rimuove un figlio destro da un qualsiasi nodo, poiché l’albero ha un numero dispari di nodi, rimuovendo un nodo, il numero dei nodi interni non cambia: $$\left\lfloor\displaystyle\frac{n}{2}\right\rfloor=\left\lfloor\frac{n-1}{2}\right\rfloor=\left\lfloor\frac{n'}{2}\right\rfloor$$ L’albero ha un numero dispari di nodi poiché è un albero binario quasi completo dove ogni nodo è di grado due oppure è una foglia, per cui il numero di nodi totali è dispari, rimuovendo un figlio destro diventa quindi pari. Si considera ora una rimozione di un figlio sinistro, avendo ora un numero $n$ pari di nodi nell’albero, per cui: $$\left\lfloor\displaystyle\frac{n}{2}\right\rfloor=\left\lfloor\frac{n-1}{2}\right\rfloor+1$$ Dopo la rimozione il numero dei nodi diminuisce di uno $n'=n-1$, mentre il numero dei nodi interni diminuisce anch’esso di uno, poiché il nodo da cui viene rimosso il figlio sinistro diventa una foglia: $$\left\lfloor\displaystyle\frac{n-1}{2}\right\rfloor=\left\lfloor\frac{n'}{2}\right\rfloor=\left\lfloor\frac{n}{2}\right\rfloor-1$$ Per cui la relazione è verificata per ogni albero binario quasi completo.

Per trasformare un albero quasi completo, salvato su un array `A`, in un *max-heap* si definisce la procedura `max_heapify`, che prende come parametri un riferimento ad un heap, contenente l’albero, ed un indice $i$ dove è radicato l’albero. In caso sia l’albero intero l’indice $i$ corrisponde a zero, altrimenti rappresenta un sotto-albero radicato in $i$. Questa procedura itera su ogni nodo del sotto-albero radicato in $i$ ricorsivamente trasformandolo in un *max-heap*: “‘c void max_heapify(heap\* h, int i)

int l = left(i); int r = right(i); int i_max = i; if(l \<= h-\>size-1 && h-\>A\[l\] \> h-\>A\[i_max\]) i_max = l; if(r \<= h-\>size-1 && h-\>A\[r\] \> h-\>A\[i_max\]) i_max = r;

if(i_max != i) swap(h-\>A, i, i_max); max_heapify(h, i_max);

“‘ Questa funzione trova il valore maggiore, tra i valori contenuti nel nodo, e nei suoi figli. In caso è presente in uno dei suoi figli, per renderlo un *max-heap* deve sostituire i valori contenuti nel nodo corrente e nel figlio di valore maggiore, altrimenti termina la sua esecuzione. Se ha scambiato i valori invece, deve chiamare di nuovo la procedura, ora sull’indice corrispondente al figlio che ha sostituito il nodo per renderlo un *max-heap*. Le operazioni di assegnazione e scambio avvengono in tempo costante $\Theta(1)$, per cui la complessità temporale della procedura deriva dalle sue chiamate ricorsive su un sotto-albero radicato di dimensione minore. Il caso peggiore avviene quando è necessario chiamare la procedura sul sotto-albero radicato di altezza $h-1$, dove $h$ è l’altezza dell’albero binario quasi completo. Ciò avviene quando si chiama la procedura sulla radice dell’albero, i suoi figli sono quindi sotto-alberi di altezza $h-1$ uno e $h-2$ l’altro, poiché si tratta di un albero quasi completo. Per cui il numero di nodi nel sotto-albero più pesante sono $2/3$ del numero di nodi totali $n$. Si può quindi esprimere il tempo di calcolo $T(n)$ tramite la seguente disequazione di ricorrenza: $$T(n)\leq T\left(\displaystyle\frac{2n}{3}\right)+c$$ Questa viene risolta tramite il teorema dell’esperto con $a=1$, $b=3/2$ e $k=0$, per cui la sua espressione deriva dal caso $a=b^k$: $$T(n)\in\Theta(n^k\cdot\log n)=\Theta(\log n)$$ Quindi nel caso migliore ha un tempo di esecuzione costante $\Theta(1)$, mentre nel caso peggiore ha un tempo logaritmico $\Theta(1)\cdot\Theta(\log n)=\Theta(\log n)$. Per trasformare un’array in un *max-heap* bisogna iterare su tutti i nodi interni e chiamare la procedura `max_heapify`. La lunghezza dell’array corrisponde al numero dei nodi dell’albero, per cui per iterare sui solo nodi interni, bisogna considerare tutti gli indici minori di $\left\lfloor n/2\right\rfloor$, dove $n$ è la lunghezza dell’array. Quindi si itera partendo da $i=\left\lfloor n/2\right\rfloor$ fino a raggiungere la radice a $i=0$. Tutti gli elementi di indice maggiore sono degli heap con un solo elemento. La procedura `build_max_heap ` è quindi definita come: “‘c void build_max_heap(heap\* h, int\* A1, int len_A1) h-\>A_length = len_A1; h-\>A = A1; helper_build_max_heap(h);

void helper_build_max_heap(heap\* h) h-\>size = h-\>A_length; int i; for(i = (h-\>A_length)/2 - 1 ; i \>= 0 ; i–) max_heapify(h, i); “‘ Le operazioni di assegnazione avvengono in tempo costante $\Theta(1)$, mentre l’istruzione iterativa ripete $n$ volte la procedura di costruzione di un *max-heap*. Ha quindi un costo $\Theta(n)\cdot\Theta(\log n')$, dove $n'$ è il numero di nodi del sotto-albero radicato all’indice corrente. Poiché $n'\leq n$, si ha che $\Theta(\log n')\subseteq O(\log n)$, per cui ha un tempo massimo di esecuzione definito dalla relazione $O(n\cdot\log n)$. Ma questo non rappresenta un limite asintoticamente stretto sul tempo di esecuzione. Per cui si dimostra ora come questa procedura abbia una complessità lineare $\Theta(n)$.

La sua complessità coincide alla somma di tutte le altezze dei sotto-alberi radicati ai nodi dell’albero $S(n)$. Si vuole quindi calcolare asintoticamente questa espressione. L’altezza di un albero binario completo, avente $n$ nodi si ottiene mediante la seguente relazione: $$h=\log(n+1)-1$$ Si dimostra per induzione come $S(n)$ sia: $$S(n)=n-h-1=n-\log(n+1)$$ Si considera un albero avente la sola radice come caso base, per cui si ha $n=1$ e $h=0$: $$S(n)=S(1)=n-h-1=0$$ Si considera ora un albero binario completo di altezza $h$, e si suppone si abbia dimostrata la formula per i suoi due sotto-alberi radicati ai figli della radice di altezza $h-1$ e nodi $(n-1)/2$. La somma delle altezze è quindi: $$\begin{gathered}
    S(n)=2S\left(\displaystyle\frac{n-1}{2}\right)+h
\end{gathered}$$ Per l’ipotesi induttiva $S(n)=n-h-1$ si ha: $$\begin{gathered}
    S(n)=2\left(\displaystyle\frac{n-1}{2}-(h-1)-1\right)+h\\
    S(n)=n-1-2h+h=n-h-1
\end{gathered}$$ Quindi questa procedura ha una complessità: $$T(n)\equiv S(n)=n-\log n-1\in\Theta(n)$$

Le code di priorità si possono realizzare mediante un heap, in cui l’array può essere gestito con crescita telescopica. La creazione di una nuova coda di priorità avviene in tempo costante $\Theta(1)$, così come la consultazione dell’elemento a più alta priorità e la verifica se la coda è vuota: “‘c heap\* new_queue(int maxsize) heap\* h = (heap\*) malloc(sizeof(heap)); h-\>A = (int\*) malloc(maxsize\*sizeof(int)); h-\>size = 0; h-\>A_length = maxsize; return h; “‘ “‘c int maximum(heap\* h) return h-\>A\[0\]; “‘ “‘c int is_empty_heap(heap\* h) return h-\>size == 0; “‘ Invece per estrarre l’elemento a più alta priorità dalla coda, bisogna decrementare la dimensione della coda, e ri-ordinare l’heap. Per effettuare quest’ ultima operazione si assegna l’ultimo elemento in coda all’indice $i=0$, e si chiama la procedura `max_heapify ` sulla radice: “‘c int extract_max(heap\* h) if(is_empty_heap(h)) printf("errore di underflow"); int max = h-\>A\[0\]; h-\>A\[0\] = h-\>A\[h-\>size - 1\]; h-\>size–; max_heapify(h, 0); return max; “‘ Ha quindi una complessità al caso peggiore $\Theta(\log n)$, e costante nel caso migliore $\Theta(1)$. Invece per inserire un nuovo elemento nella coda, si parte dall’elemento a più bassa priorità e si itera verso l’alto, spostando ad ogni iterazione il genitore verso il basso, ed il nuovo elemento verso l’alto fino a trovare la sua posizione nella coda: “‘c void insert_max_heap(heap\* h, int z) if(h-\>size == h-\>A_length) // per una crescita telescopica realloc_heap(h); h-\>size++; int i; for(i = h-\>size - 1 ; (i \> 0 && h-\>A\[parent(i)\] \< z) ; i = parent(i)) h-\>A\[i\] = h-\>A\[parent(i)\]; h-\>A\[i\] = z; “‘ Nel caso migliore il nuovo elemento è effettivamente l’elemento a più bassa priorità, quindi effettua quest’operazione in tempo costante $\Theta(1)$, ma nel caso peggiore è necessario iterare fino ad arrivare alla radice, attraversando l’intero cammino dal nodo a più bassa priorità al nodo a più alta priorità. Ha quindi una complessità lineare $\Theta(h)$, dove $h$ è l’altezza dell’albero, per cui può essere espresso rispetto al numero dei nodi $n$ come $\Theta(\log n)$.

Utilizzando un heap, è possibile ordinare una sequenza di interi tramite la procedura `heap_sort`  
descritta nella sezione sul problema dell’ordinamento .

# Array Associativi

Un *array associativo* è una struttura dati contenente elementi omogenei acceduti tramite delle *chiavi*, anch’esse omogenee. Rappresenta quindi un insieme di coppie valore dell’elemento e chiave associata. Questa chiave può essere di qualsiasi tipo, e si suppone sia unica per ogni elemento dell’array. Questo tipo astratto di dato viene definito dai seguenti *domini*:

- L’insieme degli array associativi $\mathbb{A}$;

- L’insieme delle chiavi $\mathbb{K}$;

- L’insieme dei valori dell’array associativo $\mathbb{V}$;

- L’insieme dei booleani $\mathbb{B}$.

La *costante* è l’array associativo vuoto. Per inserire, rimuovere e consultare un elemento è quindi necessario fornire una chiave valida. Si possono quindi definire le seguenti *operazioni* sugli array associativi:

- `put`: $\mathbb{A}\times\mathbb{K}\times\mathbb{V}\to\mathbb{A}$, inserisce una coppia valore-chiave. nell’array;

- `get`: $\mathbb{A}\times\mathbb{K}\to\mathbb{V}$, restituisce il valore associato ad una chiave;

- `delete`: $\mathbb{A}\times\mathbb{K}\to\mathbb{A}$, rimuove una coppia valore-chiave, nell’array;

- `exists`: $\mathbb{A}\times\mathbb{K}\to\mathbb{B}$, verifica che una chiave sia utilizzata nell’array.

Si vogliono ottenere tempi di esecuzioni logaritmici $\Theta(\log n)$ per ognuna di queste operazioni. Ma una realizzazione tramite array o liste, ordinati o non ordinati, non lo permette. In un’array ordinato l’inserimento deve spostare tutti gli elementi all’inserimento di una nuova coppia, per cui ha un costo lineare $\Theta(n)$, mentre la ricerca può essere effettuata in tempi logaritmici, tramite una ricerca dicotomica, o binaria. Questo tipo di ricerca presuppone l’array sia ordinato in maniera crescente, quindi comincia la ricerca consultando il valore alla posizione centrale dell’array, in seguito se il valore letto è minore del valore cercato, scarta il semi-array sinistro, poiché sicuramente contiene valori anch’essi minori, quindi ripete la procedura sul semi-array destro, contenente valori sicuramente maggiori. Analogamente in caso il valore sia maggiore, ripete la procedura sul semi-array sinistro, fino a quando non trova l’elemento. Il tempo di esecuzione di questa operazione può essere espresso dalla seguente formula di ricorrenza: $$\begin{gathered}
    T(n)=\begin{cases}
        \Theta(1) &n=1\\
        T\left(\displaystyle\frac{n}{2}\right)+\Theta(1)&n>1
    \end{cases}
\end{gathered}$$ Per il teorema dell’esperto quindi si ha $a=1$, $b=1$, e $k=0$. Per cui viene risolta da $a=b^k$: $$T(n)=\Theta(n^k\cdot\log n)=\Theta(\log n)$$

## Alberi Binari di Ricerca

Tramite un albero binario è possibile implementare questo tipo di ricerca. Questa strutture dati vengono chiamati *Alberi di Ricerca Binaria* ABR o *Binary Search Tree* BST. Queste strutture di dati quindi utilizzate per implementare array associativi, formati da una coppia chiave-valore, dove viene definita una relazione di ordine totale o lineare sulle chiavi. Vengono quindi definite due funzioni `minore ` e `uguale ` per determinare la posizione reciproca tra due chiavi. In caso le chiavi siano interi questa relazione viene descritta dalla relazione d’ordine strettamente minore $<$. Questa struttura dati viene realizzata tramite alberi binari radicati, definendo un nodo dell’albero come:

``` c
typedef struct Nodo_abr{
    struct Nodo_abr* parent;    // riferimento al genitore
    struct Nodo_abr* left;      // riferimento al figlio sinistro
    struct Nodo_abr* right;     // riferimento al figlio destro
    obj_k key;                  // valore della chiave
    obj_v value;                // valore associato alla chiave
    }nodo_abr;
```

Nelle analisi seguenti si considerano le chiavi interi, e si omette il valore associato. Per essere un albero binario di ricerca, tutti i nodi del sotto-albero sinistro di un generico nodo contengono solo chiavi di valore minore. Analogamente il sotto-albero destro contiene solo nodi aventi chiavi di valore maggiore della radice. Questa struttura dati supporta operazioni di consultazione, inserimento e rimozione. Inoltre è possibile verificare la validità dell’albero binario di ricerca. La ricerca del valore massimo e del valore minimo consiste nello scorrere sempre sui figli o sinistri o destri, poiché contengono una chiave di valore sempre o minore o maggiore. Per la ricerca del riferimento al nodo contenente la chiave di valore massimo o minimo può essere implementata semplicemente come: “‘c nodo\* max_abr(albero_bin t) if(t == NULL \|\| t-\>right == NULL) return t; return max_abr(t-\>right);

nodo\* min_abr(albero_bin t) if(t==NULL \|\| t-\>left == NULL) return t; return min_abr(t-\>left); “‘ Si può notare come il nodo minimo non abbia figli sinistri, ed il nodo massimo non abbia figli destri. Per cui il ramo all’estrema sinistra termina nel valore minimo, mentre il ramo all’estrema destra termina nel valore massimo. L’operazione di ricerca del massimo o minimo ha tempo lineare rispetto all’altezza dell’albero $\Theta(h)$. Per cui nel caso migliore è costante $\Theta(1)$, poiché l’albero è una catena lineare mentre nel caso peggiore è sempre una catena lineare, ma di figli opposti, per cui bisogna iterare su ogni elemento dell’albero $\Theta(n)$.

Mentre la ricerca di un nodo per chiave avviene in maniera simile, iterando sul sotto-albero che potrebbe contenere quel valore di chiave, fino ad arrivare all’elemento oppure ad una foglia: “‘c nodo\* search_abr(albero_bin t, int z) if(t == NULL \|\| t-\>info == z) return t; if(z \< t-\>info) return search_abr(t-\>left, z); return search_abr(t-\>right, z); “‘ Anche questa operazione presenta una complessità dipendente dall’altezza del nodo contente il valore, per cui è costante nel caso migliore $\Theta(1)$, e lineare nel caso peggiore $\Theta(n)$, dove $n$ è il numero dei nodi nell’albero.

L’inserimento e la rimozione non sono invece di facile implementazione, poiché bisogna mantenere le proprietà dell’albero a seguito di queste operazioni. In caso l’albero sia vuoto, l’inserimento avviene in tempo costante $\Theta(1)$. Per inserire un nodo di chiave generica in un albero binario di ricerca non vuoto, bisogna iterare e cercare un nodo di grado uno o minore, tale che sia un possibile genitore valido del nuovo nodo da inserire. Poiché la relazione tra le chiavi è una relazione stretta, questa operazione deve rifiutare un inserimento quando è già presente un nodo contenente la stessa chiave all’interno dell’albero: “‘c int add_abr(albero_bin\* t, int z) if(\*t == NULL) add_root_bin(t,z); else if((\*t)-\>info == z) return 0; else if(z \< (\*t)-\>info) if((\*t)-\>left == NULL) add_left_bin(\*t,z); else add_abr(&((\*t)-\>left), z); else if(z \> (\*t)-\>info) if((\*t)-\>right == NULL) add_right_bin(\*t,z); else add_abr(&((\*t)-\>right),z); return 1; “‘

Più complessa ancora è la strategia utilizzata per rimuovere un elemento da un albero binario di ricerca. In caso il nodo da rimuovere sia una foglia, è possibile rimuoverlo semplicemente modificando il parametro del nodo genitore con il riferimento non valido. Invece se il nodo ha un solo figlio si può collegare il genitore al figlio per poi eliminare il nodo. Altrimenti bisogna cercare il nodo successore, questo nodo presenta la chiave minima, tra i nodi aventi chiave maggiore. Si cerca quindi il massimo sul sotto-albero sinistro, questo nodo ha al massimo un figlio sinistro, si sostituisce quindi con il nodo, e si rimuove questo nodo successore. Analogamente si può cercare il nodo predecessore nel sotto-albero sinistro, corrispondente al valore massimo tra i nodi di chiave minore. Si definisce quindi una funzione di appoggio per l’eliminazione: “‘c void tree_bypass_abr(albero_bin\* t,nodo\* x)

nodo\* figlio = NULL; if(x-\>left != NULL) figlio = x-\>left; else figlio = x-\>right;

if(figlio != NULL) figlio-\>parent = x-\>parent;

if(x-\>parent != NULL) if(x-\>parent-\>left == x) x-\>parent-\>left = figlio; else x-\>parent-\>right = figlio; else \*t = figlio;

“‘ La complessità temporale di questa operazione è costante $\Theta(1)$. La procedura di eliminazione deve cercare prima il successore, o il predecessore, quindi ha una complessità $\Theta(h)$: “‘c void delete_node_abr(albero_bin\* t, nodo\* x) if(t == NULL \|\| x == NULL) return; nodo\* del = x; if(x-\>left != NULL && x-\>right != NULL) del=min_abr(x-\>right); swap_nodes(x, del); tree_bypass_abr(t, del); free(del); “‘

Tutti questi algoritmi sono quindi lineari rispetto all’altezza $h$ $\Theta(h)$, questo dipende dall’ordine degli inserimenti nell’albero, poiché se fosse sbilanciato, nel caso peggiore l’altezza dipenderebbe linearmente dal numero dei nodi nell’albero $h\in\Theta(n)$. Quindi riuscire a mantenere bilanciato l’albero è una specifica richiesta in molte applicazioni per mantenere una complessità logaritmica per queste operazioni $\Theta(h)=\Theta(\log n)$. Nel caso medio l’altezza dell’albero binario di ricerca è logaritmica, quindi anche nel caso medio tutte logaritmiche $\Theta(\log n)$.

Se un albero binario di ricerca viene visitato tramite una visita simmetrica allora produce una sequenze di elementi ordinati in maniera crescente, quindi dato un albero binario per confermare che sia un albero binario di ricerca è possibile trasformarlo in una sequenza di interi tramite una visita simmetrica, e verificare che questa sequenza sia strettamente crescente. Queste operazioni avvengono in tempo lineare poiché ogni procedura ha tempo di esecuzione $\Theta(n)$: “‘c void bin_to_array(albero_bin t, int\* a, int \*i) if(t != NULL) if(t-\>left != NULL) bin_to_array(t-\>left, a, i); a\[\*i\] = t-\>info; (\*i)++; if(t-\>right != NULL) bin_to_array(t-\>right, a, i);

int is_sorted(int\* a, int len) int i; for(i = 0 ; i \< len - 1 ; i++) if(a\[i\] \> a\[i+1\]) return 0; return 1;

int is_abr(albero_bin t) int len = nodes_bin(&t); int\* a = malloc(len \* sizeof(int)); int i = 0; bin_to_array(t, a, &i); return is_sorted(a, len); “‘

Inoltre è possibile operare all’inverso partendo da un array non ordinato e trasformarlo in un albero binario di ricerca, per poi trasformarlo in un array tramite una visita simmetrica, effettivamente ordinando la sequenza di interi, trattato nella sezione .

Per verificare se un albero binario sia effettivamente un albero binario di ricerca è possibile utilizzare altre due strategie, tramite una visita un pre-ordine, la prima, ed una visita in post-ordine, la seconda: “‘c int is_abr_pre(albero_bin t) if(t == NULL) return 1; return all_smaller_abr(t-\>left, t-\>info) && all_greater_abr(t-\>right, t-\>info) && is_abr_pre(t-\>left) && is_abr_pre(t-\>right);

int all_greater_abr(albero_bin t, int z) if(t == NULL) return 1; return (t-\>info \> z) && all_greater_abr(t-\>left, z) && all_greater_abr(t-\>right, z);

int all_smaller_abr(albero_bin t, int z) if(t == NULL) return 1; return (t-\>info \< z) && all_smaller_abr(t-\>left, z) && all_smaller_abr(t-\>right, z); “‘ Questa procedura impiega un tempo $\Theta(n\cdot\log n)$ nel caso migliore, poiché ad ogni iterazione i due sotto-alberi che deve controllare sono hanno lo stesso numero di nodi. Mentre nel caso peggiore, dove l’albero è fortemente sbilanciato si ha un’equazione di ricorrenza: $$\begin{gathered}
    T(n)=T(n-1)+\Theta(n)\\
    T(n)=\displaystyle\sum_{k=1}^n\Theta(k)=\Theta(n^2)
\end{gathered}$$

La verifica in post-ordine è più complessa nella sua implementazione, ma fornisce un tempo di esecuzione sempre lineare $\Theta(n)$. a scapito della sua occupazione in memoria. Questa procedura restituisce un array di tre elementi, contenti la verifica se il sotto-albero è un albero binario di ricerca, il valore massimo ed il valore minimo. Inoltre utilizzando la stessa procedura, è possibile aumentare la dimensione dell’array per calcolare altri parametri notevoli per l’albero, ma questi tre sono necessari per verificare sia un albero binario di ricerca.

## Alberi Rosso-Neri

Si è descritto nella sezione precedente la differenza tra i tempi di esecuzione di alberi binari bilanciati rispetto ad alberi sbilanciati, e di come questo provoca per ogni operazioni un peggioramento delle prestazioni:

<div class="center">

|               | *Sbilanciati* |   *Bilanciati*   |
|:-------------:|:-------------:|:----------------:|
|   *Ricerca*   |  $\Theta(n)$  | $\Theta(\log n)$ |
| *Inserimento* |  $\Theta(n)$  | $\Theta(\log n)$ |
|  *Rimozione*  |  $\Theta(n)$  | $\Theta(\log n)$ |

</div>

Quindi è legittimo spendere risorse per cercare di mantenere bilanciato l’albero ed avere tempi di esecuzione logaritmici per queste procedure. Si usano quindi delle varianti degli alberi binari di ricerca che includono nella loro struttura strumenti per mantenere il bilanciamento entro certi livelli. Le strutture che verranno analizzate in questa sezione sono gli *Alberi Rosso-Neri*, ideati da Leonidas J. Guibas e Robert Sedgewick nel 1978. Altre strutture che hanno lo stesso scopo sono gli alberi AVL, introdotti da Adelson-Velsky e Landis nel 1962, mantengono simili le altezze dei due sotto-alberi sinistri e destri; gli alberi WAVL, introdotti da Haeupler, Sen e Tarjan nel 2015; e i B-alberi introdotti da Bayer e McCreight.

Per semplificare le operazioni si vuole avere ogni nodo di grado due, per cui si introduce un *nodo sentinella* `null`, che effettivamente sostituisce il riferimento non valido. Poiché un albero viene definito come un riferimento al nodo radice dell’albero, nelle seguenti implementazioni in linguaggio C si considera come un array di riferimenti a nodo aventi nel secondo indice il riferimento al *nodo sentinella*: “‘c albero_rb\* new_tree_rb() albero_rb\* rb = (albero_rb\*) malloc(2\*sizeof(albero_rb)); rb\[1\] = new_nodo_bin(0, NULL, NULL, NULL); rb\[0\] = rb\[1\]; return rb; “‘

Un *Albero Rosso-Nero* viene definito un albero binario di ricerca, dove valgono le seguenti condizioni:

1.  Ogni nodo è *rosso* o *nero*;

2.  La *radice* ed il *nodo sentinella* sono *neri*;

3.  I figli di un nodo *rosso* sono necessariamente *neri*;

4.  Ogni cammino dalla *radice* alla *sentinella* contengono lo stesso numero di nodi *neri*.

Quindi l’altezza dell’albero è maggiore di uno, poiché il cammino più lungo considera anche il nodo sentinella, ciò va considerato nel calcolo della sua altezza:

``` c
int height_rb(albero_rb* t){
    return height_bin(t) - 1;
}
```

Ciò è possibile poiché in questa implementazione si considera il nodo sentinella avente come figli il riferimento non valido `NULL ` per cui risulta compatibile con le funzioni realizzate precedentemente per gli alberi binari. Per semplificare l’implementazione si utilizza la stessa struttura per i nodi di un albero binario, e vengono codificate le informazioni sul colore all’interno del valore della chiave del nodo, poiché si lavora con interi. Vengono quindi definite le seguenti funzioni: “‘c int encode_rb(int val, int col) return val\*10 + col;

int info_rb(nodo\* n) return n-\>info/10;

int colore_rb(albero_rb\* rb, nodo\* n) return (n == rb\[1\]) \|\| (n-\>info) & 1; “‘

Per essere un albero rosso-nero, deve essere un valido albero binario di ricerca, ma non tutti gli alberi binari di ricerca qualificano come possibili alberi rosso-neri. Dato un albero rosso-nero avente un cammino avente solo $k$ nodi neri, allora sarà possibile un cammino avente al massimo $2\cdot(k-1)$ archi, poiché nel cammino più lungo, per mantenere la validità dell’albero, i nodi neri si alternano a nodi rossi dalla radice nera, fino alla sentinella nera. Quindi il cammino più lungo è al massimo due volte il cammino più corto. Poiché tutti i cammini contengono lo stesso numero di $k$ nodi neri, allora l’albero contiene un sotto-albero completo di altezza $h'$: $$h'=\displaystyle\frac{h}{2}-1=\frac{2(k-1)}{2}-1$$ Dove $h$ è l’altezza massima dell’albero, corrispondente al cammino più lungo. Per cui l’albero contiene almeno lo stesso numero di nodi di questo sotto albero: $$\begin{gathered}
    n\geq2^{h'+1}-1=2^{\frac{h}{2}}-1\\
    n+1\geq2^{\frac{h}{2}}\\
    \log_2(n+1)\geq\frac{h}{2}\\
    h\leq2\log(n+1)\to h\in O(\log n)
\end{gathered}$$ Questo rappresenta il limite superiore per l’altezza di un albero rosso-nero, ma essendo anche un albero binario, la sua altezza corrisponde al minimo all’altezza di un albero binario completo avente $n$ nodi: $$\begin{gathered}
    h\in\Omega(\log n)\\
    h\in\Theta(\log n)
\end{gathered}$$ Per cui in un albero rosso-nero l’altezza dell’albero è una funzione logaritmica del numero dei nodi, per cui tutte le operazioni di ricerca, inserimento e rimozione avvengono in tempo logaritmico $\Theta(\log n)$: “‘c nodo\* search_rb(albero_rb\* rb, int z) if(rb\[0\] == rb\[1\]) return rb\[1\]; nodo\* scorri = rb\[0\]; while(scorri != rb\[1\]) if(info_rb(scorri) == z) return scorri; if(info_rb(scorri) \< z) scorri = scorri-\>right; else scorri = scorri-\>left; return rb\[1\];

nodo\* min_rb(albero_rb\* rb) if(rb\[0\] == rb\[1\]) return rb\[1\]; nodo\* scorri = rb\[0\]; while(scorri-\>left != rb\[1\]) scorri = scorri-\>left; return scorri;

nodo\* max_rb(albero_rb\* rb) if(rb\[0\] == rb\[1\]) return rb\[1\]; nodo\* scorri = rb\[0\]; while(scorri-\>right != rb\[1\]) scorri = scorri-\>right; return scorri; “‘ Queste due ultime operazione però non mantengono le proprietà dell’albero rosso-nero, per cui è necessario definire delle procedure, che dato un albero rosso-nero dopo un’aggiunta o una rimozione, permette di recuperare le proprietà. Queste procedure, devono anch’esse avere un tempo di esecuzione logaritmico, per mantenere la complessità totale delle operazioni di inserimento e rimozione. Si considera l’operazione di inserimento, implementata tramite la funzione `add_rb`: “‘c nodo\* new_node_rb(albero_rb\* rb, int z) return new_nodo_bin(encode_rb(z, 0), rb\[1\], rb\[1\], rb\[1\]); “‘ “‘c

int add_rb(albero_rb\* rb, int z) nodo\* nuovo = new_node_rb(rb, z); nodo\* par = rb\[1\]; nodo\* scorri = rb\[0\]; while(scorri != rb\[1\]) par = scorri; if(info_rb(nuovo) \< info_rb(scorri)) scorri = scorri-\>left; else if(info_rb(nuovo) \> info_rb(scorri)) scorri = scorri-\>right; else return 0; // se il valore è già presente, rifiuta l’inserimento nuovo-\>parent = par; if(par == rb\[1\]) rb\[0\] = nuovo; else if(info_rb(par) \> info_rb(nuovo)) par-\>left = nuovo; else par-\>right = nuovo; recover_add_rb(rb, nuovo); return 1; “‘ Le tecniche utilizzate per recuperare le proprietà dell’albero si basano su semplici operazioni, in tempo costante $\Theta(1)$:

- `left-rotate`: $\mathbb{T}\times\mathbb{R}\to\mathbb{T}$, scambia un nodo con il suo figlio destro, diventando il suo figlio sinistro;

- `right-rotate`: $\mathbb{T}\times\mathbb{R}\to\mathbb{T}$, scambia un nodo con il suo figlio sinistro, diventando ils uo figlio desto.

Queste due operazioni sono inverse tra di loro, e simmetriche. Le operazioni di rotazione cambiano la struttura dell’albero, ma non cambiano i colori dei nodi. Per cui in seguito si applicano delle ri-colorazioni sui nodi necessari, sempre in tempo costante $\Theta(1)$: “‘c void left_rotate(albero_rb\* rb, nodo\* x) nodo\* y = x-\>right; x-\>right = y-\>left; if(y-\>left != rb\[1\]) y-\>left-\>parent = x; y-\>parent = x-\>parent; if(x-\>parent == rb\[1\]) rb\[0\] = y; else if(x-\>parent-\>left == x) x-\>parent-\>left = y; else x-\>parent-\>right = y; y-\>left = x; x-\>parent = y;

void right_rotate(albero_rb\* rb, nodo\* y) nodo\* x = y-\>left; y-\>left = x-\>right; if(x-\>right != rb\[1\]) x-\>right-\>parent = y; x-\>parent = y-\>parent; if(y-\>parent == rb\[1\]) rb\[0\] = x; else if(y-\>parent-\>left == y) y-\>parent-\>left = x; else y-\>parent-\>right = x; x-\>right = y; y-\>parent = x;

void recolor(albero_rb\* rb, nodo\* par, nodo\* gpar) if(par != rb\[1\]) par-\>info = encode_rb(info_rb(par), 1); // coloro il genitore di nero if(gpar != rb\[1\])gpar-\>info = encode_rb(info_rb(gpar), 0); // coloro il nonno di rosso “‘ Ogni nuovo nodo aggiunto è una foglia, e di colore rosso, poiché è più semplice ripristinare la terza condizione rispetto alla quarta Quindi l’inserimento può violare solo la seconda o la terza condizione di un albero rosso-nero. In caso l’albero sia vuoto, l’inserimento corrisponderebbe all’aggiunta della radice, e per ripristinare le proprietà basterebbe colorare il nuovo nodo di nero: “‘c void case_0(nodo\* nuovo) nuovo-\>info = encode_rb(info_rb(nuovo), 1); “‘ Invece se il nodo viene appeso ad un genitore rosso, l’inserimento viola la terza condizione, si possono individuare sei situazioni diverse, simmetriche tra di loro. Per semplificare l’analisi si definisce lo *zio* del nuovo nodo inserito, il fratello del suo genitore, può corrispondere al nodo sentinella. Se lo zio è nero sono possibili quattro casi dove la condizione viene violata:

<div class="center">

| *Nuovo*,*Zio* |      Destro       |     Sinistro      |
|:-------------:|:-----------------:|:-----------------:|
|   Sinistro    | Caso 1 (Sinistro) | Caso 2 (Sinistro) |
|    Destro     |  Caso 2 (Destro)  |  Caso 1 (Destro)  |

</div>

Nel primo caso, sinistro o destro, il nodo ed il suo zio sono figli opposti, uno sinistro e l’altro destro, per cui è sufficiente ricolorare il genitore ed il genitore del genitore o *nonno*, ed in seguito applicare una rotazione destra sul nonno, nel caso sinistro, ed una rotazione sinistra nel caso destro: “‘c void case_1_left(albero_rb\* rb, nodo\* par, nodo\* gpar) recolor(rb, par, gpar); right_rotate(rb, gpar);

void case_1_right(albero_rb\* rb, nodo\* par, nodo\* gpar) recolor(rb, par, gpar); left_rotate(rb, gpar); “‘ Nel secondo caso i due nodi, il nuovo ed il suo zio, sono figli dallo stesso lato, per cui si applica una rotazione opposta, destra se sono figli sinistri, e sinistra se sono figli destri, al genitore del nuovo nodo inserito. Dopo aver effettuato questa rotazione, ci si ritrova nel primo caso, poiché il nuovo nodo ed il suo genitore sono entrambi rossi, e lo zio è un figlio opposto rispetto al nodo, quindi si applica la procedura definita per il primo caso: “‘c void case_2_right(albero_rb\* rb, nodo\* par, nodo\* gpar) left_rotate(rb, par); case_1_left(rb, par-\>parent, gpar);

void case_2_left(albero_rb\* rb, nodo\* par, nodo\* gpar) right_rotate(rb, par); case_1_right(rb, par-\>parent, gpar); “‘ Invece se lo zio è rosso bisogna coloralo di nero, insieme al genitore del nuovo nodo, e colorare di rosso il loro genitore, ma dopo questa operazione, è possibile che il nonno del nuovo nodo non rispetti la condizione, poiché potrebbe avere il genitore rosso, per cui è necessario chiamare nuovamente la procedura, questa volta sul nonno: “‘c void case_3_left(albero_rb\* rb, nodo\* par, nodo\* gpar) recolor(rb, par, gpar); if(gpar-\>left != rb\[1\]) gpar-\>left-\>info = encode_rb(info_rb(gpar-\>left), 1); recover_add_rb(rb, gpar);

void case_3_right(albero_rb\* rb, nodo\* par, nodo\* gpar) recolor(rb, par, gpar); if(gpar-\>right != rb\[1\]) gpar-\>right-\>info = encode_rb(info_rb(gpar-\>right), 1); recover_add_rb(rb, gpar); “‘ Quest’ultimo caso risale l’albero, ed è possibile che sia necessario iterare fino a raggiungere la radice, quindi ha una complessità nel caso peggiore $\Theta(h)=\Theta(\log n)$. In caso si arrivi alla radice e questa sia colorata di rosso, è sufficiente ricolorarla di nero per ripristinare le proprietà dell’albero rosso-nero. Nei prime due casi invece ha un tempo di esecuzione costante $\Theta(1)$. Poiché nel caso peggiore la procedura di ripristino ha una complessità logaritmica, allora l’inserimento ha una complessità logaritmica nel caso peggiore $\Theta(\log n)$. “‘c void recover_add_rb(albero_rb\* rb, nodo\* nuovo) if(rb\[0\] == nuovo) return case_0(nuovo); nodo\* par = nuovo-\>parent; if(colore_rb(rb, par)) return; nodo\* gpar = par-\>parent; if(par-\>left == nuovo && gpar-\>left == par && colore_rb(rb, gpar-\>right)) case_1_left(rb, par, gpar); else if(par-\>right == nuovo && gpar-\>right == par && colore_rb(rb, gpar-\>left)) case_1_right(rb, par, gpar); else if(par-\>right == nuovo && gpar-\>left == par && colore_rb(rb, gpar-\>right)) case_2_right(rb, par, gpar); else if(par-\>left == nuovo && gpar-\>right == par && colore_rb(rb, gpar-\>left)) case_2_left(rb, par, gpar); else if(gpar-\>left == par && colore_rb(rb, gpar-\>right) != 1) case_3_right(rb, par, gpar); else if(gpar-\>right == par && colore_rb(rb, gpar-\>left) != 1) case_3_left(rb, par, gpar); case_0(rb\[0\]); “‘ La rimozione di un elemento utilizza una strategia simile, tramite rotazioni e ri-colorazioni è possibile mantenere il tempo di esecuzione della procedura logaritmico $\Theta(\log n)$. Quindi è possibile mantenere bilanciato l’albero ed avere tempi di esecuzione logaritmici per ogni operazione di inserimento, ricerca e rimozione. Per cui implementando un algoritmo di ordinamento tramite un albero rosso-nero è possibile avere una complessità nel caso migliore, medio e peggiore $\Theta(n\cdot\log n)$, .

## Tabelle di Hash

Prendiamo la definizione di array associativi, ovvero dei tipi astratti di dato con la coppia chiave, valore, in cui faremo le solite operazione. Li possiamo implementare con le strutture che abbiamo visto precedentemente. Ovviamente la più efficiente è utilizzare gli alberi rosso-neri, con tempo $O(\log n)$ Le tabelle di hash sono array associativi che non usano confronti negli algoritmi standard e che vengono in $O(n)$ in peggiore ma $O(1)$ in caso medio. I problemi sono che possiamo avere troppe diverse possibili chiavi e quelle effettivamente utilizzate sono molto inferiori. Allora uso un array $T$ di dimensione $m$, vicino al numero di chiavi utilizzate e una funzione hash $h$. L’array con gli indici dati dalla funzione hash è una tabella di hash. Quindi per fare una tabella di hash servono le funzioni hash e qual definite in base lal contesto, che genericamente devono essere calcolabili in tempo costante. La funzione `equal ` deve essere adattata, infatti quando ci sono le stringhe ci sono operazioni diverse di variabili semplici. Questa funzione che mette la corrispondenza da L’universo delle possibili chiavi agli indici dell’array, ovvero con numeri diversi da $0$ a $m-1$. Questa funzione deve essere deterministica e con tempo costante. Vista la differenza da dominio a codominio è quasi sicuro si generino collisioni, ovvero due chiavi diversa danno lo stesso indice.

### Liste di Trabocco

Le possiamo risolvere con le liste di trabocco, ovvero si creano delle liste semplicemente concatenate nell’indice dell’array $T$ dove si è creata una collisione. Un altro requisito di questa funzione è la sua pseudo-casualità, ovvero dell’associazione degli indici alle chiavi. Definiamo il fattore di carico $\alpha$ come il rapporto tra il numero $n$ di elementi memorizzati e di posti disponibili $m$, dunque il numero medio di elementi nella lista concatenata delle liste di trabocco. Per quanto riguarda la complessità abbiamo che le liste di trabocco abbiano $1$ elemento e quindi $\Theta(1)$ nel caso migliore. Nel caso peggiore tutte le chiavi sono nella stessa posizione e dunque $\Theta(n)$ Nel caso medio, se viene garantita la distribuzione uniforme e $\alpha$ non supera $\alpha_{\max}$, la complessità è $\Theta(1)$ Questo è sensato dato che $\alpha$ non dipende solo da $n$, ma anche da $m$ che deve crescere in maniera telescopica per garantire i tempi costanti. Ci sono diverse funzioni di hash utilizzate generalmente: Divisione, utilizzando il resto $h(k)=k\,\mathrm{mod}\,m$ mantiene la pseudo-casualità in caso ci sia. In questo caso è utile prendere come m un numero primo lontano da una potenza di 2. Moltiplicazione $h(k)=\lfloor m\cdot(k\cdot \mathrm{irr}-\lfloor k\cdot\mathrm{irr}\rfloor)\rfloor$ dove irr è numera irrazionale tra $0$ e $1$, $m$ arbitrario.

Quando abbiamo le stringhe di solito si usa il numero dato come somma dei ASCII dei caratteri, ma da facilmente collisioni, e allora esiste il DJB2 che moltiplica il codice ASCII aggiunto a $33$ e sommato tutto a $5381$. I numeri sono risultati sperimentali.

Per oggetti vengono utilizzate diverse funzioni hash per ogni campo e sommate.

Si può usare la tabella di hash come rappresentazione di insiemi.

### Indirizzamento Aperto

In questo caso le collisioni vengono gestite utilizzando i posti liberi nella tabella spessa, e il fattore di carico non supera mai $1$, e non uso riferimenti. Quindi in caso di collisione cerco in sequenza circolare una cella libera, ma si può fare in diversi modo, con una funzione di scansione $h(k,i)$ dove i tiene conto i tentativi precedenti che hanno colliso. Questa funzione deve avere come valori di uscita una permutazione degli indici di $T$. Utilizzando l’indirizzamento aperto però, si complicano le cose con le cancellazioni, perché potrebbero fallire ricerche future. ALlora di solito le cella cancellate vengono marcate con *deleted* e non `NULL`, così in inserimento si devono tener conto di queste, mentre in ricerca non ci sono problemi.

La complessità è $1/\alpha\cdot\ln(171-\alpha)$, in cui di ipotizza una distribuzione uniforme di probabilità.

### Scansione Lineare

$$h(k,i)=(h(k)+i)\mathrm{mod}\,m$$ Facile ma dà vita all’addensamento primario, ovvero ci creeranno delle sequenze di celle non vuote che altereranno la probabilità uniforme di inserimento, ovvero la prima libera dopo la sequenza sarà la più probabile. Allora scansione quadratica $$h(k,i)=(h(k)+c_1i + c_2i^2)\mathrm{mod}\,m$$ le costanti devono essere diverse da $0$ e multipli di $m$. Utilizzando $m$ come potenza di $2$, si possono usare le costanti con valore $1/2$ infatti in questo caso l’unico modo in possano collidere è con la stessa chiave. Ma qui genera l’addensamento secondario, ovvero che se il primo risultato è uguale, allora anche i seguenti allora si usa il doppio hashing $$h(k,i)=[h_1(k) + ih_2(k)] \mathrm{mod}\,m$$ Dove $h_1$ e $h_2$ sono due funzioni di hash distinte, e $h_2$ deve sempre essere maggiore di $0$ e primo con $m$, condizione sufficiente e necessaria.

# Grafi
