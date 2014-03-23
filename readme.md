

### run 

 - install requirements.txt using pip
 - `python service.py`
 - server runs in `http:localhost:5000`

### get_event

retorna una lista de articulos de prensa dada una lista de palabras extraida de los flags.

- Los articulos se buscan deacuerdo a una lista de feeds rss.
- Los articulos candidatos estan en un rango de 24horas alrededor de la fecha del flag

- method: get

#### params

- **max** : maximo numero de articulos
- **date** : fecha pivote del flag
- **words**: lista json de las palabras del flag

#### retorna

Json list con los articulos candidatos y su respectivo score.

#### Ejemplo:

```
http://localhost:5000/get_event?max=10&date=2014-03-21%2011:00:00&words=["Destitucion","Gustavo%20Petro","decision","CIDH","alcalde","Bogota","Medidas%20cautelares","caso","acoge"]
```

retorna:

```json
[{"url": "http://www.caracol.com.co/noticias/actualidad/8203santos-afirma-haber-tomado-la-decision-correcta-en-el-caso-de-petro/20140321/nota/2140328.aspx", "score": 0.1049727762162956}, {"url": "http://www.caracol.com.co/noticias/actualidad/registraduria-revisara-2-millones-de-firmas-para-referendo-contra-el-aborto/20140322/nota/2141383.aspx", "score": 0.06917144638660747}, {"url": "http://www.eltiempo.com/politica/-santos-cita-a-gabinete-ministerial-para-analizar-crisis-de-bogota_13700357-4", "score": 0.06608720452851707}, {"url": "http://www.eltiempo.com/politica/santos-se-reunio-con-los-que-casi-lo-tumban-en-secreto_13710455-4", "score": 0.011896808488345666}, {"url": "http://www.eltiempo.com/elecciones-2014/presidencia/registradura-y-cne-reiteran-que-pealosa-ya-puede-inscribirse/13696996", "score": 0.009606950260552083}, {"url": "http://www.eltiempo.com/politica/santos-defiende-inversiones-en-las-regiones_13705475-4", "score": 0.004741893401604133}, {"url": "http://www.eltiempo.com/politica/maria-holguin-destaca-frutos-de-dos-proyectos-de-su-cartera_13705355-4", "score": 0.004341552193956563}, {"url": "http://www.eltiempo.com/elecciones-2014/presidencia/coincidencias-y-diferencias-de-cuatro-encuestas-electorales/13710237", "score": 0.00368712614292249}, {"url": "http://www.eltiempo.com/politica/german-chica-director-de-la-fnd-hablo-sobre-ninez-en-el-conflicto_13705416-4", "score": 0.0}, {"url": "http://www.eltiempo.com/politica/intencion-de-voto-para-presidencia_13697875-4", "score": 0.0}]
```

