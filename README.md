<h1 align="center">
  Agro Digital
  <br />
  <img alt="Agro Digital CI" src="https://github.com/WesGtoX/agro_digital/workflows/Agro%20Digital%20CI/badge.svg" />
</h1>

<p align="center">
  <a href="#tecnologias">Tecnologias</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#começando">Começando</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#uso">Uso</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#licença">Licença</a>
</p>

<p align="center">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/wesgtox/agro_digital?style=plastic" />
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/wesgtox/agro_digital?style=plastic" />
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/wesgtox/agro_digital?style=plastic" />
  <img alt="License" src="https://img.shields.io/github/license/wesgtox/agro_digital?style=plastic" />
</p>


# Agro Digital

- [x] Etapa ADMIN
  - [x] Criar o admin para os models do app `imovel`
  - [x] Neste admin, faça:
      - [x] Um filtro por tipo de imovel
      - [x] Busca pelo nome do imovel
  - [x] Criar campos para `criado_em`, `modificado_em` no model de imovel.
  - [x] Adicionar no admin uma formar de importar e exportar os dados de cada admin por planilha
      - [x] Procure um projeto para lhe ajudar, não faça do zero

- [x] Etapa LOCALIZACAO
  - [x] Adicionar uma nova aplicação chamada `localizacao`
  - [x] Com o seguinte model:
      - [x] regiao (slug, nome, estado)
      - [x] cidade (slug, nome, estado, regiao)
  - [x] Adicionar uma relação do `imovel` com `regiao`
  - [x] Adiciona-los no Admin
  - [x] Adiciona-los na API

- [x] Etapa GEOLOCALIZACAO
  - [x] Adicionar um campo de `posicao` em propriedade
  - [x] Adicionar no admin uma forma de cadastrar esse ponto (dica: `django-leaflet`)
  - [x] Crie um endpoint que retorne os imóveis mais próximos de um ponto (lat, long)
  - [x] Ordenar estes pontos pela distancia em linha reta do ponto (lat, long) informado.

- [x] Etapa INFRA
  - [x] Criar o docker para o projeto
  - [x] Adicionar cache para o projeto (dica: `django-cacheops`)
  - [x] Preparar o docker-compose para rodar todo o projeto apenas executando `docker-compose up -d`

- [x] Etapa DOCUMENTACAO
  - [x] Crie um arquivo de `CHANGELOG.md` explicando o que foi feito em cada etapa executada deixando claro qual foi a ordem de execução de cada tarefa.
  - [x] Marque no readme do projeto que tópicos foram feito no `README.md`, e explique o motivo de não ter conseguido fazer alguma etapa.
  - [x] [Explique no README o que foi feito além do que foi solicitado](#informações-adicionais).


## Informações adicionais

- [x] Estrutura do projeto mais simplificada.
- [x] Autenticação para acesso aos endpoins.
- [x] Endpoint para criação de usuários.
- [x] Inserção do campo `slug` de forma automática.
- [x] Criação de testes com fixtures.


## Tecnologias

Este projeto foi desenvolvido com as seguintes tecnologias:

- [Python](https://www.python.org/)
- [Django Framework](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/)


## Começando

### Pré-requisitos

- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)


### Instalação e execução

1. Clone o repositório:
```bash
git clone https://github.com/WesGtoX/agro_digital.git
```
2. Defina uma `SECRET_KEY` em `.env`:
```bash
cp .env.sample .env
```
3. Construção
```bash
make build
```
4. Execução:
```bash
make run
```
4. Execução dos testes:
```bash
make test
```


## Uso

### Endpoints

### Auth Token

Para ter acesso a todos os endpoints, exceto o de de criação de usuário, precisa ser um usuário autenticado.

| Método | Endpoint           | Descrição                |
| :----: | ------------------ | ------------------------ |
| `POST` | `/api-token-auth/` | Autenticação do Usuário. |
> _Exemplo de retorno: `{"token": "0a405e7b82de0675d12b5b77a9648e0596f0d161"}`_

#### Usuário

| Método | Endpoint     | Descrição               |
| :----: | ------------ | ----------------------- |
| `POST` | `/usuarios/` | Insere um novo usuário. |

#### Propriedade

| Método | Regiao                                                  | Descrição                                               |
| :----: | ------------------------------------------------------- | ------------------------------------------------------- |
| `GET`  | `/propriedades/`                                        | Lista todas as propriedades cadastradas.                |
| `GET`  | `/propriedades?dist=distancia&point=latitude,longitude` | Lista as propriedades próximas de um ponto determinado. |
| `GET`  | `/propriedades/:id`                                     | Mostra o detalhe de uma propriedade específica.         |
> _Exemplo: `/propriedades?dist=2000&point=-21.13625,-48.00624`_

#### Regiao

|  Método  | Endpoint       | Descrição                                   |
| :------: | -------------- | ------------------------------------------- |
|  `POST`  | `/regioes/`    | Insere uma região.                          |
|  `GET`   | `/regioes/`    | Lista todas as regiões cadastradas.         |
|  `GET`   | `/regioes/:id` | Mostra o detalhe de uma região específica.  |
|  `PUT`   | `/regioes/:id` | Atualiza os dados de uma região específica. |
| `DELETE` | `/regioes/:id` | Remove uma região específica.               |

#### Cidade

|  Método  | Endpoint       | Descrição                                   |
| :------: | -------------- | ------------------------------------------- |
|  `POST`  | `/cidades/`    | Insere uma cidade.                          |
|  `GET`   | `/cidades/`    | Lista todos as cidades cadastradas.         |
|  `GET`   | `/cidades/:id` | Mostra o detalhe de uma cidade específica.  |
|  `PUT`   | `/cidades/:id` | Atualiza os dados de uma cidade específica. |
| `DELETE` | `/cidades/:id` | Remove uma cidade específica.               |


## Licença

Distribuído sob a Licença MIT. Consulte [LICENSE](LICENSE.md) para mais informações.

---

Feito com ♥ por [Wesley Mendes](https://wesleymendes.com.br/) :wave:
