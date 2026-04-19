# 🚀 Servidor Web com Windows Server 2022 + IIS (VirtualBox)

<p align="center">
  <img src="https://img.shields.io/badge/Windows%20Server-2022-blue?style=for-the-badge&logo=windows" />
  <img src="https://img.shields.io/badge/IIS-Web%20Server-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/VirtualBox-Virtualization-orange?style=for-the-badge&logo=virtualbox" />
  <img src="https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge" />
</p>

---

## 📌 Sobre o Projeto

Este projeto demonstra a criação e configuração de um servidor web utilizando **Windows Server 2022** em ambiente virtualizado com **Oracle VirtualBox**, simulando um cenário real de hospedagem.

---

## 🖥️ Tecnologias Utilizadas

* Windows Server 2022
* Oracle VirtualBox
* IIS (Internet Information Services)
* HTML, CSS e JavaScript

---

## ⚙️ Arquitetura

PC (Host)
↓
VirtualBox (NAT)
↓
Windows Server (VM)
↓
IIS (porta 80)
↓
Site hospedado

---

## 🔧 Etapas do Projeto

### 1. Máquina Virtual

* Criação no VirtualBox
* Configuração de memória e disco
* Instalação do Windows Server

### 2. IIS

* Instalação via Server Manager
* Ativação do serviço

### 3. Publicação do Site

Diretório:
C:\inetpub\wwwroot

Acesso:
http://localhost

---

## 🌐 Rede

### NAT (utilizado)

* IP interno: 10.0.2.15
* Necessário redirecionamento

### Port Forwarding

Host: 8080 → VM: 80

Acesso externo:
http://localhost:8080

---

## 🔐 Segurança

* HTTP (porta 80)
* Estudo de HTTPS (porta 443)
* Ambiente local para testes

---

## 🗄️ Banco de Dados

Não foi utilizado banco de dados neste projeto.
Em cenários reais, recomenda-se MySQL ou PostgreSQL.

---

## 🧪 Testes

* Acesso interno (localhost)
* Acesso externo (localhost:8080)
* Verificação do IIS
* Testes de rede

---

## ⚠️ Desafios

* Erro HTTP 403
* Configuração do IIS
* Acesso via IP da VM
* Conflito de portas

---

## 📸 Demonstração

### 🔹 Máquina Virtual criada
![VM criada](./images/vm-criada.png)

---

### 🔹 Serviço IIS em execução
![IIS rodando](./images/iis.png)

---

### 🔹 Comando ipconfig (IP da VM)
![IP da VM](./images/ipconfig.png)

---

### 🔹 Configuração de Port Forwarding
![Port Forwarding](./images/port-forwarding.png)

---

### 🔹 Site funcionando na VM
![Site VM](./images/site-vm.png)

---

### 🔹 Armazenamento arquivos wwwroot no Site funcionando na VM
![Arquivos wwwroot Site VM](./images/wwwroot.png)

---

### 🔹 Acesso via Host (localhost:8080)
![Host acesso](./images/host-8080.png)

---

## 🚀 Melhorias Futuras

* Implementar HTTPS
* Integrar banco de dados
* Publicar na internet

---

## 👨‍💻 Autor

Adriano Mantoan
Engenharia da Computação

---
