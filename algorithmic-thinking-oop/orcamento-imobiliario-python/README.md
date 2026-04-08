# 🏢 Sistema de Orçamento de Aluguel Imobiliário em Python

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/POO-Aplicado-important?style=for-the-badge">
</p>

---

## 📌 Contexto do Projeto 

Este projeto foi desenvolvido como parte da disciplina de **Algorithmic Thinking & Introduction to Object-Oriented Programming – UniFECAF**, com base no desafio proposto pela instituição.

📖 Conforme o enunciado, a aplicação simula uma imobiliária digital capaz de gerar orçamentos de aluguel automatizados, com base em regras de negócio reais :contentReference[oaicite:1]{index=1}.

---

## 🎯 Objetivo

Desenvolver um sistema capaz de:

- Gerar orçamento de aluguel mensal
- Aplicar regras de negócio imobiliárias
- Calcular taxas contratuais
- Gerar arquivo CSV com parcelas
- Demonstrar aplicação de lógica e POO

---

## ⚙️ Funcionalidades do Sistema

### ✔ Entrada de Dados
O sistema solicita ao usuário:

- Tipo de imóvel:
  - Apartamento
  - Casa
  - Estúdio
- Quantidade de quartos
- Quantidade de vagas de garagem
- Informação sobre crianças
- Quantidade de parcelas do contrato

---

### ✔ Processamento (Regras de Negócio)

De acordo com o PDF do projeto:

#### 🏢 Apartamento
- Base: R$ 700,00
- + R$ 200 → 2 quartos
- + R$ 300 → vaga
- -5% → sem crianças

#### 🏠 Casa
- Base: R$ 900,00
- + R$ 250 → 2 quartos
- + R$ 300 → vaga

#### 🏙️ Estúdio
- Base: R$ 1200,00
- + R$ 250 → até 2 vagas
- + R$ 60 → vagas adicionais

#### 💰 Contrato
- Valor fixo: R$ 2.000,00
- Parcelamento: até 5 vezes

✔ Todas essas regras foram implementadas conforme especificação do trabalho :contentReference[oaicite:2]{index=2}

---

### ✔ Saída de Dados

O sistema gera automaticamente:

- Valor do aluguel mensal
- Parcelas do contrato
- Total mensal
- Arquivo `.csv` com 12 meses

---

## 🧠 Lógica do Sistema

Fluxo principal:

1. Entrada de dados do usuário
2. Validação das informações
3. Seleção do tipo de imóvel
4. Instanciação da classe correspondente
5. Cálculo do aluguel
6. Cálculo da taxa de contrato
7. Geração das parcelas
8. Exportação para CSV

---

## 🔄 Fluxograma

<p align="center">
  <img src="documentos/fluxograma_imobiliario.png" width="80%">
</p>

---

## 🏗️ Arquitetura do Código

O sistema foi desenvolvido utilizando **Programação Orientada a Objetos (POO)**:

### 🔹 Classe Abstrata

```python
from abc import ABC, abstractmethod

class Imovel(ABC):
    @abstractmethod
    def calcular_aluguel(self):
        pass