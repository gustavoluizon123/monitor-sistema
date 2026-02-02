# 🔐 Monitor de Sistema e Rede em Python

Projeto em **Python** focado em **monitoramento de sistema e análise de tráfego de rede**, aplicando conceitos fundamentais utilizados em **CyberSecurity, Blue Team e SOC**.

O script funciona via **terminal (CLI)** e fornece feedback visual em tempo real sobre o estado do sistema e da rede.

---

## 🧠 Objetivo do Projeto

Este projeto foi desenvolvido com fins educacionais e práticos, visando:

- Aplicar conceitos de **observabilidade**
- Praticar **monitoramento de infraestrutura**
- Entender métricas básicas usadas em **análise defensiva**
- Simular comportamentos comuns de ferramentas de monitoramento em ambientes de segurança

---

## ⚙️ Funcionalidades

### 🖥️ Monitoramento do Sistema
- Uso de **CPU**
- Consumo de **Memória RAM**
- Utilização de **Disco**
- Classificação automática:
  - 🟢 Normal  
  - 🟡 Atenção  
  - 🔴 Crítico  

### 🌐 Monitoramento de Rede
- Tráfego de **Download e Upload em tempo real (Mbps)**
- Identificação de **picos de consumo**
- Atualização contínua a cada segundo
- Encerramento seguro via tecla **Q**

### 🎨 Interface
- Feedback visual com **cores no terminal**
- Animações de carregamento (loading)
- Exibição clara e organizada das informações

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **psutil** — Coleta de métricas do sistema
- **colorama** — Cores no terminal
- **keyboard** — Interação via teclado

---

## ▶️ Como Executar

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seuusuario/monitor-sistema-rede.git
