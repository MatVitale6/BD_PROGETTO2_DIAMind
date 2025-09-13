---
author:
- "*Giacomo Sturm*"
date:
- 
- |
  *Dipartimento di Ingegneria Civile, Informatica e delle Tecnologie Aeronautiche  
  Università degli Studi “Roma Tre"*
title: |
  **Fondamenti di Telecomunicazioni**  
  Formulario di Fondamenti di Telecomunicazioni  
  *Anno Accademico: 2023/24*
---

\providecommand{\labelText}[2]{#1}

# Analisi nel Tempo

## Energia e Potenza

Dato un segnale tempo continuo $x(t)$, o una sequenza $x[n]$, la sua energia e potenza si ottengono come: $$\begin{aligned}
    &E_x=\displaystyle\int_{-\infty}^{+\infty}|x(t)|^2\mathrm{d}t=\displaystyle\int_{-\infty}^{+\infty}|X(f)|^2\mathrm{d}f=R_{xx}(0)&E_x=\displaystyle\sum_{n=-\infty}^{+\infty}|x[n]|^2=T\int_{-1/2T}^{1/2T}|X(f)|^2\mathrm{d}f=R_{xx}[0]\\
    &P_x=\lim_{T\to+\infty}\displaystyle\frac{1}{T}\int_{-T/2}^{T/2}|x(t)|^2\mathrm{d}t&P_x=\displaystyle\lim_{N\to+\infty}\frac{1}{2N+1}\sum_{n=-N}^N|x[n]|^2
\end{aligned}$$ Se il segnale $x(t)$ è periodico di periodo $T$ o la sequenza $x[n]$ è periodica di periodo $M$, la loro potenza si calcola come: $$\begin{aligned}
    &P_x=\displaystyle\frac{1}{T}\int_{-T/2}^{T/2}|x(t)|^2\mathrm{d}t=\frac{1}{T}\displaystyle\sum_{n=-\infty}^{+\infty}|c_n|^2&P_x=\displaystyle\frac{1}{M}\sum_{n=0}^{M-1}|x[n]|^2
\end{aligned}$$

## Proprietà della Delta di Dirac

La delta ha area unitaria: $$\begin{aligned}
    &\displaystyle\int_{-\infty}^{+\infty}\delta(t)\mathrm{d}t=1&\displaystyle\sum_{n=-\infty}^{+\infty}\delta[n]=1
\end{aligned}$$ Proprietà del Campionamento: $$\begin{aligned}
    &x(t)\cdot\delta(t-\tau)=x(\tau)\cdot\delta(t-\tau)&x[n]\cdot\delta[n-m]=x[m]\cdot\delta[n-m]\\
    &\displaystyle\int_{-\infty}^{+\infty}x(t)\cdot\delta(t-\tau)\mathrm{d}t=x(\tau)&\displaystyle\sum_{n=-\infty}^{+\infty}x[n]\cdot\delta[n-m]=x[m]
\end{aligned}$$ Convoluzione per una Delta: $$\begin{aligned}
    &x(t)*\delta(t)=x(t)
    &x[n]*\delta[n]=x[n]\\
    &u(t-t')=\displaystyle\int_{-\infty}^{t-t'}\delta(\tau)\mathrm{d}\tau
    &u[n-m]=\displaystyle\sum_{k=-\infty}^{n-m}\delta[k+1]\\
    &\delta(t)=\delta(-t)
    &\delta[n]=\delta[-n]
\end{aligned}$$ Proprietà di Scala: $$\begin{aligned}
    &\delta(at)=\displaystyle\frac{1}{a}\delta(t)
    &\delta[an]=\displaystyle\frac{1}{a}\delta[n]
\end{aligned}$$

## Convoluzione

Definizione: $$\begin{aligned}
    &x(t)*y(t)=\displaystyle\int_{-\infty}^{+\infty}x(\tau)y(t-\tau)\mathrm{d}\tau
    &x[n]*y[n]=\displaystyle\sum_{k=-\infty}^{+\infty}x[n]y[n-k]
\end{aligned}$$ Proprietà Distributiva: $$\begin{aligned}
    &(x(t)+y(t))*z(t)=x(t)*z(t)+y(y)*z(t)
    &(x[n]+y[n])*z[n]=x[n]*z[n]+y[n]*z[n]
\end{aligned}$$ Traslazione: $$\begin{aligned}
    &x(t-t_1)*y(t-t_2)=z(t-t_1-t_2)
    &x[n-n_1]*y[n-n_2]=z[n-n_1-n_2]
\end{aligned}$$

## Correlazione

Definizione: $$\begin{aligned}
    &x(t)\otimes y(t)=\displaystyle\int_{-\infty}^{+\infty}x(t+\tau)y^*(\tau)\mathrm{d}\tau=R_{xy}(t)
    &x[n]\otimes y[n]=\displaystyle\sum_{k=-\infty}^{+\infty}x[n+k]y[k]=R_{xy}[n]\\
    &x(t)\otimes y(t)=x(t)*y^*(-t)
    &x[n]\otimes y[n]=x[n]*y^*[-n]
\end{aligned}$$ Proprietà: $$\begin{aligned}
    &R_{xy}(t)=R_{yx}^*(-t)
    &R_{xy}[n]=R_{yx}^*[-n]\\
    &R_{xx}(0)=E_x
    &R_{xx}[0]=E_x
\end{aligned}$$

# Analisi in Frequenza

## Serie di Fourier

Definizione per un segnale $x(t)$ periodico di periodo $T$: $$\begin{aligned}
    &x(t)=\displaystyle\sum_{n=-\infty}^{+\infty}c_ne^{i\frac{2\pi nt}{T}}
    &c_n=\displaystyle\frac{1}{T}\int_{-T/2}^{T/2}x(t)e^{-i\frac{2\pi nt}{T}}\mathrm{d}t
\end{aligned}$$ Proprietà di Linearità: $$\begin{gathered}
    ax(t)+by(t)=\displaystyle\sum_{n=-\infty}^{+\infty}\left(ac_{n}^{(x)}+bc_{n}^{(y)}\right)e^{i\frac{2\pi nt}{T}}
\end{gathered}$$ Traslazione nel Tempo e di Armonica: $$\begin{aligned}
    &x(t-\tau)=\displaystyle\sum_{n=-\infty}^{+\infty}\left(c_n^{(x(t))}e^{-i\frac{2\pi nt_0}{T}}\right)e^{i\frac{2\pi nt}{T}}
    &x(t)\cdot e^{i\frac{2\pi kt}{T}}=\displaystyle\sum_{n=-\infty}^{+\infty}c_{n-k}e^{i\frac{2\pi nt}{T}}
\end{aligned}$$ Proprietà della Modulazione: $$\begin{gathered}
    x(t)\cdot\cos\left(\displaystyle\frac{2\pi t}{T}\right)=\displaystyle\sum_{n=-\infty}^{+\infty}\left(\frac{1}{2}c_{k-1}+\frac{1}{2}c_{k+1}\right)e^{i\frac{2\pi nt}{T}}
\end{gathered}$$ Proprietà della Derivazione: $$\begin{gathered}
    \displaystyle\frac{\mathrm{d}x(t)}{\mathrm{d}t}=\displaystyle\sum_{n=-\infty}^{+\infty}\left(c_n\frac{2i\pi n}{T}\right)e^{i\frac{2\pi nt}{T}}
\end{gathered}$$ Potenza di una Serie: $$\begin{gathered}
    P_x=\frac{1}{T}\displaystyle\sum_{n=-\infty}^{+\infty}|c_n|^2
\end{gathered}$$ Serie di Segnali Reali: $$\begin{gathered}
    x(t)=c_0+\displaystyle\sum_{n=-\infty}^{+\infty}a_n\cos\left(\frac{2\pi nt}{T}\right)-\displaystyle\sum_{n=-\infty}^{+\infty}b_n\sin\left(\frac{2\pi nt}{T}\right)\\
    \begin{cases}
        a_n=\displaystyle\frac{1}{T}\int_{-T/2}^{T/2}x(t)\cos\left(\frac{2\pi nt}{T}\right)\mathrm{d}t\\
        b_n=\displaystyle\frac{1}{T}\int_{-T/2}^{T/2}x(t)\sin\left(\frac{2\pi nt}{T}\right)\mathrm{d}t
    \end{cases}
\end{gathered}$$ Serie Notevoli: $$\begin{gathered}
    e^{\frac{2i\pi kt}{T}}\to c_n=\mathrm{sinc}(n-k)=\delta(n-k)\\
    \cos\left(\displaystyle\frac{2\pi t}{T}\right)\to c_1=c_{-1}=\frac{1}{2}\\
    \sin\left(\displaystyle\frac{2\pi t}{T}\right)\to c_1=c_{-1}^*=\frac{1}{2i}\\
    \pi(t)\to c_n=\displaystyle\frac{1}{T}
\end{gathered}$$

## Trasformata di Fourier

Definizione: $$\begin{aligned}
    &x(t)=\displaystyle\int_{-\infty}^{+\infty}X(f)e^{2i\pi tf}\mathrm{d}f
    &X(f)=\displaystyle\int_{-\infty}^{+\infty}x(t)e^{-2i\pi tf}\mathrm{d}t
\end{aligned}$$ Proprietà di Linearità: $$\begin{gathered}
    ax(t)+by(t)=aX(f)+bY(f)
\end{gathered}$$ Proprietà di Dualità: $$\begin{gathered}
    x(t)\to X(f)\iff X(t)\to x(-f)
\end{gathered}$$ Proprietà di Scala: $$\begin{gathered}
    x(at)\to\displaystyle\frac{1}{|a|}X\left(\frac{1}{a}\right)
\end{gathered}$$ Traslazione nel Tempo ed in Frequenza: $$\begin{aligned}
    &x(t-t_0)\to e^{-2i\pi ft_0}X(f)
    &e^{2i\pi f_0t}x(t)\to X(f-f_0)
\end{aligned}$$ Proprietà della Modulazione: $$\begin{gathered}
    x(t)\cos(2\pi f_0t)\to\displaystyle\frac{1}{2}X(f-f_0)+\frac{1}{2}X(f+f_0)
\end{gathered}$$ Proprietà della Derivazione e dell’Integrazione: $$\begin{aligned}
    &\displaystyle\frac{\mathrm{d}x(t)}{\mathrm{d}t}\to 2i\pi fX(f)
    &2i\pi tx(t)\to\displaystyle\frac{\mathrm{d}X(f)}{\mathrm{d}f}
\end{aligned}$$ $$\begin{gathered}
    \displaystyle\int_{-\infty}^{t}x(\tau)\mathrm{d}\tau\to\frac{1}{2}X(0)\delta(f)+\frac{X(f)}{2i\pi f}\\
\end{gathered}$$ Proprietà della Convoluzione e della Correlazione: $$\begin{gathered}
    x^*(t)\to X^*(-f)\\
    x(t)\otimes y(t)\to X(f)\cdot Y^*(f)\\
    x(t)*y(t)\to X(f)\cdot Y(f)\\
    x(t)\cdot y(t)\to X(f)*Y(f)
\end{gathered}$$ Energia in Frequenza: $$\begin{gathered}
    \displaystyle\int_{-\infty}^{+\infty}|X(f)|^2\mathrm{d}f=E_x
\end{gathered}$$ Trasformata di Segnali Reali: $$\begin{gathered}
    X(f)=\displaystyle\int_{-\infty}^{+\infty}x(t)\cos(2\pi ft)\mathrm{d}t-i\displaystyle\int_{-\infty}^{+\infty}x(t)\sin(2\pi ft)\mathrm{d}t\\
    X(-f)=X^*(f)
\end{gathered}$$ Trasformata di segnali periodici, di periodo $T$, dove $\overline{X}$ è la trasformata di una replica $\overline{x}(t)$ del segnale $x(t)$ in un unico periodo: $$\begin{gathered}
    \displaystyle\sum_{n=-\infty}^{+\infty}c_ne^{2i\pi nt/T}\to\displaystyle\sum_{n=-\infty}^{+\infty}\frac{1}{T}\overline{X}\left(\frac{n}{T}\right)\delta\left(f-\frac{n}{T}\right)
\end{gathered}$$ Trasformate Notevoli: $$\begin{aligned}
    &e^{2i\pi f_0 t}\to\delta(f-f_0)&\delta(t-t_0)\to e^{-2i\pi ft_0}\\
    &\displaystyle\frac{1}{T}\mathrm{rect}\left(\frac{t}{T}\right)\to\mathrm{sinc}(fT)
    &T\sin(Tt)\to\displaystyle\mathrm{rect}\left(\frac{f}{T}\right)\\
    &\mathrm{tri}\displaystyle\left(\frac{t}{T}\right)\to T\,\mathrm{sinc}^2(Tf)
    &T\mathrm{sinc}^2(Tt)\to\mathrm{tri}\left(\displaystyle\frac{f}{T}\right)\\
    &\cos\left(\displaystyle2\pi f_0t+\phi\right)=\frac{1}{2}\left[\delta(f-f_0)e^{i\phi}+\delta(f+f_0)e^{-i\phi}\right]
    &\sin\left(\displaystyle2\pi f_0t+\phi\right)=\frac{1}{2}\left[\delta(f-f_0)e^{i\phi}-\delta(f+f_0)e^{-i\phi}\right]
\end{aligned}$$ $$\begin{gathered}
    e^{-\frac{t^2}{2\sigma^2}}\to\sqrt{2\pi}\sigma e^{-2\pi^2\sigma^2f^2}\\
    e^{-\alpha t}u(t)\to\displaystyle\frac{1}{\alpha+2i\pi f}\\
    e^{-\alpha|t|}\to\displaystyle\frac{2\alpha}{\alpha^2+4\pi^2 f^2}\\
    u(t)\to\displaystyle\frac{1}{2}\delta(f)+\frac{1}{2i\pi f}\\
\end{gathered}$$

## Trasformata di Fourier Tempo Discreta

Definizione: $$\begin{aligned}
    &X(f)=\displaystyle\sum_{k=-\infty}^{+\infty}x[n]e^{-2i\pi fnT}
    &x[n]=T\displaystyle\int_{-1/2T}^{1/2T}X(f)e^{2i\pi nfT}\mathrm{d}f\\
\end{aligned}$$ Proprietà del Valor Medio: $$\begin{aligned}
    &X(0)=\displaystyle\sum_{n=-\infty}^{+\infty}x[n]
    &x[0]=T\displaystyle\int_{-1/2T}^{1/2T} X(f)\mathrm{d}f
\end{aligned}$$ Traslazione in Frequenza, e Ritardo di Campioni: $$\begin{aligned}
    &x[n-n_0]\to X(f)e^{-2i\pi n_0fT}
    &x[n]e^{2i\pi n_0fT}\to X(f-f_0)
\end{aligned}$$ Proprietà della Convoluzione e della Correlazione: $$\begin{gathered}
    x[n]*y[n]\to X(f)\cdot Y(f)\\
    x[n]\cdot y[n]\to X(f)\circledast Y(f)\\
    X(f)\circledast Y(f)=T\displaystyle\int_{-1/2T}^{1/2T}X(\theta)Y(f-\theta)\mathrm{d}\theta\\
    X(f)*Y(f)=\displaystyle\sum_{n=-\infty}^{+\infty}X(f)\circledast Y(f-n/T)\\
    R_{xy}[n]\to X(f)Y^*(f)\\
    R_{xx}[n]\to|X(f)|^2
\end{gathered}$$ Energia in Frequenza: $$\begin{gathered}
    E_x=T\displaystyle\int_{-1/2T}^{1/2T}|X(f)|^2\mathrm{d}f
\end{gathered}$$ Trasformate Notevoli: $$\begin{gathered}
    \delta[n]\to 1\\
    \displaystyle\sum_{n=0}^{N-1}\delta[n]\to e^{-i\pi(N-1)fT}\frac{\sin(\pi fNT)}{\sin(\pi fT)}\\
    \delta[n]+\delta[n-1]\to2ie^{-i\pi fT}\cos(\pi fT)\\
    \delta[n]-\delta[n-1]\to2ie^{-i\pi fT}\sin(\pi fT)\\
\end{gathered}$$ Campionamento di un Segnale $x(t)$ con Passo $T_c$: $$\begin{gathered}
    x[n]=x(t)\cdot\pi(t)=x_c(t)=\displaystyle\sum_{n=-\infty}^{+\infty}x(nT_c)\delta(t-nT_c)\\
    X_c(f)=\displaystyle\frac{1}{T_c}\displaystyle\sum_{n=-\infty}^{+\infty}X\left(f-\frac{n}{T_c}\right)
\end{gathered}$$ Frequenza Minima di Campionamento senza Aliasing: $$\begin{gathered}
    f_{c\min}=2f_{X\max}\\
    T_{c\max}=\displaystyle\frac{1}{2f_{X\max}}
\end{gathered}$$ Ricostruzione di un Segnale Campionato: $$\begin{gathered}
    x'(t)=x_c(t)*h(t)\\
    X'(f)=X_c(f)\cdot H(f)
\end{gathered}$$

# Fenomeni Aleatori

Distribuzione Cumulativa di Probabilità: $$\begin{gathered}
    D_X(x)=\Pr(X\leq x)\\
    D_X(x)=\displaystyle\sum_{i=-\infty}^{+\infty}\Pr(x=x_i)u(x-x_i)
\end{gathered}$$ Densità di Probabilità: $$\begin{gathered}
    P_X(x)=\displaystyle\frac{\mathrm{d}D_X(x)}{\mathrm{d}x}\\
    D_X(x)=\displaystyle\int_{-\infty}^xP_X(\overline{x})\mathrm{d}\overline{x}\\
    P_X(x)=\displaystyle\sum_{i=-\infty}^{+\infty}\Pr(x=x_i)\delta(x-x_i)\\
    \displaystyle\int_{-\infty}^{+\infty}P_X(x)\mathrm{d}x=1
\end{gathered}$$ Variabile Aleatoria Dipendente: $$\begin{gathered}
    Y=f(X):\,D_Y(y)=D_X(f^{-1}(y))\\
    Y=f(X):\,P_Y(y)=P_X(f^{-1}(y))\left|\displaystyle\frac{\mathrm{d}f^{-1}(y)}{\mathrm{d}y}\right|\\
    P_Y(y)=\displaystyle\sum_{i=0}^NP_X(f_i^{-1}(y))\left|\frac{\mathrm{d}f_i^{-1}(y)}{\mathrm{d}y}\right|
\end{gathered}$$ Valore Medio: $$\begin{gathered}
    \mu_x=E[x]=\displaystyle\int_{-\infty}^{+\infty}xP_X(x)\mathrm{d}x=\sum_{i=0}^Nx_iP_i
\end{gathered}$$ Valore Quadratico Medio: $$\begin{gathered}
    \mu_x^{(2)}=E[n^2]
\end{gathered}$$ Varianza: $$\begin{gathered}
    \sigma_x^2=E[(x-\mu_x)^2]=\mu_x^{(2)}-\mu_x^2
\end{gathered}$$ Deviazione Standard: $$\begin{gathered}
    \sigma_x=E[x-\mu_x]
\end{gathered}$$ Funzione Caratteristica: $$\begin{gathered}
    \mathbf{P}_x(f)=E[e^{-2i\pi fx}]\\
    \left[-\displaystyle\frac{\mathrm{d}\mathbf{P}_x(f)}{\mathrm{d}f}\right]_{f=0}=\mu_x
\end{gathered}$$ Proprietà Funzione Valore Atteso: $$\begin{gathered}
    E[y]=E[f(x)]\\
    E[af(x)+bg(x)]=aE[f(x)]+bE[g(x)]
\end{gathered}$$

## Statistica Uniforme su $[a,b]$

$$\begin{gathered}
    P_X(x)=\displaystyle\frac{1}{|b-a|}\mathrm{rect}\left(\frac{x-\mu_x}{|b-a|}\right)\\ 
    \mu_x=\displaystyle\frac{b+a}{2}\\
    \mu_x^{(2)}=\displaystyle\frac{b^2+ab+a^2}{3}\\
    \sigma_x^2=\displaystyle\frac{(b-a)^2}{12}\\
    \mathbf{P}_x(f)=\mathrm{sinc}[(b-a)f]e^{-i\pi f(b-a)}
\end{gathered}$$

## Statistica Esponenziale

$$\begin{gathered}
    P_X(x)=\lambda e^{-\lambda t}u(t)\\
    \mu_x=\displaystyle\frac{1}{\lambda}\\
    \mu_x^{(2)}=\displaystyle\frac{2}{\lambda^2}\\
    \sigma_x^2=\displaystyle\frac{1}{\lambda^2}\\
    \mathbf{P}_x(f)=\displaystyle\frac{\lambda}{\lambda+2i\pi f}
\end{gathered}$$

## Statistica Gaussiana

$$\begin{gathered}
    P_X(x)=\displaystyle\frac{1}{\sqrt{2\pi}\sigma_x}e^{-\frac{(x-\mu_x)^2}{2\sigma_x^2}}\\
    \mu_x=\mu_x\\
    \sigma_x^2=\sigma_x^2\\
    \mu_x^{(2)}=\sigma_x^2+\mu_x^2\\
    \mathbf{P}_x(f)=e^{-\pi^2\sigma^2_xf^2}e^{-2i\pi f\mu_x}
\end{gathered}$$

## Fenomeni Aleatori Bidimensionali

Distribuzione Cumulativa di Probabilità: $$\begin{gathered}
    D_{X,Y}(x,y)=\Pr(X\leq x,Y\leq y)\\
    \displaystyle\frac{\mathrm{d}^2}{\mathrm{d}x\mathrm{d}y}D_{X,Y}(x,y)=P_{X,Y}(x,y)
\end{gathered}$$ Densità di Probabilità Congiunta: $$\begin{gathered}
    P_{X,Y}(x,y)=\displaystyle\sum_{i=0}^N\sum_{j=0}^MP_{i,j}\delta(x-x_i)\delta(y-y_j)\\
    \iint_{\mathbb{R}^2}P_{X,Y}(x,y)\mathrm{d}x\mathrm{d}y=1
\end{gathered}$$ Densità di Probabilità Marginali: $$\begin{gathered}
    \displaystyle\int_{-\infty}^{+\infty}P_{X,Y}(x,y)\mathrm{d}y=P_X(x)\\
    \displaystyle\int_{-\infty}^{+\infty}P_{X,Y}(x,y)\mathrm{d}y=P_Y(y)
\end{gathered}$$ Valore Atteso Bidimensionale: $$\begin{gathered}
    E[f(x,y)]=\iint_{\mathbb{R}^2}f(x,y)P_{X,Y}(x,y)\mathrm{d}x\mathrm{d}y
\end{gathered}$$ Momento Misto di Ordine $1,1$: $$\begin{gathered}
    \mu_{xy}^{1,1}=E[xy]
\end{gathered}$$ Se le due variabili aleatorie $X$ e $Y$ sono indipendenti, la probabilità congiunta fattorizza: $$\begin{gathered}
    P_{X,Y}(x,y)=P_X(x)\cdot P_Y(y)\\
    E[xy]=\mu_x\mu_y
\end{gathered}$$ Covarianza: $$\begin{gathered}
    \sigma_{x,y}=E[(x-\mu_x)\cdot(y-\mu_y)]=\mu_{x,y}^{1,1}-\mu_x\mu_y\
\end{gathered}$$ Fattore di Correlazione: $$\begin{gathered}
    \rho_{x,y}=\displaystyle\frac{\sigma_{x,y}}{\sqrt{\sigma_x^2\sigma_y^2}}
\end{gathered}$$

## Variabile Dipendente Bidimensionale

Data la variabile aleatoria dipendente $Z$: $$\begin{gathered}
    Z=X+Y
\end{gathered}$$ Funzione Caratteristica: $$\begin{gathered}
    \mathbf{P}_z(f)=\mathbf{P}_x(f)\cdot\mathbf{P}_y(f)
\end{gathered}$$ Densità di Probabilità: $$\begin{gathered}
    P_Z(z)=P_X(x)*P_Y(y)
\end{gathered}$$ Valore Medio: $$\begin{gathered}
    \mu_z=\mu_x+\mu_y
\end{gathered}$$ Valore Quadratico Medio: $$\begin{gathered}
    \mu_z^{(2)}=\mu_x^{(2)}+2\mu_{x,y}^{1,1}+\mu_y^{(2)}
\end{gathered}$$ Varianza: $$\begin{gathered}
    \sigma_z^2=\sigma_x^2+\sigma_y^2
\end{gathered}$$

# Processi Aleatori

Definizione di una variabile aleatoria $X$ discreta, dato un processo aleatorio, composto da $N$ possibili realizzazioni se discreto: $$\begin{gathered}
    X_i:\left\{x_1(t_i),\cdots,x_N(t_i)\right\}
\end{gathered}$$ Oppure una variabile aleatoria continua, se sono possibili infinite realizzazioni di $x(t_i)$: $$\begin{gathered}
    X_i:x(t_i)
\end{gathered}$$

## Gerarchie del Primo Ordine

Valore Medio: $$\begin{gathered}
    \mu_x=E[x(t)]
\end{gathered}$$ Valore Quadratico Medio: $$\begin{gathered}
    \mu_x^{(2)}=E[x^2(t)]
\end{gathered}$$ Varianza: $$\begin{gathered}
    \sigma_x^2=E[(x(t)-\mu_x)^2]
\end{gathered}$$

## Gerarchie del Secondo Ordine

Funzione di (Auto)-Correlazione: $$\begin{gathered}
    R_x(t_1,t_2)=E[x(t_1)x(t_2)]\\
    R_x(t_1,t_1)=P_x
\end{gathered}$$ Funzione di Covarianza: $$\begin{gathered}
    C_x(t_1,t_2)=E[(x(t_1)-\mu_x(t_1))\cdot(x(t_2)-\mu_x(t_2))]=R_x(t_1,t_2)-\mu_{x}(t_1)\mu_{x}(t_2)\\
\end{gathered}$$ Fattore di Correlazione: $$\begin{gathered}
    \rho_x(t_1,t_2)=\displaystyle\frac{C_x(t_1,t_2)}{\sqrt{\sigma_x^2(t_1)\sigma_x^2(t_2)}}\\
\end{gathered}$$

## Processo Stazionario

Le gerarchie del primo ordine sono indipendenti dal tempo: $$\begin{gathered}
    \mu_x(t)=\mu_x\\
    \mu_x(t)^{(2)}=\mu_x^{(2)}\\
    \sigma_x^2(t)=\sigma_x^2
\end{gathered}$$ Le gerarchie del secondo ordine dipendono dalla differenza tra i due istanti di tempo $t_1$ e $t_2$: $$\begin{gathered}
    \tau=t_1-t_2\\
    R_x(\tau)=E[x(t+\tau)x(t)]\\
    R_x(\tau)=R_x(-\tau)\\
    R_x(0)=P_x\\
    C_x(\tau)=E[(x(t+\tau)-\mu_x(t+\tau))(x(t)-\mu_x(t))]=R_x(\tau)-\mu_x(t+\tau)\mu_x(t)\\
    \rho_x(\tau)=\displaystyle\frac{C_x(\tau)}{\sqrt{\sigma_x^2(t+\tau)\sigma_x^2(t)}}
\end{gathered}$$ Densità Spettrale di Energia: $$\begin{gathered}
    G_x(f)=\mathscr{F}\{R_x(\tau)\}\\
    P_x=\displaystyle\int_{-\infty}^{+\infty}G_x(f)\mathrm{d}f
\end{gathered}$$

## Processo Armonico

Definizione: $$\begin{gathered}
    x(t)=\cos\left(\displaystyle\frac{2\pi t}{T}+\varphi\right)\\
    P_{\Phi}(\varphi)=\displaystyle\frac{1}{2\varphi}\mathrm{rect}\left(\frac{\varphi-\pi}{2\pi}\right)
\end{gathered}$$ Valore Medio: $$\begin{gathered}
    \mu_x=0
\end{gathered}$$ Valore Quadratico Medio: $$\begin{gathered}
    \mu_x^{(2)}=\displaystyle\frac{1}{2}
\end{gathered}$$ Varianza: $$\begin{gathered}
    \sigma_x^2=\displaystyle\frac{1}{2}
\end{gathered}$$ Correlazione: $$\begin{gathered}
    R_x(\tau)=\displaystyle\frac{1}{2}\cos\left(\frac{2\pi\tau}{T}\right)
\end{gathered}$$ Covarianza: $$\begin{gathered}
    C_x(\tau)=\displaystyle\frac{1}{2}\cos\left(\frac{2\pi\tau}{T}\right)
\end{gathered}$$ Densità Spettrale di Potenza: $$\begin{gathered}
    G_x(f)=\displaystyle\frac{1}{4}\delta\left(f-\frac{1}{T}\right)+\frac{1}{4}\delta\left(f+\frac{1}{T}\right)
\end{gathered}$$

## Processo Ergodico

Processo descritto da un’unica realizzazione, le caratteristiche del processo dipendono dalla stessa realizzazione traslata nel tempo: $$\begin{gathered}
    E[f(x(t))]=\displaystyle\int_{-\infty}^{+\infty}f(x(t))P_X(x)\mathrm{d}x=\lim_{T\to+\infty}\displaystyle\frac{1}{T}\int_{-T/2}^{T/2}x(t)\mathrm{d}t\\
    E[x(t)]=\displaystyle\lim_{T\to\infty}\frac{1}{T}\int_{-T/2}^{T/2}x(t)\mathrm{d}t=\mu_x\\
    E[x^2(t)]=\displaystyle\lim_{T\to\infty}\frac{1}{T}\int_{-T/2}^{T/2}x^2(t)\mathrm{d}t=P_x
\end{gathered}$$

## Processi Dipendenti

I parametri si calcolano analogamente ai fenomeni aleatori bidimensionali, considerando i processi $x(t)$ e $y(t)$ indipendenti tra di loro: $$\begin{gathered}
    z(t)=ax(t)+by(t)
\end{gathered}$$ Gerarchie del Primo Ordine: $$\begin{gathered}
    \mu_z=a\mu_x+b\mu_y\\
    \mu_z^{(2)}=a^2\mu_x^{(2)}+2ab\mu_x\mu_y+b^2\mu_y^{(2)}\\   
    P_z=a^2P_x+2ab\mu_x\mu_y+b^2P_y\\
    \sigma_z^2=a^2\sigma_x^2+b^2\sigma_y^2
\end{gathered}$$ Gerarchie del Secondo Ordine: $$\begin{gathered}
    R_z(\tau)=a^2R_x(\tau)+2ab\mu_x\mu_y+b^2R_y(\tau)\\
    C_z(\tau)=a^2C_x(\tau)+b^2C_y(\tau)\\
    G_z(f)=a^2G_x(f)+2ab\mu_x\mu_y\delta(f)+b^2G_y(f)\\
    \rho_x(\tau)=\displaystyle\frac{a^2C_x(\tau)+b^2C_y(\tau)}{\sqrt{a^2\sigma_x^2+b^2\sigma_y^2}}
\end{gathered}$$

## Rumore

Definito come rumore additivo gaussiano bianco. Ha una statistica gaussiana e valor medio nullo: $$\begin{gathered}
    P_N(n)=\displaystyle\frac{1}{\sqrt{2\pi}\sigma_n}e^{-\frac{n^2}{2\sigma_n^2}}\\
    \mu_n=0\\
    \sigma_n^2=P_n
\end{gathered}$$ Poiché è un segnale bianco, ha densità spettrale di energia costante, su banda illimitata: $$\begin{gathered}
    G_n(f)=k\\
    P_n=+\infty\\
    R_n(\tau)=k\delta(\tau)
\end{gathered}$$ Oppure limitata in banda: $$\begin{gathered}
    G_n(f)=\frac{k}{2B}\mathrm{rect}\left(\displaystyle\frac{f}{2B}\right)=\frac{P_n}{2B}\mathrm{rect}\left(\displaystyle\frac{f}{2B}\right)\\
    P_n=k\\
    R_n(\tau)=k\mathrm{sinc}\left(2B\tau\right)=P_n\mathrm{sinc}(2B\tau)
\end{gathered}$$

## Transito Attraverso un Sistema

Dato un filtro di risposta impulsiva $h(t)$, si considera l’uscita $y(t)$, con un processo aleatorio $x(t)$ in entrata: $$\begin{gathered}
    y(t)=h(t)*x(t)
\end{gathered}$$ Valore Medio: $$\begin{gathered}
    \mu_y=\mu_xH(0)
\end{gathered}$$ Correlazione: $$\begin{gathered}
    R_y(\tau)=h(-t)*h(t)*R_X(\tau)
\end{gathered}$$ Densità Spettrale di Energia: $$\begin{gathered}
    G_y(f)=|H(f)|^2G_X(f)
\end{gathered}$$ Potenza: $$\begin{gathered}
    P_y=R_y(0)=\displaystyle\int_{-\infty}^{+\infty}G_y(f)\mathrm{d}f
\end{gathered}$$
