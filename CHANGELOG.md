# Processo de Desenvolvimento

- Ambiente utilizado para o desenvolvimento:
  - Docker
  - Docker Compose
  - Python 3.8.6
  - Pycharm


## 1° Etapa INFRA

- Criado o arquivo `Dockerfile` e configura o ambiente da execução do projeto.
- Criado o arquivo `docker-compose.yml` e `docker-entrypoint.sh` para a execução do projeto com as configurações do Web/API, banco de dados (`PostgreSQL`) e bando de cache (`Redis`):
  - `docker-entrypoint.sh`: executa alguns comandos necessários para a execução do projeto, extrai os arquivos estáticos, migração para a criação e configurações das tabelas do banco de dados e execução do servidor.
- Foram criados dois arquivos de para a instalação das dependências:
  - `requirements-dev.txt`: para execução apenas em desenvolvimento, instalação das libs de testes.
  - `requirements.txt`: bibliotecas para o total funcionamento do projeto.
- Criado as configurações dos para execução de testes.
- Configurações de CI: `.github/workflows/docker-image.yml`, arquivo de configurações do [GitHub Actions](https://github.com/WesGtoX/agro_digital/actions) para rodar os testes após o `push` no repositório.
- Criado o arquivo `Makefile` para facilitar a execução do projeto.


## 2° Etapa ADMIN

- Criado uma estrutura base projeto, mais simplificada.
- Criado o admin para o models de `imovel`.
- Criado filtros de busca por tipo e busca por nome do `imovel`.
- Criado campos (`criado_em` e `modificado_em`) que são gerados automáticos quando se é criado uma `propriedade`.
- Adicionado opção de importação e exportação dos dados através de um arquivo no admin de `tipo` e `propriedade`.
  - Tipo de arquivos aceitos: `csv`, `xml`, `xlsx`, `tsv`, `json`, `yaml`.
- Criados testes de inserção de dados para `tipo` e `propriedade`.


## 3° Etapa LOCALIZACAO

- Criado nova app `localização`.
- Criado o model para a app:
  - Model `Regiao` campos:
    - **slug**: `String`; gerada automático quando é inserido pelo admim quando via REST.
    - **nome**: `String`; nome da região.
    - **estado**: `String`: estado da região.
  - Model `Cidade` campos:
    - **slug**: `String`; gerada automático quando é inserido pelo admim quando via rest.
    - **nome**: `String`; nome da cidade.
    - **regiao**: `Regiao`; relação com o modelo de região (slug, nome, estado).
- Adicionado `regiao` e `cidade` no admin e na API.
- Criado testes de inserção de dados `regiao` e `cidade`.
- Criado testes para os endpoints de `regiao` e `cidade`.
- Criado `fixture` para facilitar a inserção de dados para os testes.


## 4° Etapa GEOLOCALIZACAO

- Adicionado o campo `posicao` em `imovel.Propriedade`.
- Esse campo recebe os dados de cadastro através do admin, ponto: `longitude` e `latitude`.
- Criado um endpoint para retornar a listam dos dados de `propriedade`.
- Criado filtro para retornar apenas os itens mais próximos de um determinado ponto.
- Listagem ordenada pela distância dos pontos.


## 5° Etapa DOCUMENTACAO

- Criado o arquivo `CHANGELOG.md` para descrição das etapas realizadas.
- Atualização do `README.me` com marcação dos tópicos realizados e melhor descrição do projeto.
