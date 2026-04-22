# 🚀 Servidor Web com Windows Server 2022 + IIS (VirtualBox)

<p align="center">
  <img src="https://img.shields.io/badge/Windows%20Server-2022-blue?style=for-the-badge&logo=windows" />
  <img src="https://img.shields.io/badge/IIS-Web%20Server-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/VirtualBox-Virtualization-orange?style=for-the-badge&logo=virtualbox" />
  <img src="https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge" />
</p>

---

## 📌 Sobre o Projeto

Este projeto demonstra a criação e configuração de um **servidor web completo** utilizando **Windows Server 2022** em ambiente virtualizado com **Oracle VirtualBox**, simulando um cenário real de hospedagem.

Durante o desenvolvimento, foram aplicados conceitos de:

✔ Virtualização  
✔ Redes (NAT e Port Forwarding)  
✔ Servidor Web (IIS)  
✔ Protocolos HTTP e HTTPS  
✔ Exposição de serviços para acesso externo  

---

## 🎯 Objetivo

Criar um ambiente funcional onde um site possa ser:

✔ Hospedado em uma máquina virtual  
✔ Acessado localmente (VM)  
✔ Acessado pelo host (PC)  
✔ Exposto para a internet (via ngrok)  

---

## 🖥️ Tecnologias Utilizadas

- Windows Server 2022  
- Oracle VirtualBox  
- IIS (Internet Information Services)  
- HTML, CSS e JavaScript  
- Ngrok (túnel para acesso externo)  

---

## 🏗️ Arquitetura

PC (Host)
↓
VirtualBox (NAT)
↓
Windows Server 2022 (VM)
↓
IIS (porta 80)
↓
Site hospedado


---

## 🔧 Etapas do Projeto

### 🔹 1. Máquina Virtual
- Criação no VirtualBox  
- Configuração de memória, CPU e disco  
- Instalação do Windows Server 2022  

---

### 🔹 2. Instalação do IIS
- Instalação via Server Manager  
- Ativação do serviço Web Server  
- Configuração do ambiente  

---

### 🔹 3. Publicação do Site
- Criação de arquivo HTML  
- Diretório padrão:
C:\inetpub\wwwroot

- Acesso interno:
http://localhost

---

## 🌐 Configuração de Rede

### 🔹 NAT (utilizado)
- IP interno da VM: `10.0.2.15`
- Rede isolada

---

### 🔹 Port Forwarding
- Porta do host: **8080**
- Porta da VM: **80**

Acesso pelo PC:
http://localhost:8080

---

## 🌍 Acesso Externo (NGROK) ⭐ DIFERENCIAL

Para simular um ambiente real de hospedagem, foi utilizado o **ngrok**, permitindo acesso ao servidor via internet.

### 🔹 Comando utilizado:
ngrok http 80

### 🔹 Resultado:
- Geração de URL pública HTTPS
- Acesso externo ao site hospedado na VM

Exemplo:
https://xxxx.ngrok-free.dev

---

## 🔐 Segurança

- Utilização do protocolo HTTP (porta 80)
- Estudo do HTTPS (porta 443)
- Ambiente local controlado
- ngrok fornece camada segura (HTTPS automático)

---

## 🗄️ Banco de Dados

Não foi utilizado banco de dados neste projeto.

Em cenários reais, recomenda-se:
- MySQL  
- PostgreSQL  

---

## 🧪 Testes Realizados

✔ Acesso via localhost na VM  
✔ Acesso via localhost:8080 no host  
✔ Verificação do IIS em execução  
✔ Teste de IP interno da VM  
✔ Teste de acesso externo via ngrok  

---

## ⚠️ Desafios Enfrentados

- Erro HTTP 403 (acesso negado)  
- Configuração inicial do IIS  
- Falha ao acessar via IP da VM  
- Conflito de portas no VirtualBox  
- Configuração do ngrok  

---

## 📸 Demonstração

### 🔹 Máquina Virtual criada
![VM criada](./imagens/maquina-virtual.png)

---

### 🔹 Serviço IIS em execução
![IIS rodando](./imagens/iis.png)

---

### 🔹 Comando ipconfig (IP da VM)
![IP da VM](./imagens/ipconfig.png)

---

### 🔹 Configuração de Port Forwarding
![Port Forwarding](./imagens/port-forwarding.png)

---

### 🔹 Site funcionando na VM
![Site VM](./imagens/site-vm.png)

---

### 🔹 Acesso via Host (localhost:8080)
![Host acesso](./imagens/host-8080.png)

---

### 🔹 Execução do ngrok
![Ngrok](./imagens/ngrok.png)

---

### 🔹 Página de validação do ngrok
![Ngrok validação](./imagens/ngrok-validacao.png)

---

### 🔹 Site acessado externamente
![Ngrok site](./imagens/site-ngrok.png)

---

## 🚀 Melhorias Futuras

- Implementação completa de HTTPS com certificado  
- Integração com banco de dados  
- Deploy em servidor real (cloud)  
- Automação do ambiente  

---

## 👨‍💻 Autor

**Adriano Mantoan**  
Estudante de Engenharia da Computação  
Técnico em Segurança do Trabalho  

---

## 📌 Destaque

Este projeto demonstra na prática a criação de um ambiente de servidor web funcional, incluindo acesso externo, aproximando o cenário acadêmico de uma aplicação real de mercado.

