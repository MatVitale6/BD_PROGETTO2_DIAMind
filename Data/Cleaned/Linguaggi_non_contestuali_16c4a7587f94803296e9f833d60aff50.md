# Linguaggi non contestuali

Argomenti: Pumping lemma per tipo 2
.: No

## Decidibilità di una grammatica non contestuale che genera il linguaggio vuoto

- `lemma`: data una grammatica non contestuale esiste un algoritmo che decide se questa grammatica generi il linguaggio vuoto.
- `dimostrazione`: si suppone $|V_N|=k$, per verificare la producibilità di una stringa di soli terminali è sufficiente considerare l’insieme di tutti gli alberi di derivazione con tutti i terminali a profondità minore o uguale a $k$.
    - se una stringa di soli terminali è generata con almeno un terminale $y$ a profondità maggiore di $k$ allora sul cammino da $y$ a radice c’è un non terminale $A$ ripetuto 2 volte. L’albero può quindi essere potato producendo ancora una stringa di soli terminali.

## Decidibilità di una grammatica non contestuale che genera un linguaggio infinito

- `teorema`: data una grammatica non contestuale $G$, è decidibile stabilire se $L(G)$ è infinito
- `dimostrazione`: si considera l’insieme di tutti gli alberi sintattici che generano stringhe terminali in cui la foglia con maggiore profondità ha profondità tra $k$ e $2k$, con $k$ uguale al numero dei non terminali.
    - se l’insieme è vuoto allora il linguaggio è finito
    - altrimenti le derivazioni hanno almeno un non terminale ripetuto 2 volte e l’albero di derivazione può essere ampliato indefinitamente, continuando a produrre stringhe di terminali. Ottenendo quindi un linguaggio infinito.

---

## Pumping lemma per i tipo 2

- `teorema`: se $L$ è un linguaggio non contestuale allora esiste una costante $n$ tale che se $z\in L$ e $|z|\ge n$ allora esistono $u,v,w,x,y$ tali che: $(1)$ $uvwxy=z$, $(2)$ $|vx|\ge 1$, $(3)|vwx|\le n$ e $\forall i\ge 0$ $uv^iwx^iy\in L$.
- `dimostrazione`: La dimostrazione si basa sull'analisi dell'albero di derivazione per una certa stringa.

Prendendo una stringa $z$, se l’albero di derivazione di questa stringa ha altezza $h$ allora $|z|=b^h$, dove $b$ è il `branching-factor`. Supponendo che $|V_N|=h$, se $|z|\ge|V_N|+1$ allora l’albero di derivazione che genera $z$ deve avere un altezza maggiore o uguale di $|V_N|+1$. Questo vuol dire che c’è un percorso dalla radice alla foglia che ha lunghezza $|V_N|+2$ nodi e se si leva la foglia si hanno $|V_N|+1$ non terminali, di conseguenza c’è un non terminale che si ripete.

Se si suppone che il `pumping-length` sia pari a $b^{|V_N|+1}$ allora si chiama con $A$ il non terminale che si ripete se si sostituisce $A_1$ con il sottoalbero radicato $A_2$ si ottiene tutta la generazione di sottostringhe per $i$ ≠ 0 (ragionamento quando si aumentano i sottoalberi radicati)

---