# Complessità temporale

Argomenti: Equivalenza tra verificabilità polinomiale ed appartenenza a NP, Riducibilià polinomiale
.: No

## Equivalenza tra verificabilità polinomiale ed appartenenza a $\mathbb{NP}$

- `teorema`: un linguaggio appartiene a $\mathbb{NP}$ se e solo se ha un verificatore che impiega tempo polinomiale.
- `dimostrazione`: sia $V$ un verificatore che impiega tempo $n^k$ per il linguaggio $A$.

Quando si riceve in input una stringa $w$ di lunghezza $n$, si generano non deterministicamente tutte le stringhe $c$ di lunghezza $n^k$, poi si invoca $V$ su $\left\langle w,c \right\rangle$. Se $V$ accetta allora si accetta in caso contrario si rifiuta.

Sia $N$ una MTND che decide il linguaggio $A$ in tempo polinomiale. Si simula il comportamento di $N$ su $w$, si costruisce $c$ come selettore della scelta da fare ad ogni step. Se il ramo della computazione identificato da $c$ accetta si accetta, in caso contrario si rifiuta.

## Riducibilità polinomiale

La complessità computazionale di $A_1$, costruito con $A_2$ ed $R$ (dove $R$ è l’algoritmo di riduzione), dipende dalla complessità di $A_2$ e dalla complessità di $R$.

$P_1$ è `polinomialmente riducibile` a $P_2$ se la riduzione $R$ è un algoritmo $MT$ con complessità polinomiale. 

---

## Completezza

- la `completezza` è uno strumento per indagare le relazioni di inclusione fra classi di complessità, viene usato per indagare il rapporto tra $\mathbb{P}$ ed $\mathbb{NP}$.
- Un problema di decisione $P$ è $\mathbb{NP}$-completo se $P\in \mathbb{NP}$ e per ogni $P_1\in \mathbb{NP}$ si ha che $P_1\le_P P$

Se si riesce a dimostrare che un problema $\mathbb{NP}$-completo $P$ appartiene a $\mathbb{P}$, cioè è risolvibile in tempo polinomiale da un algaoritmo deterministico, allora ogni altro problema in $\mathbb{NP}$ è risolvibile in tempo polinomiale da un algoritmo deterministico.

## Teorema di Cook: $\text{SAT}$ è $\mathbb{NP}$-completo

- facciamo riferimento al linguaggio $L$ associato a $P$ e al linguaggio $\text{SAT}$ associato a $\text{SAT}$. Se $P\in \mathbb{NP}$ allora esiste una $\text{MTND}$ che accetta $L$ in tempo polinomiale. Sia $M$ una $\text{MTND}$ che accetta ogni stringa di $x$ di $L$ in tempo $p(|x|)$ con $p$ polinomio, dati $M$ ed $x$ costruiamo una formula $w$ in $CNF$ tale che $w$ è soddisfacibile se e solo se $M$ accetta $x$, cioè se e solo se $x\in L$
- ipotesi semplificative: $M$ con nastro semi-infinito con $x$ nelle prime celle; esiste uno stato $q_Y$ di accettazione; la computazione ha esattamente $p(|x|)$ passi
- $w$ è una congiunzione di 4 formule: $w=w_M \wedge w_I \wedge w_A \wedge W_T$
    - $w_M$: specifica le proprietà generali delle $MT$
    - $w_I$: specifica le condizioni iniziali di $M$
    - $w_A$: specifica le condizioni di accettazione di $M$
    - $w_T$: specifica la funzione di transizione di $M$
- le variabili di $w$ sono:
    - $Q_{t,k}$: è vero se e solo se $M$ si trova nello stato $q_k$ all’istante $t$
    - $H_{t,i}$: è vero se e solo se la testina di $M$ si trova sulla cella $i$-esima del nastro all’istante $t$
    - $C_{t,i,h}$: è vero se e solo se la cella $i$-esima del nastro contiene all’istante $t$ il simbolo $\sigma_h$
- $w_M$ è congiunzione di 3 formule: $w_M=w_{MS}\wedge w_{MH}\wedge w_{MH}$:
    - $w_{MS}$: specifica che ad ogni istante $M$ si trova in uno stato
        
        $$
        w_{MS}=\underset{t}{\wedge}\left[ (\underset{k}{\vee}Q_{t,k})\underset{k_1=k_2}{\wedge}(\overline{Q}_{t,k_1} \vee  \overline{Q}_{t,k_2}) \right]
        $$
        
    - $w_{MH}$: specifica che ad ogni istante la testina di deve trovare su una cella del nastro:
        
        $$
        w_{MH}=\underset{t}{\wedge}\left[ (\underset{i}{\vee}H_{t,i})\underset{i_1\neq i_2}{\wedge}(\overline{H}_{t,i_1} \vee  \overline{H}_{t,i_2}) \right]
        $$
        
    - $w_{MC}$: specifica che ogni cella contiene un carattere
    
    considerando tutte le possibili combinazioni si ha che $|w_M|=O(p^3(|x|))$
    
- $w_A=Q_{p(|x|),k}$ con $q_y=q_k$
- $w_T$ è congiunzione di 2 formule $w_T=w_{T1}\wedge w_{T2}$, dove la prima specifica che per ogni $t$ i contenuti del nastro agli istanti $t$ e $t+1$ sono gli stessi, eccetto, eventualmente, per ciò che riguarda la cella su cui la testina è posizionata all’istante $t$. La seconda codifica la funzione di transizione di $M$ sotto forma di un insieme di regole e si può fare con la congiunzione di $O(p^2(|x|))\cdot|Q|\cdot(|\Sigma|+1)$ formule.
- La formula $w$ ha lunghezza $O(p^3(|x|))$ e può essere costruita in tempo proporzionale alla sua lunghezza. $w$ è soddisfacibile se e solo se $M$ accetta la stringa $x$ in tempo $p(|x|)$