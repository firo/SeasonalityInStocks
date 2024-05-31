# Analisi della Stagionalità del Titolo Azionario

Disclaimer: Questa applicazione è realizzata a scopo didattico per testare le funzionalità di Python e le librerie utilizzate. Non deve essere utilizzata come strumento finanziario su cui basare le proprie strategie di investimento. L'autore non si assume alcuna responsabilità per eventuali decisioni finanziarie prese sulla base delle informazioni fornite da questa applicazione.

## Descrizione

Questa applicazione, realizzata con Streamlit, esegue un'analisi della stagionalità dei titoli azionari utilizzando i dati scaricati da Yahoo Finance. L'applicazione permette di inserire il simbolo di un titolo azionario, scaricare i dati storici relativi, e visualizzare le componenti stagionali, di trend e di residuo del titolo.

## Funzionalità

1. **Input del Ticker**
   - L'utente può inserire il simbolo del titolo azionario di interesse (ad esempio, `MSFT` per Microsoft).

2. **Scaricamento dei Dati Storici**
   - I dati storici del titolo sono scaricati da Yahoo Finance, a partire dal 1° gennaio 2010 fino alla data odierna.

3. **Visualizzazione dei Dati Storici**
   - Gli ultimi 100 dati storici sono visualizzati nell'applicazione.

4. **Preprocessing dei Dati**
   - I dati vengono aggregati su base giornaliera.
   - Viene rimosso il 29 febbraio per gestire gli anni bisestili.
   - I dati mancanti sono riempiti utilizzando l'interpolazione lineare.

5. **Decomposizione STL**
   - I dati vengono decomposti in componenti stagionali, di trend e di residuo utilizzando la decomposizione STL (Seasonal-Trend decomposition using LOESS).

6. **Visualizzazione delle Componenti**
   - Le componenti dei dati (originali, trend, stagionali, residui) sono visualizzate in un grafico.

7. **Componente Stagionale per Diversi Periodi**
   - La componente stagionale viene calcolata per periodi di 5 anni, 10 anni e per l'ultimo anno.
   - Viene visualizzato il grafico della componente stagionale per questi periodi insieme al valore di chiusura dell'anno corrente.

## Note

- La decomposizione STL richiede una frequenza regolare dei dati. Assicurati che i dati siano preparati correttamente prima di eseguire la decomposizione.
- I dati storici sono limitati al periodo a partire dal 1° gennaio 2010 fino alla data odierna.
- L'applicazione mostra i dati solo a scopo didattico e non deve essere utilizzata per prendere decisioni finanziarie.

Provalo ora qui: [https://firo-2timesnegativein.streamlit.app/](https://firo-seasonalityinstocks.streamlit.app/) o qui [https://huggingface.co/spaces/firione/SeasonalityInStocks](https://huggingface.co/spaces/firione/SeasonalityInStocks)

<a href="https://www.buymeacoffee.com/firo"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=☕&slug=firo&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff" /></a>


## Licenza

- Questo progetto è sotto licenza MIT.
