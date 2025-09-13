# Metodo NAIF

![Screenshot from 2024-03-13 15-03-18.png](Screenshot_from_2024-03-13_15-03-18.png)

Si fa un `unpin(70)`, sul blocco 70:

- il blocco 70 si trova nella pagina 0 del buffer, quindi si decrementa di 1 il numero pin (1 → 0)
- si scrive quando viene liberata la pagina (10)

![Screenshot from 2024-03-13 15-27-54.png](Screenshot_from_2024-03-13_15-27-54.png)

Si fa un `pin(60)`, libera la pagina 0

- scrive (dirty: 1 → 0), legge nella pagina 0 (deve prima salvare)
- si modifica quindi il blocco (70 → 60)
- si modifica l’istante di load (1 → 11)
- si modifica l’istante di unpin a 0

![Screenshot from 2024-03-13 15-28-53.png](Screenshot_from_2024-03-13_15-28-53.png)

Si fa un `setXXX(60,...)` quindi l’unica cosa che cambia è il dirty bit(0 → 1)

![Screenshot from 2024-03-13 19-56-42.png](Screenshot_from_2024-03-13_19-56-42.png)

Si fa `unpin(60)`

- si mette istante di unpin a 13

![Screenshot from 2024-03-13 19-59-54.png](Screenshot_from_2024-03-13_19-59-54.png)

Si fa `flushAll`

- in pratica scrive su disco tutte le pagine quindi il risultato è che tutti i page sono salvati quindi i dirty bit vanno a 0

![Screenshot from 2024-03-13 20-03-08.png](Screenshot_from_2024-03-13_20-03-08.png)

Si fa `setXXX(47,...)`

![Screenshot from 2024-03-13 20-03-38.png](Screenshot_from_2024-03-13_20-03-38.png)

Si fa `unpin(47)`

![Screenshot from 2024-03-13 20-04-35.png](Screenshot_from_2024-03-13_20-04-35.png)

Si fa `pin(70)`, libera la pagina 0

- non c’è bisogno di scrivere perchè la pagina non è dirty
- si mette istante di load è 17
- si toglie istante di unpin

![Screenshot from 2024-03-13 20-07-06.png](Screenshot_from_2024-03-13_20-07-06.png)

Si fa `setXXX(70,...)`

![Screenshot from 2024-03-13 20-07-21.png](Screenshot_from_2024-03-13_20-07-21.png)

Si fa `unpin(70)`

![Screenshot from 2024-03-13 20-08-21.png](Screenshot_from_2024-03-13_20-08-21.png)

Si fa `pin(60)`: si libera la pagina 0

- si inizializza l’istante di load
- la pagina era sporca quindi si deve sia leggere sia scrivere

![Screenshot from 2024-03-13 20-09-57.png](Screenshot_from_2024-03-13_20-09-57.png)

Si fa `unpin(60)`

- si decrementa il numero di pin
- si mette 21 all’istante di unpin

![Screenshot from 2024-03-13 20-11-28.png](Screenshot_from_2024-03-13_20-11-28.png)

Si fa `pin(70)`