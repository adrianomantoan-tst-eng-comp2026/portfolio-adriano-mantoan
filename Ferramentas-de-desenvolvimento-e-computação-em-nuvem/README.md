# 🖥️ Development Tools & Cloud Computing

# Implementação de Ambiente Cliente/Servidor com Ubuntu 26.04 LTS e Apache2

## 📚 Descrição do Projeto

Este projeto foi desenvolvido para a disciplina **Development Tools & Cloud Computing** do curso de **Engenharia da Computação – UniFECAF**.

O objetivo foi implementar um ambiente virtualizado Cliente/Servidor utilizando o **Oracle VirtualBox**, sistemas operacionais **Ubuntu Desktop 26.04 LTS** e o servidor web **Apache2**, simulando um cenário básico de infraestrutura de rede corporativa.

Ao final do projeto, foi possível hospedar páginas HTML no servidor Apache, configurar comunicação entre máquinas virtuais e disponibilizar um portfólio profissional acessado remotamente através da máquina Cliente.

Durante o desenvolvimento foram executadas atividades relacionadas à virtualização, instalação de sistemas operacionais, configuração de rede, administração de servidores Linux, hospedagem de conteúdo web e resolução de problemas de conectividade.

---

# 🎯 Objetivos

* Criar uma Máquina Virtual Cliente.
* Criar uma Máquina Virtual Server.
* Instalar o Ubuntu Desktop 26.04 LTS nas duas máquinas.
* Configurar a comunicação de rede entre Cliente e Servidor.
* Instalar e configurar o Apache Web Server.
* Criar e publicar páginas HTML.
* Hospedar um portfólio profissional.
* Realizar testes de conectividade.
* Validar o acesso remoto ao servidor web.

---

# 🏗️ Arquitetura do Ambiente

```text
┌─────────────────────┐
│     VM CLIENTE      │
│ Ubuntu 26.04 LTS    │
│ Hostname: cliente   │
│ IP: 192.168.10.20   │
└──────────┬──────────┘
           │
           │ Rede Interna
           │
┌──────────┴──────────┐
│      VM SERVER      │
│ Ubuntu 26.04 LTS    │
│ Hostname: server    │
│ Apache2             │
│ IP: 192.168.10.10   │
└─────────────────────┘
```

---

# 🛠️ Tecnologias Utilizadas

* Oracle VirtualBox
* Ubuntu Desktop 26.04 LTS
* Apache2
* Linux Terminal
* HTML
* Mozilla Firefox
* Git
* GitHub

---

# 💻 Configuração das Máquinas Virtuais

## VM Cliente

| Recurso             | Configuração             |
| ------------------- | ------------------------ |
| Sistema Operacional | Ubuntu Desktop 26.04 LTS |
| Memória RAM         | 4 GB                     |
| Processadores       | 2                        |
| Disco Virtual       | 20 GB                    |
| Hostname            | cliente                  |
| Endereço IP         | 192.168.10.20            |

---

## VM Server

| Recurso             | Configuração             |
| ------------------- | ------------------------ |
| Sistema Operacional | Ubuntu Desktop 26.04 LTS |
| Memória RAM         | 4 GB                     |
| Processadores       | 2                        |
| Disco Virtual       | 40 GB                    |
| Hostname            | server                   |
| Endereço IP         | 192.168.10.10            |

---

# 🌐 Configuração de Rede

Durante o projeto foi utilizada uma arquitetura de rede composta por:

### VM Cliente

* Interface de Rede Interna
* IP: 192.168.10.20

### VM Server

* Interface NAT (enp0s3)

  * Utilizada para acesso à Internet
  * IP automático fornecido pelo VirtualBox

* Interface Rede Interna (enp0s8)

  * Utilizada para comunicação Cliente ↔ Server
  * IP estático: 192.168.10.10

Essa configuração permitiu instalar pacotes através da Internet e, simultaneamente, manter a comunicação entre as máquinas virtuais.

---

# ⚙️ Instalação do Apache2

Atualização dos repositórios:

```bash
sudo apt update
```

Instalação do Apache:

```bash
sudo apt install apache2 -y
```

Verificação do serviço:

```bash
sudo systemctl status apache2
```

Teste local:

```bash
curl localhost
```

---

# 🌐 Publicação de Conteúdo Web

Inicialmente foi criada uma página HTML personalizada utilizando o arquivo:

```bash
/var/www/html/index.html
```

Posteriormente foi realizado o deploy de um portfólio profissional hospedado diretamente no servidor Apache.

O conteúdo hospedado pôde ser acessado remotamente através do navegador Firefox utilizando o endereço IP do servidor:

```text
http://192.168.10.10
```

---

# 🔎 Principais Comandos Utilizados

Verificar hostname:

```bash
hostname
```

Verificar versão do Ubuntu:

```bash
cat /etc/os-release
```

Verificar interfaces de rede:

```bash
ip a
```

Verificar endereço IP:

```bash
hostname -I
```

Verificar status do Apache:

```bash
sudo systemctl status apache2
```

Testar conectividade:

```bash
ping 192.168.10.10
```

Testar funcionamento local do Apache:

```bash
curl localhost
```

---

# 🚧 Problemas Encontrados

Durante a execução do projeto foram encontrados alguns desafios técnicos.

## 1. Falha de comunicação entre Cliente e Server

Em determinado momento a máquina Cliente não conseguia acessar o servidor.

Erro apresentado:

```bash
connect: A rede está fora de alcance
```

Após análise das interfaces de rede e rotas de comunicação foi possível identificar a origem do problema.

---

## 2. Configuração das Interfaces de Rede

Foi necessário compreender a diferença entre:

* NAT
* Rede Interna do VirtualBox

e realizar ajustes nas interfaces:

```text
enp0s3
enp0s8
```

para permitir a comunicação adequada entre as máquinas.

---

## 3. Configuração de Endereçamento IP

Foi necessária a configuração manual dos endereços IP:

Cliente:

```text
192.168.10.20
```

Servidor:

```text
192.168.10.10
```

---

## 4. Validação do Apache

Foi necessário confirmar o correto funcionamento do Apache através dos comandos:

```bash
sudo systemctl status apache2
```

e

```bash
curl localhost
```

---

# ✅ Resultados Obtidos

Ao final do projeto foi possível:

* Instalar o Ubuntu Desktop 26.04 LTS em ambas as máquinas virtuais.
* Configurar comunicação Cliente ↔ Server.
* Implementar uma rede interna funcional.
* Instalar e configurar o Apache2.
* Publicar páginas HTML personalizadas.
* Hospedar um portfólio profissional.
* Realizar testes de conectividade utilizando ICMP (Ping).
* Corrigir falhas de comunicação encontradas durante a implementação.
* Validar o acesso remoto ao servidor web.
* Consolidar conhecimentos em virtualização, Linux, redes e administração de servidores.

---

# 📸 Evidências do Projeto

O projeto possui documentação completa contendo:

* Instalação das máquinas virtuais;
* Configuração do Ubuntu;
* Configuração de rede;
* Instalação do Apache2;
* Publicação de páginas HTML;
* Hospedagem de portfólio;
* Testes de conectividade;
* Resolução de problemas encontrados durante a implementação.

Total de evidências documentadas: **28 figuras**.

---

# 🎓 Disciplina

**Development Tools & Cloud Computing**

Centro Universitário UniFECAF

Curso de Engenharia da Computação

---

# 👨‍💻 Autor

**Adriano Mantoan**

Técnico em Segurança do Trabalho

Estudante de Engenharia da Computação – UniFECAF

### GitHub

https://github.com/adrianomantoan-tst-eng-comp2026

### Portfólio

https://curriculo-adriano-mantoa-da318.web.app/
