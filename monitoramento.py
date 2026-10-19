# Importação de funções específicas 
from colorama import Fore, Style

# 1. Lista de strings armazenando as mensagens 
SITUACOES_RESERVATORIO = [
    "Nível 1: Muito baixo (crítico)",
    "Nível 2: Baixo",
    "Nível 3: Médio",
    "Nível 4: Alto",
    "Nível 5: Muito alto (alerta)"
]

# 2. Função responsável por definir a cor da mensagem conforme o nível informado
def obter_cor_nivel(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

def exibir_status_reservatorio(nivel):
    # Validação para garantir que o nível está dentro do intervalo correto da lista
    if 1 <= nivel <= len(SITUACOES_RESERVATORIO):
        mensagem = SITUACOES_RESERVATORIO[nivel - 1]
        cor = obter_cor_nivel(nivel)
        
        # 3. Exibição concatenando a Cor + Mensagem 
        print(cor + mensagem)
    else:
        print(Fore.RED + f"Erro: Nível {nivel} inválido.")

# --- Simulação do Ambiente Real de Monitoramento ---
if __name__ == "__main__":
    print("=== MONITORAMENTO DO RESERVATÓRIO ===")
    
    # Executa a simulação passando por cada nível (1 a 5) de maneira fixa/definida no código
    exibir_status_reservatorio(1)
    exibir_status_reservatorio(2)
    exibir_status_reservatorio(3)
    exibir_status_reservatorio(4)
    exibir_status_reservatorio(5)
    
    # 4. Restaura o estilo padrão do terminal ao final da execução das mensagens
    print(Style.RESET_ALL)
