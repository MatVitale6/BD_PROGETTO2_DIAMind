# Automi a pila non deterministici

Argomenti: Ambiguità, Automi a pila deterministici, Automi a pila non deterministici
.: No

## Automa a pila non deterministico

Un automa a pila non deterministico è definito da una settupla $M=\left\langle \Sigma,\Gamma, Z_0, Q, q_0, F, \delta \right\rangle$:

- $\Sigma$ alfabeto di input
- $\Gamma$ alfabeto dei simboli della pila
- $Z_0\in \Gamma$ simbolo di pila iniziale
- $Q$ insieme finito di stati
- $q_0\in Q$ stato iniziale
- $F\sube Q$ insieme di stati finali
- $\delta: Q\times(\Sigma \cup\left\{ \epsilon \right\})\times\Gamma \to P(Q\times \Gamma^*)$

La funzione di transizione a partire dallo stato interno attuale, dal carattere letto sul nastro e dal simbolo affiorante sulla pila, sostituisce il simbolo affiorante sulla pila con una stringa di simboli e si porta in un nuovo stato interno

Ci sono 2 definizioni alternative per il linguaggio riconosciuto da un automa a pila:

- `accetazione per pila vuota`: una stringa è accettata da un automa a pila $M$ se se solo se al termine della scansione della stringa la pila è vuota.

$$
N(M)=\left\{ x|\left\langle q_0,x,Z_0\right\rangle \vdash^* \left\langle q,\epsilon, \epsilon \right\rangle \right\}
$$

- `accettazione per stato finale`: una stringa è accettata da un automa a pila $M$ se e solo se al termine della scansione della stringa, $M$ si trova in uno stato finale.

$$
L(M)=\left\{ x|\left\langle q_0,x,Z_0\right\rangle\vdash^* \left\langle q, \epsilon, \gamma\right\rangle,q \in F, \gamma \in \Gamma^* \right\}
$$

---

## Automa a pila deterministico

Un automa a pila $M=\left\langle \Sigma,\Gamma, Z_0, Q, q_0, F, \delta \right\rangle$ è deterministico se $\forall \sigma\in \Sigma$, $\forall Z\in\Gamma$, $\forall q\in Q$ si ha $|\delta(q,\sigma,Z)|+|\delta(q,\epsilon, Z)|\le 1$

---

## Grammatica CF $\to$ Automa a pila

- `teorema`: se $L$ è un linguaggio non contestuale allora esiste un automa $M$ tale che $L=N(M)$
- `dimostrazione`: (si suppone che $\epsilon \notin L(G)$) sia $G=\left\langle \Sigma, V_N, P, S \right\rangle$ una grammatica in GNF che genera $L$, si costruisce un’automa a pila $M=\left\langle \Sigma,\Gamma, Z_0, Q, q_0, F,\delta \right\rangle$ come segue:
    - $\Gamma=V_N$, $Z_0=S$, $Q=\left\{ q \right\}$, $q_0=q$, $F=\empty$
    - per ogni $A\to a\gamma$ con $\gamma \in V_N^*$ si stabilisce che $\left\langle q,\gamma \right\rangle\in \delta(q,a,A)$

Per dimostrare che $\left\langle q,x,S \right\rangle \vdash^* \left\langle q,\epsilon,\alpha \right\rangle$ se e solo se $S\Rightarrow^* x\alpha$ si dimostra per induzione su $i$ che se $\left\langle q,x,S \right\rangle \vdash_i \left\langle q,\epsilon,\alpha \right\rangle$ allora $S \Rightarrow_i x\alpha$ e che se $S \Rightarrow_i x\alpha$ allora $\left\langle q,x,S \right\rangle \vdash_i \left\langle q,\epsilon,\alpha \right\rangle$.

Per dimostrare per induzione su $i$ che se $\left\langle q,x,S \right\rangle \vdash_i \left\langle q,\epsilon,\alpha \right\rangle$ allora $S\Rightarrow_i x\alpha$:

- `passo base` $(i=1, x\in \Sigma)$: se $\left\langle q,x,S \right\rangle \vdash_1 \left\langle q,\epsilon,\alpha \right\rangle$ allora per costruzione esiste in $P$ una produzione $S\to x\alpha$
- `passo induttivo` $(i\gt1,x\in \Sigma^*, x=ya, a\in \Sigma)$: se $\left\langle q,x,S \right\rangle \vdash_i \left\langle q,\epsilon,\alpha \right\rangle$ allora $\exist\beta$ tale che $\left\langle q,ya,S \right\rangle \vdash_{i-1} \left\langle q,a,\beta \right\rangle \vdash_{1}\left\langle q,\epsilon,\alpha \right\rangle$. Da cui $\left\langle q,y,S \right\rangle \vdash_{i-1} \left\langle q,\epsilon,\beta \right\rangle$
    
    Per ipotesi induttiva $S\Rightarrow_{i-1}y\beta$, inoltre $\left\langle q,a,S \right\rangle \vdash_1 \left\langle q,\epsilon,\alpha \right\rangle$ implica che in $P$ esista una produzione $A\to a\eta$ con $\beta=A\gamma$ e $\alpha=\eta\gamma$. Quindi $S\Rightarrow_{i-1}y\beta=yA\gamma\Rightarrow ya\eta\gamma=ya\alpha=xa$
    

Per dimostrare per induzione su $i$ che se $S\Rightarrow_i x\alpha$ allora $\left\langle q,x,S \right\rangle\vdash_i \left\langle q,\epsilon, \alpha \right\rangle$:

- `passo base` $(i=1, x\in \Sigma)$: se $S\Rightarrow_i x\alpha$ allora esiste in $P$ una produzione $S\to x\alpha$ e quindi, per costruzione $\left\langle q,x,S \right\rangle \vdash_1 \left\langle q,\epsilon,\alpha \right\rangle$
- `passo induttivo` $(i\gt1,x\in \Sigma^*, x=ya, a\in \Sigma)$: se $S\Rightarrow_i x\alpha=ya\alpha$ allora esiste $A\to a\eta$ in $P$ tale che $S\Rightarrow_{i-1}yA\gamma \Rightarrow ya\eta\gamma$ con $\alpha=\eta\gamma$. Per ipotesi induttiva $\left\langle q,y,S \right\rangle\vdash_{i-1} \left\langle q,\epsilon, A\gamma \right\rangle$ da cui $\left\langle q,ya,S \right\rangle\vdash_{i-1} \left\langle q,a, A\gamma \right\rangle$ ma poichè $A\to a\eta$ allora $\left\langle q,\eta \right\rangle\in \delta(q,a,A)$, quindi $\left\langle q,ya,S \right\rangle\vdash_{i-1} \left\langle q,a, A\gamma \right\rangle\vdash \left\langle q,\epsilon,\eta\gamma \right\rangle=\left\langle q,\epsilon, \alpha \right\rangle$

Rimuovendo la limistazione che $\epsilon \notin L(G)$ si aggiunge un nuovo stato $q_0$ iniziale definendo la transizione $\delta(q_0,\epsilon,Z_0)=\left\langle q_0, \epsilon \right\rangle$ e la transizione: $\delta(q_0,a,Z_0)=\left\{ \left\langle q,\gamma \right\rangle |\left\langle q,\gamma \right\rangle\in \delta(q,a,Z_0) \right\}$

---

## Automa a pila $\to$ Grammatica CF

- `teorema`: se un linguaggio è accettato da un automa a pila mediante pila vuota esiste una grammatica non contestuale che lo genera.

---

## Ambiguità

Una grammatica non contestuale $G$ è `ambigua` se esiste una stringa $x$ in $L(G)$ derivabile con 2 alberi di derivazione diversi.

Un linguaggio è `inerentemente ambiguo` se tutte le grammatiche che lo generano sono ambigue.