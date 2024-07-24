# flask_memory_leak_test

Exemplo ficticio de um app `Flask` com vazamento de memória e como encontrar a fonte do vazamento de memória

App exemplo basico no `app_base.py` e instrumentado para encontrar o vazamento de memória no `app_tracemalloc.py`

Para ver funcionando:
1. Subir o app

```sh
python app_tracemalloc.py
```

2. Fazer chamadas em `http://127.0.0.1:5000/random` para inciar alocações de memória padrão do app

3. Capturar snapshot em `http://127.0.0.1:5000/snapshot`

4. Fazer chamadas em `http://127.0.0.1:5000/random` para gerar vazamento de memória

5. Ver vazamento de memória acusado em `http://127.0.0.1:5000/snapshot`

![image](https://github.com/user-attachments/assets/86918412-32dd-4b02-b755-2dabfef7f269)
