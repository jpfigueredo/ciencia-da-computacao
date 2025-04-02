import os

def list_files_recursive(directory):
    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)

            if os.path.isfile(item_path):
                print(f"Arquivo: {item_path}")
            elif os.path.isdir(item_path):
                list_files_recursive(item_path)
    except PermissionError:
        print(f"Sem permissão para acessar: {directory}")
    except Exception as e:
        print(f"Erro ao acessar {directory}: {e}")

root_directory = r"D:\BACKUP\Estudos\3° Grau - Ensino Superior\EDS-INFNET\08-Periodo\1 - Velocidade e Qualidade com Estruturas de Dados e Algoritmos [24E4_1]\projects\at-questions"
list_files_recursive(root_directory)
