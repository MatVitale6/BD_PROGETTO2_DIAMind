---
author:
- "*Giacomo Sturm*"
date: |
  *Dipartimento di Ingegneria Civile, Informatica e delle Tecnologie Aeronautiche  
  Università degli Studi “Roma Tre"*
title: |
  **Fondamenti di Telecomunicazioni**  
  Esercizi Svolti di Fondamenti di Telecomunicazioni  
  *Anno Accademico: 2023/24*
---

\providecommand{\labelText}[2]{#1}

# Analisi nel Tempo

## Energia e Potenza

### Esercizio 1

Si determina l’energia di una gaussiana di ampiezza $A$: $$\begin{gathered}
    E_x=\lim_{\Delta t\to\infty}\displaystyle\int_{-\frac{\Delta t}{2}}^{\frac{\Delta t}{2}}A^2e^{-2\alpha t^2}\mathrm{d}t=A^2\lim_{\Delta t\to\infty}\displaystyle\int_{-\frac{\Delta t}{2}}^{\frac{\Delta t}{2}}e^{-2\alpha t^2}\mathrm{d}t
\end{gathered}$$ Si considera il cambio di variabile $\tau=\sqrt{2\alpha}t$: $$E_x=A^2\lim_{\Delta t\to\infty}\displaystyle\int_{-\frac{\Delta t}{2}}^{\frac{\Delta t}{2}}\frac{e^{-\tau^2}}{\sqrt{2\alpha}}\mathrm{d}\tau=\frac{A^2}{\sqrt{2\alpha}}\int_{-\infty}^{+\infty}e^{-\tau^2}\mathrm{d}\tau$$ L’integrale ottenuto è l’integrale di Gauss, il suo valore risulta quindi essere: $$\displaystyle\int_{\mathbb{R}}e^{-t^2}\mathrm{d}t=\sqrt\pi$$ Per cui l’energia di una gaussiana è: $$E_x=A^2\displaystyle\sqrt{\frac{\pi}{2\alpha}}$$

### Esercizio 2

Si determina l’energia e la potenza di un esponenziale complesso. Il segnale ha un modulo unitario $|x(t)|=1$, per cui la sua energia risultante è: $$E_x=\lim_{\Delta t\to\infty}\displaystyle\int_{-\frac{\Delta t}{2}}^{\frac{\Delta t}{2}}\mathrm{d}t=\lim_{\Delta t\to\infty}\left(\frac{\Delta t}{2}+\frac{\Delta t}{2}\right)=\infty$$ Per cui l’esponenziale complesso non è un segnale di energia. La potenza risulta essere: $$P_x=\lim_{\Delta t\to\infty}\displaystyle\left(\frac{1}{\Delta t}\int_{-\frac{\Delta t}{2}}^{\frac{\Delta t}{2}}\mathrm{d}t\right)=\lim_{\Delta t\to\infty}\left(\frac{1}{\Delta t}\cdot\Delta t\right)=1$$ L’esponenziale complesso è quindi un segnale di potenza.

### Esercizio 3

Si determina l’energia di un esponenziale unilatero: $$E_x=\displaystyle\int_{-\infty}^{+\infty}\left[e^{-\alpha t}u(t)\right]^2\mathrm{d}t=\int_0^{+\infty}e^{-2\alpha t}\mathrm{d}t=-\frac{1}{2\alpha}\left(\cancelto{0}{e^{-\infty}}-\cancelto{1}{e^{0}}\right)=\frac{1}{2\alpha}$$ Per cui questo segnale non è né di energia né di potenza.

### Esercizio 4

Si determina la potenza del segnale coseno, di ampiezza $A$ e frequenza naturale $f_0$: $$\begin{gathered}
    x(t)=A\cos\left(2\pi f_0t\right)\\
    P_x=\displaystyle A^2f_0\int_{-\frac{1}{2f_0}}^{\frac{1}{2f_0}}\cos^2(2\pi f_0 t)\mathrm{d}t
\end{gathered}$$ Per esprimere il quadrato del coseno, si considera la formula di bisezione del coseno: $$\begin{gathered}
    \cos(2x)=2\cos^2(x)-1\\
    \cos^2(x)=\displaystyle\frac{\cos(2x)+1}{2}\\
    A^2\cos^2(2\pi f_0t)=\displaystyle\frac{A^2}{2}(\cos(4\pi f_0t)+1)
\end{gathered}$$ Si può esprimere inoltre mediante la notazione complessa delle funzioni trigonometriche: $$\begin{gathered}
    A\cos(2\pi f_0t)=\displaystyle\frac{A}{2}(e^{2i\pi f_0t}+e^{-2i\pi f_0t})\\
    |x+y|^2\,\,x,y\in\mathbb{C}\\
    (x+y)\cdot(x+y)^*=(x+y)\cdot(x^*+y^*)\\
    xx^*+xy^*+yx^*+yy^*=|x|^2+|y|^2+xy^*+yx^*\\
    xy^*+yx^*=(a_x+ib_x)\cdot(a_y-ib_y)+(a_x-ib_x)\cdot(a_y+ib_y)=2(a_xa_y+b_xb_y)=2\Re\{x^*y\}\\
    |x|^2+|y|^2+2\Re\{|x|e^{-i\varphi_x}+|y|e^{i\varphi_y}\}\\
    |x|^2+|y|^2+2|x||y|\cos(|\varphi_y-\varphi_x|)\\
    \Bigg|\displaystyle\frac{A}{2}\left(e^{2i\pi f_0t}+e^{-2i\pi f_0t}\right)\Bigg|^2=\frac{A^2}{4}\left(1+1+2\Re\Bigl\{e^{2i\pi f_0t}\cdot\left(e^{-2i\pi f_0t}\right)^*\Bigr\}\right)\\
    A^2\cos^2(2\pi f_0t)=\displaystyle\frac{A^2}{2}(1+\cos(4\pi f_0t))
\end{gathered}$$ Considerando questa sostituzione, l’integrale diventa: $$P_x=\displaystyle\frac{A^2f_0}{2}\int_{-\frac{1}{2f_0}}^{\frac{1}{2f_0}}(\cancelto{0}{\cos(4\pi f_0 t)}+1)\mathrm{d}t=\frac{A^2f_0}{2}\left(\frac{1}{2f_0}+\frac{1}{2f_0}\right)=\frac{A^2}{2}$$ L’integrale su un periodo del coseno è nullo, poiché è una funzione pari, per cui la componente $\cos(4\pi f_0 t)$ fornisce un contributo nullo.

## Convoluzioni, Correlazioni e Sistemi Ingresso-Uscita

### Esercizio 5

Calcolare la convoluzione tra un esponenziale unilatero ed un gradino, Si considera $\alpha\in\mathbb{R}^+$. $$z(t)=e^{-\alpha t}u(t)*u(t)=\displaystyle\int_{-\infty}^{+\infty}e^{-\alpha\tau}u(\tau)u(t-\tau)\mathrm{d}\tau$$ Poiché è presente un gradino nell’integrale, la convoluzione assumerà valori nulli per $t<0$, ciò si può anche individuare graficamente, poiché per gli stessi valori i due grafici del gradino e dell’esponenziale unilatero non si sovrappongono. All’aumentare del valore di $t$, il valore del segnale $z(t)$ aumenta sempre più lentamente, poiché i contributi dell’esponenziale vanno diminuendo. Poiché entrambi i gradini nell’integrale assumono valori unitari per $t>0$, il valore del segnale in questo intervallo dipende dalla funzione integrale dell’esponenziale, da $0$ al valore di $t$ corrente: $$z(t)=\begin{cases}
        0&t<0\\
        \displaystyle\int_0^te^{-\alpha \tau}\mathrm{d}\tau&t\geq0
    \end{cases}$$ Risolvendo l’integrale si ottiene: $$\displaystyle\int_0^te^{-\alpha \tau}\mathrm{d}\tau=\left|-\frac{e^{-\alpha\tau}}{\alpha}\right|^t_0=\frac{1-e^{-\alpha t}}{\alpha}$$ Per cui il segnale convoluzione in forma analitica risulta: $$z(t)=\begin{cases}
        0&t<0\\
        \displaystyle\frac{1-e^{-\alpha t}}{\alpha}&t\geq0
    \end{cases}$$ Questo segnale tende asintoticamente a $1/\alpha$ per $t\to+\infty$.

<div class="center">

</div>

### Esercizio 6

Calcolare l’autoconvoluzione di un esponenziale unilatero $$z(t)=e^{-\alpha t}u(t)*e^{-\alpha t}u(t)=\displaystyle\int_{-\infty}^{+\infty}e^{-\alpha\tau}u(\tau)e^{-\alpha(t-\tau)}u(t-\tau)\mathrm{d}\tau$$ Poiché sono unilateri, non si sovrapporranno per $t<0$, quindi la convoluzione è nulla per quei valori di tempo. Può essere spiegato tramite la proprietà del gradino di cambiare i limiti di integrazione, per cui invece di integrare da $-\infty$ a $+\infty$, si integra nell’intervallo dove si trova il gradino $u(\tau)$, ovvero da $0$ a $+\infty$: $$z(t)=\displaystyle\int_0^{+\infty}e^{-\alpha t}u(t-\tau)\mathrm{d}\tau=e^{-\alpha t}\int_0^{+\infty}u(t-\tau)\mathrm{d}\tau$$ L’area sottesa da un gradino ribaltato e traslato di un fattore $t>0$ da $0$ a $+\infty$ equivale all’area di un rettangolo di altezza $1$ e di base $t$: $$z(t)=e^{-\alpha t}\displaystyle\int_0^t\mathrm{d}\tau=te^{-\alpha t}$$

In forma analitica risulta: $$z(t)=\begin{cases}
        0&t<0\\
        te^{-\alpha t}&t\geq0
    \end{cases}$$

<div class="center">

</div>

### Esercizio 7

Calcolare la convoluzione tra due finestre. Si considerano due casi, dove le due finestra hanno base uguale, ed un caso dove hanno base differente. Si considera il caso $T_1=T_2$: $$z(t)=\mathrm{rect}\left(\displaystyle\frac{t}{T}\right)*\mathrm{rect}\left(\frac{t}{T}\right)$$

La convoluzione assume valori nulli quando non si sovrappongono, ovvero per un valore $t+\displaystyle\frac{T}{2}<-\frac{T}{2}\to t<-T$. L’area sottesa dal prodotto di queste due finestre aumenta linearmente fino a quando non si sovrappongono per $t=0$, dove l’area assume valore massimo $T\cdot 1$, dopo il quale decresce linearmente fino a $t=T$. Se una delle due fosse stata traslata di un fattore $t_0$, l’intera convoluzione sarebbe stata traslata dello stesso fattore. Da notare che la convoluzione di due segnali pari genera un segnale pari. $$z(t)=\begin{cases}
        0&t<-T\\
        \displaystyle\int_{-T}^t\mathrm{d}\tau&-T\leq t<0\\
        \displaystyle\int_t^T\mathrm{d}\tau&0\leq t<T\\
        0&t>T
    \end{cases}=\begin{cases}
        0&t<-T\land t>T\\
        T-|t|&-T\leq t<T\\
    \end{cases}\\
    z(t)=T\,\mathrm{tri}\left(\displaystyle\frac{t}{T}\right)\tag{\stepcounter{equation}\theequation}$$ La convoluzione tra due finestre di base uguale risulta in un triangolo di base doppia $2T$, e scalata di un fattore pari alla base $T$.

<div class="center">

</div>

Si considera ora il caso dove le due finestre hanno basi $T_1>T_2$: $$z(t)=\mathrm{rect}\left(\displaystyle\frac{t}{T_1}\right)*\mathrm{rect}\left(\frac{t}{T_2}\right)$$

Poiché le due finestre sono simmetriche, si analizzano solo i casi per $t<0$, per poi aggiungere per simmetria l’equazione analitica per $t\geq0$. Le due finestre non si sovrappongono per $t+\displaystyle\frac{T_2}{2}<-\frac{T_1}{2}\to t<-\frac{1}{2}(T_1+T_2)$, per cui in quell’intervallo la convoluzione assume valore nullo. Il valore della convoluzione aumenta linearmente fino a quando la finestra più piccola trasla fino ad essere completamente interna alla finestra di base $T_1$ per un valore $t-\displaystyle\frac{T_2}{2}<-\frac{T_1}{2}\to t<-\frac{1}{2}(T_1-T_2)$. Quando le due finestre si sovrappongono, il valore della convoluzione è costante, e corrisponde all’area di un rettangolo di base, base della finestra più piccola $T_2$ ed altezza unitaria $T_2\cdot1$ fino a raggiungere $t_0$. Ribaltando questo segnale ottenuto si ottiene il segnale per valori $t\geq0$: $$\begin{gathered}
    z(t)=\begin{cases}
        0&t<-\displaystyle\frac{1}{2}(T_1+T_2)\\
        \displaystyle\int_{-\frac{1}{2}(T_1+T_2)}^t\mathrm{d}\tau&-\frac{1}{2}(T_1+T_2)\leq t <-\frac{1}{2}(T_1-T_2)\\
        T_2&-\frac{1}{2}(T_1-T_2)\leq t<\frac{1}{2}(T_1-T_2)\\
        -\displaystyle\int_{-\frac{1}{2}(T_1+T_2)}^t\mathrm{d}\tau&\frac{1}{2}(T_1-T_2)\leq t <\frac{1}{2}(T_1+T_2)\\
        0&t\geq\displaystyle\frac{1}{2}(T_1+T_2)
    \end{cases}\\
    z(t)=\begin{cases}
        0&t<-\displaystyle\frac{1}{2}(T_1+T_2)\land t\geq\frac{1}{2}(T_1+T_2)\\
        \displaystyle\frac{1}{2}(T_1+T_2)-|t| &-\frac{1}{2}(T_1+T_2)\leq t <-\frac{1}{2}(T_1-T_2)\land \frac{1}{2}(T_1-T_2)\leq t <\frac{1}{2}(T_1+T_2)\\
        T_2&-\displaystyle\frac{1}{2}(T_1-T_2)\leq t<\frac{1}{2}(T_1-T_2)
    \end{cases}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

<div class="center">

</div>

Il grafico di questa convoluzione rappresenta un trapezio di altezza $T_2$, base maggiore $T_1+T_2$ e base minore $T_1-T_2$ Si nota come l’autoconvoluzione di due finestre di base uguali rappresenta un caso speciale di questo trapezio, avente base minore nulla $T-T=0$ e base doppia rispetto alla finestra $T+T=2T$, ciò equivale ad un triangolo di altezza $T$ e base $2T$.

### Esercizio 8

Calcolare la convoluzione tra i segnali $x$ e $y$: $$\begin{gathered}
    x(t)=\displaystyle t\,\mathrm{rect}\left(\frac{t-T}{2T}\right)\\
    y(t)=\displaystyle\mathrm{rect}\left(\frac{t+T}{2T}\right)\\
    z(t)=x(t)*y(t)=\displaystyle\int_{-\infty}^{+\infty}\tau\,\mathrm{rect}\left(\frac{\tau-T}{2T}\right)\mathrm{rect}\left(\frac{t-\tau+T}{2T}\right)\mathrm{d}\tau\\
    z(t)=\begin{cases}
        0&t<-2T\\
        \displaystyle\int_{0}^{t+2T}\tau \mathrm{d}\tau&-2T\leq t<0\\
        \displaystyle\int_{t}^{2T}\tau \mathrm{d}\tau&0\leq t<2T\\
        0&t\geq2T
    \end{cases}\\
    z(t)=\begin{cases}
        0&t<-2T\land t\geq2T\\
        \displaystyle\frac{1}{2}t^2+2Tt+2T^2&-2T\leq t<0\\
        \displaystyle2T^2-\frac{1}{2}t^2&0\leq t<2T
    \end{cases}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 9

Calcolare la convoluzione tra queste due finestre: $$\begin{gathered}
    z(t)=z(t)*y(t)\\
    x(t)=\displaystyle\mathrm{rect}\left(\frac{t-3T}{4T}\right)\\
    y(t)=-\displaystyle\mathrm{rect}\left(\frac{t+2T}{2T}\right)\\
    z(t)=\begin{cases}
        0&t<-2T\\
        -\displaystyle\int^{3T+t}-{T}\mathrm{d}\tau&-2T\leq t<0\\
        -2T&0\geq t<2T\\
        -\displaystyle\int_{T+t}^{5T}\mathrm{d}\tau&2T\leq t<4T\\
        0&t\geq 4T
    \end{cases}\\
    z(t)=\begin{cases}
        0&t<-2T \land t\geq 4T\\
        -2T-t&-2T\leq t<0\\
        -2T&0\leq t<2T\\
        -4T+t&2T\leq t<4T
    \end{cases}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 10

Calcolare la correlazione tra due finestre: $$\mathrm{rect}\displaystyle\left(\frac{t-\frac{T_1}{2}}{T_1}\right)\otimes\mathrm{rect}\left(\frac{t-\frac{T_2}{2}}{T_2}\right)$$

Si considera la prima finestra di base maggiore $T_1>T_2$. Per facilitare il calcolo si esprime come una convoluzione. I due segnali non si sovrappongono per valori $T_2-t<0\to t\geq T_2$, per cui la correlazione è nulla. Cominciano a sovrapporsi da $t<T_2$ fino a quando la finestra più piccola non si trova interamente nella prima finestra per $-t<0\to t\geq0$. La finestra più piccola si trova interamente in quella più grande, risultando in un’area di $T_2$, fino ad un valore $T_2-t<T_1\to t\geq -(T_1-T_2)$. L’area comincia a scendere fino ad un valore $-t<T_1\to t\geq -T_1$. Per valori più piccoli di $-T_1$ le due finestre non si sovrappongono e la correlazione risulta nulla. $$R_{xy}(t)=\begin{cases}
        0&t\geq T_2\\
        \displaystyle\int_t^{T_2}\mathrm{d}t& 0\leq t<T_2\\
        T_2& -(T_1+T_2)\leq t<0\\
        \displaystyle\int_{-T_1}^t\mathrm{d}t& -T_1\leq t<-(T_1-T_2)\\
        0&t<-T_1
    \end{cases}\\
    R_{xy}(t)=\begin{cases}
        0& t<-T_1\land t\geq T_2\\
        T_1+t& T_1\leq t<-(T_1-T_2)\\
        T_2& -(T_1-T_2)\leq t<0\\
        T_2-t &  0\leq t<T_2
    \end{cases}\tag{\stepcounter{equation}\theequation}$$

<div class="center">

</div>

### Esercizio 11

Dato il sistema definito dall’equazione $y$: $$\begin{gathered}
    y(t)=x(t)+3u(t-1)
\end{gathered}$$ Si dimostra che non è lineare: $$\begin{gathered}
    x_1(t)\to y_1(t)=x_1(t)+3u(t-1)\\
    x_2(t)\to y_2(y)=x_2(t)+3u(t-1)\\
    ax_1(t)+bx_2(t)\to ax_1(t)+bx_2(t)+3u(t-1)\neq ay_1(t)+by_2(t)
\end{gathered}$$ Si dimostra che non è tempo invariante: $$\begin{gathered}
    x(t-\tau)\to x(t-\tau)+3u(t-1)\neq y(t-\tau)=x(t-\tau)+3u(t-\tau-1)
\end{gathered}$$ Sicuramente non è un filtro. Mentre è causale, poiché il gradino è ritardato, e quindi l’uscita non dipende da valori futuri.

### Esercizio 12

Calcolare l’uscita di un filtro discreto di risposta impulsiva $h[n]$, con un entrata parametrizzata $x[n]$: $$\begin{gathered}
    h[n]=\displaystyle\frac{1}{4}\delta[n+1]+\frac{1}{2}\delta[n]+\frac{1}{4}\delta[n-1]\\
    x[n]=\cos(2\pi\phi n)\\
    \phi_1=0\to x_1[n]=1\\
    y_1[n]=h[n]*x_1[n]=\displaystyle\left[\frac{1}{4}\delta[n+1]+\frac{1}{2}\delta[n]+\frac{1}{4}\delta[n-1]\right]*x_1[n]\\
    \displaystyle\frac{1}{4}x_1[n+1]+\frac{1}{2}x_1[n]+\frac{1}{4}x_1[n-1]=\frac{1}{4}+\frac{1}{2}+\frac{1}{4}=1\\
    y_1[n]=1\tag{\stepcounter{equation}\theequation}\\
    \phi_2=\displaystyle\frac{1}{4}\to x_2[n]=\cos\left(\displaystyle\frac{\pi n}{2}\right)\\
    y_2[n]=\left[\displaystyle\frac{1}{4}\delta[n+1]+\frac{1}{2}\delta[n]+\frac{1}{4}\delta[n-1]\right]*\cos\left(\frac{\pi n}{2}\right)\\
    \displaystyle\frac{1}{4}\cos\left(\frac{\pi (n+1)}{2}\right)+\frac{1}{2}\cos\left(\frac{\pi n}{2}\right)+\frac{1}{4}\cos\left(\frac{\pi (n-1)}{2}\right)\\
    \displaystyle\frac{1}{4}\cos\left(\frac{\pi (n+1)}{2}\right)=-\frac{1}{4}\cos\left(\frac{\pi (n-1)}{2}\right)\,\forall k\in\mathbb{Z}\\
    y_2[n]=\displaystyle\frac{1}{2}\cos\left(\frac{\pi n}{2}\right)\tag{\stepcounter{equation}\theequation}\\
    \phi_3=\displaystyle\frac{1}{2}\to x_3[n]=\cos\left(\displaystyle{\pi n}\right)\\
    y[n]=\displaystyle\frac{1}{4}\cos(\pi (n+1))+\frac{1}{2}\cos(\pi n)+\frac{1}{4}\cos(\pi(n-1))=0\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 13

Si considera un generico schema di un circuito sommatore, un tipo di sistema controllore a feedforward. Calcolarne l’uscita:

<div class="center">

</div>

Per ottenere l’uscita si somma il segnale originario allo stesso segnale ritardato di un campione e moltiplicato per un fattore $a$: $$\begin{gathered}
    y[n]=x[n]+ax[n-1]\\
    h[n]=\delta[n]+a\delta[n-1]
\end{gathered}$$

<div class="center">

</div>

# Analisi in Frequenza

## Serie di Fourier

### Esercizio 14

Dato il segnale $x(t)$, calcolare i suoi coefficienti di Fourier: $$x(t)=\left|\cos\left(\displaystyle\frac{2\pi t}{T}\right)\right|$$

Si determinano i coefficienti dell’espansione di Fourier tramite la definizione: $$\begin{gathered}
    c_k=\displaystyle\frac{2}{T}\int_{-\frac{T}{4}}^{\frac{T}{4}}\cos\left(\displaystyle\frac{2\pi t}{T}\right)e^{-i\frac{4\pi kt}{T}}\mathrm{d}t\\
    \displaystyle\frac{2}{T}\int_{-\frac{T}{4}}^{\frac{T}{4}}\cos\left(\displaystyle\frac{2\pi t}{T}\right)\left[\cos\left(\frac{4\pi kt}{T}\right)-i\sin\left(\frac{4\pi kt}{T}\right)\right]\mathrm{d}t\\
    \displaystyle\frac{2}{T}\int_{-\frac{T}{4}}^{\frac{T}{4}}\cos\left(\frac{2\pi t}{T}\right)\cos\left(\frac{4\pi kt}{T}\right)\mathrm{d}t
    {-i\int_{-\frac{T}{4}}^{\frac{T}{4}}\cos\left(\frac{2\pi t}{T}\right)\sin\left(\frac{4\pi kt}{T}\right)\mathrm{d}t}
\end{gathered}$$ Poiché è una funzione pari, il primo integrale corrisponde al doppio dell’integrale su solo una metà dell’intervallo, mentre il secondo integrale, essendo una funzione dispari, assume valore nullo su un intervallo simmetrico: $$\displaystyle\frac{4}{T}\int_{0}^{\frac{T}{4}}\cos\left(\frac{2\pi t}{T}\right)\cos\left(\frac{4\pi kt}{T}\right)\mathrm{d}t-i\cdot0$$

Per le formule di prostaferesi si ottiene una somma di due coseni. Integrandoli separatamente si ottiene: $$\begin{gathered}
    c_k=\displaystyle\frac{4}{T}\frac{1}{2}\int_{-\frac{T}{4}}^{\frac{T}{4}}\cos\left(\frac{2(2k+1)\pi t}{T}\right)+\cos\left(\frac{2(2k-1)\pi t}{T}\right)\mathrm{d}t\\
    \displaystyle\left[\frac{2}{T}\frac{T}{2(2k+1)\pi}\sin\left(\frac{2(2k+1)\pi t}{T}\right)+
    \frac{2}{T}\frac{T}{2(2k-1)\pi}\sin\left(\frac{2(2k-1)\pi t}{T}\right)\right]_{0}^{\frac{T}{4}}\\
    \left[\displaystyle\frac{\sin(2(2k+1)\pi t/T)}{(2k+1)\pi}+\frac{\sin(2(2k-1)\pi t/T)}{(2k-1)\pi}\right]_0^{\frac{T}{4}}\\
    c_k=\displaystyle\frac{\sin(2(2k+1)\pi/2)}{(2k+1)\pi}+\frac{\sin(2(2k-1)\pi/2)}{(2k-1)\pi}
\end{gathered}$$

L’argomento del seno, lo rende tale che assume solo valori pari a $\pm1$. Per valori pari di $k$, il primo seno assume valore di $1$, mentre l’altro $-1$, accade l’opposto per valori dispari di $k$. I due seni assumono sempre valori discordi e unitari, quindi si possono esprimere come: $$\begin{gathered}
    c_k=\displaystyle\frac{1}{\pi}\frac{(-1)^k}{2k+1}-\frac{1}{\pi}\frac{(-1)^k}{2k-1}=-\frac{2}{\pi}\frac{1}{4k^2-1}(-1)^k
\end{gathered}$$

### Esercizio 15

Dato un segnale periodico $x(t)$ calcolare i suoi coefficienti di Fourier: $$\begin{gathered}
    x(t)=2\cos\displaystyle\left(\frac{2\pi t}{T}+\frac{\pi}{4}\right)+6\sin\left(\frac{2\pi t}{3T}\right)
\end{gathered}$$ Il primo passaggio nella rappresentazione di Fourier corrisponde all’individuazione del periodo del segnale $x$. Il periodo della somma di due segnali periodici corrisponde al minimo comune multiplo tra il periodo dei due segnali. In questo caso il periodo del segnale $x$ è $T'=3T$. Per cui si può riscrivere come: $$\begin{gathered}
    x(t)=\displaystyle2\cos\left(\frac{6\pi t}{T'}+\frac{\pi}{4}\right)+6\sin\left(\frac{2\pi t}{T'}\right)\\
    \displaystyle e^{i\left(\frac{6\pi t}{T'}+\frac{\pi}{4}\right)}+e^{-i\left(\frac{6\pi t}{T'}+\frac{\pi}{4}\right)}+\frac{3}{i}e^{i\frac{2\pi t}{T'}}-\frac{3}{i}e^{-i\frac{2\pi t}{T'}}
\end{gathered}$$ Per confronto diretto si ottengono i seguenti coefficienti: $$\begin{gathered}
    c_k=
    \begin{cases}
        0&\forall k\neq\pm1\land\pm3\\
        \displaystyle\displaystyle\frac{\strut{3}}{\strut{ i}}=-3i=-3e^{\frac{\pi}{2}} &k=1\\
        -\displaystyle\frac{\strut{3}}{\strut{i}}=3i=3e^{\frac{\pi}{2}}&k=-1\\
        \displaystyle e^{\frac{\pi}{4}}=\displaystyle\frac{\strut{1}}{\strut{\sqrt{2}}}(1+i)&k=3\\
        \displaystyle e^{-\frac{\pi}{4}}=\displaystyle\frac{\strut{1}}{\strut{\sqrt{2}}}(1-i)&k=-3
    \end{cases}
\end{gathered}$$

### Esercizio 16

Dato un segnale $x(t)$, calcolare i suoi coefficienti di Fourier: $$\begin{gathered}
    x(t)=\sin\displaystyle(2\pi t)+\cos(4\pi t+\phi)
\end{gathered}$$ Questo segnale ha un periodo $T=1$. Per confronto diretto si ottengono dei coefficienti: $$\begin{gathered}
    x(t)=\displaystyle \frac{e^{2i\pi t}-e^{-2i\pi t}}{2i}+\frac{e^{i\phi}e^{4i\pi t}+e^{-i\phi}e^{-4i\pi t}}{2}\\
    c_k=
    \begin{cases}
        0&\forall k\neq\pm1\land\pm2\\
        \displaystyle\displaystyle\frac{\strut{1}}{\strut{2i}}=-\frac{i}{2} &k=1\\
        -\displaystyle\displaystyle\frac{\strut{1}}{\strut{2i}}=\frac{i}{2}&k=-1\\
        \displaystyle\displaystyle\frac{\strut{e^{i\phi}}}{\strut{2}}&k=2\\
        \displaystyle\displaystyle\frac{\strut{e^{-i\phi}}}{\strut{2}}&k=-2
    \end{cases}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 17

Dato il segnale $x(t)$, calcolare i suoi coefficienti di Fourier: $$\begin{gathered}
    x(t)=\sin^2\displaystyle\left(\frac{2\pi t}{T}+\phi\right)=\frac{1}{2}\left(1-\cos\left(\frac{4\pi t}{T}+2\phi\right)\right)
\end{gathered}$$ Questo segnale ha periodo $T/2$. Per confronto diretto si ottengono i coefficienti: $$\begin{gathered}
    x(t)=\displaystyle\frac{1}{2}-\frac{1}{4}e^{2i\phi}e^{i\frac{4\pi t}{T}}-\frac{1}{4}e^{-2i\phi}e^{-i\frac{4\pi t}{T}}\\
    c_k=\begin{cases}
        0&\forall k\neq0\land\pm2\\
        \displaystyle\displaystyle\frac{\strut{1}}{\strut{2}}&k=0\\
        -\displaystyle\displaystyle\frac{\strut{1}}{\strut{4}}e^{2i\phi}&k=1\\
        -\displaystyle\displaystyle\frac{\strut{1}}{\strut{4}}e^{-2i\phi}&k=-1
    \end{cases}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 18

Data un’onda quadra $z(t)$, che assume valori di $1$ e $-1$ periodicamente, con periodo $T$, calcolare i suoi coefficienti di Fourier. Può essere espressa come una differenza tra due onde quadre $x(t)$ e $y(t)$ in opposizione di fase che assumono valori di $1$ e $0$ con periodo $T$. Una delle quali ha una base di lunghezza $\tau$, mentre l’altra lunghezza di $T-\tau$ e traslata di un semi-periodo $T/2$: $$z(t)=\displaystyle\sum_{k=-\infty}^{+\infty}\left[\mathrm{rect}\left(\frac{t-kT}{\tau}\right)-\mathrm{rect}\left(\frac{t-nT-\frac{T}{2}}{T-\tau}\right)\right]$$

<div class="center">

</div>

Si calcolano ora i coefficienti dell’espansione di Fourier: $$\begin{gathered}
    c_k=\displaystyle\frac{1}{T}\int_{-\frac{T}{2}}^{\frac{T}{2}}\left[\mathrm{rect}\left(\frac{t-kT}{\tau}\right)-\mathrm{rect}\left(\frac{t-kT-\frac{T}{2}}{T-\tau}\right)\right]\mathrm{d}t\\
    \displaystyle\frac{1}{T}\int_{-\frac{\tau}{2}}^{\frac{\tau}{2}}\mathrm{rect}\left(\frac{t-kT}{\tau}\right)\mathrm{d}t-\frac{1}{T}\int_{-\frac{T-\tau}{2}}^{\frac{T-\tau}{2}}\mathrm{rect}\left(\frac{t-kT-\frac{T}{2}}{T-\tau}\right)\mathrm{d}t\\
    \displaystyle\frac{e^{-i\pi k\frac{\tau}{T}}-e^{i\pi k\frac{\tau}{T}}}{-2i}\frac{1}{\pi k}\frac{\tau}{T}-\frac{e^{-i2\pi k\frac{T-\tau/2}{T}}-e^{i2\pi k\frac{T-\tau/2}{T}}}{-2i}\frac{1}{\pi k}\frac{\tau}{T}
\end{gathered}$$ Per $k=0$ si ottiene una forma indeterminata, per cui bisogna risolvere l’integrale considerando il valor medio assunto dal segnale nell’intervallo $\left[-T/2,T/2\right]$. $$\begin{gathered}
    \displaystyle\frac{\tau}{T}\mathrm{sinc}\left(\frac{k\tau}{T}\right)-\frac{e^{i\pi k\frac{\tau}{T}}-e^{-i\pi k\frac{\tau}{T}}}{-2i}\frac{1}{\pi k}\\
    c_k=\displaystyle\frac{2\tau}{T}\mathrm{sinc}\left(\frac{k\tau}{T}\right)
\end{gathered}$$

Il segnale originale può essere espresso come un’onda quadra doppia, di stesso periodo $T$ e base $\tau$, e traslata verso il basso: $$z(t)=\displaystyle\sum_{k=-\infty}^{+\infty}\left[2\,\mathrm{rect}\left(\frac{t-kT}{\tau}\right)\right]-1=2x(t)-1$$ In questo modo si effettuano meno calcoli per determinare i coefficienti di Fourier, usufruendo della proprietà di linearità bisogna tenere conto che il fattore costante $-1$, assume un valore non nullo solo per $k=0$. Si considerano i coefficienti del segnale $x$ come $c_k$, mentre del segnale costante $d_k$, per cui in questo caso i coefficienti del segnale $z$ si esprimono come: $$a_k=\begin{cases}
        2c_k+d_k &k=0\\
        2c_k&k\neq0
    \end{cases}=\begin{cases}
        \displaystyle\frac{\strut 2\tau}{\strut T}-1&k=0\\
        \displaystyle\frac{\strut 2\tau}{\strut T}\mathrm{sinc}\left(\frac{ k\tau}{ T}\right)&k\neq0
    \end{cases}$$

### Esercizio 19

Si considera un’onda quadra di periodo $T$ traslata di un fattore $\tau$, corrispondente alla lunghezza della sua base. Dati i coefficienti di un onda quadra non traslata $c_k$, calcolare i suoi coefficienti di Fourier.

I coefficienti $d_k$ del segnale traslato si possono esprimere direttamente come: $$d_k=\displaystyle\frac{\tau}{T}\mathrm{sinc}\left(\frac{k\tau}{T}\right)e^{-i\frac{2\pi k\tau}{T}}$$

In caso il periodo sia esattamente il doppio della base $T=2\tau$: $$d_k=\displaystyle\frac{1}{2}\mathrm{sinc}\left(\frac{k}{2}\right)e^{-i\pi k}=\frac{1}{2}\frac{e^{i\frac{\pi k}{2}}-e^{-i\frac{\pi k}{2}}}{i\pi k}e^{-i\pi k}=
    \frac{e^{-i\frac{\pi k}{2}}-e^{-i\frac{3\pi k}{2}}}{2i\pi k}$$ Per cui i coefficienti dell’onda quadra di armoniche di ordine pari risultano nulli.

### Esercizio 20

Dato il segnale dente di sega, calcolare i suoi coefficienti di Fourier:

<div class="center">

</div>

Si calcolano i coefficienti di Fourier tramite la definizione, e si calcola l’integrale per parti: $$\begin{gathered}
    c_k=\displaystyle\frac{1}{T}\int_{-\frac{T}{2}}^{\frac{T}{2}}te^{-i\frac{2\pi kt}{T}}\mathrm{d}t=\displaystyle\left[-\frac{1}{T}\frac{T}{2i\pi k}te^{-i\frac{2\pi kt}{T}}\right]_{-\frac{T}{2}}^{\frac{T}{2}}-
    \frac{1}{T}\int_{-\frac{T}{2}}^{\frac{T}{2}}-\frac{T}{2i\pi k}e^{-i\frac{2\pi kt}{T}\mathrm{d}t}\\
    \displaystyle-\frac{T}{2i\pi k}\left(\frac{e^{-i\pi k}+e^{i\pi k}}{2}\right)+\frac{1}{2i\pi k}\left[\frac{T}{2i\pi k}e^{-i\frac{2\pi kt}{T}}\right]_{-\frac{T}{2}}^{\frac{T}{2}}\\
    \displaystyle-\frac{T}{2i\pi k}\left(\frac{e^{i(-\pi k)}+e^{-i(-\pi k)}}{2}\right)-\frac{2iT}{4\pi^2k^2}\left(\frac{e^{i(-\pi k)}-e^{-i(-\pi k)}}{2i}\right)\\
    \displaystyle-\frac{T}{2i\pi k}\cos\left(-\pi k\right)+\frac{2iT}{4\pi^2k^2}\sin(-\pi k)
\end{gathered}$$ La componente sinusoidale è nulla per ogni valore di $k$, per cui il coefficiente generico si esprime come: $$\begin{gathered}
    c_k=\displaystyle-\frac{T}{2i\pi k}\cos(-\pi k)=\frac{Ti}{2\pi k}\cos(\pi k)=\frac{Ti}{2\pi k}(-1)^k \;\;k\neq0
\end{gathered}$$ Il coefficiente $c_0$ è nullo, poiché rappresenta il valor medio del periodo. In questo caso essendo un segnale dispari, il valor medio nel periodo è nullo: $$c_0=\displaystyle\frac{1}{T}\int_{-\frac{T}{2}}^{\frac{T}{2}}t\,\mathrm{d}t=0$$

### Esercizio 21

Dato il seguente segnale dente di sega, calcolare i suoi coefficienti di Fourier:

<div class="center">

</div>

Si può esprimere come il precedente segnale analizzato, traslato nel tempo e nello spazio di uno stesso fattore $T/2$. La traslazione nello spazio può essere sia un ritardo che un anticipo, poiché si ottiene lo stesso segnale risultante: $$y(t)=x\left(t\pm\frac{T}{2}\right)+\displaystyle\frac{T}{2}$$ Si considera in questo caso un ritardo di $T/2$. Conoscendo i coefficienti di $c_k$, si può attuare una traslazione nel tempo, per ottenere i coefficienti della serie di Fourier del segnale $y$: $$\begin{gathered}
    d_k=\begin{cases}
        \displaystyle c_0+\frac{T}{2}=\frac{T}{2} &k=0\\
        c_ke^{-i\frac{2\pi k}{T}\frac{T}{2}}=\displaystyle\frac{T}{2i\pi k}(-1)^ke^{-i\pi k}&k\neq0
    \end{cases}
\end{gathered}$$

### Esercizio 22

Dato un segnale treno di triangoli $x(t)$, calcolare i suoi coefficienti di Fourier: $$x(t)=\displaystyle\sum_{k=-\infty}^{+\infty}\mathrm{tri}\left(\frac{2(t-kT)}{\tau}\right)$$

<div class="center">

</div>

Si calcolano i coefficienti tramite la definizione. Poiché è presente un solo triangolo nell’intervallo di integrazione, si può restringere l’intervallo: $$\begin{gathered}
    c_k=\displaystyle\frac{1}{T}\int_{-\frac{T}{2}}^{\frac{T}{2}}\mathrm{tri}\left(\frac{2t}{\tau}\right)e^{-i\frac{2\pi kt}{T}}\mathrm{d}t=\frac{1}{T}\int_{-\frac{\tau}{2}}^{\frac{\tau}{2}}\left(1-\left|\frac{2t}{\tau}\right|\right)e^{-i\frac{2\pi kt}{T}}\mathrm{d}t\\
    \displaystyle\frac{1}{T}\int_{-\frac{\tau}{2}}^{\frac{\tau}{2}}e^{-i\frac{2\pi kt}{T}}\mathrm{d}t+\frac{1}{T}\int_{-\frac{\tau}{2}}^{\frac{\tau}{2}}-\left|\frac{2t}{\tau}\right|e^{-i\frac{2\pi kt}{T}}\mathrm{d}t\\
    \displaystyle\frac{1}{T}\int_{-\frac{\tau}{2}}^{\frac{\tau}{2}}e^{-i\frac{2\pi kt}{T}}\mathrm{d}t-\frac{1}{T}\left(\int_{-\frac{\tau}{2}}^{0}-\frac{2t}{\tau}e^{-i\frac{2\pi kt}{T}}\mathrm{d}t+\int_{0}^{\frac{\tau}{2}}\frac{2t}{\tau}e^{-i\frac{2\pi kt}{T}}\mathrm{d}t\right)
\end{gathered}$$ Il primo integrale corrisponde all’integrale ai coefficienti di una finestra, ed è stato già precedentemente calcolato, per cui si omette la risoluzione. Si considera la sostituzione $t=-t'$ nel secondo integrale: $$\begin{gathered}
    \displaystyle\frac{\tau}{T}\mathrm{sinc}\left(\frac{\tau k}{T}\right)-\frac{1}{T}\left(\int_{-\frac{-\tau}{2}}^{0}-\frac{2(-t)}{\tau}e^{-i\frac{2\pi k(-t)}{T}}\mathrm{d}(-t)+\int_{0}^{\frac{\tau}{2}}\frac{2t}{\tau}e^{-i\frac{2\pi kt}{T}}\mathrm{d}t\right)\\
    \displaystyle\frac{\tau}{T}\mathrm{sinc}\left(\frac{\tau k}{T}\right)-\frac{1}{T}\left(-\int_{\frac{\tau}{2}}^{0}\frac{2t}{\tau}e^{i\frac{2\pi kt}{T}}\mathrm{d}t+\int_{0}^{\frac{\tau}{2}}\frac{2t}{\tau}e^{-i\frac{2\pi kt}{T}}\mathrm{d}t\right)\\
    \displaystyle\frac{\tau}{T}\mathrm{sinc}\left(\frac{\tau k}{T}\right)-\frac{1}{T}\left(\int^{\frac{\tau}{2}}_{0}\frac{2t}{\tau}e^{i\frac{2\pi kt}{T}}\mathrm{d}t+\int_{0}^{\frac{\tau}{2}}\frac{2t}{\tau}e^{-i\frac{2\pi kt}{T}}\mathrm{d}t\right)\\
    \displaystyle\frac{\tau}{T}\mathrm{sinc}\left(\frac{\tau k}{T}\right)-\frac{1}{T}\int^{\frac{\tau}{2}}_{0}\frac{4t}{\tau}\frac{e^{i\frac{2\pi kt}{T}}+e^{-i\frac{2\pi kt}{T}}}{2}\mathrm{d}t\\
    \displaystyle\frac{\tau}{T}\mathrm{sinc}\left(\frac{\tau k}{T}\right)-\frac{4}{\tau T}\int_{0}^{\frac{\tau}{2}}t\cos\left(\frac{2\pi kt}{T}\right)\mathrm{d}t
\end{gathered}$$ Quest’ultimo integrale così ottenuto si risolve mediante integrazione per parti: $$\begin{gathered}
    \displaystyle\frac{\tau}{T}\mathrm{sinc}\left(\frac{\tau k}{T}\right)-\frac{4}{\tau T}\left[\frac{T}{2\pi k}t\sin\left(\frac{2\pi kt}{T}\right)\right]^{\frac{\tau}{2}}_0
    +\frac{4}{\tau T}\int_{0}^{\frac{\tau}{2}}\frac{T}{2\pi k}\sin\left(\frac{2\pi kt}{T}\right)\mathrm{d}t\\
    \displaystyle\frac{\tau}{T}\mathrm{sinc}\left(\frac{\tau k}{T}\right)-\frac{\tau}{T}\frac{T}{\pi k\tau}\sin\left(\frac{\pi k\tau}{T}\right)+0+
    \frac{4}{\tau T}\left[-\left(\frac{T}{2\pi k}\right)^2\cos\left(\frac{2\pi kt}{T}\right)\right]^{\frac{\tau}{2}}_0\\
    \displaystyle\frac{\tau}{T}\mathrm{sinc}\left(\frac{\tau k}{T}\right)-\displaystyle\frac{\tau}{T}\mathrm{sinc}\left(\frac{\tau k}{T}\right)-
    \frac{T}{\pi^2k^2\tau}\left[\cos\left(\frac{\pi k\tau}{T}\right)-1\right]\\
    \displaystyle\frac{2T}{\pi^2k^2\tau}\sin^2\left(\frac{\pi kt}{2T}\right)=
    \frac{\tau}{2T}\left[\frac{2T}{\pi k\tau}\sin\left(\frac{\pi kt}{2T}\right)\right]\left[\frac{2T}{\pi k\tau}\sin\left(\frac{\pi kt}{2T}\right)\right]\\
    \displaystyle\frac{\tau}{2T}\left[\mathrm{sinc}\left(\frac{k\tau}{2T}\right)\right]\left[\mathrm{sinc}\left(\frac{k\tau}{2T}\right)\right]\\
    c_k=\displaystyle\frac{\tau}{2T}\mathrm{sinc}^2\left(\frac{k\tau }{2T}\right)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$ I coefficienti di un treno di triangoli risultano essere dei seni cardinali quadrati.

## Trasformata di Fourier

### Esercizio 23

Data una gaussiana traslata nel tempo, calcolare la sua trasformata: $$\begin{gathered}
    x(t)=e^{-\alpha(t-t_0)^2}\\
    X(f)=\displaystyle\sqrt{\frac{\pi}{\alpha}}e^{-\left(\frac{\pi^2f^2}{\alpha}+2i\pi ft_0\right)}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 24

Calcolare l’antitrasformata del segnale $X_1(f)$: $$\begin{gathered}
    X_1(f)=\displaystyle\frac{1}{(\alpha+2i\pi f)^2}
\end{gathered}$$ Per ottenere la trasformata del segnale, si considera il duale della proprietà della derivazione della trasformata. Si considera il segnale esponenziale unilatero e la sua trasformata: $$\begin{gathered}
    x(t)=e^{-\alpha t}u(t)\\
    X(f)=\displaystyle\frac{1}{\alpha+2i\pi f}\\
    \displaystyle\frac{\mathrm{d}}{\mathrm{d}f}X(f)=\frac{-2i\pi}{(\alpha+2i\pi f)^2}\\
    X_1(f)=\displaystyle-\frac{1}{2i\pi}\frac{\mathrm{d}}{\mathrm{d}f}X(f)\to-\frac{1}{2i\pi}(-2i\pi tx(t))=te^{-\alpha t}u(t)\\
    x_1(t)=te^{-\alpha t}u(t)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 25

Calcolare l’energia segnale $x(t)$: $$\begin{gathered}
    x(t)=\displaystyle\frac{\sin(\pi t)}{\pi t}\cos(2\pi \alpha t)=\frac{1}{2}\mathrm{sinc}(t)(e^{2i\pi\alpha t}+e^{-2i\pi\alpha t})\\
\end{gathered}$$ Per il teorema della traslazione in frequenza, la trasformata del segnale $x$ risulta essere: $$\begin{gathered}
    X(f)=\displaystyle\frac{1}{2}\mathrm{rect}(f+\alpha)+\frac{1}{2}\mathrm{rect}(f-\alpha)
\end{gathered}$$ La sua energia si calcola come: $$\begin{gathered}
    E_x=\displaystyle\int_{-\infty}^{+\infty}|X(f)|^2\mathrm{d}f\\
    \displaystyle\frac{1}{4}\left(\int_{-\infty}^{+\infty}\left[\mathrm{rect}(f+\alpha)+\mathrm{rect}(f-\alpha)\right]^2\mathrm{d}f\right)\\
    E_x=\begin{cases}
        \displaystyle\frac{1}{4}\int_{-\alpha-1/2}^{-\alpha+1/2}\mathrm{d}f+\frac{1}{4}\int_{\alpha-1/2}^{\alpha+1/2}\mathrm{d}f& \alpha\geq1/2\\
        \displaystyle\frac{1}{4}\int_{-\alpha-1/2}^{\alpha-1/2}\mathrm{d}f+\frac{1}{2}\int_{\alpha-1/2}^{-\alpha+1/2}\mathrm{d}f+\frac{1}{4}\int_{-\alpha+1/2}^{\alpha+1/2}\mathrm{d}f&\alpha<1/2
    \end{cases}\\
    E_x=\begin{cases}
        \displaystyle\frac{\strut 1}{\strut 2}&\alpha\geq1/2\\
        \displaystyle\frac{\strut 2\alpha}{\strut 4}+\frac{\strut 2\alpha}{\strut 4}+1-2\alpha=1-\alpha&\alpha<1/2
    \end{cases}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 26

Calcolare la trasformata del segnale $x(t)$: $$\begin{gathered}
    x(t)=e^{3t}u(-t)
\end{gathered}$$ Tramite la proprietà di ribaltamento e di scala: $$\begin{gathered}
    x_1(t)=e^{-3t}u(t)\\
    X_1(f)=X(-f)=\displaystyle\frac{1}{3+2i\pi f}\\
    X(f)=\displaystyle\frac{1}{3-2i\pi f}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 27

Calcolare la trasformata del segnale $x(t)$: $$\begin{gathered}
    x(t)=e^{-2t+4}u(t-2)=e^{-2*(t-2)}u(t-2)
\end{gathered}$$ Per la proprietà della traslazione nel tempo: $$\begin{gathered}
    x_1(t)=e^{-2t}u(t)\\
    X_1(f)=\displaystyle\frac{1}{2+2i\pi f}\\
    X(f)=\displaystyle\frac{1}{2+2i\pi f}e^{-4i\pi f}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 28

Calcolare la trasformata del segnale $x(t)$: $$\begin{gathered}
    x(t)=e^{-t/2}\cos(100\pi t)u(t)
\end{gathered}$$ Si applica la proprietà di modulazione: $$\begin{gathered}
    x_1(t)=e^{-t/2}u(t)\\
    X_1(f)=\displaystyle\frac{1}{1/2+2i\pi f}\\
    X(f)=\displaystyle\frac{1}{2}\left(X_1(f-50)+X_1(f+50)\right)\\
    X(f)=\displaystyle\frac{1}{2}\frac{1}{1/2+2i\pi (f-50)}+\frac{1}{2}\frac{1}{1/2+2i\pi (f+50)}\\
    X(f)=\displaystyle\frac{1}{1+4i\pi (f-50)}+\frac{1}{1+4i\pi (f+50)}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 29

Calcolare l’autoconvoluzione del segnale $x(t)$, passando per la sua trasformata: $$\begin{gathered}
    x(t)=A\,\mathrm{rect}\displaystyle\left(\frac{2(t-3T/4)}{T}\right)-A\,\mathrm{rect}\displaystyle\left(\frac{2(t-T/4)}{T}\right)\\
    X(f)=\displaystyle\frac{AT}{2}\,\mathrm{sinc}\left(\frac{Tf}{2}\right)e^{-3i\pi fT/2}-\displaystyle\frac{AT}{2}\,\mathrm{sinc}\left(\frac{T}{2}f\right)e^{-i\pi fT/2}\\
    X(f)=\displaystyle\frac{AT}{2}\,\mathrm{sinc}\left(\frac{Tf}{2}\right)\left(e^{-3i\pi fT/2}-e^{-i\pi fT/2}\right)\\
    X^2(f)=\displaystyle\frac{A^2T^2}{4}\,\mathrm{sinc}^2\left(\frac{Tf}{2}\right)\left(e^{-3i\pi fT}+e^{-i\pi fT}-2e^{-2i\pi fT}\right)\\
    x(t)*x(t)=\displaystyle\int_{-\infty}^{+\infty}X^2(f)e^{2i\pi ft}\mathrm{d}f\\
    \displaystyle\int_{-\infty}^{+\infty}\left[\frac{A^2T^2}{4}\,\mathrm{sinc}^2\left(\frac{Tf}{2}\right)\left(e^{-3i\pi fT}+e^{-i\pi fT}-2e^{-2i\pi fT}\right)\right]e^{2i\pi ft}\mathrm{d}f
\end{gathered}$$ Un prodotto nel domino delle frequenze corrisponde ad una convoluzione nel domino del tempo, per cui si può esprimere l’autoconvoluzione come la convoluzione tra un segnale triangolo e una combinazione lineare di impulsi: $$\begin{gathered}
    X_1(f)=\displaystyle\frac{A^2T^2}{4}\,\mathrm{sinc}^2\left(\frac{Tf}{2}\right)\\
    x_1(t)=\displaystyle\frac{A^2T^2}{4}\frac{2}{T}\,\mathrm{tri}\left(\frac{2t}{T}\right)\\
    X_2(f)=e^{-3i\pi fT}+e^{-i\pi fT}-2e^{-2i\pi fT}\\
    x_2(t)=\delta(t-3T/2)+\delta(t-T/2)-2\delta(t-T)\\
    x(t)*x(t)=\displaystyle\int_{-\infty}^{+\infty}X(f)^2e^{2i\pi ft}\mathrm{d}f=\int_{-\infty}^{+\infty}X_1(f)X_2(f)e^{2i\pi ft}\mathrm{d}f=x_1(t)*x_2(t)\\
    \displaystyle\frac{A^2T^2}{4}\frac{2}{T}\,\mathrm{tri}\left(\frac{2t}{T}\right)*\left[\delta(t-3T/2)+\delta(t-T/2)-2\delta(t-T)\right]\\
    x(t)*x(t)=\displaystyle\frac{A^2T^2}{4}\left(\mathrm{tri}\left(\frac{2}{T}(t-3T/2)\right)+\mathrm{tri}\left(\frac{2}{T}(t-T/2)\right)-2\,\mathrm{tri}\left(\frac{2}{T}(t-T)\right)\right)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 30

Calcolare la trasformata del segnale $x(t)$: $$\begin{gathered}
    x(t)=\mathrm{rect}(3t-1/2)=\mathrm{rect}(3(t-1/6))
\end{gathered}$$ Per la proprietà di scala e di traslazione nel tempo: $$\begin{gathered}
    X(f)=\displaystyle\frac{1}{3}\mathrm{sinc}\left(\frac{f}{3}\right)e^{-i\pi f/3}
\end{gathered}$$

### Esercizio 31

Calcolare la trasformata del segnale $x(t)$, esprimibile come un segnale triangolo moltiplicato per un gradino, oppure una retta moltiplicata per una finestra, si sceglie quest’ultima rappresentazione per facilitare il calcolo: $$\begin{gathered}
    x(t)=A\,\displaystyle\mathrm{tri}\left(\frac{t+T/2}{T}\right)u(t+T/2)\lor x(t)=A\left(\frac{1}{2}-\frac{t}{T}\right)\mathrm{rect}\left(\frac{t}{T}\right)\\
    \displaystyle\frac{A}{2}\mathrm{rect}\left(\frac{t}{T}\right)-\frac{A}{T}t\,\mathrm{rect}\left(\frac{t}{T}\right)
\end{gathered}$$ Per la proprietà duale alla derivazione, si calcola il secondo componente: $$\begin{gathered}
    x_1(t)=-2i\pi tx_2(t)\\
    X_1(f)=\displaystyle\frac{\mathrm{d}X_2}{\mathrm{d}f}\\
    x_1(t)=-\displaystyle\frac{A}{T}t\,\mathrm{rect}\left(\frac{t}{T}\right)\\
    x_2(t)=\displaystyle\frac{1}{2i\pi}\frac{A}{T}\mathrm{rect}\left(\frac{t}{T}\right)\\
    X_2(f)=\displaystyle\frac{1}{2i\pi}\frac{A}{T}T\,\mathrm{sinc}(Tf)=\frac{A}{\pi T}\frac{\sin(\pi Tf)}{f}\\
    X_1(f)=\displaystyle\frac{\mathrm{d}X_2}{\mathrm{d}f}=\frac{1}{2i\pi}\frac{A}{\pi T}\frac{\cos(\pi Tf)\pi Tf-\sin(\pi Tf)}{f^2}\\
\end{gathered}$$ Per cui la trasformata complessiva è: $$\begin{gathered}
    X(f)=\displaystyle\frac{AT}{2}\mathrm{sinc}(Tf)+\frac{A}{\pi Tf^2(2\pi i)}\left[\cos(\pi Tf)\pi Tf-\sin (\pi Tf)\right]\\
    \displaystyle\frac{AT}{2\pi Tf}\frac{i}{i}\sin(\pi Tf)+\frac{A}{2i\pi f}\cos(\pi Tf)-\frac{A}{2i\pi f}\frac{\sin(\pi Tf)}{\pi Tf}\\
    \displaystyle\frac{A}{2i\pi f}\frac{i}{i}\left[\cos(\pi Tf)+i\sin(\pi Tf)\right]-\frac{A}{2i\pi f}\frac{i}{i}\mathrm{sinc}( Tf)\\
    X(f)=\displaystyle-\frac{Ai}{2\pi f}\left[e^{i\pi fT}-\mathrm{sinc}(fT)\right]\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

Calcolare ora questa trasformata usando la proprietà alla derivazione: $$\begin{gathered}
    x_1(t)=\displaystyle\frac{A}{2}\mathrm{rect}\left(\frac{t}{T}\right)-\frac{A}{T}t\,\mathrm{rect}\left(\frac{t}{T}\right)\\
    \displaystyle\frac{\mathrm{d}x_1}{\mathrm{d}t}=x_2(t)
\end{gathered}$$ Il segnale $x_1$ presente una discontinuità in $-T/2$, e rimane costante fino al valore $T/2$: $$\begin{gathered}
    x_2(t)=A\delta(t+T/2)-\displaystyle\frac{A}{T}\mathrm{rect}\left(\frac{t}{T}\right)\\
    X_2(f)=Ae^{i\pi fT}-\displaystyle\frac{A}{T}T\mathrm{sinc}(Tf)\\
    X_2(f)=2i\pi fX_1(f)\\
    X_1(f)=\displaystyle\frac{A}{2i\pi f}\frac{i}{i}\left[e^{i\pi fT}-\mathrm{sinc}(Tf)\right]\\
    X_1(f)=\displaystyle-\frac{Ai}{2\pi f}\left[e^{i\pi fT}-\mathrm{sinc}(Tf)\right]\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 32

Calcolare l’antitrasformata del segnale $X_1(f)$: $$\begin{gathered}
    X_1(f)=\displaystyle\frac{1}{2}\left[X(f-f_0)+X(f+f_0)\right]\cos(2\pi f/f_0)
\end{gathered}$$ Per l’inverso della proprietà di modulazione, e per la proprietà di convoluzione: $$\begin{gathered}
    x_1(t)=\left[x(t)\cos(2\pi tf_0)\right]*\left[\displaystyle\frac{1}{2}\delta(t+1/f_0)+\frac{1}{2}\delta(t-1/f_0)\right]\\
    x_1(t)=\displaystyle\frac{1}{2}x\left(t+\frac{1}{f_0}\right)\cos\left[2\pi f_0\left(t+\frac{1}{f_0}\right)\right]+\frac{1}{2}x\left(t-\frac{1}{f_0}\right)\cos\left[2\pi f_0\left(t-\frac{1}{f_0}\right)\right]
\end{gathered}$$ Poiché il coseno è traslato di un periodo $1/f_0$: $$\begin{gathered}
    x_1(t)=\left[\displaystyle\frac{1}{2}x\left(t+\frac{1}{f_0}\right)+\frac{1}{2}x\left(t-\frac{1}{f_0}\right)\right]\cos(2\pi tf_0)
\end{gathered}$$

### Esercizio 33

Calcolare la trasformata del segnale $x(t)$: $$\begin{gathered}
    x(t)=2\,\mathrm{rect}(2t)-\mathrm{rect}(t)=\mathrm{rect}(2t)-\mathrm{rect}\left[\displaystyle4\left(t-\frac{3}{2}\right)\right]-\mathrm{rect}\left[\displaystyle4\left(t-\frac{3}{8}\right)\right]\\
    X(f)=\displaystyle\frac{1}{2}\mathrm{sinc}\left(\frac{f}{2}\right)-\frac{1}{4}\mathrm{sinc}\left(\frac{f}{4}\right)e^{-3i\pi f/4}-\frac{1}{4}\mathrm{sinc}\left(\frac{f}{4}\right)e^{-3i\pi f}\\
    X(f)=\displaystyle\frac{1}{2}\left[\mathrm{sinc}\left(\frac{f}{2}\right)-\mathrm{sinc}\left(\frac{f}{4}\right)\cos\left(\frac{3\pi f}{4}\right)\right]\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 34

Calcolare la trasformata del segnale $x(t)$: $$\begin{gathered}
    x(t)=\mathrm{rect}\left(\displaystyle\frac{t+T/2}{T}\right)-\mathrm{rect}\left(\displaystyle\frac{t-T/2}{T}\right)
\end{gathered}$$

<div class="center">

</div>

Per la linearità della trasformata e per la proprietà di traslazione nel tempo la trasformata si ottiene come: $$\begin{gathered}
    X(f)=T\left(e^{i\pi fT}-e^{-i\pi fT}\right)\mathrm{sinc}\left(T f\right)=2Ti\sin(\pi fT)\mathrm{sinc}(Tf)\\
    2iT\displaystyle\frac{\sin(\pi fT)}{\pi fT}\sin(\pi fT)=2i\frac{\sin^2(\pi fT)}{\pi f}\\
    X(f)=2i\displaystyle\frac{\sin^"(\pi fT)}{\pi f}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 35

Calcolare la trasformata del seguente segnale onda quadra di base $\tau$ e di periodo $T$: $$\begin{gathered}
    x(t)=\displaystyle\sum_{k=-\infty}^{+\infty}\mathrm{rect}\left(\frac{t-kT}{\tau}\right)\\
    X(f)=\displaystyle\sum_{k=-\infty}^{+\infty}\frac{\tau}{T}\mathrm{sinc}\left(\frac{\tau k}{T}\right)\delta\left(f-\frac{k}{T}\right)\tag{\stepcounter{equation}\theequation}\\
    c_k=\displaystyle\frac{\tau}{T}\mathrm{sinc}\left(\frac{\tau k}{T}\right)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 36

Calcolare la trasformata di un treno di trapezi di base maggiore $2T$, di base minore $T$, di altezza $T$ e di periodo $\overline T=5T/2$: $$\begin{gathered}
    X(f)=\displaystyle\sum_{k=-\infty}^{+\infty}c_k\delta\left(f-\frac{k}{\overline T}\right)
\end{gathered}$$ Per calcolare i coefficienti della serie, si può esprimere un singolo trapezio come l’autoconvoluzione di un segnale finestra. Inoltre è sufficiente calcolare la trasformata di un singolo trapezio per ottenere i coefficienti: $$\begin{gathered}
    x_1(t)=2\displaystyle\mathrm{rect}\left(\frac{2t}{3T}\right)\\
    x_2(t)=\displaystyle\mathrm{rect}\left(\frac{2t}{T}\right)\\
    c_k=\displaystyle\frac{1}{\overline T}\int_{-\overline T/2}^{\overline T/2}x_1(t)*x_2(t)e^{-2i\pi kt/\overline T}\mathrm{d}t\\
    c_k=\displaystyle\frac{1}{\overline T}X_1\left(\frac{k}{ T}\right)X_2\left(\frac{k}{ T}\right)\\
    c_k=\displaystyle\frac{2}{\overline T}\left[\frac{3T}{2}\mathrm{sinc}\left(\frac{3T}{2}\frac{k}{ T}\right)\frac{T}{2}\mathrm{sinc}\left(\frac{T}{2}\frac{k}{ T}\right)\right]\\
    c_k=\displaystyle\frac{6T^2}{4}\frac{2}{5T}\mathrm{sinc}\left(\frac{3T}{2}\frac{k}{ T}\right)\mathrm{sinc}\left(\frac{T}{2}\frac{k}{ T}\right)\\
    c_k=\displaystyle\frac{3T}{5}\mathrm{sinc}\left(\frac{3k}{2}\right)\mathrm{sinc}\left(\frac{k}{2}\right)\\
    X(f)=\displaystyle\frac{2}{5T}\sum_{n=-\infty}^{+\infty}\left[\frac{3T}{5}\mathrm{sinc}\left(\frac{3k}{2}\right)\mathrm{sinc}\left(\frac{k}{2}\right)\right]\delta\left(f-\frac{2k}{5T}\right)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 37

Calcolare la seguente convoluzione, passando per il dominio della frequenza: $$\begin{gathered}
    x(t)=\left[\cos(2\pi f_0t)\sin(2\pi f_0t)\right]*\displaystyle\frac{\sin(3\pi f_0t)}{\pi t}\\
    \left[\cos(2\pi f_0t)\sin(2\pi f_0t)\right]*\displaystyle3f_0\frac{\sin(3\pi f_0t)}{3\pi f_0t}\\
    \left[\cos(2\pi f_0t)\sin(2\pi f_0t)\right]*3f_0\mathrm{sinc}(3f_0 t)
\end{gathered}$$ Si applica la formula di duplicazione del seno, e si passa per il dominio della frequenza: $$\begin{gathered}
    x(t)=\displaystyle\frac{3f_0}{2}\sin(4\pi f_0t)*\mathrm{sinc}(3f_0t)\\
    X(f)=\displaystyle\frac{1}{4i}\left[\delta(f-2f_0)-\delta(f+2f_0)\right]\frac{3f_0}{3f_0}\mathrm{rect}\left(\frac{f}{3f_0}\right)\\
    \displaystyle\frac{1}{4i}\left[\mathrm{rect}\left(-\frac{2f_0}{3f_0}\right)\delta(f-2f_0)-\mathrm{rect}\left(\frac{2f_0}{3f_0}\right)\delta(f+2f_0)\right]\\
    \displaystyle\frac{1}{4i}\mathrm{rect}\left(\frac{2}{3}\right)\left[\delta(f-2f_0)-\delta(f+2f_0)\right]
\end{gathered}$$ Poiché il valore $2/3$ è esterno all’intervallo di valori non nulli del segnale finestra $[-1/2,1/2]$, la trasformata assume valore nullo. $$\begin{gathered}
    x(t)=0
\end{gathered}$$

### Esercizio 38

Calcolare il segnale $x(t)$, passando per il dominio della frequenza: $$\begin{gathered}
    x(t)=\cos(2\pi f_0t)\left[\sin(2\pi f_0t)*\displaystyle\frac{\sin(3\pi f_0t)}{\pi t}\right]\\
    x_1(t)=\sin(2\pi f_0t)*\displaystyle\frac{\sin(3\pi f_0t)}{\pi t}\\
    X_1(f)=\displaystyle\frac{1}{2i}\left[\delta(f-f_0)-\delta(f+f_0)\right]\cdot \frac{3f_0}{3f_0}\mathrm{rect}\left(\frac{f}{3f_0}\right)\\
    \displaystyle\frac{1}{2i}\delta(f-f_0)\mathrm{rect}\left(-\frac{f_0}{3f_0}\right)-\frac{1}{2i}\delta(f+f_0)\mathrm{rect}\left(\frac{f_0}{3f_0}\right)\\
    \displaystyle\frac{1}{2i}\mathrm{rect}\left(\frac{1}{3}\right)\left[\delta(f-f_0)-\delta(f+f_0)\right]\\
    X_1(f)=\displaystyle\frac{1}{2i}\left[\delta(f-f_0)-\delta(f+f_0)\right]\\
    x_1(t)=\sin(2\pi f_0t)
\end{gathered}$$ Per la formula di duplicazione del seno: $$\begin{gathered}
    x(t)=\cos(2\pi f_0t)\sin(2\pi f_0t)=\displaystyle\frac{\sin(4\pi f_0t)}{2}
\end{gathered}$$

### Esercizio 39

Dato il segnale $x(t)$, calcolare il periodo, i coefficienti di Fourier, la potenza, e la sua trasformata: $$\begin{gathered}
    x(t)=2e^{2i\pi t/T_0}-e^{-i\pi t/2T_0}=2e^{2i\pi t/T_0}-e^{-2i\pi t/4T_0}
\end{gathered}$$ Il periodo di un segnale combinazione lineare di altri segnali è il minimo comune multiplo tra i periodi dei segnali considerati: $$\begin{gathered}
    T=4T_0
\end{gathered}$$ Si calcola la potenza del segnale: $$\begin{gathered}
    P_x=\displaystyle\frac{1}{4T_0}\int_{-2T_0}^{2T_0}\left|2e^{2i\pi t/T_0}-e^{-2i\pi t/4T_0}\right|^2\mathrm{d}t\\
    \displaystyle\frac{1}{4T_0}\int_{-2T_0}^{2T_0}\left(4+1+4\cos\left[\frac{2\pi t}{T_0}\left(1+\frac{1}{4}\right)\right]\right)\mathrm{d}t\\
    \displaystyle\frac{20T_0}{4T_0}+\frac{2T_0}{5\pi }\cancelto{0}{\left[\sin\left(\frac{5\pi t}{2T_0}\right)\right]_{-2T_0}^{2T_0}}\\
    P_x=5\tag{\stepcounter{equation}\theequation}
\end{gathered}$$ Si determinano i coefficienti di Fourier: $$\begin{gathered}
    c_k=\displaystyle\frac{1}{4T_0}\int_{-2T_0}^{2T_0}\left(2e^{2i\pi t/T_0}-e^{-2i\pi t/4T_0}\right)e^{-2i\pi kt/4T_0}\mathrm{d}t\\
    c_k=\displaystyle\frac{2}{4T_0}\int_{-2T_0}^{2T_0}e^{2i\pi t(1-k/4)/T_0}\mathrm{d}t+\frac{1}{4T_0}\int_{-2T_0}^{2T_0}2e^{-2i\pi t(1+k)/4T_0}\mathrm{d}t\\
    c_k=\begin{cases}
        0 &\forall k\neq4\lor-1\\
        \displaystyle\frac{\strut 1}{\strut 4T_0}& k=-1\\
        \displaystyle\frac{\strut 1}{\strut 2T_0}&k=4
    \end{cases}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$ Si ottiene lo stesso risultato, più velocemente, per confronto diretto. La sua trasformata si ottiene sia trasformando la sua serie di Fourier, sia attuando l’integrale di trasformazione: $$\begin{gathered}
    X(f)=\displaystyle\frac{1}{4T_0}\delta\left(f+\frac{1}{4T_0}\right)+\frac{1}{2T_0}\delta\left(f-\frac{1}{T_0}\right)
\end{gathered}$$

### Esercizio 40

Calcolare la trasformata del segnale $x$: $$\begin{gathered}
    x(t)=\cos\left[\displaystyle\frac{\pi(t-T)}{2T}\right]\cos\left(\frac{2\pi t}{T}\right)=\cos\left[\displaystyle\frac{2\pi(t-T)}{4T}\right]\cos\left(\frac{2\pi t}{T}\right)
\end{gathered}$$ Questo segnale ha periodo $4T$. Espandendo l’argomento del primo coseno si ottiene: $$\begin{gathered}
    x(t)=\displaystyle\cos\left[\frac{2\pi t}{4T}-\frac{\pi}{2}\right]\cos\left(\frac{2\pi t}{T}\right)\\
    \sin\left(\displaystyle\frac{2\pi t}{4T}\right)\cos\left(\frac{2\pi t}{T}\right)
\end{gathered}$$ Si rappresenta il segnale in forma esponenziale: $$\begin{gathered}
    x(t)=\displaystyle\frac{1}{2i}\left(e^{2i\pi t/4T}-e^{-2i\pi t/4T}\right)\cdot\displaystyle\frac{1}{2}\left(e^{2i\pi t/T}+e^{-2i\pi t/T}\right)\\
    \displaystyle\frac{1}{4i}\left[e^{\frac{2\pi t}{T}\left(\frac{1}{4}+1\right)}-e^{\frac{2\pi t}{T}\left(1-\frac{1}{4}\right)}+e^{\frac{2\pi t}{T}\left(\frac{1}{4}-1\right)}-e^{-\frac{2\pi t}{T}\left(1+\frac{1}{4}\right)}\right]\\
    \displaystyle\frac{1}{4i}\left[e^{\frac{2\pi t}{T}\frac{5}{4}}-e^{\frac{2\pi t}{T}\frac{3}{4}}+e^{-\frac{2\pi t}{T}\frac{3}{4}}-e^{-\frac{2\pi t}{T}\frac{5}{4}}\right]\\
    X(f)=\displaystyle\frac{1}{4i}\left[\delta\left(f+\frac{5}{4T}\right)-\delta\left(f+\frac{3}{4T}\right)+\delta\left(f-\frac{3}{4T}\right)-\delta\left(f-\frac{5}{4T}\right)\right]\\
    X(f)=\displaystyle\frac{1}{4i}\left[\delta\left(f+\frac{5}{4T}\right)-\delta\left(f-\frac{5}{4T}\right)\right]-\frac{1}{4i}\left[\delta\left(f+\frac{3}{4T}\right)-\delta\left(f-\frac{3}{4T}\right)\right]\tag{\stepcounter{equation}\theequation}
\end{gathered}$$ Per cui il segnale originale corrisponde ad una differenza di due seni, considerando operazioni trigonometriche del segnale originario. Alternativamente, per la proprietà della convoluzione, si può calcolare come convoluzione tra le due trasformate dei segnali moltiplicati: $$\begin{gathered}
    x(t)=\cos\left[\displaystyle\frac{\pi(t-T)}{2T}\right]\cos\left(\frac{2\pi t}{T}\right)=x_1(t)\cdot x_2(t)\\
    X(f)=X_1(f)*X_2(f)\\
    X_1(f)=\displaystyle\frac{1}{2}\left[\delta\left(f+\frac{1}{4T}\right)+\delta\left(f-\frac{1}{4T}\right)\right]e^{-2i\pi fT}\\
    \displaystyle\frac{1}{2}e^{-2i\pi/4}\delta\left(f+\frac{1}{4T}\right)+\frac{1}{2}e^{2i\pi /4}\delta\left(f-\frac{1}{4T}\right)\\
    \displaystyle-\frac{i}{2}\delta\left(f+\frac{1}{4T}\right)+\frac{i}{2}\delta\left(f-\frac{1}{4T}\right)\\
    X_2(f)=\displaystyle\frac{1}{2}\left[\delta\left(f+\frac{1}{T}\right)+\delta\left(f-\frac{1}{T}\right)\right]
\end{gathered}$$ Si attua quindi una convoluzione nel dominio della frequenza per ottenere la trasformata del segnale originale: $$\begin{gathered}
    X(f)=\displaystyle\frac{i}{2}\left[\delta\left(f-\frac{1}{4T}\right)-\delta\left(f+\frac{1}{4T}\right)\right]*\frac{1}{2}\left[\delta\left(f+\frac{1}{T}\right)+\delta\left(f-\frac{1}{T}\right)\right]\\
    X(f)=\displaystyle\frac{i}{4}\left[-\delta\left(f+\frac{5}{4T}\right)+\delta\left(f+\frac{3}{4T}\right)-\delta\left(f-\frac{3}{4T}\right)+\delta\left(f-\frac{5}{4T}\right)\right]\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 41

Dato un filtro di risposta impulsiva $h(t)$, calcolare la sua funzione di trasferimento, e la risposta ad un gradino: $$\begin{gathered}
    h(t)=\delta(t-2T)+\delta(t)-\delta(t-T)\\
    H(f)=e^{-4i\pi fT}+1-e^{-2i\pi fT}\tag{\stepcounter{equation}\theequation}\\
    h(t)*u(t)=\delta(t-2T)+\delta(t)-\delta(t-T)*u(t)=\delta(t-2T)u(t-2T)+\delta(t)u(t)-\delta(t-T)u(t-T)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

<div class="center">

</div>

### Esercizio 42

Calcolare l’uscita $Y(f)$ di un sistema di risposta impulsiva $h(t)$ con un’entrata $x(t)$: $$\begin{gathered}
    h(t)=\displaystyle\frac{1}{T}\mathrm{sinc}\left(\frac{t}{T}\right)\\
    x(t)=\cos(2\pi f_0t)
\end{gathered}$$ Per la proprietà di scala: $$\begin{gathered}
    H(f)=\mathrm{rect}(Tf)\\
    X(f)=\displaystyle\frac{1}{2}\delta(f-f_0)+\frac{1}{2}\delta(f+f_0)\\
    Y(f)=\frac{1}{2}\mathrm{rect}(Tf)(\delta(f-f_0)+\delta(f+f_0))\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

## Trasformata di Fourier Tempo Discreto

### Esercizio 43

Calcolare la trasformata della sequenza $x[n]$: $$\begin{gathered}
    x[n]=\left[\displaystyle\frac{\sin(2\pi f_cnT)}{\pi n}\right]^2=4f_c^2T^2\mathrm{sinc}^2(2f_cnT)
\end{gathered}$$ Questa sequenza si può considerare estratta dal segnale tempo continuo $x$: $$\begin{gathered}
    x(t)=4f_c^2T^2\mathrm{sinc}(2f_ct)\\
    X(f)=\displaystyle 2f_cT^2\mathrm{tri}\left(\frac{f}{2f_c}\right)
\end{gathered}$$

Per cui si esprime la trasformata della sequenza come: $$\begin{gathered}
    X_c(f)=\displaystyle\frac{1}{T}\sum_{n=-\infty}^{+\infty}X\left(f-\frac{n}{T}\right)=2f_cT\sum_{n=-\infty}^{+\infty}\mathrm{tri}\left(\frac{f-\frac{n}{T}}{2f_c}\right)
\end{gathered}$$ Se $T$ il passo di campionamento non è abbastanza grande, i triangoli si sovrappongono tra di loro.

### Esercizio 44

Calcolare la convoluzione $y$ tempo discreta tra $x$ e $h$, esponenziali unilateri: $$\begin{gathered}
    y[n]=x[n]*h[n]\\
    x[n]=a^nu[n]\\
    h[n]=b^nu[n]\\
    y[n]=\displaystyle\sum_{k=-\infty}^{+\infty}x[k]h[n-k]=\sum_{k=-\infty}^{+\infty}a^ku[k]b^{n-k}u[n-k]=\sum_{k=0}^na^kb^{n-k}\\
    \displaystyle b^n\sum_{k=0}^n\left(\frac{a}{b}\right)^k=b^n\frac{1-\left(\frac{a}{b}\right)^{n+1}}{1-\frac{a}{b}}\\
    y[n]=\displaystyle\frac{b^{n+1}-a^{n+1}}{b-a}u[n]\tag{\stepcounter{equation}\theequation}
\end{gathered}$$ Si può calcolare analogamente nel dominio della frequenza, poi attuando un antitrasformata: $$\begin{gathered}
    Y_c(f)=X_c(f)H_c(f)\\
    X_c(f)=\displaystyle\sum_{n=0}^{+\infty}a^ne^{-2i\pi nfT}=\sum_{n=0}^{+\infty}\left(ae^{-2i\pi fT}\right)^n=\frac{1}{1-ae^{-2i\pi fT}}\\
    H_c(f)=\displaystyle\frac{1}{1-be^{-2i\pi fT}}
\end{gathered}$$ Poiché le due sommatorie diventano delle serie geometriche. Si considera ora il loro prodotto: $$\begin{gathered}
    Y_c(f)=X_c(f)H_c(f)=\displaystyle\frac{1}{1-ae^{-2i\pi fT}}\frac{1}{1-be^{-2i\pi fT}}
\end{gathered}$$ Si può decomporre in fratti semplici come: $$\begin{gathered}
    Y_c(f)=\displaystyle\frac{A}{1-ae^{-2i\pi fT}}+\frac{B}{1-be^{-2i\pi fT}}\\
    \begin{cases}
        A+B=1\\
        Ab+Ba=0
    \end{cases}\to
    \begin{cases}
        A=1-B\\
        b-Bb+Ba=0
    \end{cases}\to\begin{cases}
        A=\displaystyle\frac{\strut a}{\strut a-b}\\
        B=\displaystyle\frac{\strut b}{\strut b-a}
    \end{cases}
\end{gathered}$$ Per cui il segnale convoluzione si esprime come: $$\begin{gathered}
    Y_c(f)=\displaystyle\frac{a}{a-b}\frac{1}{1-ae^{-2i\pi fT}}+\frac{b}{b-a}\frac{1}{1-be^{-2i\pi fT}}\\
    y[n]=\displaystyle\frac{a}{a-b}a^nu[n]+\displaystyle\frac{b}{b-a}b^nu[n]\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 45

Calcolare la trasformata di Fourier della sequenza $x[n]$: $$\begin{gathered}
    x[n]=\displaystyle\frac{\sin(\pi n/3)}{\pi n}\cos\left(\frac{2\pi n}{6}\right)
\end{gathered}$$ Si considera $T=1$, e si esprime il segnale da cui è stata campionata la sequenza: $$\begin{gathered}
    x(t)=\frac{1}{3}\mathrm{sinc}\left(\frac{t}{3}\right)\cos\left(\frac{2\pi t}{6}\right)
\end{gathered}$$ Si determina la trasformata di questo segnale tempo continuo: $$\begin{gathered}
    X(f)=\displaystyle\mathrm{rect}(3f)*\frac{1}{2}\left[\delta\left(f-\frac{1}{6}\right)+\delta\left(f+\frac{1}{6}\right)\right]\\
    X(f)=\displaystyle\frac{1}{2}\mathrm{rect}\left(3f-\frac{1}{2}\right)+\frac{1}{2}\mathrm{rect}\left(3f+\frac{1}{2}\right)\\
    X_c(f)=\displaystyle\frac{1}{T}\sum_{n=-\infty}^{+\infty}X\left(f-\frac{n}{T}\right)=\frac{1}{T}\sum_{n=-\infty}^{+\infty}\left[\frac{1}{2}\mathrm{rect}\left(3f-\frac{1}{2}-3n\right)+\frac{1}{2}\mathrm{rect}\left(3f+\frac{1}{2}-3n\right)\right]\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 46

Calcolare la trasformata di Fourier della sequenza $x[n]$: $$\begin{gathered}
    x[n]=\left[\displaystyle\frac{\sin(\pi n/3)}{\pi n}\right]^2=\frac{1}{9}\mathrm{sinc}^2\left(\frac{n}{3}\right)\\
    T=1\\
    x(t)=\displaystyle\frac{1}{9}\mathrm{sinc}^2\left(\frac{t}{3}\right)\\
    X(f)=\displaystyle \frac{1}{3}\mathrm{tri}(3f)\\
    X_c(f)=\displaystyle\frac{1}{3}\sum_{n=-\infty}^{+\infty}\mathrm{tri}(3f-n)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

## Campionamento

### Esercizio 47

Dato un segnale coseno di frequenza $f_0$ si determina la frequenza di Nyquist: $$\begin{gathered}
    x(t)=\cos(2\pi f_0t)\\
    X(f)=\displaystyle\frac{1}{2}\left[\delta(f-f_0)+\delta(f+f_0)\right]
\end{gathered}$$ Per cui la frequenza massima corrisponde a $f_0$, per cui la frequenza di Nyquist si ottiene come: $$\begin{gathered}
    f_c=2f_0
\end{gathered}$$ Il segnale campionato corrisponde a: $$\begin{gathered}
    x_c(t)=\displaystyle\sum_{n=-\infty}^{+\infty}x(nT)\delta(t-nT)=\sum_{n=-\infty}^{+\infty}\cos(\pi n)\delta\left(t-\frac{n}{2f_0}\right)
\end{gathered}$$ Ma utilizzando la frequenza di Nyquist come la frequenza di campionamento gli impulsi coincidono per $f=2f_0$, per cui questa sequenza non individua univocamente il segnale coseno, per cui è necessaria una frequenza di campionamento maggiore. Si considera allora: $$\begin{gathered}
    f_c=4f_0
\end{gathered}$$ Si suppone sia presente aliasing nel segnale campionato in frequenza. Per cui si ha una frequenza $f_c<2f_0$, e sono presenti degli impulsi in più nell’intervallo $[-f_0,f_0]$, corrispondenti alle repliche antecedenti e posteriori alla replica centrata in $f=0$. Lo spettro si sovrappone, quindi ricomponendo il segnale non si ricostruisce il segnale coseno originario. Il segnale ricostruito si ottiene antitrasformando il segnale ottenuto in frequenza: $$\begin{gathered}
    Y(f)=X_c(f)H(f)=\displaystyle\frac{1}{2}\left(f-\frac{1}{T}-f_0\right)+\frac{1}{2}\left(f-\frac{1}{T}+f_0\right)\\
    y(t)=\cos\left[2\pi \left(f_0-\frac{1}{T}\right)t\right]\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 48

Dato il segnale campionato $x(t)$, determinare la frequenza di Nyquist: $$\begin{gathered}
    x(t)=1+\left[\displaystyle\frac{\sin(20\pi t)}{\pi t}\right]^2=1+400\,\mathrm{sinc}^2\left(20\pi t\right)
\end{gathered}$$ Lo spettro del segnale corrisponde a: $$\begin{gathered}
    X(f)=\displaystyle \delta(f)+20\,\mathrm{tri}\left(\frac{f}{20}\right)
\end{gathered}$$ Per cui la frequenza minima di campionamento corrisponde a $f_c>40\,\mathrm{Hz}$, mentre il tempo di campionamento massimo corrisponde a: Non è presente aliasing quando la frequenza assume valori maggiori di: $$\begin{gathered}
    f>\displaystyle\frac{2}{\frac{1}{20}}=40\,\mathrm{Hz}
\end{gathered}$$ Il tempo di campionamento deve essere: $$\begin{gathered}
    T>\displaystyle\frac{2}{f_{\max}}=\frac{2}{40\,\mathrm{Hz}}=25\,\mathrm{ms}
\end{gathered}$$ Si suppone si stia campionando con un passo di campionamento doppio al valore massimo $\overline{T}=2T=50\,\mathrm{ms}$. Lo spettro del segnale campionato corrisponde a: $$\begin{gathered}
    X_c(f)=\displaystyle \frac{1}{\overline{T}}\sum_{n=-\infty}^{+\infty}X\left(f-\frac{n}{\overline{T}}\right)=20\sum_{n=-\infty}^{+\infty}\delta(f-20n)+20\,\mathrm{tri}\left(\frac{f-20n}{20}\right)
\end{gathered}$$ Se il tempo di campionamento fosse pari a $T=50\times10^{-3}\mathrm{s}$, i triangoli in frequenza sarebbero sfasati tra di loro di esattamente metà della loro base, per cui la somma di tutti i triangoli assume valore costante in frequenza. Lo spettro del segnale campionato diventa una costante sommata ad un treno di delta: $$\begin{gathered}
    X_c(f)=400+20\displaystyle\sum_{n=-\infty}^{+\infty}\delta\left(f-\frac{n}{20}\right)
\end{gathered}$$ Si effettua ora quest’analisi nel dominio del tempo: $$\begin{gathered}
    x_c(t)=x(t)\pi(t)=x(t)\displaystyle\sum_{n=-\infty}^{+\infty}x(nT)\delta(t-nT)=\sum_{n=-\infty}^{+\infty}\left[1+400\,\mathrm{sinc}^2\left(20t\right)\right]\delta(t-50\times10^{-3}n)\\
    x_c(t)=\displaystyle\sum_{n=-\infty}^{+\infty}\delta(t-50\times10^{-3}n)+400\sum_{n=-\infty}^{+\infty}\mathrm{sinc}^2(20t)\delta(t-50\times10^{-3}n)\\
    x_c(t)=\displaystyle\sum_{n=-\infty}^{+\infty}\delta(t-50\times10^{-3}n)+400\delta(t)
\end{gathered}$$ La sua trasformata corrisponde a: $$\begin{gathered}
    X_c(f)=\displaystyle\sum_{n=-\infty}^{+\infty}\delta\left(f-\frac{n}{50\times10^{-3}}\right)\frac{1}{50\times10^{-3}}+400
\end{gathered}$$

### Esercizio 49

Dato il segnale $x(t)$, si vuole calcolare il massimo intervallo di campionamento: $$\begin{gathered}
    x(t)=\cos^2\left(\displaystyle\frac{2\pi t}{T_0}\right)=\frac{1}{2}+\frac{1}{2}\cos\left(\frac{4\pi t}{T_0}\right)
\end{gathered}$$

Il periodo del segnale corrisponde a $T=\displaystyle\frac{T_0}{2}$. La sua trasformata equivale a: $$\begin{gathered}
    X(f)=\displaystyle\frac{1}{2}\delta(f)+\frac{1}{4}\delta\left(f+\frac{2}{T_0}\right)+\frac{1}{4}\delta\left(f-\frac{2}{T_0}\right)
\end{gathered}$$ Quindi la frequenza di Nyquist corrisponde a: $$\begin{gathered}
    f<2\frac{2}{T_0}=\frac{4}{T_0}
\end{gathered}$$ Per cui il passo di campionamento del segnale è: $$\begin{gathered}
    T>\displaystyle\frac{1}{f_c}=\frac{T_0}{4}
\end{gathered}$$

Si considera un passo di campionamento minore rispetto al valore necessario per non avere aliasing: $$\begin{gathered}
    T=\frac{4}{9}T_0
\end{gathered}$$ Si vuole calcolare lo spettro del segnale considerando questo tempo di campionamento: $$\begin{gathered}
    X_c(f)=\displaystyle\frac{9}{4T_0}\sum_{n=-\infty}^{+\infty}X\left(f-\frac{9n}{4T_0}\right)\\
    X_c(f)=\sum_{n=-\infty}^{+\infty}\left[\frac{9}{8T_0}\delta\left(f-\frac{9n}{4T_0}\right)+\frac{9}{16T_0}\delta\left(f+\frac{2}{T_0}-\frac{9n}{4T_0}\right)+\frac{9}{16T_0}\delta\left(f-\frac{2}{T_0}-\frac{9n}{4T_0}\right)\right]
\end{gathered}$$ $$\begin{gathered}
    X_c(f)=\displaystyle\sum_{n=-\infty}^{+\infty}\left[\frac{9}{8T_0}\delta\left(f-\frac{9n}{4T_0}\right)+\frac{9}{16T_0}\delta\left(f+\frac{8-9n}{4T_0}\right)+\frac{9}{16T_0}\delta\left(f-\frac{8+9n}{4T_0}\right)\right]
\end{gathered}$$

### Esercizio 50

Dato il segnale $x(t)$ calcolare il periodo di campionamento: $$\begin{gathered}
    x(t)=2f_0\mathrm{sinc}(2f_0t)\cos(6\pi f_0t)\\
    X(f)=\displaystyle2\,\mathrm{tri}\left(\frac{f}{f_0}\right)*\left[\frac{1}{2}\delta\left(f-3f_0\right)+\frac{1}{2}\delta(f+3f_0)\right]\\
    X(f)=\displaystyle\mathrm{tri}\left(\frac{f-3f_0}{f_0}\right)+\mathrm{tri}\left(\frac{f+3f_0}{f_0}\right)
\end{gathered}$$ La frequenza di Nyquist corrisponde a $6f_0$, per cui il tempo di campionamento corrisponde a $T=\displaystyle\frac{1}{6f_0}$. Si considera il segnale campionato con un passo di campionamento: $$\begin{gathered}
    T=\displaystyle\frac{1}{4f_0}
\end{gathered}$$

Per cui la trasformata del segnale campionato corrisponde a: $$\begin{gathered}
    X_c(f)=\displaystyle\sum_{n=-\infty}^{+\infty}\mathrm{tri}\left(\frac{f-(4n+3)f_0}{f_0}\right)+\mathrm{tri}\left(\frac{f-(4n-3)f_0}{f_0}\right)
\end{gathered}$$

Si ricostruisce il segnale inserendolo in un filtro ricostruttore DAC di funzione di trasferimento $H(f)$, filtro passa basso ideale, che si estende tra le frequenze $[-2f_0,+2f_0]$, si considera un tempo di campionamento pari ad $1$: $$\begin{gathered}
    H(f)=\displaystyle\mathrm{rect}\left(\frac{f}{2f_0}\right)\\
    X(f)=X_c(f)H(f)=\displaystyle\mathrm{tri}\left(\frac{f-f_0}{f_0}\right)+\mathrm{tri}\left(\frac{f+f_0}{f_0}\right)\\
    x(t)=2f_0\mathrm{sinc}^2(f_0t)\cos(2\pi f_0t)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 51

Dato un segnale che occupa una banda $[-6\,\mathrm{kHz}, 6\,\mathrm{kHz}]$. Il segnale viene campionato con passo $T$. Il segnale viene filtrato per essere ricostruito da un filtro la cui funzione di trasferimento assume una forma trapezoidale in frequenza: $$\begin{gathered}
    H(f)=\begin{cases}
        0 &f<-2K_f\land f\geq 2K_f\\
        A\left(2-\left|\displaystyle\frac{f}{K_f}\right|\right) &-2K_f\leq f<-K_f\land K_f\leq f<2K_f\\
        A & -K_f\leq f<K_f
    \end{cases}
\end{gathered}$$ Calcolare il valore massimo di $T$, $K_f$ e $A$ affinché il segnale ricostruito coincida con il segnale di partenza. Il parametro $A$ affinché si ritorni al segnale originario deve essere necessariamente: $$\begin{gathered}
    A=\displaystyle\frac{1}{T}
\end{gathered}$$ Il massimo passo di campionamento se fosse presente un filtro ideale sarebbe $T=1/12\times10^{-3}\,\mathrm{s}$, ma per ricostruire il segnale originale con un filtro trapezoidale, bisognerebbe assegnare al valore $K_f=6\,\mathrm{kHz}$. Ma in questo modo il filtro del DAC considera altre repliche, poiché la sua banda arriva fino ad un valore di $2K_f=12\,\mathrm{kHz}$. La frequenza di campionamento deve essere quindi: $$\begin{gathered}
    f\geq\displaystyle\frac{1}{T}+K_f=12+6=18\,\mathrm{kHz}
\end{gathered}$$ Il passo di campionamento è quindi: $$\begin{gathered}
    T=\displaystyle\frac{1}{f}=55\,\mu \mathrm{s}
\end{gathered}$$

### Esercizio 52

Un segnale viene campionato con frequenza di campionamento (di Nyquist) $f_c=100\,\mathrm{Hz}$, dando origine ai seguenti campioni: $$\begin{gathered}
    T_c=\displaystyle\frac{1}{100}\,s=10\,\mathrm{ms}\\
    f_{\max}=\frac{f_c}{2}=50\,\mathrm{Hz}\\
    x(nT)=\begin{cases}
        -1&n=-2,-1\\
        1&n=1,2\\
        0&\forall n\neq\pm1,\pm2
    \end{cases}
\end{gathered}$$ Il segnale viene ricostruito con un filtro ideale di funzione di trasferimento $H$: $$\begin{gathered}
    H(f)=T\,\mathrm{rect}(Tf)\to  h(t)=\mathrm{sinc}\left(\frac{t}{T}\right)
\end{gathered}$$ Calcolare il valore del segnale ricostruito al tempo $t=5\,\mathrm{ms}$. Il segnale campionato si esprime come: $$\begin{gathered}
    x_c(t)=\displaystyle\sum_{n=-\infty}^{+\infty}x(nT)\delta(t-nT)\\
    x(2T)\delta(t-2T)+x(T)\delta(t-T)+x(-T)\delta(t+T)+x(-2T)\delta(t+2T)\\
    x_c(t)=\delta(t-2T)+\delta(t-T)-\delta(t+T)-\delta(t+2T)
\end{gathered}$$ Si calcola l’uscita del filtro DAC: $$\begin{gathered}
    y(t)=x_c(t)*h(t)=\left[\delta(t-2T)+\delta(t-T)-\delta(t+T)-\delta(t+2T)\right]*\mathrm{sinc}\left(\displaystyle\frac{t}{T}\right)\\
    \displaystyle\mathrm{sinc}\left(\frac{t-2T}{T}\right)+\mathrm{sinc}\left(\frac{t-T}{T}\right)-\mathrm{sinc}\left(\frac{t+T}{T}\right)-\mathrm{sinc}\left(\frac{t+2T}{T}\right)\\
    y(5\,\mathrm{ms})=\displaystyle\mathrm{sinc}\left(\frac{5-20}{10}\right)+\mathrm{sinc}\left(\frac{5-10}{10}\right)-\mathrm{sinc}\left(\frac{5+10}{10}\right)-\mathrm{sinc}\left(\frac{5+20}{10}\right)\\
    \displaystyle\mathrm{sinc}\left(\frac{15}{10}\right)+\mathrm{sinc}\left(\frac{5}{10}\right)-\mathrm{sinc}\left(\frac{15}{10}\right)-\mathrm{sinc}\left(\frac{25}{10}\right)\\
    \displaystyle\mathrm{sinc}\left(\frac{1}{2}\right)-\mathrm{sinc}\left(\frac{5}{2}\right)=\frac{\sin\left(\frac{\pi}{2}\right)}{\frac{\pi}{2}}-\frac{\sin\left(\frac{5\pi}{2}\right)}{\frac{5\pi}{2}}=\frac{2}{\pi}-\frac{2}{5\pi}\\
    y(5\,\mathrm{ms})=\displaystyle\frac{8}{5\pi}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 53

Dato un segnale $x(t)$ di banda $[-W,W]$, campionato con un passo $T_c=\displaystyle\frac{1}{2W}$. Si considerano tre filtri, di risposta impulsiva: $$\begin{gathered}
    h_1(t)=\mathrm{sinc}\left(\displaystyle\frac{t}{T}\right)\to H_1(f)=T\mathrm{sinc}(Tf)\\
    h_2(t)=\mathrm{tri}\left(\displaystyle\frac{t}{T}\right)\\
    h_3(t)=\mathrm{tri}\left(\displaystyle\frac{t}{2T}\right)
\end{gathered}$$ Il segnale campionato si ottiene come: $$\begin{gathered}
    x_c(t)=\displaystyle\sum_{n=-\infty}^{+\infty}x(nT)\delta(t-nT)\\
    y_1(t)=x_c(t)*h_1(t)=\left[\displaystyle\sum_{n=-\infty}^{+\infty}x(nT)\delta(t-nT)\right]*\mathrm{sinc}\left(\frac{t}{T}\right)
\end{gathered}$$ Questo caso corrisponde al teorema del campionamento, poiché il passo di campionamento corrisponde esattamente al reciproco del doppio della frequenza massima del segnale: $$\begin{gathered}
    y_1(t)=\displaystyle\sum_{n=-\infty}^{+\infty}x(nT)\mathrm{sinc}\left(\frac{t-nT}{T}\right)=x(t)
\end{gathered}$$ Per cui il segnale ricostruito corrisponde esattamente al segnale originario.

Considerando il secondo filtro: $$\begin{gathered}
    y_2(t)=x_c(t)*h_2(t)=\displaystyle\sum_{n=-\infty}^{+\infty}x(nT)\mathrm{tri}\left(\frac{t-nT}{T}\right)
\end{gathered}$$ Questo filtro ricostruisce il segnale, ma presenta degli errori alle alte frequenze.

Considerando il terzo filtro: $$\begin{gathered}
    y_3(t)=x_c(t)*h_3(t)=\displaystyle\sum_{n=-\infty}^{+\infty}x(nT)\mathrm{tri}\left(\frac{t-nT}{2T}\right)
\end{gathered}$$ Questo filtro non ricostruisce a pieno il segnale.

### Esercizio 54

Dato il segnale $x(t)$: $$\begin{gathered}
    x(t)=\mathrm{tri}\left(\displaystyle\frac{t}{T}\right)-\mathrm{tri}\left(\frac{t+T}{T}\right)\\
    x(t)=\begin{cases}
        \displaystyle\frac{\strut t}{\strut T} -2T\leq t<-T\\
        1+\displaystyle\frac{\strut 3t}{\strut T} -T\leq t<0\\
        1-\displaystyle\frac{\strut t}{\strut T} 0\leq t<2T
    \end{cases}
\end{gathered}$$ Viene campionato con intervallo di campionamento $T_c=T$. Il segnale campionato viene ricostruito con un filtro passa basso ideale di ampiezza $1$ di banda $[-1/2T_c,1/2T_c]$. Calcolare il segnale ricostruito nel tempo continuo $y(t)$ e la sua trasformata $Y(f)$.

Sicuramente lo spettro del segnale originario non è limitato in banda, per cui la sua ricostruzione non potrà coincidere con il segnale originale. Il segnale è invece limitato nel tempo, per cui il suo campionamento produce una sequenza limitata, ovvero non nulla solo per un numero limitato di campioni: $$\begin{gathered}
    x_c(t)=\displaystyle\sum_{n=-\infty}^{+\infty}x(nT)\delta(t-nT)=x(-T)\delta(t+T)+x(0)\delta(t)=\delta(t)-\delta(t+T)
\end{gathered}$$ Il segnale ricostruito è quindi: $$\begin{gathered}
    y(t)=x_c(t)*h(t)=\left[\delta(t)-\delta(t+T)\right]*\frac{1}{T}\mathrm{sinc}\left(\frac{t}{T}\right)=\frac{1}{T}\mathrm{sinc}\left(\frac{t}{T}\right)-\frac{1}{T}\mathrm{sinc}\left(\frac{t+T}{T}\right)\\
    Y(f)=\mathrm{rect}(Tf)-\mathrm{rect}(Tf)e^{2i\pi fT}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 55

Dato il segnale $x(t)$, determinare il segnale campionato $x_c$ e la sua trasformata di Fourier $X_c$: $$\begin{gathered}
    x(t)=\mathrm{sinc}\left(\displaystyle\frac{t}{2T}\right)+\cos\left(\frac{2\pi t}{T}\right)
\end{gathered}$$ Il segnale viene campionato con un passo $\overline{T}$ pari a quattro volte il periodo di Nyquist $T_c$: $$\begin{gathered}
    \overline{T}=4T_c
\end{gathered}$$ Si considera la trasformata di Fourier del segnale $x$ per determinare la sua frequenza massima: $$\begin{gathered}
    X(f)=2T\,\mathrm{rect}(2Tf)+\displaystyle\frac{1}{2}\delta\left(f-\frac{1}{T}\right)+\frac{1}{2}\delta\left(f+\frac{1}{T}\right)
\end{gathered}$$ La banda del segnale è limitata nell’intervallo $[-1/T, 1/T]$, per cui la frequenza di Nyquist corrisponde a $2/T$: $$\begin{gathered}
    T_c=\displaystyle\frac{T}{2}\\
    \overline{T}=2T\\
    x_c(t)=\displaystyle\sum_{n=-\infty}^{+\infty}x(n\overline{T})\delta(t-n\overline{T})=\sum_{n=-\infty}^{+\infty}\left[\mathrm{sinc}\left(\frac{2nT}{2T}\right)+\cos\left(\frac{4\pi nT}{T}\right)\right]\delta(t-2nT)\\
    x_c(t)=\displaystyle\sum_{n=-\infty}^{+\infty}\left[\mathrm{sinc}(n)+\cancelto{1}{\cos(4\pi n)}\right]\delta(t-2nT)\\
    x(t)=\displaystyle\delta(t)+\sum_{n=-\infty}^{+\infty}\delta(t-2nT)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$ Si svolge ora la medesima analisi in frequenza: $$\begin{gathered}
    X_c(f)=\displaystyle\frac{1}{2T}\sum_{n=-\infty}^{+\infty}X\left(f-\frac{n}{2T}\right)\\
    \displaystyle\frac{1}{2T}\sum_{n=-\infty}^{+\infty}2T\,\mathrm{rect}\left[2T\left(f-\frac{n}{2T}\right)\right]+\frac{1}{4T}\sum_{n=-\infty}^{+\infty}\delta\left(f-\frac{1}{T}-\frac{n}{T}\right)+\frac{1}{4T}\sum_{n=-\infty}^{+\infty}\delta\left(f+\frac{1}{T}-\frac{n}{T}\right)\\
    X_c(t)1+\displaystyle\frac{1}{2T}\sum_{n=-\infty}^{+\infty}\delta\left(f-\frac{n}{2T}\right)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$ Si ottiene lo stesso risultato della trasformata del segnale campionato nel tempo.

### Esercizio 56

Dato il segnale $x(t)$: $$x(t)=2\mathrm{sinc}(4t)\cos(6\pi t)$$ Calcolare la frequenza minima di campionamento per cui non sia presente aliasing. In seguito campionato con il tempo di campionamento massimo $T_c$, determinare l’espressione analitica di $x'(t)$ e $X'(f)$ del segnale ricostruito da un filtro $H(f)$ passa basso ideale definito sull’intervallo $[-3,3]$. Si determina la frequenza massima del segnale: $$\begin{gathered}
    X(f)=\displaystyle\frac{1}{2}\mathrm{rect}\left(\frac{f}{4}\right)\left[\frac{1}{2}\delta(f-3)+\frac{1}{3}\delta(f+3)\right]\\
    X(f)=\mathrm{rect}\left(\displaystyle\frac{f-3}{4}\right)+\mathrm{rect}\left(\frac{f+3}{4}\right)
    f_{\max}=5\\
    f_c=2f_{\max}=10\to T_c=\displaystyle\frac{1}{10}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$ Si campiona con questo tempo $T_c$: $$\begin{gathered}
    x_c(t)=\displaystyle\sum_{n=-\infty}^{+\infty}x\left(\frac{n}{10}\right)\delta\left(t-\frac{n}{10}\right)\\
    X_c(f)=10\displaystyle\sum_{n=-\infty}^{+\infty}X(f-10n)
\end{gathered}$$ Si filtra tramite $H(f)$: $$\begin{gathered}
    H(f)=\displaystyle\mathrm{rect}\left(\frac{f}{6}\right)\\
    X'(f)=\left[10\displaystyle\sum_{n=-\infty}^{+\infty}X(f-10n)\right]\cdot\mathrm{rect}\left(\frac{f}{6}\right)\\
    \left[10\displaystyle\sum_{n=-\infty}^{+\infty}\mathrm{rect}\left(\displaystyle\frac{f-3-10n}{4}\right)+\mathrm{rect}\left(\frac{f+3-10n}{4}\right)\right]\cdot\mathrm{rect}\left(\frac{f}{6}\right)\\
    X'(f)=10\left[\displaystyle\mathrm{rect}\left(\frac{f-2}{2}\right)+\mathrm{rect}\left(\frac{f+2}{2}\right)\right]\tag{\stepcounter{equation}\theequation}
\end{gathered}$$ Antitrasformando si ottiene il segnale ricostruito nel tempo: $$x'(t)=40\mathrm{sinc}(2t)\cos(4\pi t)$$

### Esercizio 57

Il segnale $x(t)$ viene campionato con il massimo passo di campionamento tale da non provocare aliasing, producendo solamente due campioni diversi da zero: $$\begin{gathered}
    x[n]=
    \begin{cases}
        1 &n=\pm1\\
        0 &n\neq\pm1
    \end{cases}
\end{gathered}$$ Viene poi ricostruito da un filtro passa basso ideale sull’intervallo $[-1/2T,1/2T]$ e di ampiezza $T$: $$\begin{gathered}
    H(f)=\mathrm{rect}\displaystyle\left(Tf\right)
\end{gathered}$$ Determinare il segnale ricostruito $x'(t)$ e la sua trasformata $X'(f)$. Si determina il segnale campionato: $$\begin{gathered}
    x_c(t)=\displaystyle\sum_{n=-\infty}^{+\infty}x[n]\delta(t-nT)=x[1]\delta(t-T)+x[-1]\delta(t+T)\\
    X_c(f)=2\cos(2T\pi f)
\end{gathered}$$ Passando questo segnale attraverso il filtro si ottiene: $$\begin{gathered}
    X'(f)=X_c(f)\cdot H(f)=2\cos(2T\pi f)T\mathrm{rect}(Tf)
\end{gathered}$$ Antitrasformando si ottiene il segnale ricostruito nel tempo: $$x'(t)=\displaystyle\mathrm{sinc}\left(\frac{t-T}{T}\right)+\mathrm{sinc}\left(\frac{t+T}{T}\right)$$

# Fenomeni Aleatori

### Esercizio 58

Si consideri una sorgente $S$ ed un destinatario $D$ che possono trasmettere e ricevere solamente $1$ o $0$. La probabilità che si ricevi uno $0$, quando viene trasmesso uno $0$ è dell’$80\%$, mentre la probabilità che si ricevi un $1$ quando viene trasmesso uno $0$ è del $20\%$: $$\begin{gathered}
    \Pr(D=0|S=0)=0.8\\
    \Pr(D=1|S=1)=0.2
\end{gathered}$$ Mentre la probabilità di errore nella trasmissione di un $1$ è: $$\begin{gathered}
    \Pr(D=1|S=1)=0.7\\
    \Pr(D=0|S=1)=0.3
\end{gathered}$$ Per cui si conosco le probabilità di errore del canale di trasmissione. I simboli $0$ e $1$ non sono equiprobabili alla sorgente: $$\begin{gathered}
    \Pr(S=0)=0.6\\
    \Pr(S=1)=0.4
\end{gathered}$$

Si vuole calcolare la probabilità sia stato trasmesso un $1$ dalla sorgente quando viene misurato un $1$: $$\begin{gathered}
    \Pr(S=1|D=1)
\end{gathered}$$ Si esprime tramite il teorema di Bayes: $$\begin{gathered}
    \Pr(S=1|D=1)=\displaystyle\frac{\Pr(D=1|S=1)\Pr(S=1)}{\Pr(D=1)}=\frac{0.7\cdot0.4}{\Pr(D=1)}
\end{gathered}$$

Per determinare la probabilità che il ricevitore misuri $1$ si determina tramite il teorema delle proprietà totali: $$\begin{gathered}
    \Pr(D=1)=\Pr(D=1|S=1)\Pr(S=1)+\Pr(D=1|S=0)\Pr(S=0)=0.7\cdot0.4+0.3\cdot0.6
\end{gathered}$$ La probabilità che si misuri un $1$ quando viene effettivamente trasmesso un $1$ dalla sorgente risulta essere: $$\begin{gathered}
    \Pr(S=1|D=1)=\displaystyle\frac{0.7\cdot0.4}{0.7\cdot0.4+0.2\cdot0.6}=0.7
\end{gathered}$$

### Esercizio 59

Sia data la probabilità di una variabile aleatoria $X$: $$\begin{gathered}
    P_X(x)=\displaystyle\frac{e^{-\left(\frac{x}{\sqrt{2}{\sigma_x}}\right)^2}}{\sqrt{2\pi}\sigma_x}
\end{gathered}$$

Nota la sua relazione con un’altra variabile aleatoria $Y$: $$\begin{gathered}
    y=ax+b
\end{gathered}$$ Si calcola la densità di probabilità della variabile aleatoria $Y$: $$\begin{gathered}
    P_Y(y)=\displaystyle\frac{e^{-\left(\frac{y-b}{a}\right)^2\frac{1}{2\sigma_x^2}}}{\sqrt{2\pi}\sigma_x}\left|\frac{1}{a}\right|
\end{gathered}$$ Per cui se $X$ ha una statistica gaussiana, anche $Y$ ha una statistica gaussiana, ma non centrata nell’origine.

### Esercizio 60

La densità di probabilità della variabile aleatoria $X$ è uniformemente distribuita sull’intervallo $[2,3]$. Sia data una variabile aleatoria $Y$ legata da una relazione lineare: $$\begin{gathered}
    Y=aX+b
\end{gathered}$$ Determinare la distribuzione di probabilità della variabile aleatoria $Y$: $$\begin{gathered}
    P_X(x)=\mathrm{rect}\left(x-\displaystyle\frac{5}{2}\right)\\
    P_Y(y)=P_X(g(y))|g'(y)|=\displaystyle\frac{1}{|a|}\mathrm{rect}\left(\frac{2y-2b-5a}{2a}\right)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 61

Data la densità di probabilità gaussiana di una variabile aleatoria $X$, calcolare la densità di probabilità di una variabile $Y$ legata dalla relazione: $$\begin{gathered}
    y=x^3\\
    P_X(x)=\displaystyle\frac{e^{-\left(\frac{x}{\sqrt{2}{\sigma_x}}\right)^2}}{\sqrt{2\pi}\sigma_x}\\
    P_Y(y)=P_X(g(y))|g'(y)|=\displaystyle\frac{e^{-\left(\frac{\sqrt[3]{y}}{\sqrt{2}{\sigma_x}}\right)^2}}{\sqrt{2\pi}\sigma_x}\frac{1}{3\sqrt[3]{y^2}}
\end{gathered}$$

### Esercizio 62

Sia data una variabile aleatoria $X$ uniformemente distribuita sull’intervallo $[0,\pi]$ ed una variabile $Y$ dipendente dalla prima, tramite la seguente relazione: $$\begin{gathered}
    y=\cos(x)\\
    P_X(x)=\displaystyle\frac{1}{\pi}\mathrm{rect}\left(\frac{x-\pi/2}{\pi}\right)
\end{gathered}$$ Determinare la densità di probabilità della variabile $Y$ $P_Y(y)$. Noto l’andamento della funzione coseno, la densità di probabilità di $y$ è una funzione compresa nell’intervallo $[-1,+1]$. Si applica quindi la formula su questo intervallo: $$\begin{gathered}
    P_Y(y)=P_X(\arccos(y))\displaystyle\frac{\mathrm{d}}{\mathrm{d}y}\arccos(y)\\
    P_Y(y)=\displaystyle\frac{1}{\pi}\mathrm{rect}\left(\frac{\arccos(y)-\pi/2}{\pi}\right)\frac{1}{\sqrt{1-y^2}}\\
    P_Y(y)=\displaystyle\mathrm{rect}\left(\frac{y}{2}\right)\frac{1}{\sqrt{1-y^2}}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 63

Date due variabili aleatori legate dalla relazione $y=f(x)=\cos(x)$, con $X$ uniformemente distribuita sull’intervallo $[0,2\pi]$, calcolare la densità di probabilità della variabile $y$: $$\begin{gathered}
    P_X(x)=\displaystyle\frac{1}{2\pi}\mathrm{rect}\left(\frac{x-\pi}{2\pi}\right)
\end{gathered}$$ Poiché il coseno non è invertibile sull’intero intervallo dove è definita la variabile $X$, si divide in $[0,\pi]$ e $[\pi,2\pi]$, e si definiscono due funzioni aggiuntive che legano le variabili aleatorie nei due intervalli: $$\begin{gathered}
    f_1(x)=\cos(x)\\
    g_1(y)=\arccos(y)\\
    g_2(y)=-g_1(y)
\end{gathered}$$ La densità di probabilità sull’intervallo $[0,\pi]$, è già stata calcolata nell’esercizio precedente, in questo caso la variabile $X$ è distribuita uniformemente su un intervallo di ampiezza doppia, per cui si divide in un due funzioni centrate nei due intervalli: $$\begin{gathered}
    P_X(x)=\displaystyle\frac{1}{2\pi}\left[\mathrm{rect}\left(\frac{x-\pi/2}{\pi}\right)+\mathrm{rect}\left(\frac{x-3\pi/2}{\pi}\right)\right]\\
    P_{Y,1}(y)=\displaystyle\frac{1}{2\pi}\mathrm{rect}\left(\frac{\arccos(y)-\pi/2}{\pi}\right)\frac{1}{\sqrt{1-y^2}}\\
    P_{Y,2}(y)=\displaystyle\frac{1}{2\pi}\mathrm{rect}\left(\frac{-\arccos(y)-3\pi/2}{\pi}\right)\frac{1}{\sqrt{1-y^2}}\\
    P_{Y,1}(y)+P_{Y,2}(y)=\displaystyle\frac{1}{2\pi}\frac{1}{\sqrt{1-y^2}}\left[\mathrm{rect}\left(\frac{y}{2}\right)+\mathrm{rect}\left(\frac{y}{2}\right)\right]=\frac{1}{\pi}\mathrm{rect}\left(\displaystyle\frac{y}{2}\right)\frac{1}{\sqrt{1-y^2}}=P_Y(y)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$ Si vuole calcolare il valore atteso, può essere calcolato sul dominio $y$ o $x$: $$\begin{gathered}
    E[\cos (x)]=\displaystyle\int_{-\infty}^{+\infty}\cos (x)P_X(x)\mathrm{d}x =\int_0^{2\pi}\frac{1}{2\pi}\cos(x)\mathrm{d}x=0\\
    E[\cos(x)]=E[y]=\displaystyle\int_{-\infty}^{+\infty}yP_Y(y)\mathrm{d}y=\int_{-\infty}^{+\infty}y\,\mathrm{rect}\left(\frac{y}{2}\right)\frac{1}{\pi}\frac{1}{\sqrt{1-y^2}}\mathrm{d}y\\
    \displaystyle\int_{-1}^1\frac{y}{\sqrt{1-y^2}}\mathrm{d}y=0\\
    \mu_y=0\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 64

Calcolare la densità di probabilità della variabile aleatoria $Y$, nota la densità di una variabile indipendente $X$ e la loro relazione: $$\begin{gathered}
    y=f(x)=\begin{cases}
        x+2&-4\leq x<-1\\
        -x&-1\leq x<+1\\
        x-2&x\geq +1
    \end{cases}\\
    P_X(x)=\displaystyle\frac{1}{8}\mathrm{rect}\left(\frac{x}{8}\right)
\end{gathered}$$ Si studiano i tre casi separatamente, per cui si scompone la densità di probabilità della variabile $X$: $$\begin{gathered}
    P_{X,1}(x)=\displaystyle\frac{1}{8}\mathrm{rect}\left(\frac{x+5/2}{3}\right)\\
    P_{X,2}(x)=\displaystyle\frac{1}{8}\mathrm{rect}\left(\frac{x}{2}\right)\\
    P_{X,3}(x)=\displaystyle\frac{1}{8}\mathrm{rect}\left(\frac{x-5/2}{3}\right)
\end{gathered}$$ Si ottengono quindi le seguenti densità di probabilità per la variabile $Y$: $$\begin{gathered}
    P_{Y,1}(y)=\displaystyle\frac{1}{8}\mathrm{rect}\left(\frac{y-2+5/2}{3}\right)\\
    P_{Y,2}(y)=\displaystyle\frac{1}{8}\mathrm{rect}\left(\frac{-y}{3}\right)\\
    P_{Y,3}(y)=\displaystyle\frac{1}{8}\mathrm{rect}\left(\frac{y+2+5/2}{3}\right)
\end{gathered}$$ Per cui la densità della variabile $Y$ si ottiene dalla somma di quest’ultime: $$P_Y(y)=\displaystyle\frac{1}{8}\left(\mathrm{rect}\left(\frac{y-1/2}{3}\right)+\mathrm{rect}\left(\frac{y}{2}\right)+\mathrm{rect}\left(\frac{y+1/2}{3}\right)\right)$$

### Esercizio 65

Sia data la densità di probabilità $P_X(x)$ e la relazione con la variabile aleatoria $Y$, determinare la densità di probabilità di $Y$: $$\begin{gathered}
    P_X(x)=\displaystyle\frac{1}{2}\mathrm{rect}\left(\frac{x}{2}\right)\\
    y=f(x)=\begin{cases}
        -x&x<0\\
        x^2&x\geq 0
    \end{cases}
\end{gathered}$$ Si divide l’intervallo in $[-1/2,0]$ e $[0,1/2]$: $$\begin{gathered}
    P_X(x)=\displaystyle\frac{1}{2}\mathrm{rect}\left(x+\frac{1}{2}\right)+\frac{1}{2}\mathrm{rect}\left(x-\frac{1}{2}\right)\\
    P_{Y,1}(y)=\displaystyle\frac{1}{2}\mathrm{rect}\left(-y+\frac{1}{2}\right)\\
    P_{Y,2}(y)=\displaystyle\frac{1}{2}\mathrm{rect}\left(\sqrt{y}-\frac{1}{2}\right)\frac{1}{2\sqrt{y}}\\
    P_Y(y)=\displaystyle\frac{1}{2}\mathrm{rect}\left(y+\frac{1}{2}\right)+\frac{1}{4}\mathrm{rect}\left(y-\frac{1}{2}\right)\frac{1}{\sqrt{y}}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$ Si considera la seguente densità di probabilità per la variabile $X$: $$\begin{gathered}
    P_X(x)=\displaystyle\frac{1}{\sqrt{2\pi}\sigma_x}e^{-\left(\frac{x}{\sqrt2\sigma_x}\right)^2}\\
    P_Y(y)=\displaystyle\frac{1}{\sqrt{2\pi}\sigma_x}e^{-\left(\frac{y}{\sqrt2\sigma_x}\right)^2}u(y)+\frac{1}{2\sqrt{2\pi y} \sigma_x}e^{-\frac{y}{2\sigma_x^2}}u(y)\\
    P_Y(y)=\displaystyle\frac{1}{\sqrt{2\pi}\sigma_x}\left(e^{-\left(\frac{y}{\sqrt2\sigma_x}\right)^2}+\frac{1}{2\sqrt{y}}e^{-\frac{y}{2\sigma_x^2}}\right)u(y)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 66

Sia data una variabile aleatoria discreta $X$, la sua densità di probabilità e la relazione con la variabile aleatoria $Y$. Determinare la densità di probabilità di $Y$: $$\begin{gathered}
    P_X(x)=\displaystyle\frac{1}{4}\delta(x+1)+\frac{1}{2}\delta(x)+\frac{1}{4}\delta(x-1)\\
    y=x^2\\
    P_Y(y)=\displaystyle\frac{1}{4}\delta(y-1)+\frac{1}{2}\delta(y)+\frac{1}{4}\delta(y-1)=\frac{1}{2}\left[\delta(y)+\delta(y-1)\right]\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 67

Sia data la variabile aleatoria $X$ di statistica gaussiana centrata in $x=1$, e la relazione con la variabile aleatoria $Y$, tramite un rettificatore: $$\begin{gathered}
    P_X(x)=\displaystyle\frac{1}{\sqrt{2\pi}\sigma_x}e^{-\left(\frac{x-1}{\sigma_x}\right)^2}\\
    y=\begin{cases}
        -1&x< 1\\
        2&x\geq 1
    \end{cases}
\end{gathered}$$ Poiché la statistica di $X$ è centrata in $1$, la probabilità che sia maggiore o minore di $1$ è pari a $1/2$, per cui la densità di probabilità di $Y$ corrisponde a due impulsi: $$\begin{gathered}
    \displaystyle\int_{-\infty}^1P_X(x<1)\mathrm{d}x=\int_{1}^{+\infty}P(x>1)\mathrm{d}x=\frac{1}{2}\\
    P_Y(y)=\displaystyle\frac{1}{2}\delta(y-2)+\frac{1}{2}\delta(y+1)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 68

Sia data la distribuzione di probabilità della variabile $X$, e la funzione che la associa alla variabile aleatoria $Y$. Determinare la densità della probabilità $Y$: $$\begin{gathered}
    P_X(x)=\displaystyle\frac{1}{2\pi}\mathrm{rect}\left(\frac{x-\pi}{2\pi}\right)
    y=\begin{cases}
        \pi &x<\pi\\
        x &x\geq\pi
    \end{cases}
\end{gathered}$$ La variabile aleatoria $Y$ è una variabile mista: $$\begin{gathered}
    P_Y(y)=\displaystyle\int_0^{\pi}P_X(x\leq\pi)\mathrm{d}x\delta(y-\pi)+\int_{\pi}^{2\pi}P_X(x\geq\pi)\mathrm{d}x \frac{1}{2\pi}\mathrm{rect}\left(\frac{y-\pi-\pi/2}{\pi}\right)\\
    P_Y(y)=\displaystyle\frac{1}{2}\delta(y-\pi)+\frac{1}{4\pi}\mathrm{rect}\left(\frac{y-3\pi/2}{\pi}\right)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 69

Sia data la variabile aleatoria $X$ e la sua relazione con la variabile aleatoria $Y$, determinare la densità di probabilità di quest’ultima: $$\begin{gathered}
    P_X(x)=\frac{1}{4a}\mathrm{rect}\left(\frac{x}{4a}\right)
    y=\begin{cases}
        -a&x<-a\\
        x&-a\geq x<a\\
        a&x\geq a
    \end{cases}\\
    P_Y(y)=\displaystyle\int_{-2a}^{-a}\frac{1}{4a}\mathrm{d}x\,\delta(y+a)+\int_{-a}^a\frac{1}{4a}\mathrm{d}x\frac{1}{2a}\,\mathrm{rect}\left(\frac{y}{2a}\right)+\int_{a}^{2a}\frac{1}{4a}\mathrm{d}x\,\delta(y-a)\\
    P_Y(y)=\displaystyle\frac{1}{4}\left[\delta(y+a)+\delta(y-a)+\frac{1}{a}\mathrm{rect}\left(\frac{y}{2a}\right)\right]\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 70

Determinare il valore medio e deviazione standard della seguente densità di probabilità: $$\begin{gathered}
    P_x(x)=\displaystyle\frac{1}{2}\mathrm{rect}\left({t+\frac{3}{2}}\right)+\frac{1}{2}\left({t-\frac{3}{2}}\right)\\
    \mu_x=\displaystyle\int_{-\infty}^{+\infty}x\left[\frac{1}{2}\mathrm{rect}\left({t+\frac{3}{2}}\right)+\frac{1}{2}\left({t-\frac{3}{2}}\right)\right]\mathrm{d}x\\
    \displaystyle\frac{1}{2}\int_{-2}^{-1}x\mathrm{d}x+\frac{1}{2}\int_{1}^2x\mathrm{d}x=-\frac{1}{2}\int_1^2x\mathrm{d}x+\frac{1}{2}\int_1^2x\mathrm{d}x=0\\
    \mu_x=0\tag{\stepcounter{equation}\theequation}\\
    \sigma_x^2=\displaystyle\int_{-\infty}^{+\infty}x^2\left[\frac{1}{2}\mathrm{rect}\left({t+\frac{3}{2}}\right)+\frac{1}{2}\left({t-\frac{3}{2}}\right)\right]\mathrm{d}x\\
    \displaystyle\frac{1}{2}\int_{-2}^{-1}x^2\mathrm{d}x+\frac{1}{2}\int_1^2x^2\mathrm{d}x=\int_1^2x^2\mathrm{d}x\\
    \displaystyle\left[\frac{x^3}{3}\right]_1^2=\frac{8}{3}-\frac{1}{3}=\frac{7}{3}\\
    \sigma_x^2=\displaystyle\frac{7}{3}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 71

Date due variabili aleatorie indipendenti $X$ e $Y$ di statistica gaussiana, determinare la densità di probabilità della variabile dipendente $Z=X+Y$. Si può risolvere sia nel dominio di $z$ oppure in frequenza tramite la funzione caratteristica: $$\begin{gathered}
    P_X(x)=\displaystyle\frac{1}{\sqrt{2\pi}\sigma_x}e^{-\frac{(x-\mu_x)^2}{2\sigma_x^2}}\\
    P_Y(y)=\displaystyle\frac{1}{\sqrt{2\pi}\sigma_y}e^{-\frac{(y-\mu_y)^2}{2\sigma_y^2}}\\
    P_Z(z)=P_X(x)*P_Y(y)=\displaystyle\frac{1}{\sqrt{2\pi(\sigma_x^2+\sigma_y^2)}}e^{-\frac{z-\mu_x-\mu_y}{2(\sigma_x^2+\sigma_y^2)}}\\
    P_Z(z)=\displaystyle\frac{1}{\sqrt{2\pi}\sigma_y}e^{-\frac{z-\mu_z}{2\sigma_z^2}}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 72

Data la variabile aleatoria $Z$ data dalla combinazione lineare di due variabili aleatorie uniformemente distribuite sull’intervallo $[-1/2,1/2]$: $$\begin{gathered}
    z=ax+by+c
\end{gathered}$$ Per ritornare ad un caso noto si applicano le seguenti sostituzioni: $$\begin{gathered}
    x'=ax\\
    y'=by+c\\
    z=x'+y'
\end{gathered}$$ Si calcolano le densità di probabilità di queste nuove variabili aleatorie: $$\begin{gathered}
    P_{X'}(x')=\mathrm{rect}\displaystyle\left(\frac{x'}{a}\right)\left|\frac{1}{a}\right|\\
    P_{Y'}(y')=\mathrm{rect}\displaystyle\left(\frac{y'-c}{b}\right)\left|\frac{1}{b}\right|\\
    P_Z(z)=P_{X'}(x')*P_{Y'}(y')=\displaystyle\left|\frac{1}{ab}\right|\mathrm{rect}\left(\frac{x'}{a}\right)*\mathrm{rect}\left(\frac{y'-c}{b}\right)\\
    P_Z(z)=\begin{cases}
        0 &z<c-\displaystyle\frac{\strut a+b}{\strut 2} \land z\geq c-\frac{\strut a+b}{\strut 2}\\
        \displaystyle \left|\frac{\strut 1}{\strut ab}\right|\frac{\strut 1}{\strut a}\left(\frac{\strut a+b}{\strut 2}-|z-c|\right)&\displaystyle c-\frac{\strut a+b}{2}\leq z< c-\frac{\strut b-a}{\strut 2}\land c+\frac{\strut b-a}{\strut 2}\leq z<c+\frac{\strut a+b}{\strut 2}\\
        \displaystyle\left|\frac{\strut 1}{\strut ab}\right|&c-\displaystyle\frac{\strut b-a}{\strut 2}\leq z<c+\frac{\strut b-a}{\strut 2}
    \end{cases}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 73

Data la variabile aleatoria dipendente $Y$, combinazione lineare di due variabili aleatorie $X_1$ e $X_2$. Determinare date le densità di probabilità di queste ultime la densità di probabilità di $Y$: $$\begin{gathered}
    y=7x_1+x_2-3\\
    \Pr(x_1=-2)=0.6\\
    \Pr(x_1=2)=0.4\\
    \Pr(x_2=-1)=0.5\\
    \Pr(X_2=1)=0.5
\end{gathered}$$ Poiché sono possibili solo $4$ realizzazioni della variabile $Y$, è possibile creare una tabella caratterizzata dai quattro possibili valori:

<div class="center">

|                  | $x_1=-2$,$P=0.6$ | $x_1=2$,$P=0.4$ |
|:----------------:|:----------------:|:---------------:|
|                  |                  |                 |
| $x_2=-1$,$P=0.5$ |  $-18$,$P=0.3$   |  $10$,$P=0.2$   |
|                  |                  |                 |
| $x_2=1$,$P=0.5$  |  $-16$,$P=0.3$   |  $12$,$P=0.2$   |
|                  |                  |                 |

</div>

Si esprime quindi la densità di probabilità della variabile discreta $Y$: $$P_Y(y)=\displaystyle\frac{3}{10}\delta(y+18)+\frac{1}{5}\delta(y-10)+\frac{3}{10}\delta(y+16)+\frac{1}{5}\delta(y-12)$$

Si può ottenere lo stesso risultato lavorando con le densità discrete delle due variabili $X_1$ e $X_2$: $$\begin{gathered}
    P_{X_1}(x_1)=\displaystyle\frac{3}{5}\delta(x_1+2)+\frac{2}{5}\delta(x_1-2)\\
    P_{X_2}(x_2)=\displaystyle\frac{1}{2}\delta(x_2+1)+\frac{1}{2}\delta(x_2-1)
\end{gathered}$$ Si sostituiscono due variabili di appoggio: $$\begin{gathered}
    x_1'=7x_1\\
    x_2'=x_2-3\\
    P_{X_1'}(x_1')=\displaystyle\frac{1}{7}\left[\frac{3}{5}\delta(x_1'/7+2)+\frac{2}{5}\delta(x_1'/7-2)\right]=\frac{3}{5}\delta(x_1'+14)+\frac{2}{5}\delta(x_1'-14)\\
    P_{X_2'}(x_2')=\displaystyle\frac{1}{2}\delta(x_2'+4)+\frac{1}{2}\delta(x_2'+2)\\
    P_Y(y)=P_{X_1'}(x_1')*P_{X_2'}(x_2')=\left[\displaystyle\frac{3}{5}\delta(x_1'+14)+\frac{2}{5}\delta(x_1'-14)\right]*\left[\frac{1}{2}\delta(x_2'+4)+\frac{1}{2}\delta(x_2'+2)\right]\\
    P_Y(y)=\displaystyle\frac{3}{10}\delta(y+18)+\frac{1}{5}\delta(y-10)+\frac{3}{10}\delta(y+16)+\frac{1}{5}\delta(y-12)
\end{gathered}$$

### Esercizio 74

Dato il processo aleatorio $x(t)$ stazionario, avente densità di probabilità uniforme sull’intervallo $[-2,10]$, ed una covarianza: $$\begin{gathered}
    C_x(\tau)=A\mathrm{tri}\displaystyle\left(\frac{\tau}{2}\right)
\end{gathered}$$ Calcolare il valor medio e $A$: $$\begin{gathered}
    \mu_x=\displaystyle\int_{-\infty}^{+\infty}xP_X(x)\mathrm{d}x=\int_{-2}^{10}\frac{x}{12}\mathrm{d}x=4\\
    C_x(\tau)=E[(x(t+\tau)-\mu_x)(x(t)-\mu_x)]\\
    C_x(0)=E[(x(t)-\mu_x)^2]=\sigma_x^2\\
    \mu_x^{(2)}=\displaystyle\int_{-\infty}^{+\infty}xP_X(x)\mathrm{d}x=\int_{-2}^{10}\frac{x^2}{12}\mathrm{d}x=28\\
    \sigma_x^2=\mu_x^{(2)}-\mu_x^2=28-16=12\\
    C_x(0)=A=12\tag{\stepcounter{equation}\theequation}
\end{gathered}$$ Calcolare la funzione di autocorrelazione di $X$: $$\begin{gathered}
    R_x(\tau)=C_x(\tau)+\mu_x^2=12\mathrm{tri}\displaystyle\left(\frac{\tau}{2}\right)+16
\end{gathered}$$ Sia: $$\begin{gathered}
    y(t)=x(t)+x(t-1)
\end{gathered}$$ Determinare il valore medio e la funzione di autocorrelazione di $y(t)$: $$\begin{gathered}
    \mu_y=E[y(t)]=E[x(t)]+E[x(t-1)]=2\mu_x=8\tag{\stepcounter{equation}\theequation}\\
    R_y(\tau)=E[t(t+\tau)y(t)]=E[(x(t+\tau)+x(t+\tau-1))(x(t)+x(t-1))]\\
    E[x(t+\tau)x(t)]+E[x(t+\tau)x(t-1)]+E[x(t+\tau-1)x(t)]+E[x(t+\tau-1)x(t-1)]\\
    R_x(\tau)+R_X(\tau-1)+R_x(\tau+1)+R_x(\tau)=2R_X(\tau)+2R_x(\tau+1)\\
    R_y(\tau)=24\mathrm{tri}\displaystyle\left(\frac{\tau}{2}\right)+32+24\mathrm{tri}\left(\frac{\tau+1}{2}\right)+32\\
    R_y(\tau)=24\mathrm{tri}\displaystyle\left(\frac{\tau}{2}\right)+24\mathrm{tri}\left(\frac{\tau+1}{2}\right)+64\tag{\stepcounter{equation}\theequation}
\end{gathered}$$ Determinare la potenza di $Y$: $$P_y=R_y(0)=24+24\displaystyle\frac{1}{2}+64=100$$

### Esercizio 75

Date tre variabili aleatorie indipendenti tra di loro $A$, $B$ e $\theta$, determinare il valore medio e la densità spettrale di potenza del processo $x(t)$: $$\begin{gathered}
    x(t)=(A+2B)\cos(300\pi t+\theta)+n(t)
\end{gathered}$$ Le tre variabili aleatorie hanno distribuzione uniforme rispettivamente in $[-1,+1]$, $[-2,+2]$ e $[0,4\pi]$: $$\begin{gathered}
    P_A(a)=\displaystyle\frac{1}{2}\mathrm{rect}\left(\frac{a}{2}\right)\\
    P_B(b)=\displaystyle\frac{1}{4}\mathrm{rect}\left(\frac{b}{4}\right)\\
    P_\theta(\theta)=\displaystyle\frac{1}{4\pi}\mathrm{rect}\left(\frac{\theta-2\pi}{4\pi}\right)
\end{gathered}$$ Il rumore è un rumore bianco a valor medio nullo, è anch’esso indipendente dalle variabili aleatorie $A$, $B$ e $\theta$, ed ha una funzione di autocorrelazione: $$\begin{gathered}
    R_n(\tau)=10\delta(\tau)
\end{gathered}$$ Il rumore ha quindi potenza: $$\begin{gathered}
    P_n=R_n(0)=10
\end{gathered}$$

Si calcola il valore attesto tramite la definizione: $$\begin{gathered}
    \mu_x=E[x(t)]=E[(A+2B)\cos(300\pi t+\theta)+n(t)]
\end{gathered}$$ Poiché sono variabili indipendenti, si può usufruire della proprietà di linearità della funzione “expectation”: $$\begin{gathered}
    (E[A]+2E[B])E[\cos(300\pi t+\theta)]+\cancelto{0}{E[n(t)]}
\end{gathered}$$ Poiché le variabili $A$ e $B$ sono distribuite uniformemente su un intervallo centrato nell’origine, i loro valori attesi sono nulli, per cui: $$\begin{gathered}
    \mu_x=0\cdot E[\cos(300\pi t+\theta)]=0
\end{gathered}$$ Per calcolare la densità spettrale di potenza si calcola la funzione di autocorrelazione e si pone $\tau=0$: $$\begin{gathered}
    R_x(\tau)=E[x(t+\tau)x^*(t)]\\
    E\left[\left\{(A+2B)\cos[300\pi (t+\tau)+\theta]+n(t+\tau)\right\}\left\{(A+2B)\cos[300\pi t+\theta]+n(t)\right\}\right]\\
    E[(A+2B)^2\cos\{300\pi(t+\tau)+\theta\}\cos(300\pi t+\theta)]+E[(A+2B)\cos\{300\pi (t+\tau)+\theta\}n(t)]\\
    +E[(A+2B)\cos(300\pi t+\theta)n(t+\tau)]+E[n(t+\tau)n(t)]
\end{gathered}$$ Poiché sono indipendenti tra di loro, si possono calcolare i contributi di ciascuna variabile indipendentemente: $$\begin{gathered}
    E[(A+2B)^2]=E[A^2]+4E[B^2]+\cancelto{0}{2E[A]E[B]}=\displaystyle\int_{-1}^1\frac{a^2}{2}\mathrm{d}a+4\int_{-2}^{2}\frac{b^2}{4}\mathrm{d}b=\frac{1}{3}+4\frac{4}{3}=\frac{17}{3}\\
    E[\cos\{300\pi(t+\tau)+\theta\}\cos(300\pi t+\theta)]=\displaystyle\int_{0}^{4\pi}\frac{1}{4\pi}\cos[300\pi(t+\tau)+\theta]\cos(300\pi t+\theta)\mathrm{d}\theta\\
    \displaystyle\frac{1}{8\pi}\cancelto{0}{\int_{0}^{4\pi}\cos[300\pi(2t+\tau)-2\theta]\mathrm{d}\theta}+\frac{1}{8\pi}\int_0^{4\pi}\cos(300\pi \tau)\mathrm{d}\theta=\frac{1}{2}\cos(300\pi\tau)\\
    E[(A+2B)^2\cos[300\pi(t+\tau)+\theta]\cos(300\pi t+\theta)]=\displaystyle\frac{17}{3}\frac{1}{2}\cos(300\pi\tau)=\frac{17}{6}\cos(300\pi\tau)\\
    E[n(t)]=E[n(t+\tau)]=0\\
    E[(A+2B)\cos\{300\pi (t+\tau)+\theta\}n(t)]=E[(A+2B)\cos(300\pi t+\theta)n(t+\tau)]=0\\
    E[n(t+\tau)n(t)]=R_n(\tau)=10\delta(\tau)\\
\end{gathered}$$ Per cui la funzione di autocorrelazione del processo $x(t)$ risulta essere: $$R_x(\tau)=\displaystyle\frac{17}{6}\cos(300\pi\tau)+10\delta(\tau)$$ Si applica quindi la trasformata di Fourier per ottenere la densità spettrale di potenza: $$G_x(f)=\displaystyle\frac{17}{12}\left[\delta(f-150)+\delta(f+150)\right]+10$$

### Esercizio 76

Dato il segnale stocastico $x(t)$, sia $y(t)$ il segnale definito dalla seguente espressione: $$\begin{gathered}
    y(t)=\displaystyle\int_{t-T}^{t+T}x(t')\mathrm{d}t'
\end{gathered}$$ Calcolare la densità spettrale di potenza di $y(t)$ in funzione di $x(t)$, e la potenza di $y(t)$. Il segnale $y(t)$ può essere espresso come un integrale su $[-\infty,+\infty]$, moltiplicato per una finestra: $$\begin{gathered}
    y(t)=\displaystyle\int_{-\infty}^{+\infty}x(t')\mathrm{rect}\left(\frac{t'-t}{2T}\right)\mathrm{d}t'=x(t)*\mathrm{rect}\left(\frac{t}{2T}\right)
\end{gathered}$$ Per cui la finestra rappresenta la risposta impulsiva $h(t)$ di un filtro, per cui la densità spettrale di potenza dell’uscita di un filtro si ottiene come: $$\begin{gathered}
    G_y(f)=|H(f)|^2G_X(f)=4T^2\mathrm{sinc}^2(2Tf)G_x(f)
\end{gathered}$$ Calcolare la potenza del segnale $y(t)$, nel caso in cui $x(t)$ sia un segnale bianco e densità spettrale di potenza: $$\begin{gathered}
    G_x(f)=\displaystyle\frac{N_0}{2}
\end{gathered}$$ Si calcola la potenza integrando la densità spettrale di $y$, oppure si calcola la funzione di autocorrelazione di $y$ in $\tau=0$: $$\begin{gathered}
    R_y(\tau)=\mathscr{F}^{-1}\left\{4T^2\mathrm{sinc}^2(2Tf)\displaystyle\frac{N_0}{2}\right\}=2T\mathrm{tri}\left(\frac{\tau}{2T}\right)\frac{N_0}{2}
\end{gathered}$$ La potenza è quindi: $$R_y(0)=N_0T=P_y$$

### Esercizio 77

Dato un processo $y(t)$: $$\begin{gathered}
    y(t)=4x(t-3)+4x(t+3)
\end{gathered}$$ Dove $x(t)$ è un processo stazionario a valor medio nullo, e di funzione di autocorrelazione: $$\begin{gathered}
    R_x(\tau)=3e^{-|\tau|}
\end{gathered}$$ Calcolare la densità spettrale di potenza di $y(t)$, il suo valore atteso, la sua funzione di autocorrelazione e la sua potenza. Si calcola il valore atteso: $$\begin{gathered}
    \mu_y=E[y(t)]=E[4x(t-3)+4x(t+3)]=4E[x(t-3)]+4E[x(t+3)]=0
\end{gathered}$$ Si calcola ora la funzione di autocorrelazione: $$\begin{gathered}
    R_y(\tau)=E[y(t+\tau)y^*(t)]=E[\{4x(t+\tau-3)+4x(t+\tau+3)\}\{4x(t-3)+4x(+3)\}]\\
    16E[x(t+\tau-3)x(t-3)]+16E[x(t+\tau-3)x(t+3)]\\
    +16E[x(t+\tau+3)x(t-3)]+16E[x(t+\tau+3)x(t+3)]\\
    16R_x(\tau-6)+16R_x(\tau)+16R_x(\tau)+16R_X(\tau+6)\\
    R_y(\tau)=16R_x(\tau-6)+32R_x(\tau)+16R_x(\tau+6)\\
    R_y(\tau)=16\left(3e^{-|\tau-6|}+6e^{-|\tau|}+3e^{-|\tau+6|}\right)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$ Si calcola ora la potenza: $$P_y=R_y(0)=16(3e^{-6}+6+3e^{-6})=96+96e^{-6}$$ Si calcola la densità spettrale di potenza come il transito attraverso un filtro, poiché il segnale $y(t)$ può essere espresso come: $$\begin{gathered}
    y(t)=x(t)*[4\delta(t-3)+4\delta(t+3)]\\
    h(t)=4\delta(t-3)+4\delta(t+3)\\
    H(f)=\displaystyle8\cos(6\pi f)\\
    G_x(f)=\mathscr{F}\left\{3e^{-|\tau|}\right\}=\displaystyle\frac{3}{1+2i\pi f}+\frac{3}{1-2i\pi f}=\frac{6}{1+4\pi f}\\
    G_y(f)=64\cos^2(6\pi f)\displaystyle\frac{6}{1+4\pi f}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 78

Dato un processo $x(t)$ stazionario, avente potenza $P_X=19$ e covarianza $C_X(\tau)=3\mathrm{tri}(\tau)$, determinare il valor medio e la varianza: $$\begin{gathered}
    C_x(0)=E[(x(t)-\mu_x)^2]=\sigma_x^2=3\tag{\stepcounter{equation}\theequation}\\
    R_x(0)=E[x^2(t)]=P_X=\mu_x^{(2)}=19\\
    \mu_x=\sqrt{\sigma_x^2-\mu_x^{(2)}}=\sqrt{16}=4\tag{\stepcounter{equation}\theequation}
\end{gathered}$$ Si suppone il segnale attraversa un filtro di risposta impulsiva $h(t)=\mathrm{rect}(t/3)$, calcola il valore medio dell’uscita $y(t)$: $$\begin{gathered}
    \mu_y=E[y(t)]=E[x(t)*h(t)]=E[x(t)]*h(t)=\displaystyle\int_{-\infty}^{+\infty}\mu_x\mathrm{rect}\left(\frac{t}{3}\right)\mathrm{d}t=4\int_{-3}^3\mathrm{d}t=24
\end{gathered}$$

### Esercizio 79

Dato un processo $x(t)$ stazionario, di valore medio $\mu_x=-3$, potenza $P_X=12$ e coefficiente di correlazione $\rho_X(\tau)=\mathrm{sinc}(\tau/4)$, calcolare la densità spettrale di potenza: $$\begin{gathered}
    \sigma_x^2=P_X-\mu_X^2=12-9=3\\
    C_x(\tau)=\rho_x(\tau)\sigma_x^2=3\mathrm{sinc}\displaystyle\left(\frac{\tau}{4}\right)\\
    R_x(\tau)=C_x(\tau)+\mu_x^2=3\mathrm{sinc}\displaystyle\left(\frac{\tau}{4}\right)+9\\
    G_x(f)=\mathscr{F}\{R_X(\tau)\}=12\mathrm{rect}(4f)+9\delta(f)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$ Questo processo viene filtrato con un filtro avente una funzione di trasferimento $H(f)=\cos(4\pi f)$, calcolare la potenza di $y(t)$: $$\begin{gathered}
    G_y(f)=|H(f)|^2G_x(f)=\cos^2(4\pi f)\left[12\mathrm{rect}(4f)+9\delta(f)\right]\\
    P_y=\displaystyle\int_{-\infty}^{+\infty}G_y(f)\mathrm{d}f=12\int_{-1/8}^{1/8}\cos^2(4\pi f)\mathrm{d}f+9=6\cancelto{0}{\int_{-1/8}^{1/8}\cos(8\pi f)\mathrm{d}f}+6\int_{-1/8}^{1/8}\mathrm{d}f+9\\
    \displaystyle6\frac{2}{8}+9\\
    P_y=\displaystyle\frac{21}{2}\tag{\stepcounter{equation}\theequation}
\end{gathered}$$ Sia il processo $z(t)$: $$\begin{gathered}
    z(t)=x(t)+x(t-6)
\end{gathered}$$ Determinare il valore medio, la varianza e la funzione di autocorrelazione di $z(t)$: $$\begin{gathered}
    \mu_z=E[z(t)]=E[x(t)+x(t-6)]=2\mu_x=-6\tag{\stepcounter{equation}\theequation}\\
    R_z(\tau)=E[z(t+\tau)z(t)]=E[x(t+\tau)x(t)]+E[x(t+\tau-6)x(t)]+E[x(t+\tau)x(t-6)]\\
    +E[x(t+\tau-6)x(t-6)]=R_x(\tau)+R_x(\tau-6)+R_x(\tau+6)+R_X(\tau)\\
    2R_x(\tau)+2R_x(\tau-6)+R_x(\tau-6)\\
    6\mathrm{sinc}\displaystyle\left(\frac{\tau}{4}\right)+18+3\mathrm{sinc}\left(\frac{\tau-6}{4}\right)+9+3\mathrm{sinc}\left(\frac{\tau+6}{4}\right)+9\\
    R_z(\tau)=6\mathrm{sinc}\left(\displaystyle\frac{\tau}{4}\right)+6\sin\left(\frac{\tau+6}{4}\right)+36\tag{\stepcounter{equation}\theequation}\\
    \sigma_z^2=P_z-\mu_z^2=R_z(0)-36=42+6\mathrm{sinc}\displaystyle\left(\frac{3}{2}\right)-36=6\left[1+\mathrm{sinc}\left(\frac{3}{2}\right)\right]\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 80

Dato un processo $x(t)=A+n(t)$, il rumore è bianco, ha varianza $\sigma_n^2$ nota e valor medio nullo $\mu_n=0$, calcolare la potenza del processo $x$: $$\begin{gathered}
    P_x=E[x^2(t)]=E[A^2]+2A\cancelto{0}{E[n(t)]}+E[n^2(t)]=A^2+\sigma_n^2
\end{gathered}$$ Il segnale viene filtrato in un filtro istantaneo: $$\begin{gathered}
    y(t)=x(t)+x(t-1)
\end{gathered}$$ Calcolare la potenza del segnale in uscita dal filtro: $$\begin{gathered}
    P_y=E[y^2(t)]=E[(x(t)+x(t-1))^2]=E[x^2(t)]+2E[x(t)x(t-1)]+E[x^2(t-1)]\\
    P_x+2R_x(1)+P_x=2A^2+2\sigma_n^2+2R_x(1)\\
    R_x(\tau)=E[(A+n(t+\tau))(A+n(t))]=A^2+A\cancelto{0}{E[n(t)]}+A\cancelto{0}{E[n(t+\tau)]}+R_n(\tau)=A^2+\sigma_n^2\delta(\tau)\\
    P_y=2A^2+\sigma_n^2+2A^2+2\sigma_n^2\cancelto{0}{\delta(1)}\\
    P_y=4A^2+2\sigma_n^2\tag{\stepcounter{equation}\theequation}
\end{gathered}$$

### Esercizio 81

Dati due processi aleatori $x(t)$ e $y(t)$ statisticamente indipendenti, bianchi nella banda $[-W,W]$ con densità di probabilità uniforme nell’intervallo $[-A,A]$. Calcolare il valore medio $\mu_z$, la potenza $P_z$, la correlazione $R_z(\tau)$, la densità spettrale di potenza $G_z(f)$ e la densità di probabilità $P_z(z)$ del processo $z(t)$: $$\begin{gathered}
    z(t)=x(t)+y(t)
\end{gathered}$$ Si calcola il valore medio, la potenza, la densità spettrale di potenza e la correlazione del processo $x(t)$: $$\begin{gathered}
    P_X(x)=\displaystyle\frac{1}{2A}\mathrm{rect}\left(\frac{x}{2A}\right)\\
    \mu_x=\displaystyle\int_{-\infty}^{+\infty}xP_X(x)\mathrm{d}x=\frac{1}{2A}\int_{-A}^Ax\mathrm{d}x=0\\
    P_x=\displaystyle\int_{-\infty}^{+\infty}x^2P_X(x)\mathrm{d}x=\frac{1}{2A}\int_{-A}^Ax^2\mathrm{d}x=\frac{A^2}{3}\\
    G_x(f)=\displaystyle\frac{P_x}{2W}\mathrm{rect}\left(\frac{f}{2W}\right)=\frac{A^2}{6W}\mathrm{rect}\left(\frac{f}{2W}\right)\\
    R_x(\tau)=\displaystyle\frac{A^2}{3}\mathrm{sinc}(2W\tau)
\end{gathered}$$ Poiché il processo $y(t)$ è definito analogamente ad $x(t)$, i suoi parametri caratteristici sono anch’essi analoghi: $$\begin{gathered}
    P_Y(f)=\displaystyle\frac{1}{2A}\mathrm{rect}\left(\frac{y}{2A}\right)\\
    \mu_y=0\\
    P_y=\displaystyle\frac{A^2}{3}\\
    G_y(f)=\displaystyle\frac{A^2}{6W}\mathrm{rect}\left(\frac{f}{2W}\right)\\
    R_y(\tau)=\displaystyle\frac{A^2}{3}\mathrm{sinc}(2W\tau)
\end{gathered}$$ Si calcola ora la densità di probabilità del processo $z(t)$, ed il suo valore medio: $$\begin{gathered}
    P_Z(z)=P_X(x)*P_Y(y)=\frac{1}{4A^2}\left[\mathrm{rect}\left(\frac{z}{2A}\right)*\mathrm{rect}\left(\frac{z}{2A}\right)\right]\\
    P_Z(z)=\displaystyle\frac{1}{4A^2}\mathrm{tri}\left(\frac{z}{2A}\right)\tag{\stepcounter{equation}\theequation}
\end{gathered}$$ Poiché il triangolo è simmetrico, e centrato in $z=0$, il valore medio è nullo: $$\mu_z=0$$ Si calcola la potenza e la correlazione di $z(t)$: $$\begin{gathered}
    P_z=E[z^2(t)]=E[(x(t)+y(t))^2]=P_x+P_y+2\mu_x\mu_y=\displaystyle\frac{2A^2}{3}\\
    R_z(\tau)=E[z(t+\tau)z(t)]=R_x(\tau)+R_y(\tau)+2\mu_x\mu_y=\displaystyle\frac{2A^2}{3}\mathrm{sinc}(2W\tau)
\end{gathered}$$ Si calcola la densità spettrale del processo $z(t)$: $$G_z(f)=\displaystyle\frac{2A^3}{6W}\mathrm{rect}\left(\frac{f}{2W}\right)$$

### Esercizio 82

Dato il processo $y(t)$: $$\begin{gathered}
    y(t)=x(t-T)+x(t+T)
\end{gathered}$$ Dove $x(t)$ è un processo armonico: $$\begin{gathered}
    x(t)=\displaystyle\cos\left(2\pi f_0t+\varphi\right)\\
    P_{\Phi}(\varphi)=\displaystyle\frac{1}{2\pi}\mathrm{rect}\left(\frac{\varphi-\pi}{2\pi}\right)
\end{gathered}$$ Calcolare il valore medio $\mu_y$ la potenza $P_y$, la funzione correlazione a la densità spettrale di potenza $G_y(f)$ del processo $y(t)$. Si considera il processo $y(t)$ l’uscita di un filtro di risposta impulsiva $h(t)$: $$\begin{gathered}
    y(t)=x(t)[\delta(t-T)+\delta(t+T)]\\
    h(t)=\delta(t-T)+\delta(t+T)\\
    H(f)=2\cos\left(2\pi fT\right)
\end{gathered}$$ Si calcola il valore medio del processo $x(t)$: $$\begin{gathered}
    \mu_x=E[\cos(2\pi f_0t+\varphi)]=0
\end{gathered}$$ Si calcola ora il valore medio del processo $y(t)$: $$\begin{gathered}
    \mu_y=E[y(t)]=E[x(t-T)]+E[x(t+T)]=2\mu_x
\end{gathered}$$ Si considera la correlazione e la densità spettrale di potenza del processo armonico $x(t)$: $$\begin{gathered}
    R_x(\tau)=\displaystyle\frac{1}{2}\cos(2\pi f_0\tau)\\
    G_x(f)=\displaystyle\frac{1}{4}\left[\delta(f-f_0)+\delta(f+f_0)\right]
\end{gathered}$$ Per le formule di passaggio attraverso un filtro si calcola la correlazione e la densità spettrale di energia del processo $y(t)$: $$\begin{gathered}
    G_y(f)=G_x(f)|H(f)|^2=\displaystyle\frac{1}{4}\left[\delta(f-f_0)+\delta(f+f_0)\right]\cdot4\cos^2(2\pi fT)\\
    \cos^2(2\pi f_0T)\delta(f-f_0)+\cos^2(-2\pi f_0T)\delta(f+f_0)\\
    G_y(f)=\cos^2(2\pi f_0T)[\delta(f-f_0)+\delta(f+f_0)]\tag{\stepcounter{equation}\theequation}
\end{gathered}$$ Antitrasformando la densità spettrale di energia si ottiene la funzione di autocorrelazione del processo $y(t)$: $$R_y(\tau)=2\cos^2(2\pi f_0T)\cos(2\pi f_0\tau)$$ Si determina la potenza, calcolando la funzione di autocorrelazione in $\tau=0$: $$P_y=R_y(0)=2\cos^2(2\pi f_0T)$$
