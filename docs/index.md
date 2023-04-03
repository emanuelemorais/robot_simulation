# Documentação do sistema proposto

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

## Arquivos no diretorio src/backend
A pasta backend possui toda a estrutura de rotas, querys e banco de dados criados. Dentro da pasta models existem arquivos referentes a criação da estrutura de banco de dados utilizando a ORM SQLAlchemy. Já arquivo banco.db é o banco de dados que será utilizado para guardar informações de localizações passadas para a simulação e db.py possui função criar a sessão de comunicação com o banco de dados.

O arquivo main.py é onde toda a lógica do backend está sendo puxada e rodando. Dessa maneira existem três rotas existentes, sendo elas uma página inicial de GET ("/"), uma rota GET que será puxada constantemente pela simulação ("/simulation") e por fim uma rota POST para enviar novos valores para a simulação e banco de dados

## Arquivos no diretorio src/frontend
Esse diretorio possui uma subpasta chamada templates e, dentro desta o arquivo index.html que rendeniza a parte visual que interação com a simulação

## Arquivos no diretorio src/backend
Por fim, este diretório possui todda a simulaçaõ feita dentro da engine godot