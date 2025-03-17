# restaurant-orders

## Contexto
Este projeto trata-se de uma ferramenta de back-office para armazenar e buscar dados de pedidos em um restaurante. ferramenta de construção de cardápios. O restaurante necessita desta ferramenta para que possa, de maneira simples, gerar seus cardápios considerando possíveis restrições alimentares e também a disponibilidade dos ingredientes em estoque. Implemente a classe MenuData que fará todo o mapeamento de pratos e ingredientes baseado nos arquivos csv disponibilizados.

## Testes
Implementar testes para a classe Ingredient e Dish já implementadas anteriormente.

## Tecnologias usadas

### Back-end:
- Desenvolvido usando: Python
- 
## Crie o ambiente virtual para o projeto
```
python3 -m venv .venv && source .venv/bin/activate
```
## Instalando Dependências
```
python3 -m pip install -r dev-requirements.txt
```
## Executando aplicação
* Para rodar a aplicacão:
```
python3 -m uvicorn app:app
```

## Executando Testes
* executando todos os testes
 ```
 python3 -m pytest
```
* Caso precise executar apenas um arquivo de testes basta executar o comando:
```
python3 -m pytest tests/nomedoarquivo.py
```
## Arquivos desenvolvidos pela Trybe
* data:
- inventory_base_data.csv, menu_base_data.csv
* src:
- dev-requirements.txt, requirements.txt
