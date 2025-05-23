import os, sys
sys.stdout.reconfigure(encoding="utf-8")  # Corrige acentuação no terminal Windows


def criar_pasta(outputs): 
    if not os .path.exists(outputs): 
        os.makedirs(outputs)
        print(f"Pasta '{outputs}, criada com sucesso")
    else:
        print(f"A pasta '{outputs}' já existe!!!")