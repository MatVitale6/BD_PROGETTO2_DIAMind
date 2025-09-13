# Cardinalità Transfinite

Argomenti: Pidgeon Principle
.: No

## Pidgeon principle

- `teorema`: dati 2 insiemi $A$ e $B$ tali che $0<|B|<|A|<\infty$, allora non esiste una funzione $f:A\to B$ che sia totale e iniettiva
- `passo base`$(|B|=1)$: si ha $B=\left\{b\right\}$, $|A|>1$, es. $A=\left\{a_1,a_2\right\}$. Se $f$ è totale allora $f(a_1)=b$ e $f(a_2)=b$, il problema è che $f$ non è inettiva perché $|f^{-1}(b)|>1$
- `passo induttivo`$(|B|>1)$: si suppone sia vero per $|B|=n$ ed$|A|\ge n+1$, si dimostra che è vero per $|B|=n+1$ e $|A|\ge n+2$. Si ipotizza per assurdo che esista una funzione totale e iniettiva $f$ e si sceglie un qualunque elemento di $B$:
    - se $|f^{-1}(b)|\ge2$ si ha una contraddizione, quindi teorema dimostrato
    - se $|f^{-1}(b)|\le1$ si considera $A'=A-\left\{f^{-1}(b)\right\}$ e $B'=B-\left\{b\right\}$. Da qui si applica l’ipotesi induttiva ottenendo una contraddizione

---

## Cardinalità di insiemi infiniti

- Due insiemi sono `equinumerosi` se esiste una biiezione tra essi
- Un insieme è numerabile se è `equinumeroso` a $\mathbb{N}$ ed ha cardinalità $\aleph_0$
    - Un insieme è `contabile` se è finito o numerabile.