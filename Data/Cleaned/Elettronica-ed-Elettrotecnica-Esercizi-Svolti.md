---
author:
- "*Giacomo Sturm*"
date: |
  *Dipartimento di Ingegneria Civile, Informatica e delle Tecnologie Aeronautiche  
  Università degli Studi “Roma Tre"*
title: |
  **Elettrotecnica ed Elettronica**  
  Esercizi Svolti di Elettrotecnica ed Elettronica  
  *Anno Accademico: 2023/24*
---

\providecommand{\labelText}[2]{#1}

# Elettronica

## Amplificatori Operazionali

Esercizi relativi al file “Amplificatori operazionali.pdf”, disponibile sul canale teams del corso.

### Esercizio 1.1

Determinare la tensione in uscita $V_o$ dal seguente circuito:

<div class="center">

</div>

Il generatore $V_2$ connesso all’ingresso non invertente del circuito non verrà considerato nel calcolo dei nodi, poiché il suo contributo in corrente è nullo. Per la legge costitutiva di un operazionale ideale si ricava l’equazione di vincolo, ovvero il nodo $A$, all’ingresso invertente, si trova allo stesso potenziale dell’ingresso non invertente, ovvero ha una tensione $V_2$, nota. Si risolve mediante il metodo dei nodi: $$\begin{gathered}
    \begin{bmatrix}
        \displaystyle\frac{\strut 1}{\strut R_1}+\frac{\strut 1}{\strut R_2}&-\displaystyle\frac{\strut 1}{\strut R_2}&0\\
        -\displaystyle\frac{\strut 1}{\strut R_2}&\displaystyle\frac{\strut 1}{\strut R_2}+\frac{\strut 1}{\strut R_3}+\frac{\strut 1}{\strut R_4}&-\displaystyle\frac{\strut 1}{\strut R_3}\\
        0&-\displaystyle\frac{\strut 1}{\strut R_3}&\displaystyle\frac{\strut 1}{\strut R_3}
    \end{bmatrix}\begin{bmatrix}
        V_A=V_2\\V_B\\V_O
    \end{bmatrix}=\begin{bmatrix}
        V_1\displaystyle\frac{\strut 1}{\strut R_1}\\0\\-i_x
    \end{bmatrix}\\
    \begin{bmatrix}
        0&-\displaystyle\frac{\strut 1}{\strut R_2}&0\\
        0&\displaystyle\frac{\strut 1}{\strut R_2}+\frac{\strut 1}{\strut R_3}+\frac{\strut 1}{\strut R_4}&-\displaystyle\frac{\strut 1}{\strut R_3}\\
        1&-\displaystyle\frac{\strut 1}{\strut R_3}&\displaystyle\frac{\strut 1}{\strut R_3}
    \end{bmatrix}\begin{bmatrix}
        i_x\\V_B\\V_O
    \end{bmatrix}=\begin{bmatrix}
        -\displaystyle\frac{\strut 1}{\strut R_1}-\frac{\strut 1}{\strut R_2}V_2+\frac{\strut 1}{\strut R_1}V_1\\
        \displaystyle\frac{\strut 1}{\strut R_2}V_2\\
        0
    \end{bmatrix}
\end{gathered}$$ Si applica il metodo di Cramer per ottenere la tensione in uscita: $$\begin{gathered}
    V_o=R_2R_3\begin{vmatrix}
        0 &-\displaystyle\frac{\strut1}{\strut R_2}&-\displaystyle\frac{\strut 1}{\strut R_1}-\frac{\strut 1}{\strut R_2}V_2+\frac{\strut 1}{\strut R_1}V_1\\
        0&\displaystyle\frac{\strut 1}{\strut R_2}+\frac{\strut 1}{\strut R_3}+\frac{\strut 1}{\strut R_4}&\displaystyle\frac{\strut 1}{\strut R_2}V_2\\
        1&-\displaystyle\frac{\strut1}{\strut R_3}&0
    \end{vmatrix}\\
    V_o=\displaystyle V_2R_2R_3\left[-\frac{1}{R_2^2}V_2+\frac{1}{R_1}\left(\frac{1}{R_2}+\frac{1}{R_3}+\frac{1}{R_4}\right)+\frac{1}{R_2}\left(\frac{1}{R_2}+\frac{1}{R_3}+\frac{1}{R_4}\right)\right]\\
    +V_1R_2R_3\left[-\frac{1}{R_1}\left(\frac{1}{R_2}+\frac{1}{R_3}+\frac{1}{R_4}\right)\right]\\
    V_o=\displaystyle\frac{(R_1+R_2)(R_3+R_4)+R_3R_4}{R_1R_3}V_2-\frac{R_2(R_3+R_3)+R_3R_4}{R_1R_4}V_1\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 1.2

Determinare la potenza assorbita dal resistore $R_L$:

<div class="center">

</div>

Per le leggi costitutive dell’amplificatore operazionale si ha $V_A=0$, per cui si può direttamente esprimere l’equazione risolutiva del metodo dei nodi, con già sostituita la corrente $i_x$ in uscita al posto di $V_A$: $$\begin{gathered}
    \begin{bmatrix}
        0&-\displaystyle\frac{\strut1}{\strut6}\\1&\displaystyle\frac{\strut1}{\strut2}+\frac{\strut1}{\strut6}+\frac{\strut1}{\strut12}+\frac{\strut1}{\strut15}+
    \end{bmatrix}\begin{bmatrix}
        i_x\\V_B
    \end{bmatrix}=\begin{bmatrix}
        \displaystyle\frac{\strut1}{\strut3}\\0
    \end{bmatrix}
\end{gathered}$$ Si applica il metodo di Cramer: $$\begin{gathered}
    V_B=6\begin{vmatrix}
        0&\displaystyle\frac{\strut1}{\strut3}\\1&0
    \end{vmatrix}=6\left(-\frac{1}{3}\right)=-2
\end{gathered}$$ La potenza si ottiene quindi come: $$P_{R_L}=\displaystyle\frac{V_B^2}{R_L}=\frac{4\,\mathrm{V}^2}{2\,\mathrm{k\Omega}}=2\,\mathrm{mW}$$

### Esercizio 1.3

Determinare il valore di $V_o$:

<div class="center">

</div>

La tensione in uscita al secondo operazionale $V_o$ è indipendente da ciò che entra nella sua entrata invertente. Passa una stessa corrente attraverso le due resistenze connesse al nodo $P$, poiché la corrente in entrata all’amplificatore è nulla, quindi non si biforca la corrente. Poiché la tensione di uscita $V_o$ è fissata, e misurata rispetto alla massa comune, si può determinare la tensione del nodo $P$ per la legge dei partitori di tensione, dato che le due resistenze sono virtualmente in serie: $$\begin{gathered}
    V_P=1\,\mathrm{k\Omega}\cdot\displaystyle\frac{V_o}{5\,\mathrm{k\Omega}}=\frac{V_o}{5}
\end{gathered}$$ Per la legge costitutiva degli amplificatori operazionali, la tensione misurata in $P$ coincide alla tensione misurata sul nodo $B$, l’ingresso non invertente dell’amplificatore.

Quindi è possibile risolvere questo circuito utilizzando solo tre nodi $A$, $B$ e $O$: $$\begin{gathered}
    \begin{bmatrix}
        1+\displaystyle\frac{\strut1}{\strut 10}+\frac{\strut 1}{\strut 50}&-\displaystyle\frac{\strut 1}{\strut 10}&-\displaystyle\frac{\strut 1}{\strut 50}\\
        -\displaystyle\frac{\strut 1}{\strut 10}&\displaystyle\frac{\strut1}{\strut10}&0\\
        -\displaystyle\frac{\strut 1}{\strut 50}&0&G_o\\
    \end{bmatrix}\begin{bmatrix}
        V_A\\V_B\\V_o
    \end{bmatrix}=\begin{bmatrix}
        0.2\\-i{x_1}\\-i_{x_2}
    \end{bmatrix}
\end{gathered}$$ Si inseriscono i vincoli ottenuti precedentemente: $$\begin{gathered}
    V_A=0\\
    V_B=\displaystyle\frac{V_o}{5}
\end{gathered}$$ L’equazione risolutiva diventa: $$\begin{gathered}
    \begin{bmatrix}
        0&0&-\displaystyle\frac{\strut 1}{\strut 50}-\frac{\strut 1}{\strut 50}\\
        1&0&-\displaystyle\frac{\strut 1}{\strut 50}+0\\
        0&1&G_o\\
    \end{bmatrix}\begin{bmatrix}
        i_{x_1}\\i_{x_2}\\V_o
    \end{bmatrix}=\begin{bmatrix}
        0.2\\0\\0
    \end{bmatrix}
\end{gathered}$$ Si ricava la tensione in uscita tramite il metodo di Cramer: $$\begin{gathered}
    V_o=-25\begin{vmatrix}
        0&0&0.2\\
        1&0&0\\
        0&1&0\\
    \end{vmatrix}=-25\cdot0.2=-5\,\mathrm{V}
\end{gathered}$$

### Esercizio 1.4

Determinare l’espressione della corrente $i_x$:

<div class="center">

</div>

Per la legge costitutiva degli amplificatori operazionali, si ha che $V_A=V_C$. Si risolve mediante il metodo dei nodi: $$\begin{gathered}
    \begin{bmatrix}
        \displaystyle\frac{\strut1}{\strut R_1}+\displaystyle\frac{\strut1}{\strut R_2}&-\displaystyle\frac{\strut1}{\strut R_2}&0\\
        -\displaystyle\frac{\strut1}{\strut R_2}&\displaystyle\frac{\strut2}{\strut R_2}&-\displaystyle\frac{\strut1}{\strut R_2}\\
        0&-\displaystyle\frac{\strut1}{\strut R_2}&\displaystyle\frac{\strut1}{\strut R_1}+\displaystyle\frac{\strut1}{\strut R_2}+\displaystyle\frac{\strut1}{\strut R_3}
    \end{bmatrix}\begin{bmatrix}
        V_A\\V_B\\V_C=V_A
    \end{bmatrix}=\begin{bmatrix}
        0\\-i_{xo}\\\displaystyle\frac{\strut v_g}{\strut R_1}
    \end{bmatrix}\\
    \begin{bmatrix}
        \displaystyle\frac{\strut1}{\strut R_1}+\displaystyle\frac{\strut1}{\strut R_2}&-\displaystyle\frac{\strut1}{\strut R_2}&0\\
        -\displaystyle\frac{\strut1}{\strut R_2}-\displaystyle\frac{\strut1}{\strut R_2}&\displaystyle\frac{\strut2}{\strut R_2}&1\\
        \displaystyle\frac{\strut1}{\strut R_1}+\displaystyle\frac{\strut1}{\strut R_2}+\displaystyle\frac{\strut1}{\strut R_3}&-\displaystyle\frac{\strut1}{\strut R_2}&0
    \end{bmatrix}\begin{bmatrix}
        V_A\\V_B\\i_{xo}
    \end{bmatrix}=\begin{bmatrix}
        0\\0\\\displaystyle\frac{v_g}{R_1}
    \end{bmatrix}
\end{gathered}$$ Utilizzando il metodo di Cramer, si ottiene la seguente espressione per la tensione $V_A$: $$\begin{gathered}
    V_A=V_C=\displaystyle\frac{1}{\displaystyle\frac{1}{R_2}\left(\frac{1}{R_1}+\frac{1}{R_2}\right)+\frac{1}{R_2}\left(-\frac{1}{R_1}-\frac{1}{R_2}-\frac{1}{R_3}\right)}
    \begin{vmatrix}
        0&-\displaystyle\frac{\strut1}{\strut R_2}&0\\
        0&\displaystyle\frac{\strut2}{\strut R_2}&1\\
        \displaystyle\frac{\strut v_g}{\strut R_1}&-\displaystyle\frac{\strut1}{\strut R_2}&0
    \end{vmatrix}\\
    \displaystyle\frac{\displaystyle\frac{1}{R_2}\left(-\frac{v_g}{R_1}\right)}{\displaystyle\frac{1}{R_2}\left(\frac{1}{R_1}+\frac{1}{R_2}\right)+\frac{1}{R_2}\left(-\frac{1}{R_1}-\frac{1}{R_2}-\frac{1}{R_3}\right)}\\
    V_A=\displaystyle\frac{v_gR_3}{R_1}
\end{gathered}$$ La corrente $i_x$ risulta quindi essere: $$i_x=\displaystyle\frac{V_A}{R_3}=\frac{v_g}{R_1}$$

### Esercizio 1.5

Determinare il valore di $v_o$:

<div class="center">

</div>

Poiché $V_A=0$, si indica come incognita la corrente in uscita dall’amplificatore $i_x$: $$\begin{gathered}
    \begin{bmatrix}
        0&-\displaystyle\frac{\strut1}{\strut3}\\
        1&\displaystyle\frac{\strut1}{\strut3}
    \end{bmatrix}\begin{bmatrix}
        i_x\\V_o
    \end{bmatrix}=\begin{bmatrix}
        \displaystyle\frac{\strut12}{\strut4}+2\\0
    \end{bmatrix}
\end{gathered}$$ $$V_o=3\begin{vmatrix}
        0&5\\1&0
    \end{vmatrix}=-15\,\mathrm{V}$$

### Esercizio 1.6

Determinare il valore di $v_o$:

<div class="center">

</div>

Poiché la corrente in entrata all’ingresso non invertente è nulla, per la legge costitutiva degli amplificatori, la tensione allo stesso ingresso coincide con la tensione erogata dal generatore a valle. Poiché anche la corrente in entrata all’ingresso invertente è nulla, la tensione che si trova al morsetto di ingresso, coincide alla tensione sul nodo $A$, poiché la resistenza che li collega non provoca una caduta di tensione, essendo attraversata da una corrente nulla. A questo punto per la legge del partitore di tensione inversa si ricava la tensione $v_o$, poiché la tensione $V_A$ è fissa: $$\begin{gathered}
    V_A=\displaystyle\frac{4\,\mathrm{k\Omega}}{(8+4)\mathrm{k\Omega}}v_o\\
    v_o=3V_A=3\cdot2.5\,\mathrm{V}=7.5\,\mathrm{V}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 1.7

Determinare il valore di corrente $i_o$:

<div class="center">

</div>

Per la legge costitutiva degli amplificatori, il potenziale sulla porta in entrata di A1 è pari alla somma delle tensioni erogate tra i generatori: $$\begin{gathered}
    v_{1,\mathrm{in}}=7.8\,\mathrm{V}
\end{gathered}$$ Mentre il potenziale in entrata al secondo operazionale equivale alla tensione erogata dal generatore più a valle: $$\begin{gathered}
    v_{2,\mathrm{in}}=5.8\,\mathrm{V}
\end{gathered}$$ Poiché le correnti in entrata sono nulle, le resistenze di $6\,\mathrm{k\Omega}$ non provocano una caduta di tensione, per cui sui nodi $A$ e $B$ sono presenti rispettivamente i potenziali $v_{1,\mathrm{in}}$ e $v_{2,\mathrm{in}}$. Per cui la tensione sul resistore da $4\,\mathrm{k\Omega}$ si ottiene come la differenza tra i potenziali di $A$ e $B$: $$\begin{gathered}
    V_{4\,\mathrm{k\Omega}}=V_A-V_B=v_{1,in}-v_{2,\mathrm{in}}=2\,\mathrm{V}
\end{gathered}$$ La corrente che fluisce per la resistenza $4\,\mathrm{k\Omega}$ è la stessa che attraversa le due resistenza da $8\,\mathrm{k\Omega}$, per cui si può ricavare la tensione ai capi della tre resistenze in serie: $$\begin{gathered}
    i_{4\,\mathrm{k\Omega}}=\displaystyle\frac{2\,\mathrm{V}}{4\,\mathrm{k\Omega}}=\frac{1}{2}\,\mathrm{mA}\\
    V_x=(8+8+4)\mathrm{k\Omega}\cdot\frac{1}{2}\,\mathrm{mA}=10\,\mathrm{V}
\end{gathered}$$ La corrente $i_o$ si ottiene quindi come: $$i_x=\displaystyle\frac{V_x}{4\,\mathrm{k\Omega}}=\frac{10}{4}\,\mathrm{mA}=2.5\,\mathrm{mA}$$

### Esercizio 1.8

Determinare il valore di $v_o$:

<div class="center">

</div>

Questo circuito rappresenta un inseguitore di tensione, poiché l’amplificatore è connesso in modo tale che il potenziale inserito nel morsetto non invertente viene trasferito sul nodo $O$. Poiché la corrente in entrata è nulla, non è presente una retroazione, può essere risolto separatamente dall’amplificatore il circuito di sinistra per calcolare il potenziale del nodo $A$, in seguito si applica al nodo $O$ e tramite la legge dei partitori di tensione si ottiene la tensione in uscita dalla rete. Si calcola mediante il metodo dei nodi il potenziale $V_A$: $$\begin{gathered}
    V_A=\displaystyle\frac{\displaystyle\frac{2}{20}-\frac{5}{40}}{\displaystyle\frac{1}{20}+\frac{1}{40}+\frac{1}{40}}\,\mathrm{V}=-\frac{1}{4}\,\mathrm{V}
\end{gathered}$$ La tensione in uscita si ottiene come: $$\begin{gathered}
    V_o=\displaystyle\frac{(1+9)\,\mathrm{k\Omega}}{1\,\mathrm{k\Omega}}V_A=-2.5\,\mathrm{V}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 1.9

Determinare la tensione in uscita $v_o$:

<div class="center">

</div>

Si calcola il potenziale sul nodo $B$, morsetto non invertente dell’operazionale, tramite la legge dei partitori di tensione: $$\begin{gathered}
    V_B=\displaystyle\frac{\displaystyle-\frac{4}{4}+2}{\displaystyle\frac{1}{4}}\,\mathrm{V}=4\,\mathrm{V}
\end{gathered}$$ I potenziali ad entrambi i morsetti dell’operazionale sono uguali, per cui $V_A=V_B$, si inserisce questa equazione di vincolo direttamente nell’equazione risolutiva mediante il metodo dei nodi: $$\begin{gathered}
    \begin{bmatrix}
        \displaystyle\frac{\strut1}{\strut8}+\frac{\strut1}{\strut24}&-\displaystyle\frac{\strut1}{\strut24}\\
        -\displaystyle\frac{\strut1}{\strut24}&\displaystyle\frac{\strut1}{\strut24}+\frac{\strut1}{\strut10}
    \end{bmatrix}\begin{bmatrix}
        4\\v_o
    \end{bmatrix}=\begin{bmatrix}
        \displaystyle\frac{\strut3}{\strut8}\\-i_x
    \end{bmatrix}\\
    \begin{bmatrix}
        0&-\displaystyle\frac{\strut1}{\strut24}\\
        1&G_o
    \end{bmatrix}\begin{bmatrix}
        i_x\\v_o
    \end{bmatrix}=\begin{bmatrix}
        \displaystyle\frac{\strut3}{\strut8}-\frac{\strut4}{\strut6}\\\displaystyle\frac{\strut1}{\strut6}
    \end{bmatrix}
\end{gathered}$$ Si calcola la tensione in uscita tramite il metodo di Cramer: $$v_o=24\begin{vmatrix}
        0&\displaystyle\frac{\strut9-16}{25}\\
        1&\displaystyle\frac{\strut1}{\strut6}
    \end{vmatrix}=7\,\mathrm{V}$$

## Dominio di Laplace

Eserciti relativi al file “Laplace Esercizi.pdf”, disponibile sul canale teams del corso.

### Esercizio 2.1

Calcolare la trasformata di Laplace della funzione: $$\begin{gathered}
    f(t)=\sin(t-2)u(t-2)\\
    F(s)=\displaystyle\int_{0^-}^{+\infty}\sin(t-2)u(t-2)e^{-st}\mathrm{d}t\\
    \tau=t-2\\
    F(s)=\displaystyle\int_{0^-}^{+\infty}\sin(\tau)e^{-s(\tau+2)}\mathrm{d}\tau=\frac{e^{-e^{2s}}}{s^2+1}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 2.2

Calcolare la trasformata di Laplace del seguente segnale:

<div class="center">

</div>

$$\begin{gathered}
    f(t)=\displaystyle\frac{5}{2}tu(-t+2)u(t)\\
    F(s)=\displaystyle\int_{0^-}^{+\infty}\frac{5}{2}u(-t+2)e^{-st}\mathrm{d}t=\frac{5}{2}\int_{0^-}^2te^{-st}\mathrm{d}t\\
    \displaystyle\frac{5}{2}\left(-\frac{te^{-st}}{s}+\frac{e^{-st}}{s^2}\right.\Bigg|_{0^-}^2=\frac{5}{s^2}\left(2se^{-2s}+e^{-2s}-0-1\right)\\
    F(s)=\displaystyle\frac{5}{2}\frac{1-e^{-2s}-2se^{-2s}}{s^2}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 2.3

Calcolare l’antitrasformata di Laplace della seguente funzione: $$\begin{gathered}
    F(s)=\displaystyle\frac{10}{(s+2)(s^2+6+10)}=\frac{10}{(s+2)(s+3-j)(s+3+j)}\\
    F(s)=\displaystyle\frac{A}{s+2}+\frac{B}{s+3-j}+\frac{B^*}{s+3+j}\\
    A=(s+2)F(s)\bigg|_{s=-2}=\displaystyle\frac{10}{(-2)^2+6(-2)+10}=5\\
    B=(s+3-i)F(s)\bigg|_{s=-3+j}=\displaystyle\frac{10}{(-3+j+2)(-3+j+3+j)}=\frac{1}{2j}\frac{10}{-1-j}\frac{-1+j}{-1+j}\\
    B=\displaystyle\frac{1}{2j}5(-1-j)=\frac{1}{2j}5\sqrt{2}e^{-j3\pi/4}\\
    f(t)=5e^{-2t}+5e^{-3t}\sqrt2\sin\left(t-\frac{3\pi}{4}\right)u(t)\\
    f(t)=5e^{-2t}+5e^{-3t}\left[\cancelto{-1}{\sqrt{2}\cos\left(\frac{3\pi}{4}\right)}\sin(t)-\cancelto{1}{\sqrt2\sin\left(\frac{3\pi}{4}\right)}\cos(t)\right]u(t)\\
    f(t)=5e^{-2t}-5e^{-3t}\left[\sin(t)+\cos(t)\right]u(t)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 2.4

Calcolare l’antitrasformata di Laplace della seguente funzione: $$\begin{gathered}
    F(s)=\displaystyle\frac{3e^{-s}}{s^2+2s+17}=G(s)e^{-s}\to g(t-1)\\
    G(s)=\displaystyle\frac{3}{s^2+2s+1+16}=\frac{3}{(s+1)^2+16}=\frac{3}{(s+1-4j)(s+1+4j)}\\
    G(s)=\displaystyle\frac{A}{s+1-4j}+\frac{A^*}{s+1+4j}\\
    A=(s+1-4j)G(s)\bigg|_{s=-1+4j}=\displaystyle\frac{3}{-1+4j+1+4j}=\frac{1}{2j}\frac{3}{4}
\end{gathered}$$ Il fattore $3/4$ corrisponde al modulo del fasore $\overline{G}$, poiché è puramente reale, ha fase nulla. La pulsazione coincide alla parte immaginaria del polo, quindi si ha: $$\begin{gathered}
    g(t)=\frac{3}{4}e^{-t}\sin(4t)u(t)\\
    f(t)=g(t-1)=\displaystyle\frac{3}{4}e^{-(t-1)}\sin(4(t-1))u(t-1)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 2.5

Calcolare la tensione ai capi dei morsetti $v_o(t)$ del seguente circuito, dopo la commutazione da $A$ e $B$:

<div class="center">

</div>

Il circuito prima della commutazione si trova a regime, per cui la tensione ai capi del condensatore corrisponde alla tensione erogata dal generatore: $$\begin{gathered}
    v_C(0^-)=12\,\mathrm{V}
\end{gathered}$$ La memoria dell’induttore invece corrisponde a: $$\begin{gathered}
    i(0^-)=\displaystyle\frac{12\,\mathrm{V}}{0.2\,\Omega}=60\,\mathrm{A}
\end{gathered}$$

<div class="center">

</div>

Si applica il metodo dei nodi, corrispondente al teorema di Millman in questo caso: $$\begin{gathered}
    V_\mathrm{out}(s)=\displaystyle\frac{\displaystyle\frac{Li(0^-)}{sL}+\frac{sCv_C(0^-)}{s}}{\displaystyle\frac{1}{sL}+\frac{1}{R}+sC}=\frac{\displaystyle\frac{Li(0^-)+sLCv_C(0^-)}{sL}}{\displaystyle\frac{1+sGL+s^2LC}{sL}}\\
    V_\mathrm{out}(s)=\displaystyle\frac{Li(0^-)+sLCv_C(0^-)}{LC\left(s^2+s\displaystyle\frac{1}{RC}+\frac{1}{LC}\right)}
\end{gathered}$$ Si considera il denominatore e si individuano i poli $s_1$ e $s_2$: $$\begin{gathered}
    D(s)=LC\left(s^2+s\displaystyle\frac{1}{RC}+\frac{1}{LC}\right)=LC(s-s_1)(s-s_2)
\end{gathered}$$ Si considerano i valori delle grandezze: $$\begin{gathered}
    Li(0^-)=30\\
    LC=\displaystyle\frac{3}{2}\\
    \displaystyle\frac{1}{RC}=\frac{5}{3}
\end{gathered}$$ Sostituendo i valori ottenuti nella funzione, si ottiene: $$\begin{gathered}
    \displaystyle D(s)=\frac{3}{2}\left[s^2+\frac{5}{3}s+\frac{2}{3}\right]\\
    s_{1,2}=\displaystyle\frac{1}{2}\left(-\frac{5}{3}\pm\sqrt{\frac{25}{9}-\frac{8}{3}}\right)=-\frac{5}{6}\pm\sqrt{\frac{25-24}{9}}=-\frac{5}{6}\pm\frac{1}{6}\\
    s_1=-1\\
    s_2=\displaystyle-\frac{2}{3}\\
    F(s)=\displaystyle\frac{30+s\displaystyle\frac{3}{2}12}{\displaystyle\frac{3}{2}(s+1)\left(s+\frac{2}{3}\right)}
\end{gathered}$$ Si scompone la funzione di rete in fratti semplici: $$\begin{gathered}
    F(s)=\displaystyle\frac{A_1}{s-s_1}+\frac{A_2}{s-s_2}=\frac{20+12s}{(s+1)\left(s+\displaystyle\frac{2}{3}\right)}
\end{gathered}$$ Si considerano due metodi per risolvere: $$\begin{gathered}
    A_1(s-s_1)+A_2(s-s_2)=20+12s\\
    \begin{cases}
        A_1+A_2=12\\
        A_1s_1+A_2s_2=-20
    \end{cases}\\
    f(t)=A_1e^{s_1t}+A_2e^{s_2t}
\end{gathered}$$ Poiché i poli hanno parte reale negativa, per cui la funzione di rete è asintoticamente stabile. Alternativamente si applica il metodo dei residui per determinare $A_1$ e $A_2$: $$\begin{gathered}
    \lim_{s\to s_1}(s-s_1)F(s)=\lim_{s\to s_1}\displaystyle\frac{20+12s}{s-s_2}=\lim_{s\to s_1}\left(A_1+A_2\frac{s-s_1}{s-s_2}\right)=A_1\\
    A_1=\displaystyle\frac{20+12s_1}{s_1-s_2}=\frac{20-12}{-1+\displaystyle\frac{2}{3}}=-24\\
    A_2=\displaystyle\frac{20+12s_2}{s_2-s_1}=\frac{20-8}{-\displaystyle\frac{2}{3}+1}=36
\end{gathered}$$ Per cui la funzione nel dominio del tempo risulta essere: $$\begin{gathered}
    f(t)=-24e^{-t}+36^{-\frac{2}{3}t}=v_o(t)
\end{gathered}$$ Corrisponde alla tensione ai capi del condensatore, e coincide alla tensione ai capi dei morsetti del circuito, poiché la commutazione avviene in un tempo $t=0$, questa espressione è valida solo per un tempo $t\geq0^+$: $$v_o(t)=(36e^{-\frac{2}{3}t}-24e^{-t})u_{-1}(t)$$

### Esercizio 2.6

Determinare l’espressione di $i_x(t)$ del seguente circuito a memorie nulle:

<div class="center">

</div>

Considerando la memoria dell’induttore nulla si esprime il circuito nel dominio di Laplace:

<div class="center">

</div>

Si applica il teorema di Millman per il nodo $A$: $$\begin{gathered}
    V_A(s)\left(\displaystyle\frac{1}{5}+\frac{1}{4s+3}\right)=\frac{7}{s+6}\\
    V_A(s)=\displaystyle\frac{7}{s+6}\frac{5\left(s+\displaystyle\frac{3}{4}\right)}{(s+2)}=\frac{35\left(s+\displaystyle\frac{3}{4}\right)}{(s+2)(s+6)}
\end{gathered}$$ Si determina ora la corrente di lato $I_x(s)$: $$\begin{gathered}
    I_x(s)=\displaystyle\frac{V_A(s)}{\displaystyle4\left(s+\frac{3}{4}\right)}=\frac{35}{4}\frac{1}{(s+2)(s+6)}=\frac{A}{s+2}+\frac{B}{s+6}\\
    A=\displaystyle(s+2)I_x(s)\bigg|_{s=-2}=\frac{35}{16}\\
    B=\displaystyle(s+6)I_x(s)\bigg|_{s=-6}=-\frac{35}{16}\\
    i_x(t)=\displaystyle\frac{35}{16}\left(e^{-2t}-e^{-6t}\right)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 2.7

Determinare l’espressione della corrente $i_L(t)$, dopo la commutazione, del seguente circuito:

<div class="center">

</div>

$$\begin{gathered}
    i_L(0^-)=4\,A\\
    v_C(0^-)=8\,V
\end{gathered}$$

Si rappresenta il circuito equivalente nel dominio di Laplace:

<div class="center">

</div>

Si risolve mediante il metodo dei nodi per avere direttamente la trasformata di $i_L(t)$: $$\begin{gathered}
    \begin{bmatrix}
        1+\displaystyle\frac{\strut 1}{\strut s}&\displaystyle-\frac{\strut 1}{\strut s}\\ \displaystyle-\frac{\strut 1}{\strut s}&\displaystyle\frac{\strut 1}{\strut s}+s+1
    \end{bmatrix}\begin{bmatrix}
        I_{m_1}(s)\\I_{m_2}(s)
    \end{bmatrix}=\begin{bmatrix}
        \displaystyle\frac{\strut 12}{\strut s}-\frac{\strut 8}{\strut s}\\ \displaystyle\frac{\strut 8}{\strut s}+4
    \end{bmatrix}\\
    \begin{bmatrix}
        \displaystyle\frac{\strut s+1}{\strut s}&\displaystyle-\frac{\strut 1}{\strut s}\\ \displaystyle-\frac{\strut 1}{\strut s}&\displaystyle\frac{\strut 1+s(s+1)}{\strut s}
    \end{bmatrix}\begin{bmatrix}
        I_{m_1}(s)\\I_{m_2}(s)
    \end{bmatrix}=\begin{bmatrix}
        \displaystyle\frac{\strut 4}{\strut s}\\ \displaystyle\frac{\strut 4(s+2)}{\strut s}
    \end{bmatrix}
\end{gathered}$$ Si ricava la corrente della seconda maglia tramite il metodo di Cramer: $$\begin{gathered}
    I_{m_2}(s)=\displaystyle\frac{s^2}{(s+1)+s(s+1)^2-1}\begin{vmatrix}
        \displaystyle\frac{\strut s+1}{\strut s}&\displaystyle\frac{\strut 4}{\strut s}\\ \displaystyle-\frac{\strut 1}{\strut s}
        &\displaystyle\frac{\strut 4(s+2)}{\strut s}
    \end{vmatrix}\\
    I_{m_2}(s)=\displaystyle\frac{s^2}{(s+1)+s(s+1)^2-1}\frac{4+(8s+8+4s^2+4s)}{s^2}=\frac{4s^2+12s+12}{s(s^2+2s^1+2)}=I_L(s)
\end{gathered}$$

Si individuano ora i poli al finito di $I_L(s)$: $$\begin{gathered}
    s_{p_1}=0\\
    s_{p_{2,3}}=-{-1\pm\sqrt{1-2}}=-1\pm j\\
    s_{p_2}=-1+j=s_{p_3}^*
\end{gathered}$$ Si calcolano i residui $A$ e $B$, poiché il residuo di $s_{p_3}$ è pari al coniugato del suo coniugato $B^*$, usando la formula per i residui: $$\begin{gathered}
    I_L(s)=\displaystyle\frac{A}{s-s_{p_1}}+\frac{B}{s-s_{p_2}}+\frac{B^*}{s-s_{p_2}^*}\\
    A=\lim_{s\to 0}\displaystyle\cancel{\frac{s}{s}}\frac{4s^2+12s+12}{s^2+2s+2}=\frac{12}{2}=6\\
    B=\lim_{s\to -1+j}\displaystyle\cancel{\frac{s+1-j}{s+1-j}}\frac{4s^2+12s+12}{s(s+1+j)}=\frac{4(-1+j)^2+12(-1+j)+12}{(-1+j)(-1+j+1+j)}\\
    \displaystyle\frac{1}{2j}\frac{4-4-8j-12+12j+12}{-1+j}=\frac{1}{2j}\frac{4j}{-1+j}\frac{-1-j}{-1-j}=\frac{1}{2j}\frac{4j(-1-j)}{2}\\    
    \displaystyle\frac{1}{2j}(-2j+2)=\frac{1}{2j}\left(2\sqrt{2}e^{-j\frac{\pi}{4}}\right)
\end{gathered}$$ Ricordando l’espressione in fasori di un’entrata sinusoidale: $$\begin{gathered}
    I_M\sin(\omega t+\beta)=\displaystyle\frac{I_M}{2j}e^{j\beta}e^{\omega t}-\frac{I_M}{2j}e^{-j\beta}e^{-\omega t}
\end{gathered}$$ La trasformata di Laplace di un esponenziale si esprime come: $$\begin{gathered}
    \mathcal{L}\{Ae^{\sigma t}\}=\displaystyle\frac{A}{s-\sigma}
\end{gathered}$$ Per cui la trasformata di Laplace di una sinusoide smorzata si ottiene come: $$\begin{gathered}
    \mathcal{L}\{e^{j\sigma t}I_M\sin(\omega t+\beta)\}=\mathcal{L}\left\{e^{j\sigma t}\left[\displaystyle\frac{I_M}{2j}e^{j\beta}e^{j\omega t}-\frac{I_M}{2j}e^{-j\beta}e^{-j\omega t}\right]\right\}\\
    \mathcal{L}\left\{\displaystyle\frac{I_M}{2j}e^{j\beta}e^{(j\omega+\sigma) t}-\frac{I_M}{2j}e^{-j\beta}e^{-(j\omega+\sigma) t}\right\}=\frac{I_M}{2j}e^{\alpha t}\frac{1}{s-(j\omega +\sigma)}-\frac{I_M^*}{2j}e^{-\alpha t}\frac{1}{s-(-j\omega +\sigma)}
\end{gathered}$$ I residui ottenuti da $I_L(s)$ corrispondono quindi ad una funzione sinusoidale nel domino del tempo: $$\begin{gathered}
    I_L(s)=\displaystyle\frac{6}{s}+\frac{2\sqrt{2}e^{-j\frac{\pi}{4}}}{2j}\frac{1}{s-(-1+j)}-\frac{2\sqrt{2}e^{j\frac{\pi}{4}}}{2j}\frac{1}{s-(-1-j)}\\
    i_L(t)=6+2\sqrt{2}e^{-t}\sin\left(t-\displaystyle\frac{\pi}{4}\right)
\end{gathered}$$ Poiché il circuito si chiude per $t=0$, si moltiplica l’espressione ottenuta per il segnale gradino: $$i_L(t)=\left[6+2\sqrt{2}e^{-t}\sin\left(t-\displaystyle\frac{\pi}{4}\right)\right]u(t)$$

### Esercizio 2.8

Determinare l’espressione della corrente $i_L(t)$, dopo la commutazione da $A$ a $B$ del seguente circuito:

<div class="center">

</div>

Per calcolare la memoria si considerano $v_C=0$ e $i_L=0$, per cui si ottiene per la formula del partitore: $$\begin{gathered}
    v_C(0^-)=12\cdot\displaystyle\frac{8}{8+4}=8\,\mathrm{V}\\
\end{gathered}$$ Analogamente si ottiene un’espressione per la tensione: $$\begin{gathered}
    i_L(0^-)=\displaystyle\frac{12}{8+4}=1\,\mathrm{A}
\end{gathered}$$

Si rappresenta il modello equivalente nel dominio di Laplace, dopo aver chiuso l’interruttore:

<div class="center">

</div>

Si risolve mediante il metodo delle maglie: $$\begin{gathered}
    \begin{bmatrix}
        \displaystyle\frac{\strut{4s+20}}{\strut{s}}&-\displaystyle\frac{\strut{20}}{\strut{s}}\\
        -\displaystyle\frac{\strut{20}}{\strut{s}}&\displaystyle\frac{\strut{8s+4s^2+20}}{\strut{s}}
    \end{bmatrix}\begin{bmatrix}
        I_{m_1}(s)\\I_{m_2}(s)
    \end{bmatrix}=\begin{bmatrix}
        -\displaystyle\frac{\strut{8}}{\strut{s}}\\\displaystyle\frac{\strut{8}}{\strut{s}}+4
    \end{bmatrix}
\end{gathered}$$ Si calcola $I_{m_2}(s)$ mediante il metodo di Cramer: $$\begin{gathered}
    I_{m_2}(s)=\displaystyle\frac{s^2}{(4s^2+8s+20)(4s+20)-400}\begin{vmatrix}
        \displaystyle\frac{\strut{4s+20}}{\strut{s}}&
        -\displaystyle\frac{\strut{8}}{\strut{s}}\\-\displaystyle\frac{\strut{20}}{\strut{s}}&\displaystyle\frac{\strut{8}}{\strut{s}}+4
    \end{vmatrix}\\
    I_{m_2}(s)=\displaystyle\frac{s^2}{16s^3+32s^2+80s+80s^2+160s+400-400}\frac{(8+4s)(4s+20)-8\cdot20}{s^2}\\
    I_{m_2}(s)=\displaystyle\frac{s}{s}\frac{16s+112}{16s^2+112+240}=\frac{s+7}{s^2+7s+15}\\
    s_{p_{1,2}}=-\displaystyle\frac{7}{2}\pm j\frac{\sqrt{11}}{2}\\
    I_{m_2}(s)=\displaystyle\frac{A}{s+s_{p_1}}+\frac{A^*}{s+s_{p_2}}\\
    A=(s+s_{p_1})I_{m_2}(s)\bigg|_{s=s_{p_1}}=\displaystyle\frac{1}{j\sqrt{11}}\left(-\frac{7}{2}+j\frac{\sqrt{11}}{2}+\frac{14}{2}\right)\\
    A=\displaystyle\frac{1}{2j}\frac{1}{\sqrt{11}}\left(7+j\sqrt{11}\right)=\frac{1}{2j}\left(\frac{7}{\sqrt{11}}+j\right)\\
    \varphi=\arctan\left(\displaystyle\frac{\sqrt{11}}{7}\right)\\
    A=\displaystyle\frac{1}{2j}\frac{2\sqrt{165}}{11}e^{j\varphi}
\end{gathered}$$ Poiché $A$ corrisponde al fasore della corrente, si può esprimere l’espressione della corrente nel tempo come: $$\begin{gathered}
    i_L(t)=\displaystyle\frac{2\sqrt{165}}{11}e^{-7t/2}\sin\left(\frac{\sqrt{11}}{2}t+\varphi\right)u(t)\\
    \displaystyle\frac{2\sqrt{165}}{11}\sin\left(\frac{\sqrt{11}}{2}t+\varphi\right)=\displaystyle\frac{2\sqrt{165}}{11}\displaystyle\sin\left(\frac{\sqrt{11}}{2}t\right)\cos\varphi+\displaystyle\frac{2\sqrt{165}}{11}\cos\left(\frac{\sqrt{11}}{2}t\right)\sin\varphi\\
    \tan\varphi=\displaystyle\frac{\sqrt{11}}{7}\to \tan^2\varphi=\frac{11}{49}\\
    \sin^2\varphi+\cos^2\varphi=1\to \tan^2\varphi+1=\displaystyle\frac{1}{\cos^2\varphi}\\
    \cos\varphi=\displaystyle\sqrt{\frac{1}{1+\tan^2\varphi}}=\sqrt{\frac{1}{1+\frac{11}{49}}}=\frac{7\sqrt{15}}{30}\\
    \sin\varphi=\sqrt{1-\cos^2\varphi}=\sqrt{\displaystyle1-\left(\frac{7\sqrt{15}}{30}\right)^2}=\frac{\sqrt{165}}{30}\\
    \displaystyle\frac{2\sqrt{165}}{11}\cos\varphi=\displaystyle\frac{2\sqrt{165}}{11}\frac{7\sqrt{15}}{30}=\frac{7}{\sqrt{11}}\\
    \displaystyle\frac{2\sqrt{165}}{11}\sin\varphi=\displaystyle\frac{2\sqrt{165}}{11}\frac{\sqrt{165}}{30}=1\\
    i_L(t)=\displaystyle \left[\frac{7}{\sqrt{11}}\sin\left(\frac{\sqrt{11}}{2}t\right)+\cos\left(\frac{\sqrt{11}}{2}t\right)\right]e^{-7t/2}u(t)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 2.9 (3.6)

Determinare l’espressione della corrente $i(t)$, dopo la commutazione. Il circuito si trova a regima prima della commutazione nell’istante $t=0$:

<div class="center">

</div>

A regime, prima della commutazione, poiché il circuito è formato da un’unica maglia, tutta la tensione si trova ai capi del condensatore: $$\begin{gathered}
    v_C(0^-)=10\,\mathrm{V}
\end{gathered}$$ Mentre la corrente sull’induttore è nulla, poiché se tutta la carica è ai capi del condensatore non fluisce corrente: $$\begin{gathered}
    i_L(0^-)=0\,\mathrm{A}
\end{gathered}$$ É possibile ora esprimere il circuito nel dominio di Laplace:

<div class="center">

</div>

Si risolve mediante il metodo delle maglie: $$\begin{gathered}
    \begin{bmatrix}
        400&0\\0&400+s+\displaystyle\frac{\strut{2\cdot 10^5}}{\strut{s}}
    \end{bmatrix}\begin{bmatrix}
        I_{m_1}(s)\\I_{m_2}(s)
    \end{bmatrix}=\begin{bmatrix}
        \displaystyle\frac{\strut{10}}{\strut{s}}\\-\displaystyle\frac{\strut{10}}{\strut{s}}
    \end{bmatrix}
\end{gathered}$$ Si calcola $I_{m_2}(s)=I(s)$ mediante il metodo di Cramer: $$\begin{gathered}
    I(s)=\displaystyle\frac{s}{400(s^2+400s+2\cdot10^5s)}\begin{vmatrix}
        400&\displaystyle\frac{\strut{10}}{\strut{s}}\\0&-\displaystyle\frac{\strut{10}}{\strut{s}}
    \end{vmatrix}=\frac{s}{400(s^2+400s+2\cdot10^5)}\frac{-4000}{s}\\
    I(s)=\displaystyle-\frac{10}{s^2+400s+2\cdot10^5}=-\frac{10}{(s+200-400j)(s+200+400j)}\\
    A=(s+200-400j)I(s)\bigg|_{s=-200+400j}=\displaystyle\frac{1}{2j}\frac{-10}{400}=\frac{1}{2j}(-0.025)\\
    i(t)=-0.25e^{-200t}\sin(400t)u(t)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 2.10

Determinare la funzione di rete, data la risposta impulsiva $h(t)$ di un circuito: $$\begin{gathered}
    h(t)=\sqrt{2}e^{-t/\sqrt{2}}\sin\left(\frac{t}{\sqrt{2}}\right)u(t)\\
    \displaystyle\frac{\sqrt{2}}{2j}e^{-t/\sqrt{2}}\left(e^{jt/\sqrt{2}}-e^{-jt/\sqrt{2}}\right)=\frac{\sqrt{2}}{2j}e^{-t(1-j)/\sqrt{2}}-\frac{\sqrt{2}}{{2j}}e^{-t(1+j)/\sqrt{2}}\\
    H(s)=\displaystyle\frac{\sqrt{2}}{2j}\left(\frac{1}{s+\frac{1-j}{\sqrt{2}}}-\frac{1}{s+\frac{1+j}{\sqrt{2}}}\right)=\frac{\sqrt{2}}{s^2+\sqrt{2}s+1}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 2.11

Determinare per quali valori di $k$ il circuito è stabile:

<div class="center">

</div>

Per controllare la stabilità bisogna analizzare la funzione di rete del circuito. Si dice che un sistema è stabile, quando la funzione di trasferimento associata presenta solo poli a parte reale negativa. Per cui bisogna analizzare le soluzioni del denominatore della funzione di rete. Il denominatore della funzione di rete corrisponde al determinante della matrice delle ammettenze: $$\begin{gathered}
    \begin{bmatrix}
        1+1+\displaystyle\frac{\strut{1}}{\strut{s}}&-\displaystyle\frac{\strut{1}}{\strut{s}}\\-\displaystyle\frac{\strut{1}}{\strut{s}}&\displaystyle\frac{\strut{1}}{\strut{s}}+\displaystyle\frac{\strut{1}}{\strut{2s}}+1
    \end{bmatrix}\begin{bmatrix}
        V_x(s)\\V_o(s)
    \end{bmatrix}=\begin{bmatrix}
        I_{x_1}(s)\\-kV_x(s)+I_{x_2}(s)
    \end{bmatrix}\\
    \begin{vmatrix}
        \displaystyle\frac{\strut{2s+1}}{\strut{2}}&-\displaystyle\frac{\strut{1}}{\strut{s}}\\\displaystyle\frac{\strut{ks-1}}{\strut{s}}&\displaystyle\frac{\strut{3+s}}{\strut{2s}}
    \end{vmatrix}=s^2+(7+k)s+2
\end{gathered}$$ Un binomio ammette soluzioni a parte reale negativa solo se tutti i suoi coefficienti hanno lo stesso segno: $$7+k>0\to k>-7$$

### Esercizio 3.1

Determinare la stabilità del seguente circuito:

<div class="center">

</div>

Per determinare la stabilità bisogna calcolare la funzione di rete del circuito. Si considerano memorie nulle, quindi si esprime il circuito nel dominio di Laplace:

<div class="center">

</div>

Si risolve mediante il metodo delle maglie: $$\begin{gathered}
    \begin{bmatrix}
        1+s&-s\\-s&1+\displaystyle\frac{\strut{1}}{\strut{s}}+s
    \end{bmatrix}\begin{bmatrix}
        I_{m_1}(s)=I_x(s)\\I_{m_2}(s)
    \end{bmatrix}=\begin{bmatrix}
        V_g(s)\\-\displaystyle\frac{\strut{I_x(s)}}{\strut{2}}
    \end{bmatrix}\\
    \begin{bmatrix}
        1+s&-s\\\displaystyle\frac{\strut{-2s+1}}{\strut{2}}&\displaystyle\frac{\strut{s^2+s+1}}{\strut{s}}
    \end{bmatrix}\begin{bmatrix}
        I_x(s)\\I_{m_2}(s)
    \end{bmatrix}=\begin{bmatrix}
        V_g(s)\\0
    \end{bmatrix}
\end{gathered}$$ Si calcola $I_{m_2}(s)$ mediante il metodo di Cramer: $$\begin{gathered}
    I_{m_2}(s)=\displaystyle\frac{2s}{2(1+s)(s^2+s+1)-s^2(2s-1)}\begin{vmatrix}
        1+s&V_g(s)\\\displaystyle\frac{\strut{-2s+1}}{\strut{2}}&0
    \end{vmatrix}\\
    I_{m_2}(s)=\displaystyle\frac{2s}{5^2+4s+2}\frac{2s-1}{2}V_g(s)=\frac{s(2s-1)}{5s^2+4s+1}V_g(s)
\end{gathered}$$ La tensione in uscita al circuito corrisponde alla tensione ai capi del condensatore. Data la corrente di maglia si può calcolare la tensione come $V_o(s)$: $$\begin{gathered}
    V_o(s)=I_{m_1}(s)\displaystyle\frac{1}{s}=\frac{2s-1}{5s^2+4s+1}V_g(s)
\end{gathered}$$ Per cui il circuito ha una funzione di rete $F(s)$: $$\begin{gathered}
    F(s)=\displaystyle\frac{V_o(s)}{V_g(s)}=\frac{2s-1}{5s^2+4s+1}=\frac{1}{5}\frac{2s-1}{s^2+\displaystyle\frac{4}{5}+\frac{1}{5}}
\end{gathered}$$ Poiché contiene solo poli a parte reale negativa, il circuito è stabile: $$\begin{gathered}
    s_{p_{1,2}}=\displaystyle-\frac{2}{5}\pm j\frac{\sqrt{6}}{6}
\end{gathered}$$

### Esercizio 3.2

Determinare l’espressione della corrente $i_C(t)$ e della tensione $v_C(t)$ del condensatore dopo la commutazione:

<div class="center">

</div>

Si suppone il circuito sia a regime prima della commutazione, quindi si calcola la memoria del condensatore: $$\begin{gathered}
    v_C(0^-)\left(\displaystyle\frac{1}{3}+\frac{1}{6}\right)\,\mathrm{\Omega}^{-1}=2\,\mathrm{A}\\
    v_C(0^-)=\displaystyle\frac{6}{3}\cdot2=4\,\mathrm{V}
\end{gathered}$$

Si esprime ora il circuito nel dominio di Laplace:

<div class="center">

</div>

Si risolve mediante il metodo dei nodi: $$\begin{gathered}
\left(\frac{1}{3}+\frac{s}{2}\right)=\frac{4}{s}\frac{s}{2}\\
    V_C(s)=\displaystyle\frac{2(s+1)}{s}\frac{6}{2+3s}=\frac{4(s+1)}{s\left(\displaystyle s+\frac{2}{3}\right)}\\
    V_C(s)=\displaystyle\frac{A}{s}+\frac{B}{\displaystyle s+\frac{2}{3}}\\
    A=\displaystyle sV_C(s)\bigg|_{s=0}=\frac{4(0+1)}{\displaystyle0+\frac{2}{3}}=6\\
    B=\displaystyle\left(s+\frac{2}{3}\right)V_C(s)\bigg|_{s=-\frac{2}{3}}=\frac{\displaystyle 4\left(-\frac{2}{3}+1\right)}{\displaystyle-\frac{2}{3}}=-2\\
    v_C(t)=\left(6+2e^{-2t/3}\right)u(t)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$ Si calcola ora la corrente di lato $i_C(t)$ tramite la legge costitutiva del condensatore: $$\begin{gathered}
    i_C(t)=\displaystyle C\frac{\mathrm{d}v_C(t)}{\mathrm{d}t}=\frac{1}{2}\cdot-\frac{2}{3}\cdot2e^{-2t/3}u(t)=\frac{2}{3}e^{-2t/3}u(t)
\end{gathered}$$

### Esercizio 3.3

Calcolare la risposta ad un gradino unitario per il dato circuito:

<div class="center">

</div>

Con un gradino unitario in entrata, il condensatore non vede cariche prima di $t=0$, poiché il generatore controllato non può erogare corrente, se non è presente un elemento attivo nel circuito. Analogamente non scorre corrente nel circuito, quindi la memoria dell’induttore è nulla. Si rappresenta quindi il circuito nel dominio di Laplace:

<div class="center">

</div>

Si risolve mediante il metodo dei nodi: $$\begin{gathered}
    V_o(s)\left(\displaystyle\frac{1+4s+s^2}{2+\displaystyle\frac{s}{2}}\right)=\frac{1}{s}\frac{1}{2+\displaystyle\frac{s}{2}}-\frac{3}{2}V_x(s)\\
    V_x(s)=\left(\displaystyle\frac{1}{s}-V_o(s)\right)\frac{2}{\displaystyle\frac{s}{2}+2}=\frac{1}{s}\frac{2}{\displaystyle\frac{s}{2}+2}-\frac{2}{\displaystyle\frac{s}{2}+2}V_o(s)\\
    V_o(s)\left(\displaystyle\frac{1+4s+s^2}{2+\displaystyle\frac{s}{2}}\right)=\frac{1}{s}\frac{1}{2+\displaystyle\frac{s}{2}}-\frac{3}{2}\left(\frac{1}{s}\frac{2}{\displaystyle\frac{s}{2}+2}-\frac{2}{\displaystyle\frac{s}{2}+2}V_o(s)\right)\\
    V_o(s)\left(\displaystyle\frac{-2+4s+s^2}{s+\displaystyle\frac{s}{2}}\right)=-\frac{2}{s\left(2+\displaystyle\frac{s}{2}\right)}\\
    V_o(s)=-\displaystyle\frac{2}{s(s^2+4s-2)}=-\frac{2}{s(s+2-\sqrt{6})(s+2+\sqrt{6})}\\
    s_{p_1}=0\\
    s_{p_{2,3}}=-2\pm\sqrt{6}\\
    A=sV_o(s)\bigg|_{s=0}=\displaystyle\frac{2}{(0)^2+4(0)-2}=-1\\
    B_1=(s-s_{p_2})V_o(s)\bigg|_{s=s_{p_2}}=-\displaystyle\frac{2}{(-2+\sqrt{6})(-2+\sqrt{6}+2+\sqrt{6})}=-\frac{1}{\sqrt{6}(-2+\sqrt{6})}\\
    B_2=(s-s_{p_3})V_o(s)\bigg|_{s=s_{p_3}}=-\frac{1}{\sqrt{6}(2+\sqrt{6})}\\
    v_o(t)=\displaystyle\left(-1-\frac{e^{-(2-\sqrt{6})t}}{\sqrt{6}(-2+\sqrt{6})}-\frac{e^{-(2+\sqrt{6})t}}{\sqrt{6}(2+\sqrt{6})}\right)u(t)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 3.4

Data la funzione di rete $F(s)$, calcolare la risposta impulsiva e la risposta al gradino: $$F(s)=\displaystyle-\frac{5s}{s^2+15+50}=-\frac{5s}{(s+5)(s+10)}$$ Per la risposta impulsiva, è sufficiente antitrasformare la funzione di rete: $$\begin{gathered}
    F(s)=H(s)=\displaystyle\frac{A}{s+5}+\frac{B}{s+10}\\
    A=(s+5)F(s)\bigg|_{s=-5}=\displaystyle\frac{25}{-5+10}=5\\
    B=(s+10)F(s)\bigg|_{s=-10}=\displaystyle\frac{50}{-10+5}=-10\\
    h(t)=\displaystyle\left(5e^{-5t}-10e^{-10t}\right)u(t)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$ Per calcolare la risposta al gradino, si moltiplica la funzione di rete per la trasformata del gradino, e si calcola la sua antitrasformata: $$\begin{gathered}
    G(s)=\displaystyle\frac{1}{s}F(s)=-\frac{5}{(s+5)(s+10)}\\
    A=(s+5)G(s)\bigg|_{s=-5}=-\frac{5}{-5+10}=-1\\
    B=(s+10)G(s)\bigg|_{s=-10}=-\frac{5}{-10+5}=1\\
    g(t)=\left(e^{-10t}-e^{-5t}\right)u(t)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 3.5

Data la risposta impulsiva $h(t)$ di un circuito, calcolare la sua risposta ad un gradino: $$\begin{gathered}
    h(t)=5e^{-2t}\sin(4t)u(t)=\displaystyle\frac{5}{2j}\left(e^{-(2-4j)t}-e^{-(2+4j)t}\right)u(t)\\
    H(s)=\displaystyle\frac{20}{(s+(2-4j))(s+(2+4j))}\\
    F(s)=H(s)\displaystyle\frac{1}{s}=\frac{20}{s(s+(2-4j))(s+(2+4j))}\\
    A=sF(s)\bigg|_{s=0}=\frac{20}{(2-4j)(2+4j)}=\frac{20}{20}=1\\
    B=(s+(2-4j)F(s))\bigg|_{s=-2+4j}=\displaystyle\frac{20}{(-2+4j)8j}=\frac{1}{2j}\frac{5}{(-2+4j)}\frac{-2-4j}{-2-4j}=\frac{1}{2j}\frac{-1-2j}{2}\\
    B=\displaystyle\frac{1}{2j}\frac{\sqrt{5}}{2}e^{j\arctan(2)}\\
    f(t)=\displaystyle\left[1+\frac{\sqrt{5}}{2}e^{-2t}\sin(4t+\arctan(2))\right]u(t)\\
    \sin(4t+\arctan(2))=\sin(4t)\cos[\arctan(2)]+\cos(4t)\sin[\arctan(2)]\\
    \tan^2[\arctan(2)]=4\to1+\tan^2[\arctan(2)]=\displaystyle\frac{1}{\cos^2[\arctan(2)]}\\
    \cos[\arctan(2)]=\sqrt{\frac{1}{1+4}}=\frac{1}{\sqrt{5}}\\
    \sin[\arctan(2)]=\sqrt{1-\frac{1}{1+4}}=\frac{2}{\sqrt{5}}\\
    \displaystyle\frac{\sqrt{5}}{2}\sin(4t+\arctan(2))=\displaystyle\frac{\sqrt{5}}{2}\frac{1}{\sqrt{5}}\sin(4t)+\frac{\sqrt{5}}{2}\frac{2}{\sqrt{5}}\cos(4t)\\
    f(t)=\displaystyle\left[1+e^{-2t}\left(\cos(4t)+\frac{1}{2}\sin(4t)\right)\right]\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

# Elettrotecnica

## Circuiti del Primo Ordine

Esercizi relativi al file “Esercizi Circuiti I Ordine.pdf”, disponibile sul canale teams del corso.

### Esercizio 6.1

Calcolare la costante di tempo $\tau$ dei seguenti circuiti:

<div class="center">

</div>

Per trovare il tempo caratteristico è necessario solamente determinare la resistenza equivalente, e l’eccitazione del circuito. Escludendo il condensatore dalla rete resa passiva si trova una resistenza equivalente corrispondente alle due resistenze $R_1$ e $R_2$ in parallelo: $$\begin{gathered}
    R_\mathrm{eq}=\displaystyle\frac{R_1R_2}{R_1+R_2}
\end{gathered}$$ Per cui il tempo caratteristico $\tau$ è: $$\begin{gathered}
    \tau=CR_\mathrm{eq}=\displaystyle\frac{CR_1R_2}{R_1+R_2}
\end{gathered}$$

<div class="center">

</div>

Rendendo passiva la rete si osserva che la resistenza $R_1$ è collegata al vuoto, per cui la resistenza equivalente coincide con la resistenza $R_2$, per cui il tempo caratteristico corrisponde a: $$\begin{gathered}
    \tau=CR_2
\end{gathered}$$

<div class="center">

</div>

Si considera la rete resa passiva, escludendo l’elemento con memoria:

<div class="center">

</div>

Si considera il nodo $A$ il nodo di salto. Si considera una corrente di $1\,\mathrm{A}$ inserita tra i nodi $C$ e $A$, e si risolve mediante il metodo dei nodi: $$\begin{gathered}
    \begin{bmatrix}
        3&-1&-1\\-1&3&-1\\-1&-1&3
    \end{bmatrix}\begin{bmatrix}
        V_B\\V_C\\V_D
    \end{bmatrix}=R\begin{bmatrix}
        0\\1\\0
    \end{bmatrix}\\
    \begin{bmatrix}
        V_B\\V_C\\V_D
    \end{bmatrix}=\begin{bmatrix}
        0.5&0.25&0.25\\0.25&0.5&0.25\\0.25&0.25&0.5
    \end{bmatrix}R\begin{bmatrix}
        0\\1\\0 
    \end{bmatrix}\\
    V_C=\frac{R}{2}
\end{gathered}$$ Per cui la resistenza equivalente è: $$\begin{gathered}
    R_\mathrm{eq}=\displaystyle\frac{V_C}{1}=\frac{R}{2}
\end{gathered}$$ Allora il tempo caratteristico di questo circuito corrisponde a: $$\begin{gathered}
    \tau=\displaystyle\frac{L}{R_\mathrm{eq}}=\frac{2L}{R}
\end{gathered}$$

<div class="center">

</div>

Poiché in questo caso rendendo la rete passiva si sostituisce al generatore di corrente un cortocircuito, il lato formato da sole resistenze connesso in serie al generatore di corrente sono connesse a vuoto. Per cui non forniscono contributi, per cui l’unica resistenza utile è quella montata in parallelo all’induttore, per cui la resistenza equivalente coincide a questa resistenza: $$\begin{gathered}
    R_\mathrm{eq}=R
\end{gathered}$$ Per cui il tempo caratteristico corrisponde a: $$\tau=\displaystyle\frac{R_\mathrm{eq}}{L}=\frac{R}{L}$$

### Esercizio 6.2

Calcolare la tensione a vuoto $v_o(t)$ della seguente rete:

<div class="center">

</div>

$$\begin{gathered}
    E=10\,\mathrm{V}\\
    R_1=R_2=1\,\Omega\\
    C=1\,\mathrm{F}
\end{gathered}$$ Si considera la rappresentazione equivalente di Thevenin, per individuare la tensione ai capi del condensatore: $$\begin{gathered}
    E_\mathrm{th}=\displaystyle\frac{R_2}{R_1+R_2}E=5\,\mathrm{V}
\end{gathered}$$ Mentre si ottiene una resistenza equivalente data dalle due resistenze in parallelo: $$\begin{gathered}
    R_\mathrm{eq}=\displaystyle\frac{R_1R_2}{R_1+R_2}=\frac{1}{2}\,\Omega
\end{gathered}$$ La tensione ai capi del condensatore è quindi: $$\begin{gathered}
    v_C(t)=(v_C(0^-)-E_\mathrm{th})e^{-\frac{t}{R_\mathrm{eq}C}}+E_\mathrm{th}=\displaystyle -5e^{-2t}+5\,\mathrm{V}
\end{gathered}$$ Il condensatore è montato in parallelo ai morsetti in entrata al circuito, per cui l’espressione della tensione a vuoto coincide con l’espressione del condensatore: $$\begin{gathered}
    v_o(t)=5(1-e^{-2t})\,\mathrm{V}
\end{gathered}$$

### Esercizio 6.3

Determinare l’espressione della tensione a vuoto $v_o(t)$ del seguente circuito:

<div class="center">

</div>

$$\begin{gathered}
    E=10\,\mathrm{V}\\
    R_1=R_2=2\,\Omega\\
    R_3=1\,\Omega\\
    C=1\,\mathrm{F}
\end{gathered}$$

Per risolvere il circuito bisogna isolare l’elemento con memoria ed applicare il teorema di Thevenin o Norton sul circuito, considerando l’elemento con memoria esterno al circuito. Dopo aver calcolato la tensione ai capi del condensatore, considerandolo in entrata ad un circuito nei morsetti $A$ e $B$, si può sostituire l’elemento con un generatore di tensione equivalente. Per calcolare la tensione a vuoto tra i morsetti $A$ e $B$ si può riscrivere il circuito come:

<div class="center">

</div>

Si calcola la tensione a vuoto tramite la formula per i partitori di tensioni: $$\begin{gathered}
    E_\mathrm{th}=\displaystyle\frac{R_1}{R_1+R_3}E=\frac{20}{3}\,\mathrm{V}
\end{gathered}$$ La resistenza $R_2$ non influisce poiché è connessa a vuoto, per cui non può agire sulla tensione, non essendo attraversata da una corrente.

Si rende la rete passiva per calcolare la resistenza equivalente:

<div class="center">

</div>

La resistenza equivalente risulta quindi: $$\begin{gathered}
    R_\mathrm{eq}=\displaystyle\frac{R_1R_3}{R_1+R_3}+R_2=\frac{8}{3}\,\Omega
\end{gathered}$$

Si può esprimere la tensione ai capi del condensatore mediante la formula precedentemente dimostrata, oppure si può dimostrare la formula in questo specifico caso. Si ottiene quindi: $$\begin{gathered}
    v_C(t)=\left[v_C(0^-)-E_\mathrm{th}\right]e^{-\frac{t}{R_\mathrm{eq}C}}+E_\mathrm{th}\\
    v_C(t)=\left[\displaystyle 4-\frac{20}{3}\right]e^{-\frac{3}{8}t}+\frac{20}{3}\,\mathrm{V}\\
    v_C(t)=-\displaystyle\frac{8}{3}e^{-\frac{3}{8}t}+\frac{20}{3}\,\mathrm{V}
\end{gathered}$$

Dopo aver sostituito il condensatore con un generatore di tensione equivalente si considera una maglia dove sia presente la tensione incognita, per applicare il secondo principio di Kirchhoff: $$\begin{gathered}
    E-v_C(t)=v_o(t)\\
    10-v_C(t)=v_o(t)\\
    10+\displaystyle\frac{8}{3}e^{-\frac{3}{8}t}-\frac{20}{3}\,\mathrm{V}=v_o(t)
\end{gathered}$$ La tensione a vuoto è quindi: $$\begin{gathered}
    v_o(t)=\displaystyle\frac{8}{3}e^{-\frac{3}{8}t}+\frac{10}{3}\,\mathrm{V}
\end{gathered}$$

### Esercizio 6.4

Determinare l’espressione della tensione a vuoto del seguente circuito, a regime prima della chiusura dell’interruttore:

<div class="center">

</div>

$$\begin{gathered}
    R_1=3\,\Omega\\
    R_2=R_3=6\,\Omega\\
    E=3\,\mathrm{V}\\
    C=0.05\,\mathrm{F}
\end{gathered}$$

A regime permanente la tensione del condensatore corrisponde alla tensione erogata dal generatore, per cui: $$\begin{gathered}
    v_C(0^-)=3\,\mathrm{V}
\end{gathered}$$ Si applica il teorema di Thevenin senza considerare il condensatore. Si ottiene una tensione equivalente: $$\begin{gathered}
    E_\mathrm{th}=\displaystyle\frac{R_2}{R_1+R_2}E=2\,\mathrm{V}
\end{gathered}$$ La resistenza equivalente corrisponde a: $$\begin{gathered}
    R_\mathrm{eq}=\displaystyle\frac{R_1R_2}{R_1+R_2}+R_3=8\,\Omega
\end{gathered}$$ Per cui la tensione ai capi del condensatore corrisponde a: $$\begin{gathered}
    v_C(t)=[v_C(0^-)]e^{-\frac{t}{R_\mathrm{eq}C}}+E_\mathrm{th}=2+e^{-2.5\,t}\,\mathrm{V}
\end{gathered}$$

### Esercizio 6.5

Determinare la tensione a vuoto del seguente circuito:

<div class="center">

</div>

$$\begin{gathered}
    I=2\,\mathrm{A}\\
    R=2\,\Omega\\
    L=2\,\mathrm{H}
\end{gathered}$$ A regime l’induttore contiene tutta la carica erogata dal generatore: $$\begin{gathered}
    i_L(0^-)=2\,\mathrm{A}
\end{gathered}$$ Si risolve mediante il metodo dei nodi: $$\begin{gathered}
    \begin{bmatrix}
        2&-1\\-1&2
    \end{bmatrix}\begin{bmatrix}
        V_{A0}\\V_{B0}
    \end{bmatrix}
    =R\begin{bmatrix}
        2\\0
    \end{bmatrix}\\
    \begin{bmatrix}
        V_{A0}\\V_{B0}
    \end{bmatrix}=\displaystyle\frac{1}{3}
    \begin{bmatrix}
        2&1\\1&2
    \end{bmatrix}\begin{bmatrix}
        4\\0
    \end{bmatrix}=\frac{1}{3}\begin{bmatrix}
        8\\4
    \end{bmatrix}\,\mathrm{V}
\end{gathered}$$ Per cui la tensione equivalente della rappresentazione di Thevenin si ottiene come: $$\begin{gathered}
    E_\mathrm{th}=V_{A0}-V_{B0}=\displaystyle\frac{4}{3}\,\mathrm{V}
\end{gathered}$$ Si misura la resistenza equivalente rendendo passiva la rete, si ottiene quindi: $$\begin{gathered}
    R_\mathrm{eq}=\displaystyle\frac{(R+R)R}{(R+R)+R}=\frac{4}{3}\,\Omega
\end{gathered}$$

La corrente di cortocircuito di una forma Thevenin collegata a vuoto corrisponde alla corrente del generatore di una forma Norton equivalente: $$\begin{gathered}
    I_\mathrm{no}=\displaystyle\frac{E_\mathrm{th}}{R_\mathrm{eq}}=1\,\mathrm{A}
\end{gathered}$$ Si determina la tensione ai capi dell’induttore alla chiusura dell’induttore: $$\begin{gathered}
    i_L(t)=\left[\displaystyle i_L(0^-)-\frac{E_\mathrm{th}}{R_\mathrm{eq}}\right]e^{-\frac{R_\mathrm{eq}}{L}t}+\frac{E_\mathrm{th}}{R_\mathrm{eq}}=1e^{-\frac{2}{3}t}+1\,\mathrm{A}
\end{gathered}$$ Si sostituisce ora l’induttore con un generatore di corrente che eroga la corrente equivalente ai capi dell’induttore. Si applica quindi di nuovo il metodo dei nodi in questa nuova situazione: $$\begin{gathered}
    \begin{bmatrix}
        2&-1\\-1&2
    \end{bmatrix}\begin{bmatrix}
        V_{A}\\V_{B}=V_\mathrm{out}
    \end{bmatrix}=
    R\begin{bmatrix}
        2-i_L\\i_L
    \end{bmatrix}\\
    \begin{bmatrix}
        V_{A}\\V_\mathrm{out}
    \end{bmatrix}=\displaystyle\frac{1}{3}
    \begin{bmatrix}
        2&1\\1&2
    \end{bmatrix}\begin{bmatrix}
        4-2i_L\\i_L
    \end{bmatrix}=\begin{bmatrix}
        8-4i_L+2i_L\\
        4-2i_L+4i_L
    \end{bmatrix}
\end{gathered}$$ La tensione ai capi del circuito è quindi: $$\begin{gathered}
    V_\mathrm{out}=\displaystyle\frac{1}{3}\left(4+2i_L\right)=\frac{4}{3}+\frac{2}{3}e^{-\frac{2}{3}t}+\frac{2}{3}=2+\frac{2}{3}e^{-\frac{2}{3}t}\,\mathrm{V}
\end{gathered}$$

### Esercizio 6.6

Calcolare la corrente $i_0(t)$ considerando la memoria nulla per il condensatore:

<div class="center">

</div>

$$\begin{gathered}
    R=1\,\Omega\\
    C=1\,\mathrm{F}\\
    E=1\,\mathrm{V}
\end{gathered}$$

Per le formule sui partitori di tensione si ottiene una tensione equivalente: $$\begin{gathered}
    E_\mathrm{th}=\displaystyle\frac{R\frac{RR}{R+R}}{R+\frac{RR}{R+R}}E=\frac{\frac{1}{2}}{1+\frac{1}{2}}\cdot1\,\mathrm{V}=\frac{1}{3}\,\mathrm{V}
\end{gathered}$$ La resistenza equivalente corrisponde a: $$\begin{gathered}
    R_\mathrm{eq}=\displaystyle\frac{R\frac{RR}{R+R}}{R+\frac{RR}{R+R}}\frac{1}{3}\,\Omega
\end{gathered}$$ Il tempo caratteristico corrisponde a: $$\begin{gathered}
    \tau=R_\mathrm{eq}C=\displaystyle\frac{1}{3}\,\mathrm{s}
\end{gathered}$$ La tensione ai capi del condensatore si ottiene come: $$\begin{gathered}
    v_C(t)=(v_C(0^-)-E_\mathrm{th})e^{-\frac{t}{\tau}}-E_\mathrm{th}=-\displaystyle\frac{1}{3}e^{-3t}+\frac{1}{3}\,\mathrm{V}
\end{gathered}$$ Per cui l’espressione della corrente risulta essere il rapporto tra la tensione ed il valore della resistenza del resistore ai cui capi è presente questa tensione. La corrente non cambia per il resistore in parallelo al lato dove fluisce $i_0$. $$\begin{gathered}
    i_0(t)=\displaystyle\frac{v_c(t)}{R}=\frac{1}{3}\left(1-e^{-3t}\right)
\end{gathered}$$

## Dominio dei Fasori

Esercizi relativi al file “Metodo dei fasori e potenza (1).pdf”, disponibile sul canale teams del corso.

### Esercizio 7.1

Calcolare i valori di resistenza e capacità equivalente, del seguente circuito in regime sinusoidale alla pulsazione di $\omega=2\,\mbox{rad}/s$:

<div class="center">

</div>

$$\begin{gathered}
    C_2=0.5\,\mathrm{F}\\
    L_1=1\,\mathrm{H}\\
    R_1=R_2=1\,\Omega
\end{gathered}$$ Si può risolvere applicando trasformazioni in serie ed in parallelo dell’impedenza: $$\begin{gathered}
    z_1=j\omega L_1+R_2=2j+1\\
    z_2=-j\displaystyle\frac{1}{\omega C_2}=-j\\
    z_3=R_1=1
\end{gathered}$$ Si considera il parallelo tra $z_1$ e $z_2$: $$\begin{gathered}
    z_{p12}=\displaystyle\frac{z_1z_2}{z_1+z_2}=\frac{-j(1+2j)}{1+2j-j}=\frac{-j+2}{1+j}\cdot\frac{1-j}{1-j}\\
    z_{p12}=\frac{1-3j}{2}
\end{gathered}$$ Si considera la serie tra $z_{p12}$ e $z_3$: $$\begin{gathered}
    z_{AB}=z_{p12}+z_3=\displaystyle\frac{1}{2}+j\frac{3}{2}+1=\frac{3}{2}+j\frac{3}{2}
\end{gathered}$$ $$\begin{gathered}
    R_\mathrm{eq}=\displaystyle\frac{3}{2}\,\Omega\\
    C_\mathrm{eq}=\frac{2}{3}\,\Omega\cdot \omega=\frac{1}{3} \,\mathrm{F}
\end{gathered}$$

Alternativamente per trovare l’impedenza equivalente della rappresentazione Thevenin si considera un generatore che eroga una tensione $\overline{V}_\mathrm{in}$, e si risolve mediante il metodo dei nodi o delle maglie:

<div class="center">

</div>

La matrice delle ammettenze modali diventa solamente l’autoammettenza del nodo $A$: $$\begin{gathered}
    (y_1+y_2+y_3)\overline{V}_A=\overline{V}_\mathrm{in}y_3\\
    \overline{I}_\mathrm{in}=\displaystyle\frac{\overline{V}_\mathrm{in}-\overline{V}_A}{z_3}\\
    z_\mathrm{in}=\displaystyle\frac{\overline{V}_\mathrm{in}}{\overline{I}_\mathrm{in}}
\end{gathered}$$ Si calcola ora numericamente: $$\begin{gathered}
    \overline{V}_\mathrm{in}=1\,V\\
    \overline{V}_A=\displaystyle\frac{y_3}{y_1+y_2+y_3}\cdot 1\,V\\
    \overline{V}_A=\displaystyle\frac{1}{\frac{1}{1+2j}-\frac{1}{j}+1}=\displaystyle\frac{1}{\frac{j-1-2j-j(1+2j)}{j(1+2j)}}=\frac{j(1+2j)}{j-1-2j+j-2}\\
    \overline{V}_A=\frac{j-2}{-3}\\
    \overline{I}_\mathrm{in}=1+\displaystyle\frac{j-2}{3}=\frac{3+j-2}{3}=\frac{1+j}{3}\\
    z_\mathrm{in}=\displaystyle\frac{1}{1+j}\cdot\frac{1-j}{1-j}\cdot3=\frac{3}{2}+j\frac{3}{2}
\end{gathered}$$

### Esercizio 7.2

Calcolare l’espressione a regime della tensione di nodo $v_x$:

<div class="center">

</div>

Si risolve mediante il metodo dei nodi. Si considerano per ogni lato le loro impedenze: $$\begin{gathered}
    z_1=z_2=10\,\Omega\\
    z_3=\displaystyle-\frac{j}{\omega C}=-\frac{j}{10\cdot 10\times10^{-3}}=-10j\,\Omega\\
    z_4=5\,\Omega+\omega L=5\,\Omega+5j\,\Omega
\end{gathered}$$ Poiché oltre al nodo di salto è presente un solo nodo, per il metodo dei nodi si ottiene un’unica equazione: $$\begin{gathered}
    (y_1+y_2+y_3+y_4)\overline{V}_x=\overline{V}_\mathrm{in}y_1-10\overline{I}_ay_4
\end{gathered}$$ Si esprime il vincolo del pilota: $$\begin{gathered}
    \overline{I}_a=(\overline{V}_\mathrm{in}-\overline{V}_x)y_1
\end{gathered}$$ Per cui l’equazione dei nodi diventa: $$\begin{gathered}
    (y_1+y_2+y_3+y_4)\overline{V}_x=\overline{V}_\mathrm{in}y_1-10(\overline{V}_\mathrm{in}-\overline{V}_x)y_1y_4\\
    (y_1+y_2+y_3+y_4-10y_1y_4)\overline{V}_x=\overline{V}_\mathrm{in}(y_1-10y_1y_4)\\
    \overline{V}_{x}=\displaystyle\frac{\overline{V}_\mathrm{in}(y_1-10y_1y_4)}{(y_1+y_2+y_3+y_4-10y_1y_4)}
\end{gathered}$$ Si calcolano le ammettenze: $$\begin{gathered}
    y_1=y_2=\displaystyle\frac{1}{10}\,\Omega^{-1}\\
    y_3=\displaystyle\frac{j}{10}\,\Omega^{-1}\\
    y_4=\displaystyle\frac{1}{5+5j}\,\Omega^{-1}=\frac{1}{10}\,\Omega^{-1}-\frac{j}{10}\,\Omega^{-1}
\end{gathered}$$ Da cui si ottiene un fasore di nodo: $$\begin{gathered}
    \overline{V}_x=2+4i\\
    |\overline{V}_x|=\displaystyle\frac{10}{\sqrt{5}}\\
    \varphi=\arctan\left(\displaystyle\frac{4}{2}\right)\cdot\frac{180^{\circ}}{\pi}=63.4^{\circ}
\end{gathered}$$ Per cui l’espressione della tensione di nodo corrisponde a: $$\begin{gathered}
    v_x=|\overline{V}_x|\cos(\omega t+\varphi)=\displaystyle\frac{10}{\sqrt{5}}\cos(10t+63.4^{\circ})
\end{gathered}$$

### esercizio 7.3

Determinare la tensione a regime dell’induttore $v_L$:

<div class="center">

</div>

$$\begin{gathered}
    E_{g1}=20\cos(1000 t)\,\mathrm{V}\\
    E_{g2}=30\cos(1000t -90^{\circ})\,\mathrm{V}\\
    R=10\,\Omega\\
    L=16\,\mathrm{mH}\\
    C=200\,\mathrm{\mu F}
\end{gathered}$$ Si determina la pulsazione e ed i fasori dei generatori: $$\begin{gathered}
    \omega=10^3\,\mathrm{rad}/\mathrm{s}\\
    \overline{E}_{g1}=20\,\mathrm{V}\\
    \overline{E}_{g2}=30e^{-j\pi/2}=-30j\,\mathrm{V}
\end{gathered}$$ Si determinano le impedenze del circuito: $$\begin{gathered}
    z_1=j\omega L=10^3\cdot15\cdot10^{-3}j\,\Omega=15e^{j\pi/2}\Omega\\
    z_2=R=10\,\Omega\\
    z_3=\displaystyle-\frac{j}{\omega C}=-j\frac{1}{10^3\cdot200\cdot10^{-6}}\,\Omega=5e^{-j\pi/2}\Omega
\end{gathered}$$ Si risolve mediante il metodo dei nodi, ottenendo una singola equazione, questo caso coincide con il teorema di Millman: $$\begin{gathered}
    \overline{V}_A=\displaystyle\frac{y_1\overline{E}_{g1}+y_3\overline{E}_{g2}}{y_1+y_2+y_3}=\frac{\frac{20}{15j}+\frac{-30j}{-5j}}{\frac{1}{15j}+\frac{1}{10}+\frac{1}{-5j}}\\
    \displaystyle\frac{\frac{1}{5j}\left[\frac{20}{3}+30j\right]}{\frac{10-30+15j}{150j}}=\frac{30\left[\frac{20}{3}+30j\right]}{-20+15j}=\frac{30\left[\frac{20}{3}+30j\right]}{20^2+15^2}(-20-15j)\\
    \displaystyle-\frac{30}{625}\left(\frac{400}{3}+600j+100j-450\right)=15.2-33.6j\,\mathrm{V}
\end{gathered}$$ Si determina ora la tensione ai capi dell’induttore: $$\begin{gathered}
    \overline{V}_L=\overline{E}_{g1}-\overline{V}_A=20-15.2+33.6j\,\mathrm{V}=4.8+33.6j\,\mathrm{V}
\end{gathered}$$ Si determina ora la fase ed il modulo: $$\begin{gathered}
    |V_L|=\sqrt{4.8^2+33.6^2}=33.941\\
    \varphi=\arctan\left(\displaystyle\frac{33.6}{4.8}\right)=81.2^{\circ}
\end{gathered}$$ Per cui l’espressione a regime della tensione corrisponde a: $$\begin{gathered}
    v_L(t)=33.941\cos(1000t+81.2^{\circ})\,\mathrm{V}
\end{gathered}$$

Si risolve ora mediante il metodo delle maglie: $$\begin{gathered}
    \begin{bmatrix}
        z_1+z_2&-z_2\\-z_2&z_2+z_3
    \end{bmatrix}\begin{bmatrix}
        \overline{I}_{m_1}\\\overline{I}_{m_2}
    \end{bmatrix}=\begin{bmatrix}
        \overline{E}_{g1}\\
        -\overline{E}_{g2}
    \end{bmatrix}\\
    \begin{bmatrix}
        \overline{I}_{m_1}\\\overline{I}_{m_2}
    \end{bmatrix}=\begin{bmatrix}
        10+15j&-10\\-10&10-5j
    \end{bmatrix}^{-1}\begin{bmatrix}
        20\\-30j
    \end{bmatrix}=\begin{bmatrix}
        -1.6-3.2j\\1.2-5.6j
    \end{bmatrix}
\end{gathered}$$ Si calcola ora il fasore della tensione dell’induttore: $$\begin{gathered}
    \overline{V}_L=\overline{E}_{g1}-(\overline{I}_{m_1}-\overline{I}_{m_2})z_1=4.8+33.6j\,\mathrm{V}
\end{gathered}$$ Corrisponde allo stesso fasore calcolato precedentemente mediante il metodo dei nodi.

### Esercizio 7.4

Determinare la potenza attiva erogata dal generatore:

<div class="center">

</div>

$$\begin{gathered}
    E_g=5\cos(2t)\,\mathrm{V}\\
    R_1=2\,\Omega\\
    R_2=1\,\Omega\\
    C=0.5\,\mathrm{F}\\
    L=2\,\mathrm{H}
\end{gathered}$$ Si calcolano le impedenze ed il fasore della tensione: $$\begin{gathered}
    z_1=2\,\Omega\\
    z_2=1\,\Omega\\
    z_3=4j\,\Omega\\
    z_4=-j\,\Omega\\
    \overline{E}_g=5\,\mathrm{V}
\end{gathered}$$

Si considera il parallelo tra $z_2$, $z_3$ e $z_4$: $$\begin{gathered}
    y_p=\displaystyle1+\frac{1}{4j}+\frac{1}{-j}=\frac{4j+1-4}{4j}=\frac{-3+4j}{4j}\\
    z_p=\displaystyle\frac{4j}{-3+4j}=\frac{4j(-3-4j)}{25}=\frac{16}{25}-\frac{12}{25}j\,\Omega
\end{gathered}$$ Si applica il metodo delle maglie: $$\begin{gathered}
    (z_1+z_p)\overline{I}_{m_1}=\overline{E}_g\\
    \overline{I}_{m_1}=\overline{I}_g=\displaystyle\frac{\overline{E}_g}{z_1+z_p}=\frac{5}{\frac{16}{25}-\frac{12}{25}j+2}\\
    \overline{I}_g=\displaystyle\frac{125}{66-12j}=\frac{125}{4500}(66+12j)\,\mathrm{A}
\end{gathered}$$ La potenza complessa erogata dal generatore si ottiene come: $$\begin{gathered}
    P_C=\displaystyle\frac{1}{2}\overline{E}_g\overline{I}_g^*=\frac{1}{2}5\frac{125}{4500}(66-12j)=4.5833-0.8333j
\end{gathered}$$

### Esercizio 7.6

> Un’impedenza $Z$ alimentata da un generatore sinusoidale da $120\,\mathrm{V}$ efficaci, assorbe la potenza apparente di $12\,\mathrm{kVA}$, con un fattore di potenza di $0.856$ induttivo. Determinare modulo e fase di $Z$.

Dato il fattore di potenza si può determinare la fase della potenza complessa: $$\begin{gathered}
    \varphi\arccos(0.856)=31.1296^{\circ}
\end{gathered}$$

Si può esprimere la corrente che attraverso l’impedenza come il rapporto tra la potenza apparente e la tensione erogata: $$\begin{gathered}
    \overline{I}=\displaystyle\frac{P_a}{\overline{E}_g}=\frac{12\cdot10^3}{120}=100\,\mathrm{A}
\end{gathered}$$ Si ricorda che l’impedenza di un dato bipolo, tramite la legge di Ohm complessa, si può ricavare dal fasore della corrente e della tensione: $$\begin{gathered}
    |Z|=\displaystyle\frac{\overline{E}_{g}}{\overline{I}_g}\frac{120\,\mathrm{V}}{100\,\mathrm{A}}=1.2\,\Omega
\end{gathered}$$

### Esercizio 7.7

Determinare la potenza complessiva assorbita dall’impedenza $z_1$ composta dal resistore e dall’induttore in serie:

<div class="center">

</div>

Si calcola il fasore della corrente: $$\begin{gathered}
    \overline{I}=\displaystyle\frac{\overline{E}_g}{z_1+z_2}=\frac{220}{4+15+(2-10)j}=\frac{220}{425}(19+8j)
\end{gathered}$$

La potenza assorbita dall’impedenza $z_1$ si calcola come: $$\begin{gathered}
    P_{C1}=z_1|\overline{I}|^2=(4+2j)\left|\frac{220}{425}(19+8j)\right|^2=455.4\,\mathrm{W}+227.7j\,\mathrm{VA}
\end{gathered}$$ Per cui questo circuito risulta ohmico-capacitivo, e per metterlo in risonanza bisognerebbe inserire un’induttore in parallelo.

### Esercizio 7.8

Determinare l’ammettenza equivalente del seguente circuito:

<div class="center">

</div>

$$\begin{gathered}
    |z_R|=0.5\,\Omega\\
    |z_C|=0.25\,\Omega\\
    |z_L|=1\,\Omega
\end{gathered}$$

Si inserisce un generatore di tensione esterno $\overline{E}_e=1\,\mathrm{V}$. Si applica quindi il metodo delle maglie: $$\begin{gathered}
    \begin{bmatrix}
        z_R+z_L&-z_C\\-z_C&z_C+z_L
    \end{bmatrix}\begin{bmatrix}
        \overline{I}_{m_1}\\\overline{I}_{m_2}
    \end{bmatrix}=\begin{bmatrix}
        \overline{E}_e\\-0.5\overline{I}_1
    \end{bmatrix}=\begin{bmatrix}
        \overline{E}_e\\0
    \end{bmatrix}+\begin{bmatrix}
        0\\-0.5\overline{I}_1
    \end{bmatrix}
\end{gathered}$$ Si può notare come la corrente di lato $\overline{I}_1$ coincide con la corrente di maglia $\overline{I}_{m_1}$, per cui l’equazione diventa: $$\begin{gathered}
    \begin{bmatrix}
        z_R+z_L&-z_C\\-z_C+0.5&z_C+z_L
    \end{bmatrix}\begin{bmatrix}
        \overline{I}_{m_1}\\\overline{I}_{m_2}
    \end{bmatrix}=\begin{bmatrix}
        \overline{E}_e\\0
    \end{bmatrix}\\
    \begin{bmatrix}
        \overline{I}_{m_1}\\\overline{I}_{m_2}
    \end{bmatrix}=\displaystyle\frac{1}{(z_R+z_L)(z_C+z_L)-(-z_C+0.5)(-z_C)}\begin{bmatrix}
        z_C+z_L&z_C-0.5\\z_C&z_R+z_L
    \end{bmatrix}\begin{bmatrix}
        \overline{E}_e\\0
    \end{bmatrix}
\end{gathered}$$ Dopo aver calcolato la corrente di maglia $\overline{I}_{m_1}$, si esprime l’ammettenza equivalente come: $$\begin{gathered}
    y_\mathrm{eq}=\displaystyle\frac{\overline{I}_{m_1}}{\overline{E}_e}=0.792+j0.226\,\Omega^{-1}
\end{gathered}$$

Alternativamente si può calcolare tramite il metodo dei Nodi, o per il teorema di Millman: $$\begin{gathered}
    \overline{V}_A=\displaystyle\frac{\overline{E}_ey_R+0.5\overline{I}_1y_C}{y_R+y_C+y_L}
\end{gathered}$$ Si inserisce il vincolo del pilota come combinazione lineare dei potenziali modali: $$\begin{gathered}
    \overline{I}_1=(\overline{E}_e-\overline{V}_A)y_R
\end{gathered}$$ Per cui l’equazione diventa: $$\begin{gathered}
    \overline{V}_A=\displaystyle\frac{\overline{E}_ey_R+0.5(\overline{E}_e-\overline{V}_A)y_Ry_C}{y_R+y_C+y_L}\\
    \overline{V}_A\left(1+\displaystyle\frac{0.5y_Ry_C}{y_R+y_C+y_L}\right)=\frac{\overline{E}_ey_R+0.5\overline{E}_ey_Ry_C}{y_R+y_C+y_L}\\
    \overline{V}_A=\displaystyle\frac{\frac{\overline{E}_ey_R+0.5\overline{E}_ey_Ry_C}{y_R+y_C+y_L}}{1+\frac{0.5y_Ry_C}{y_R+y_C+y_L}}
\end{gathered}$$ L’ammettenza equivalente si ottiene come: $$\begin{gathered}
    y_\mathrm{eq}=\displaystyle\frac{\overline{I}_1}{\overline{V}_A}=\frac{\overline{E}_e-\overline{V}_A}{\overline{V}_A}y_R=0.792+j0.226\,\Omega^{-1}
\end{gathered}$$

Invece inserendo un generatore di corrente $\overline{I}_g=1\,\mathrm{A}$, allora in questo caso assume un valore di $0.5\,\mathrm{V}$. Per cui in questo caso il potenziale nodale di $A$ si calcola come: $$\begin{gathered}
    \overline{V}_A=\displaystyle\frac{1+0.5y_3}{y_2+y_3}
\end{gathered}$$ Calcolando l’impedenza equivalente si considera anche in serie l’impedenza $z_R$: $$\begin{gathered}
    z_\mathrm{eq}=\displaystyle\frac{\overline{V}_A}{\overline{I}_g}+z_R
\end{gathered}$$ Per cui l’ammettenza si ottiene come il reciproco di quest’impedenza così calcolata: $$\begin{gathered}
    y_\mathrm{eq}=\displaystyle\frac{1}{z_\mathrm{eq}}
\end{gathered}$$

### Esercizio 7.9

Determinare la rappresentazione equivalente di Thevenin del seguente circuito:

<div class="center">

</div>

Per calcolare la tensione di Thevenin, poiché il resistore è collegato a vuoto, la corrente pilota è nulla $\overline{I}_0=0\,\mathrm{A}$, per cui la tensione di Thevenin equivalente corrisponde alla tensione del generatore montato in parallelo: $$\begin{gathered}
    \overline{E}_\mathrm{th}=1+j0\,\mathrm{V}
\end{gathered}$$ Si rende passiva la rete e si inserisce un generatore di tensione in entrata $\overline{I}_g=1\,\mathrm{A}$, in modo che la corrente pilotata coincida con la corrente inserita: $$\begin{gathered}
    \overline{I}_0=\overline{I}_g
\end{gathered}$$ Si considera il metodo dei nodi: $$\begin{gathered}
    \overline{V}_A=\displaystyle\frac{3\overline{I}_0-\overline{I}_0}{y_L}=j4\,\mathrm{V}
\end{gathered}$$

Per cui l’impedenza equivalente si ottiene come: $$\begin{gathered}
    z_\mathrm{eq}=\displaystyle\frac{\overline{V}_A}{\overline{I}_g}+1=1-j4
\end{gathered}$$

### Esercizio 7.10

Calcolare la potenza potenza attiva assorbita dal resistore $R_1$ e quella erogata dal generatore $v_g$:

<div class="center">

</div>

$$\begin{gathered}
    v_g=4\cos(5\cdot10^6t+60^{\circ})\to\overline{V}_g=2\sqrt{2}e^{j\pi/3}=\sqrt{2}+\sqrt{6}j\\
    v_1=8\cos(5\cdot10^6t)\to\overline{V}_1=4\sqrt{2}\\
    C=0.1\,\mathrm{nF}\to z_C=-2\cdot10^{3}j\\
    L=4\,\mathrm{mH}\to z_L=20\cdot10^{3}j\\
    R_1=6\,\mathrm{k\Omega}=z_{R_1}\\
    R_2=18\,\mathrm{k\Omega}=z_{R_2}
\end{gathered}$$

Si calcola il fasore della corrente passante per il circuito: $$\begin{gathered}
    \overline{I}=\displaystyle\frac{\overline{V}_g-\overline{V}_1}{z_C+z_{R_2}+z_L+z_{R_1}}=\frac{\sqrt{2}+\sqrt{6}-4\sqrt{2}}{-2\cdot10^{3}j+18\cdot10^3+20\cdot10^{3}j+6\cdot10^3}\\
    \displaystyle\frac{-3\sqrt{2}+\sqrt{6}j}{24+18j}\cdot10^{-3}=\frac{\sqrt2}{\sqrt{2}}\frac{-3+\sqrt{3}j}{3\sqrt{2}(4+3j)}\cdot10^{-3}=\frac{(3\sqrt{3}-12)+(4\sqrt{3}+9)j}{75\sqrt{2}}\cdot10^{-3}
\end{gathered}$$ Si calcola ora la potenza (attiva) assorbita dal resistore $R_1$: $$P_{R_1}=z_{R_1}|\overline{I}|^2=6\cdot10^3\cdot\displaystyle\frac{10^{-6}}{2\cdot75^2}\left(\sqrt{(3\sqrt{3}-12)^2+(4\sqrt{3}+9)^2}\right)^2=\frac{6\cdot300}{2\cdot75^2}\cdot10^{-3}=160\,\mathrm{\mu W}$$ Mentre la potenza attiva erogata dal generatore $v_g$ risulta essere: $$\begin{gathered}
    P_{v_g}=\Re\left\{\overline{V}_g\overline{I}^*\right\}=\displaystyle\Re\left\{\frac{1}{\sqrt2}(2+2\sqrt{3}j)\cdot\frac{10^{-3}}{75\sqrt2}\left[(3\sqrt3-12)-(4\sqrt3+9)j\right]\right\}\\
    \displaystyle\frac{10^{-3}}{150}\Re\left\{(6\sqrt3-24)-(8\sqrt3+18)j+(18-24\sqrt3)j+(24+18\sqrt3)\right\}=\frac{24\sqrt3}{150}\cdot10^{-3}\\
    P_{v_g}=277\,\mathrm{\mu W}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 7.21

Determinare il circuito equivalente di Thevenin tra i terminali $A$ e $B$:

<div class="center">

</div>

$$\begin{gathered}
    \overline{E}_g=5\,\mathrm{V}\\
    z_R=1\,\Omega\\
    z_C=-3j\,\Omega\\
    z_L=2j\,\Omega
\end{gathered}$$ Si risolve mediante il metodo delle maglie: $$\begin{gathered}
    \begin{bmatrix}
        z_R+z_C&-z_C\\-z_C&z_L
    \end{bmatrix}\begin{bmatrix}
        \overline{I}_{m_1}\\\overline{I}_{m_2}
    \end{bmatrix}=\begin{bmatrix}
        \overline{E}_{g1}\\\overline{E}_{g2}
    \end{bmatrix}\\
    \begin{bmatrix}
        1-3j&3j\\3j&-j
    \end{bmatrix}\begin{bmatrix}
        \overline{I}_{m_1}\\\overline{I}_{m_2}
    \end{bmatrix}=\begin{bmatrix}
        5\\\displaystyle\frac{1}{2}\overline{I}
    \end{bmatrix}
\end{gathered}$$ Il vincolo del pilota è banale, poiché la corrente di riferimento corrisponde alla corrente della maglia $1$: $$\begin{gathered}
    \overline{I}=\overline{I}_{m_1}\\
    \begin{bmatrix}
        1-3j&+3j\\\displaystyle-\frac{1}{2}+3j&-j
    \end{bmatrix}\begin{bmatrix}
        \overline{I}_{m_1}\\\overline{I}_{m_2}
    \end{bmatrix}=\begin{bmatrix}
        5\\0
    \end{bmatrix}\\
    \begin{bmatrix}
        \overline{I}_{m_1}\\\overline{I}_{m_2}
    \end{bmatrix}=\begin{bmatrix}
        1-3j&+3j\\\displaystyle-\frac{1}{2}+3j&-j
    \end{bmatrix}^{-1}\begin{bmatrix}
        5\\0
    \end{bmatrix}=\begin{bmatrix}
        -0.069-0.8276j\\0.2069-2.5172j
    \end{bmatrix}
\end{gathered}$$ La tensione di Thevenin equivalente si ottiene come: $$\begin{gathered}
    \overline{E}_\mathrm{th}=z_L\overline{I}_{m_2}=2j(0.2069-2.5172j)=5.0345+0.4138j\,\mathrm{V}
\end{gathered}$$ Si rappresenta in coordinate polari: $$\begin{gathered}
    |\overline{E}_\mathrm{th}|=\sqrt{5.0345^2+0.4138^2}=5.0515\\
    \varphi=\arctan\left(\displaystyle\frac{0.4138}{5.0345}\right)=4.6897^{\circ}\\
    \overline{E}_g=5.0515e^{j4.6897^{\circ}}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$ Applicando il metodo dei nodi si ottiene una risposta analoga: $$\begin{gathered}
    \overline{V}_A=\displaystyle\frac{\overline{E}gz_R-\frac{1}{2}\overline{I}y_L}{y_R+y_C+y_L}
\end{gathered}$$ Dove l’equazione del pilota in questo caso si ottiene come: $$\begin{gathered}
    \overline{I}=(\overline{E}_g-\overline{V}_A)y_R
\end{gathered}$$ Per cui si ottiene un’equazione per la tensione: $$\begin{gathered}
    \overline{V}_A=\displaystyle\frac{\overline{E}gz_R}{y_R+y_C+y_L}-\frac{1}{2}y_Ly_R\frac{\overline{E}_g}{y_R+y_C+y_L}+\frac{1}{2}y_LyR\frac{\overline{V}_A}{y_R+y_C+y_L}\\
    \overline{V}_A\left(\displaystyle1-\frac{1}{2}\frac{y_Ry_L}{y_R+y_C+y_L}\right)=\frac{\overline{E}gz_R-\frac{1}{2}y_Ly_R\overline{E}_g}{y_R+y_C+y_L}
\end{gathered}$$

Per calcolare l’impedenza di Thevenin si spengono solo i generatori passivi:

<div class="center">

</div>

Si inserisce dall’esterno un generatore indipendente in base al metodo di risoluzione, per cui in questo caso si inserisce un generatore di tensione esterno per applicare il metodo delle maglie, che eroga $\overline{E}_C=1\,\mathrm{V}$. L’induttore non influisce sulla tensione in ingresso, per cui si può calcolare prima un sistema di due equazioni, per trovare due correnti di maglia $\overline{I}_{m_1}$ e $\overline{I}_{m_2}$: $$\begin{gathered}
    \begin{bmatrix}
        z_R+z_C&-z_C\\-z_C&z_C
    \end{bmatrix}\begin{bmatrix}
        \overline{I}_{m_1}\\\overline{I}_{m_2}
    \end{bmatrix}=\begin{bmatrix}
        0\\\displaystyle\frac{1}{2}\overline{I}-\overline{E}_C
    \end{bmatrix}\\
    \begin{bmatrix}
        z_R+z_C&-z_C\\-\displaystyle\frac{1}{2}-z_C&z_C
    \end{bmatrix}\begin{bmatrix}
        \overline{I}_{m_1}\\\overline{I}_{m_2}
    \end{bmatrix}=\begin{bmatrix}
        0\\-\overline{E}_C
    \end{bmatrix}\\
    \begin{bmatrix}
        \overline{I}_{m_1}\\\overline{I}_{m_2}
    \end{bmatrix}=\begin{bmatrix}
        1-3j&+3j\\\displaystyle-\frac{1}{2}+3j&-3j
    \end{bmatrix}^{-1}\begin{bmatrix}
        0\\-1
    \end{bmatrix}=\begin{bmatrix}
        -2\\
        -2-\displaystyle\frac{2}{3}j
    \end{bmatrix}
\end{gathered}$$

La corrente che si vuole misurare corrisponde alla corrente della seconda maglia sommata alla corrente attraverso l’induttore $\overline{I}_C=\overline{I}_{m_1}+\overline{I}_L=\overline{I}_{m_1}+\frac{\overline{E}_C}{z_L}$: $$\begin{gathered}
    \overline{I}_C=2+\displaystyle\frac{2}{3}j-\frac{1}{2}j=2-\frac{1}{6}j
\end{gathered}$$ L’impedenza equivalente si ottiene dal rapporto tar la tensione inserita nel circuito e la corrente calcolata: $$\begin{gathered}
    z_\mathrm{eq}=\displaystyle\frac{\overline{E}_C}{\overline{I}_C}=\frac{1}{2-\frac{1}{6}j}=\frac{1}{4+\frac{1}{36}}\left(2-\frac{1}{6}j\right)=\frac{36}{145}\left(2-\frac{1}{6}j\right)
\end{gathered}$$ Rappresentandola in modulo e fase: $$\begin{gathered}
    |z_\mathrm{eq}|=\displaystyle\frac{36}{145}\sqrt{4+\frac{1}{6}}=0.4983\\
    \varphi=\arctan\left(\frac{-\frac{1}{6}}{2}\right)=-4.7636^{\circ}
\end{gathered}$$ Per cui l’impedenza equivalente della rappresentazione esterna di Thevenin risulta essere: $$\begin{gathered}
    z_\mathrm{eq}=0.4983e^{-j4.7636^{\circ}}
\end{gathered}$$
