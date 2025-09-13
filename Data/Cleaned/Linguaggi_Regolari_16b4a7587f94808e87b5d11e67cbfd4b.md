# Linguaggi Regolari

Argomenti: ASFND -> ASF, ASFND -> Grammatica, Automi a stati finiti deterministici, Automi a stati finiti non deterministici, Grammatica -> ASFND
.: No

## Automi a stati finiti deterministici

Definito come una quintupla $A=\left\langle \Sigma, K, \delta, q_0, F \right\rangle$ dove:

- $\Sigma: \left\{ \sigma_1, \sigma_2,...,\sigma_n \right\}$ alfabeto di input
- $K: \left\{ q_1, q_2,...,q_m \right\}$ insieme finito non vuoto di stati
- $F\sube K$ insieme di stati finali
- $q_0\in K$ stato iniziale
- $\delta:K \times \Sigma\to K$ funzione totale di transizione che determina lo stato successivo

$$
\begin{cases}
\underline{\delta}(q,\epsilon)=q\\
\underline{\delta}(q,xa)=\delta(\underline{\delta}(q,x),a)
\end{cases}
$$

Si estende la funzione di transizione alle stringhe: $\underline{\delta}:K\times \Sigma^*\to K$

Con $x\in \Sigma^*$ ed $a \in \Sigma$

---

## Automi a stati finiti non deterministici

Definito come una quintupla $A=\left\langle \Sigma, K, \delta_N, q_0, F \right\rangle$ dove:

- $\Sigma: \left\{ \sigma_1, \sigma_2,...,\sigma_n \right\}$ alfabeto di input
- $K: \left\{ q_1, q_2,...,q_m \right\}$ insieme finito non vuoto di stati
- $F\sube K$ insieme di stati finali
- $q_0\in K$ stato iniziale
- $\delta_N:K \times \Sigma\to P(K)$ funzione totale di transizione che determina l’insieme (eventualmente vuoto) degli stati successivi

$$
\begin{cases}
\underline{\delta}_N(q,\epsilon)=\left\{q\right\}\\
\underline{\delta}_N(q,xa)=\bigcup_{p\in \underline{\delta}_N{(q,x)}}\delta_N(p,a)
\end{cases}
$$

Si estende la funzione di transizione alle stringhe: $\underline{\delta}_N:K\times \Sigma^*\to P(K)$

Con $x\in \Sigma^*$ ed $a \in \Sigma$, $p\in K$

---

## Grammatica $\to$ ASFND

Data $G=\left\langle V_T, V_N, P, S \right\rangle$ priva di produzioni elementari si costruisce $A_N=\left\langle \Sigma, K, \delta_N, q_0, F \right\rangle$ come segue:

- $\Sigma=V_T$
- $K=\left\{ q_I | I \in V_N \right\}$
- $q_0=q_S$
- $F=\left\{ q_B | B\to \epsilon \in P \right\}$
- $\delta_N(q_B,a)=\left\{ q_C | B\to aC \in P \right\}$

Dove in generale l’automa $A_N$ è non deterministico

---

## ASFND $\to$ Grammatica

Dato $A=\left\langle \Sigma, K, \delta, q_0, F \right\rangle$ si costruisce una grammatica regolare $G=\left\langle V_T, V_N, P, S \right\rangle$ priva di produzioni elementari come segue:

- $V_T=\Sigma$
- $V_N=\left\{ A_i|q_i \in K \right\}$
- $S=A_0$

Per ogni stato $q_j$ $\in$ $\delta(q_i,a)$ si costruisce la produzione $A_i\to aA_j$.

Per ogni stato $q_j\in F$ si costruisce la produzione $A_j \to \epsilon$.

---

## ASFND $\to$ ASF

- `teorema`: dato un $ASF$ che riconosce il linguaggio $L$, esiste un $\text{ASFND}$ che riconosce $L$, questo vale vicerversa.
- `dimostrazione`: la simulazione di un $\text{ASF}$ con un $\text{ASFND}$ è banale, i 2 automi sostanzialmente coincidono. La simulazione di un $\text{ASFND}$ con un $\text{ASF}$ sfrutta la finitezza di $P(K)$

Dato $A_N=\left\langle \Sigma, K, \delta_N, q_0, F \right\rangle$ si costruisce $A'=\left\langle \Sigma', K', \delta', q_0', F' \right\rangle$ come segue:

- $\Sigma'=\Sigma$
- $K$ è in corrispondenza biunivoca con $2^K$, i nomi degli stati di $K'$ sono i sottoinsiemi in $[\space]$, cioè si ha una cosa di questo tipo: $K'=\left\{ \left[q_{i1},..., q_{ik}\right] | \left\{ q_{i1},..., q_{ik} \right\} \in 2^K\right\}$
- $q'_0=[q_0]$
- $F'=\left\{ \left[q_{i1},..., q_{ik}\right] | \left\{ q_{i1},..., q_{ik} \right\} \in 2^K \wedge \left\{ q_{i1},...,q_{ik}\right\}\cap F \neq\emptyset  \right\}$
- $\delta'([q_{i1},...,q_{ik}],a)=[q_{j1},...,q_{jm}]$ dove $\left\{ q_{j1},...,q_{jm} \right\}=\delta_N(q_{i1},a)\cup...\cup\delta_N(q_{ik},a)$