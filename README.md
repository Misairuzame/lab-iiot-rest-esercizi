# Laboratorio IIoT - ReST

## Installare le dipendenze
Creare l'ambiente virtuale:
```python -m venv venv```

Attivare l'ambiente virtuale:
```source venv/bin/activate```

Installare tutte le dipendenze con un unico comando:
```pip install -r requirements.txt```

## Far partire l'applicazione Flask
Innanzitutto eseguire il seguente comando:
```export FLASK_APP=<nome_file>.py```

Ad esempio, se l'applicazione Flask è scritta nel file "server.py":
```export FLASK_APP=server.py```

Successivamente, l'applicazione può essere fatta partire con:
```flask run```
