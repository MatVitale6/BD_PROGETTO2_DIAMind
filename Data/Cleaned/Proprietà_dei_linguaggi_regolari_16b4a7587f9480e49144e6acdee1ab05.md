# Proprietà dei linguaggi regolari

Argomenti: Pumping lemma per tipo 3, Teorema di Myhill-Nerode
.: No

## Unione di linguaggi regolari

- `teorema`: l’unione di 2 linguaggi regolari è un linguaggio regolare:
- `dimostrazione`: dati 2 automi non deterministici $A_1$ e $A_2$ che riconoscono i linguaggi regolari $L_1$ ed $L_2$ si costruisce un automa $A=\left\langle \Sigma, K, \delta_N, q_0, F \right\rangle$ che riconosca il linguaggio $L_1 \cup L_2$

$\Sigma=\Sigma_1\cup\Sigma_2$, $K=K_1\cup K_2\cup \left\{ q_0 \right\}$, $q_0$ è un nuovo stato iniziale. Se $\epsilon \in L_1$ oppure $\epsilon \in L_2$ allora $F=F_1\cup F_2\cup \left\{q_0\right\}$ altrimenti  $F=F_1\cup F_2$

- $\delta_N(q,a)=\delta_{N_1}(q,a)$  se $q \in K_1$, $a\in \Sigma_1$
- $\delta_N(q,a)=\delta_{N_2}(q,a)$  se $q \in K_2$, $a\in \Sigma_2$
- $\delta_N(q_0,a)=\delta_{N_1}(q_{01},a)\cup \delta_{N_2}(q_{02},a)$  se $a\in \Sigma_1\cup \Sigma_2$

---

## Complementazione di un linguaggio regolare

- `teorema`: il complemento di un linguaggio regolare è un linguaggio regolare
- `dimostrazione`: a partire da un $ASF$ che riconosce $L$, si costruisce l’$ASF$ $A'$ che riconosce il linguaggio complementare.

Prima di eseguire la trasformazione dell’automa $A$ in $A'$, occorre verificare che la funzione $\delta$ sia totale

---

## Intersezione di linguaggi regolari

- `teorema`: l’intersezione di 2 linguaggi regolari è un linguaggio regolare
- `dimostrazione`: si usano le leggi di de morgan: $A\cap B=\overline{\overline{A}\cup\overline{B}}$

---

## Concatenazione di linguaggi regolari

- `teorema`: la concatenazione di 2 linguaggi regolari è un linguaggio regolare
- `dimostrazione`: a partire da automi $A_1$ e $A_2$ che riconoscono i linguaggi $L(A_1)$ e $L(A_2)$, si costruisce un $\text{ASFND}$ che riconosce $L(A_1)\circ L(A_2)$

L’$\text{ASFND}$ $A$ è definito come segue: $\Sigma=\Sigma_1 \cup \Sigma_2$, $K=K_1\cup K_2$, se $\epsilon\in L(A_2)$ allora $F=F_1 \cup F_2$ altrimenti $F=F_2$, $q_0=q_{01}$

- $\delta_N(q,a)=\delta_{1}(q,a)$  se $q \in K_1-F_1$ e $a\in \Sigma_1$
- $\delta_N(q,a)=\delta_1(q,a) \cup \delta_2(q_{02},a)$ se $q \in F_1$ e $a\in \Sigma$
- $\delta_N(q,a)=\delta_2(q_,a)$  se $q\in K_2$ e $a\in \Sigma_2$

---

## Pumping lemma per tipo 3

- `lemma`: per ogni linguaggio regolare $L$ esiste una costante $n$ tale che se $z\in L$ e $|z|\ge n$ allora $z=uvw$ con $|uv|\le n$, $|v|\ge1$ e $uv^iw\in L$ per $i=0,1,...$
- `dimostrazione`: si considera l’ASF $A$ che riconosce $L$ con il minimo numero $n=|K|$ di stati.

Si suppone che esista una stringa $z\in L$ con $|z|\ge n$. Sia $q_{i0},q_{i1},...,q_{i|z|}$ la sequenza di stati attraversati da $A$ durante il riconoscimento di $z$. Dato che $|z|\ge n$ allora esiste almeno uno stato attraversato 2 volte. Sia $j$ il primo valore per cui $q_{ij}$ è attraversato 2 volte, sia $u$ il più breve prefisso di $z$ tale che $\underline{\delta}(q_0, u)=q_{ij}$ e sia $z=ux$.

Si ha che $|u|<n$ e che $\underline{\delta}(q_{ij},x)=q_{i|z|}\in F$. Sia $v$ il più breve prefisso (non vuoto) di $x$ tale che $\underline{\delta}(q_{ij},v)=q_{ij}$ e sia $x=vw$. Si ha che $|uv|\le n$ e $\underline{\delta}(q_{ij},w)=q_{i|z|}\in F$.

$$
\begin{align*}
  \underline{\delta}(q_{0},uv^iw) &= \underline{\delta}(\underline{\delta}(q_0,u),v^iw)
\\
  &= \underline{\delta}(q_{ij},v^iw)
\\
  &= \underline{\delta}(\underline{\delta}(q_{ij},v),v^{i-1}w) \\
  &= \underline{\delta}(q_{ij},v^{i-1}w) \\
  &= ... \\
  &= \underline{\delta}(q_{ij}, w) \\
  &= q_{i|z|}\in F
\end{align*}
$$

Sviluppo della stringa

---

## Decidere se un linguaggio regolare è vuoto, finito o infinito

- `teorema`: esiste un algoritmo per decidere se il linguaggio regolare $L(A)$ riconosciuto da un ASF $A$ con $n$ stati è vuoto, finito o infinito.
- `dimostrazione`:
    - $L(A)$ è `vuoto` se e solo se non accetta nessuna stringa $z$ con $|z|<n$; infatti se $A$ riconosce parole con $n$ simboli, per il pumping lemma riconosce anche parole con meno di $n$ simboli
    - $L(A)$ è `infinito` se e solo se accetta una stringa $z$ con $n\le |z|<2n$, infatti se $A$ accetta $z$ con $|z|\ge n$ per il pumping lemma accetta infinite stringhe
- `algoritmo`: in input si ha un automa $A$ che riconosce il linguaggio $L(A)$, in output si ha la risposta dove determina se $L(A)$ è vuoto, finito o infinito.
    - si propone ad $A$ tutte le stringhe di $\Sigma^*$ di lunghezza minore di $2n$
    - se nessuna stringa è accettata allora $L$ è vuoto
    - se tutte le stringhe accettate hanno lunghezza minore di $n$ allora $L$ è finito
    - se tra le stringhe accettate ce ne sono alcune con lunghezza maggiore o uguale $n$ allora $L$ è infinito.

---

## Equivalenza tra 2 linguaggi regolari

- `teorema`: il problema dell’equivalenza tra 2 linguaggi regolari è decidibile
- `dimostrazione`: basta dimostrare che la loro intersezione coincide con la loro unione:
    
    $$
    (A\cap\overline{B})\cup(\overline{A}\cap B)=\empty
    $$
    

La decidibilità dell’equivalenza implica la decidibilità della minimizzazione del numero degli stati, cioè dato un automa con $n$ stati che riconosce $L$, si costruiscono tutti gli automi con $m<n$ stati, sull’alfabeto di $L$, e si verifica l’equivalenza con $L$.

---

## Teorema di Myhill-Nerode

Un linguaggio $L$ definisce implicitamente la seguente relazione binaria di equivalenza su $\Sigma^*$

$$
x\space R_L\space y \Leftrightarrow  (\forall z\in \Sigma^* \space\space\space xz\in L \Leftrightarrow yz\in L)
$$

cioè $x$ e $y$ sono nella stessa classe di equivalenza se completate con lo stesso suffisso entrambe appartengono o non appartengono ad $L$.

- `teorema`: $L$ è regolare se e solo se $R_L$ ha indice finito
- `dimostrazione`: se $L$ è regolare si dimostra che $R_L$ ha indice finito costruendo una relazione di equivalenza più fine di $R_L$ e dimostrando che la nuova relazione ha indice finito.

Se $R_L$ ha indice finito si dimostra che $L$ è regolare costruendo un automa che riconosce $L$. Si costruisce l’ASF $A$ che riconosce $L$ e si definisce una nuova relazione binaria $R_M$ su $\Sigma^*$

$$
x\space R_M\space y \Leftrightarrow  \underline{\delta}(q_0,x)=\underline{\delta}(q_0,y)
$$

Cioè 2 stringhe sono equivalenti se portano nello stesso stato di $K$ a partire da $q_0$, questo porta a dire che $R_M$ ha indice finito, pari al più a $|K|$. 

- Se $x \space R_M\space y$ allora $\forall z\in \Sigma^*$ si ha $xz\space R_M\space yz$, infatti se $\underline{\delta}(q_0, x)=\underline{\delta}(q_0,y)$ allora anche $\underline{\delta}(q_0, xz)=\underline{\delta}(q_0,yz)$.
- Se $x \space R_M\space y$ allora $x\space R_L\space y$, infatti se $\underline{\delta}(q_0,x)=\underline{\delta}(q_0,y)$ allora anche $\underline{\delta}(q_0,xz)=\underline{\delta}(q_0,yz)$ e quindi $xz\in L \Leftrightarrow yz\in L$.

Quindi l’indice di $R_L$ è minore o uguale dell’indice di $R_M$ a sua volta finito.