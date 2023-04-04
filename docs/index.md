# Documentação do sistema proposto

Esse projeto é um simulação de braço robôtico e é composto por 3 partes:

- Frontend: O frontend é servido pelo backend e nele é posivel ver a posição atual do robô e enviar uma nova direção.
- Backend: O backend foi feito em Flask, se comunica com o frontend através de um render template e guarda os dados em um banco SQLite com a ORM SQLAlchemy.
- Simução: A simulação foi feita na plataforma godot em plano 2D. Nessa adaptação o braço representa os eixo x e y, já os eixos z e r são representados pelo quadrado como se fosse o alvo do braço.

Imagem de como é a simulação:

<img src="https://user-images.githubusercontent.com/99221221/229659374-ffb3dbf6-ee73-4ba4-9cef-0789728dd998.png" />

## Separação de pastas

```
├── docs
├── backend
│    ├── models
│    │    ├── base.py
│    │    ├── coordenadas.py
│    ├── banco.db
│    ├── db.py
│    ├── main.py
├── frontend
│    ├── templates
│    │    ├── index.html
├── simulação
```

## Rodar o programa

1. Clone este repositório
2. Instale `python` em seu computador
3. No diretorio do projeto digite os comandos `pip install flask` e `pip install sqlalchemy`
4. Entre no diretorio `backend` e rode o comando `python main.py`
5. No navegador acesse http://127.0.0.1:5000/ para te acesso ao frontend
6. Para rodar a simulação instale a engine Godot e importe o projeto dentro do diretorio 'simulação'. Ao abrir clique em play, no canto superior direito da interface do Godot
