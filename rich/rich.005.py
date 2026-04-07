from rich.traceback import install
from rich import print
install()

def div(x, y):
    return x / y

print(div(50,2))

from rich.progress import track
from time import sleep

# Exemplo: Processando uma lista de alunos ou exercícios do Mundo 4
tarefas = [f"Exercício {i}" for i in range(1, 50)]

# O 'track' envolve a sua lista e cuida da barra de progresso sozinho
for tarefa in track(tarefas, description="[cyan]Processando Mundo 4..."):
    # Simula o processamento do código
    sleep(0.5)
    print(f" Concluído: {tarefa}")

print("[bold green]Foco total! Mais um passo para a Engenharia de IA.[/bold green]")