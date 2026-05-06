<div align="center">
  <img src="icones/logo_altus.png" alt="ALTUS - Apoio ao TEA" width="220">

  <h1>ALTUS Admin</h1>

  <p>
    Plataforma administrativa desktop para gestão de usuários, médicos, exercícios, desempenho,
    pagamentos e relatórios do ecossistema <strong>ALTUS - Apoio ao TEA</strong>.
  </p>

  <p>
    <a href="https://github.com/felipe-mammana/plataforma-de-ajuda-TEA">
      Projeto principal: plataforma-de-ajuda-TEA
    </a>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/PyQt5-41CD52?style=for-the-badge&logo=qt&logoColor=white" alt="PyQt5">
    <img src="https://img.shields.io/badge/Qt%20Designer-41CD52?style=for-the-badge&logo=qt&logoColor=white" alt="Qt Designer">
    <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL">
    <img src="https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white" alt="MariaDB">
    <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=plotly&logoColor=white" alt="Matplotlib">
  </p>
</div>

---

## Visão Geral

O **ALTUS Admin** é a parte administrativa do projeto
[`plataforma-de-ajuda-TEA`](https://github.com/felipe-mammana/plataforma-de-ajuda-TEA).
Este repositório concentra a aplicação desktop utilizada por administradores para operar dados
centrais da plataforma de apoio ao TEA, incluindo usuários, responsáveis, médicos, exercícios,
progresso, relatórios e pagamentos.

A aplicação foi construída em **Python** com **PyQt5**, usando arquivos `.ui` exportados pelo
**Qt Designer** e persistência em banco **MySQL/MariaDB**. O módulo não expõe uma API HTTP própria;
ele acessa o banco diretamente por meio do `mysql.connector`.

---

## Funcionalidades

### Autenticação administrativa

- Login por e-mail e senha na tabela `tb_login`.
- Controle de acesso por tipo de usuário, permitindo entrada somente quando `tipo = 'adm'`.
- Validação visual de erro com `QMessageBox`.

### Gestão de exercícios

- Cadastro de exercícios com nome, grau, tipos, arquivo, link e imagem.
- Edição e exclusão de exercícios existentes.
- Upload local de arquivos por `QFileDialog`.
- Armazenamento de imagens em campo `longblob`.
- Classificação por áreas como comunicação, vocabulário, raciocínio, memória, autonomia,
  interação social, coordenação, percepção, rotinas e decisão.
- Listagem com filtros por ID, nome, grau, extensão de arquivo e tipos.

### Gestão de médicos

- Cadastro de médicos com nome, data de nascimento, telefone, especialidade, CRM/CRN, e-mail,
  senha e foto.
- Criação associada de credenciais na tabela `tb_login` com `tipo = 'med'`.
- Pesquisa, edição e exclusão de médicos.
- Listagem com filtros por ID, nome e especialidade.

### Gestão de usuários

- Listagem de usuários cadastrados.
- Filtros por ID, nome, sobrenome, idade e grau.
- Consulta integrada entre `tb_user`, `tb_user_med` e `tb_responsavel`.
- Exibição de dados relevantes para acompanhamento administrativo.

### Progresso e desempenho

- Visualização do progresso dos usuários por exercício.
- Filtros por usuário, exercício, nome e autonomia.
- Consulta integrada entre `tb_user` e `tb_progresso`.
- Ajuste manual de largura de colunas por duplo clique no cabeçalho da tabela.

### Relatórios mensais

- Gráfico de usuários por plano.
- Gráfico de usuários por grau de TEA.
- Gráfico de crescimento mensal de usuários.
- Renderização com `matplotlib` integrado ao PyQt5 via `FigureCanvasQTAgg`.

### Pagamentos

- Listagem de pagamentos registrados em `tb_pagamentos`.
- Integração com comprovantes em `tb_comprovantes`.
- Ações administrativas para aprovar ou rejeitar pagamentos pendentes.
- Abertura local de comprovantes PDF.
- Envio de e-mail ao responsável após mudança de status.

---

## Arquitetura

O projeto segue uma arquitetura desktop monolítica, com um arquivo Python central responsável por
orquestrar interface gráfica, acesso ao banco, regras de navegação e operações administrativas.

```text
.
├── TCC.py
├── bd_tcc_g1s (17).sql
├── frm_add_exercicios.ui
├── frm_cadastro_medicos.ui
├── frm_edit_exercicios.ui
├── frm_list_exercicios.ui
├── frm_listagem_medicos.ui
├── frm_login.ui
├── frm_menu_adm.ui
├── frm_menu_exercicios.ui
├── frm_medicos.ui
├── frm_pagamentos.ui
├── frm_progresso.ui
├── frm_relatorio_men.ui
├── frm_usuarios.ui
├── frm_config.ui
├── requirements.txt
├── .env.example
├── .gitignore
├── .gitattributes
└── icones/
    ├── logo_altus.png
    ├── logo_altusboneco.png
    ├── add_ex (2).png
    ├── edit_ex.png
    ├── list_ex.png
    ├── medico.png
    ├── progresso.png
    ├── relatorio.png
    └── ...
```

### Componentes principais

| Componente | Responsabilidade |
| --- | --- |
| `TCC.py` | Ponto de entrada da aplicação, navegação entre telas, CRUDs, consultas SQL, gráficos e envio de e-mail. |
| `*.ui` | Telas desenhadas no Qt Designer e carregadas dinamicamente por `uic.loadUi`. |
| `bd_tcc_g1s (17).sql` | Dump do banco `bd_tcc_g1s`, contendo estrutura, chaves, relacionamentos e dados iniciais. |
| `icones/` | Assets visuais usados pela interface, incluindo logotipos, ícones de menus, relatórios, médicos e exercícios. |

---

## Tecnologias

| Tecnologia | Uso no projeto |
| --- | --- |
| [Python](https://www.python.org/) | Linguagem principal da aplicação desktop. |
| [PyQt5](https://pypi.org/project/PyQt5/) | Construção da interface gráfica e manipulação de widgets. |
| [Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html) | Criação visual das telas `.ui`. |
| [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/) | Conexão direta com o banco MySQL/MariaDB. |
| [MySQL](https://www.mysql.com/) / [MariaDB](https://mariadb.org/) | Banco relacional usado pela aplicação. O dump foi gerado em MariaDB 10.4.32 via phpMyAdmin. |
| [Matplotlib](https://matplotlib.org/) | Geração dos gráficos administrativos dentro da interface PyQt5. |
| [`smtplib`](https://docs.python.org/3/library/smtplib.html) | Envio SMTP de notificações de status de pagamento. |


## Como Executar

### Pré-requisitos

- Python 3 instalado.
- MySQL ou MariaDB em execução local.
- Banco `bd_tcc_g1s` importado.
- Dependências Python instaladas.
- Arquivos `.ui` referenciados pelo código presentes no mesmo diretório do `TCC.py`.

### Clonar o repositório

```bash
git clone https://github.com/felipe-mammana/plataforma-de-ajuda-TEA-adm.git
cd plataforma-de-ajuda-TEA-adm
```

### Criar ambiente virtual

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

No Linux/macOS:

```bash
source .venv/bin/activate
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Importar o banco

Com MySQL/MariaDB disponível localmente:

```bash
mysql -u root -p < "bd_tcc_g1s (17).sql"
```

Configure a conexão em um arquivo `.env` criado a partir de `.env.example`:

```bash
DB_HOST=localhost
DB_PORT=3306
DB_NAME=bd_tcc_g1s
DB_USER=root
DB_PASSWORD=
```

### Executar a aplicação

```bash
python TCC.py
```

### Docker

Não há configuração Docker no repositório atual. A execução prevista é local, com Python e banco
MySQL/MariaDB instalados no ambiente.

### Build

Não há script de build ou empacotamento detectado. O projeto é executado diretamente pelo arquivo
`TCC.py`.

### Testes

Não há suíte de testes automatizados configurada neste repositório.

---

## Variáveis de Ambiente

O projeto inclui `.env.example` com as configurações esperadas. Para uso local, crie um arquivo
`.env` na raiz do projeto com base nesse exemplo.

| Variável | Descrição |
| --- | --- |
| `DB_HOST` | Host do MySQL/MariaDB. Padrão: `localhost`. |
| `DB_PORT` | Porta do banco. Padrão: `3306`. |
| `DB_NAME` | Nome do banco utilizado pela aplicação. Padrão: `bd_tcc_g1s`. |
| `DB_USER` | Usuário de conexão com o banco. |
| `DB_PASSWORD` | Senha de conexão com o banco. |
| `SMTP_HOST` | Servidor SMTP usado para notificações de pagamento. |
| `SMTP_PORT` | Porta SMTP. Padrão: `587`. |
| `SMTP_USER` | Conta remetente usada para autenticação SMTP. |
| `SMTP_PASSWORD` | Senha de app/token SMTP. |
| `SMTP_FROM` | Endereço exibido como remetente. |

---

## Endpoints/API

Este módulo administrativo não expõe endpoints HTTP. Todas as operações são realizadas por interface
desktop e consultas diretas ao banco de dados.

| Método | Endpoint | Descrição |
| --- | --- | --- |
| Não aplicável | Não aplicável | Não há API HTTP detectada neste repositório. |

---

## Banco de Dados

O banco de dados do projeto é `bd_tcc_g1s`, com dump disponível em `bd_tcc_g1s (17).sql`.
O arquivo foi exportado pelo phpMyAdmin e indica uso de MariaDB 10.4.32.

### Entidades principais

| Tabela | Finalidade |
| --- | --- |
| `tb_login` | Credenciais e tipo de acesso (`adm`, `med`, usuário). |
| `tb_user` | Dados principais dos usuários acompanhados pela plataforma. |
| `tb_user_med` | Informações clínicas/educacionais associadas ao usuário, como grau e dificuldades. |
| `tb_responsavel` | Dados do responsável vinculado ao usuário. |
| `tb_medico` | Cadastro de médicos e profissionais. |
| `tb_exercicios` | Exercícios, grau, tipos, arquivo, link e imagem. |
| `tb_progresso` | Registro de execução e autonomia dos usuários nos exercícios. |
| `tb_pagamentos` | Pagamentos, valores, código PIX e status. |
| `tb_comprovantes` | Arquivos de comprovante vinculados aos pagamentos. |
| `tb_consulta` | Consultas entre usuários e médicos. |
| `tb_feedback` | Feedbacks e observações sobre evolução. |
| `tb_mensagens` | Mensagens entre usuários e médicos. |
| `tb_mensagens_comunidade` | Mensagens em contexto de comunidade. |
| `tb_user_temp` | Dados temporários de cadastro de usuários. |

### Relacionamentos detectados

- `tb_login.id_user` referencia `tb_user.id_user`.
- `tb_login.id_med` referencia `tb_medico.id_med`.
- `tb_user_med.id_user` referencia `tb_user.id_user`.
- `tb_responsavel.id_user` referencia `tb_user.id_user`.
- `tb_progresso.id_user` referencia `tb_user.id_user`.
- `tb_progresso.id_ex` referencia `tb_exercicios.id_ex`.
- `tb_pagamentos.id_user` referencia `tb_user.id_user`.
- `tb_comprovantes.id_pagamento` referencia `tb_pagamentos.id_pagamento`.
- `tb_consulta.id_user` referencia `tb_user.id_user`.
- `tb_consulta.id_med` referencia `tb_medico.id_med`.
- `tb_feedback.id_user` referencia `tb_user.id_user`.
- `tb_mensagens.id_user` referencia `tb_user.id_user`.
- `tb_mensagens.id_med` referencia `tb_medico.id_med`.
- `tb_mensagens_comunidade.id_user` referencia `tb_user.id_user`.
- `tb_mensagens_comunidade.id_med` referencia `tb_medico.id_med`.

---

## Segurança

### Implementado

- Login administrativo por consulta à tabela `tb_login`.
- Restrição de acesso por tipo de conta (`tipo = 'adm'`).
- Validações de campos obrigatórios em telas de cadastro.
- Uso de consultas parametrizadas nas operações administrativas principais.
- Configurações de banco e SMTP carregadas por `.env`.
- `.gitignore` configurado para evitar versionamento de `.env` e artefatos locais.
- Confirmação visual para falhas e operações administrativas.

### Pontos de atenção

- Senhas são comparadas diretamente com o valor armazenado em banco.
- Não há middleware, JWT, OAuth ou camada HTTP de autenticação neste módulo.
- Recomenda-se substituir senhas em texto puro por hash seguro.

---

## Integrações

| Integração | Uso |
| --- | --- |
| MySQL/MariaDB | Persistência principal da aplicação. |
| Gmail SMTP | Envio de notificações de pagamento aprovado ou rejeitado. |
| Sistema operacional | Abertura local de comprovantes PDF com `os.startfile`, `open` ou `xdg-open`. |
| Arquivos locais | Seleção de arquivos e imagens por `QFileDialog`. |

---


## Deploy

Este repositório representa uma aplicação desktop administrativa. Não foram detectados scripts ou
configurações para deploy em cloud, containers ou plataformas serverless.

Modelo de distribuição compatível com o estado atual:

- Execução local em máquinas administrativas.
- Banco MySQL/MariaDB acessível pela aplicação.
- Assets e arquivos `.ui` no mesmo diretório do executável/script.
- Possível empacotamento futuro com ferramentas como PyInstaller.

---


## Equipe

O material visual do projeto identifica a equipe como:

- Eduardo Portela
- Felipe Mammana
- João Vitor Herrera
- José Victor Ficher
- Letícia Fins
- Murilo Cristovão

---

## Licença

Não foi detectado arquivo de licença neste repositório.

---

<div align="center">
  <strong>ALTUS Admin</strong><br>
  Administração desktop para o ecossistema ALTUS - Apoio ao TEA.
</div>
