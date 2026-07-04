💻 TechFlow Task Manager

Projeto desenvolvido para a disciplina de Software Engineering do curso de Engenharia da Computação da UniFECAF.

📌 Descrição

A TechFlow Solutions, empresa fictícia especializada em desenvolvimento de software, foi contratada para criar um sistema web básico de gerenciamento de tarefas para uma startup do ramo de logística.

O objetivo do projeto foi desenvolver uma aplicação simples utilizando Python e Flask, permitindo o cadastro, edição, exclusão, pesquisa e acompanhamento das tarefas, aplicando conceitos estudados na disciplina de Engenharia de Software.

🎯 Objetivo

Desenvolver um sistema web de gerenciamento de tarefas aplicando conceitos de:

Engenharia de Software;
Metodologias Ágeis;
Git e GitHub;
GitHub Projects (Kanban);
Testes Automatizados;
Integração Contínua com GitHub Actions.
📋 Escopo Inicial

O escopo inicial do projeto contemplava as seguintes funcionalidades:

Cadastro de tarefas;
Listagem de tarefas;
Edição de tarefas;
Exclusão de tarefas;
Alteração do status das tarefas;
Organização das atividades utilizando Kanban.
🔄 Metodologia Ágil Utilizada

Durante o desenvolvimento foi utilizada a metodologia Kanban, organizando as atividades nas colunas:

To Do
In Progress
Done

Essa abordagem permitiu acompanhar a evolução do projeto, controlar as atividades em andamento e registrar todas as etapas de desenvolvimento.

🛠 Tecnologias Utilizadas
Python
Flask
HTML5
CSS3
Bootstrap
SQLite
PyTest
Git
GitHub
GitHub Projects
GitHub Actions
📁 Estrutura do Projeto
engenharia-de-software/
│
├── documentos/
├── imagens/
├── src/
├── static/
├── templates/
├── tests/
├── .github/workflows/
├── app.py
├── database.py
├── banco.db
├── requirements.txt
├── README.md
└── .gitignore
✅ Funcionalidades Implementadas

O sistema desenvolvido possui as seguintes funcionalidades:

Cadastro de tarefas;
Edição de tarefas;
Exclusão de tarefas;
Pesquisa por título;
Pesquisa por descrição;
Alteração do status das tarefas;
Controle de prioridades;
Contadores automáticos de tarefas por status;
Persistência dos dados utilizando banco SQLite;
Interface web responsiva.
🧪 Testes Automatizados

Foram desenvolvidos testes automatizados utilizando PyTest, permitindo validar as principais funcionalidades implementadas.

Os testes são executados automaticamente pelo GitHub Actions, garantindo maior confiabilidade ao projeto sempre que novas alterações são enviadas ao repositório.

⚙ Integração Contínua

Foi configurado um pipeline de Integração Contínua (CI) utilizando GitHub Actions.

A cada novo commit enviado ao repositório, o workflow executa automaticamente os testes do projeto, verificando o correto funcionamento das funcionalidades implementadas.

🔄 Mudança de Escopo

Durante o desenvolvimento surgiu a necessidade de ampliar o escopo inicialmente planejado.

Foi implementada uma nova funcionalidade permitindo definir a prioridade das tarefas, classificando-as como:

Alta
Média
Baixa

Além disso, foi desenvolvido um painel contendo contadores automáticos de tarefas por status, permitindo uma visualização rápida das atividades cadastradas.

Toda essa alteração foi registrada no GitHub Projects através de novos cards, implementada em novos commits e validada novamente pelos testes automatizados.

📊 Gerenciamento do Projeto

Todas as atividades foram acompanhadas utilizando o GitHub Projects, seguindo o fluxo Kanban.

Durante o desenvolvimento foram criados cards representando cada funcionalidade implementada, permitindo acompanhar toda a evolução do projeto desde o planejamento inicial até sua conclusão.

🚀 Status do Projeto

Projeto concluído.

Todas as funcionalidades previstas foram implementadas, documentadas e testadas, atendendo aos requisitos propostos para a disciplina de Engenharia de Software.

👨‍💻 Autor

Adriano Mantoan

Curso: Engenharia da Computação

Disciplina: Software Engineering

Centro Universitário UniFECAF
