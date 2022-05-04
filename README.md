# Sala de bate-papo virtual

Esse é um projeto que contém um ambiente virtual de conversação com uso de sockets, foi realizado em python e tem como objetivo apresentar uma gerência de diálogo utilizando a arquitetura TCP/IP

### Iniciando

1. Abra o terminal, abra a pasta do projeto e rode Server.py, com os seguintes parâmetros:

- porta
- limite de participantes na sala
- nome da sala

```bash
cd <root>
python Server.py 3000 2 Nova-sala
```

2. Em outro terminal, adicione um novo usuário a sala de bate papo e rode Client.py com os seguintes parâmetros:

- nome do usuário
- porta

```bash
python Client.py fernando 3000
```

3. Você pode adicionar mais usuários rodando o Client.py em outros terminais
