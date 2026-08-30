# AutoStock – Sistema Automotivo de Gestão de Estoque de Veículos

Projeto desenvolvido para a disciplina de Programação Orientada a Objetos do curso de Engenharia da Computação da UniFECAF.

## Sobre o projeto

O AutoStock é um sistema desenvolvido para realizar o gerenciamento de um estoque de veículos.

A aplicação permite cadastrar marcas, modelos e veículos, além de consultar, editar e excluir os registros existentes. Também foram implementados filtros para facilitar a localização dos veículos cadastrados no estoque.

O projeto foi desenvolvido com o objetivo de aplicar na prática conceitos estudados em Programação Orientada a Objetos e integrar uma aplicação Java com banco de dados MySQL.

## Funcionalidades

- Cadastro de marcas;
- Cadastro de modelos associados às marcas;
- Cadastro de veículos;
- Consulta dos veículos cadastrados;
- Filtro por marca;
- Filtro por modelo;
- Filtro por ano;
- Filtro por status;
- Filtro por faixa de preço;
- Edição das informações dos veículos;
- Exclusão de veículos;
- Armazenamento dos dados em banco de dados MySQL.

## Informações dos veículos

No cadastro dos veículos são utilizadas informações como:

- Marca;
- Modelo;
- Ano;
- Cor;
- Preço;
- Quilometragem;
- Status;
- Observação.

## Tecnologias utilizadas

- Java 21;
- Spring Boot;
- Spring Data JPA;
- MySQL;
- Maven;
- Lombok;
- HTML;
- CSS;
- JavaScript;
- Visual Studio Code;
- MySQL Workbench.

## Programação Orientada a Objetos

Durante o desenvolvimento foram aplicados conceitos de Programação Orientada a Objetos.

### Classes e objetos

As entidades `Marca`, `Modelo` e `Veiculo` foram utilizadas para representar os principais elementos do sistema.

### Encapsulamento

Os atributos das entidades foram definidos como privados. O projeto utiliza as anotações `@Getter` e `@Setter` do Lombok para geração dos métodos de acesso aos atributos.

### Herança

Foi criada a classe abstrata `EntidadeBase`, responsável pelo atributo de identificação `id`.

As entidades do sistema podem herdar essa característica através de `extends EntidadeBase`, evitando a repetição do mesmo atributo.

### Relacionamento entre classes

O sistema possui relacionamento entre as entidades.

Um modelo pertence a uma marca, utilizando o relacionamento `@ManyToOne`.

Da mesma forma, cada veículo é associado ao seu respectivo modelo.

## Organização do projeto

O backend foi organizado em diferentes camadas:

- `controller` – recebe e trata as requisições;
- `service` – concentra as regras de negócio;
- `repository` – realiza o acesso aos dados;
- `model` – contém as entidades utilizadas pelo sistema.

Essa separação foi utilizada para manter o projeto organizado e facilitar a compreensão do código.

## Banco de dados

O AutoStock utiliza o MySQL para armazenamento das informações.

O banco utilizado pela aplicação é:

`autostock_db`

As principais tabelas são:

- `marcas`
- `modelos`
- `veiculos`

Os relacionamentos entre as tabelas permitem associar os modelos às suas marcas e os veículos aos seus respectivos modelos.

## Como executar o projeto

### Pré-requisitos

Para executar o projeto é necessário possuir:

- Java 21;
- MySQL 8;
- MySQL Workbench ou outro cliente MySQL.

### 1. Criar o banco de dados

No MySQL, criar o banco:

```sql
CREATE DATABASE autostock_db;
