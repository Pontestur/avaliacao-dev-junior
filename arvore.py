import os
import sys

def gerar_arvore(diretorio, arquivo_saida, nivel=0, excluir=None):
    if excluir is None:
        excluir = []
    
    conteudo = os.listdir(diretorio)
    
    for item in sorted(conteudo):
        caminho = os.path.join(diretorio, item)
        
        if os.path.isdir(caminho):
            if item not in excluir:
                arquivo_saida.write("    " * nivel + "+ " + item + "\n")
                gerar_arvore(caminho, arquivo_saida, nivel + 1, excluir)
        else:
            arquivo_saida.write("    " * nivel + "- " + item + "\n")

def main():
    diretorio_raiz = os.getcwd()
    arquivo_saida = "arvore.txt"
    
    excluir = ["node_modules", ".git"]
    
    if len(sys.argv) > 1:
        excluir.extend(sys.argv[1:])
    
    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write("Estrutura de diretórios:\n")
        gerar_arvore(diretorio_raiz, f, excluir=excluir)
    
    print(f"Árvore de diretórios gerada em {arquivo_saida}")

if __name__ == "__main__":  # Note os dois underscores __ antes e depois
    main()