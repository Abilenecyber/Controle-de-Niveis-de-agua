# Monitoramento - Controle de Níveis de Água 🚰

Este projeto consiste em um sistema automático de monitoramento para gerenciamento de reservatórios de água. Desenvolvido para execução em terminal, o sistema tem como objetivo analisar o volume atual do reservatório e emitir alertas visuais dinâmicos para facilitar a leitura e a tomada de decisões rápidas em ambientes operacionais reais.

## 💡 Ideia e Objetivo do Sistema

A visualização imediata do status de um reservatório é crítica para evitar desabastecimentos ou transbordamentos. Para tornar essa identificação visual clara e intuitiva, o software utiliza a biblioteca `colorama`, associando cada nível de volumetria a uma cor específica que segue uma escala lógica de progressão de risco.

### Mapeamento de Níveis e Estados de Alerta

O sistema categoriza a capacidade do reservatório em 5 níveis distintos:

| Nível do Reservatório | Situação Operacional | Alerta Visual (Cor) |
| :---: | :--- | :--- |
| **Nível 1** | Muito baixo (crítico) | 🔴 Vermelho |
| **Nível 2** | Baixo | 🟡 Amarelo |
| **Nível 3** | Médio | 🟢 Verde |
| **Nível 4** | Alto | 🔵 Ciano |
| **Nível 5** | Muito alto (alerta) | 🔵 Azul |

---

## 🛠️ Arquitetura e Estrutura do Código

O programa foi estruturado utilizando boas práticas de desenvolvimento em Python, dividindo as responsabilidades de forma modular:

*   **Armazenamento em Lista:** Utiliza uma estrutura de lista indexada para gerenciar as mensagens e os estados operacionais do reservatório, garantindo escalabilidade para novos níveis no futuro.
*   **Função de Decisão de Cores:** Uma função dedicada avalia o nível atual informado e mapeia o código de cor correto correspondente à biblioteca externa.
*   **Encapsulamento de Exibição:** Uma sub-rotina cuida da formatação do texto e garante que a cor seja aplicada apenas à mensagem correspondente.
*   **Reset de Estilo:** O sistema restaura automaticamente as configurações padrão de cor do terminal do usuário assim que a exibição das mensagens é finalizada, evitando comportamento inesperado em execuções posteriores.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o **Python 3** instalado em sua máquina.

### 1. Instalação das Dependências
Para instalar a biblioteca responsável pela estilização de cores no terminal, execute:
```bash
pip install colorama
```

### 2. Execução do Monitor
Para iniciar a simulação de leitura do reservatório, execute o script principal:
```bash
python monitoramento.py
```
