# Macchine di Turing e linguaggi

Argomenti: Linguaggi di tipo 0, Linguaggi di tipo 1
.: No

## Linguaggi di tipo $0$ e $MT$

- `teorema`: ogni linguaggio di tipo $0$ ha una MT che lo riconosce
- `dimostrazione`: sia $G=\left\langle V_T,V_N,P,S \right\rangle$ una grammatica di tipo $0$ con $L=L(G)$, si costruisce una MTND multinastro $M$ che riconosce $L$.

Il primo nastro contiene la stringa $w$ della quale si vuole verificare l’appartenenza $L$. Il secondo nastro contiene le forme di frase ottenute nel corso del processo generativo.

---

## Linguaggi di tipo $1$ e $MT$

- `teorema`: i linguaggi di tipo $1$ sono decidibili