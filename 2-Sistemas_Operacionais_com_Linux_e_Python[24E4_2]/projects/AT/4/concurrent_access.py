import concurrent.futures
import threading
import time
import random

database = {
    12345: ("Alice", 8.5),
    23456: ("Bob", 7.0),
    34567: ("Charlie", 9.2),
    45678: ("David", 6.8),
    56789: ("Eve", 7.9),
}

def get_record_by_id(matricula):
    time.sleep(3)
    return database.get(matricula, ("Desconhecido", 0.0))

def get_all_records():
    time.sleep(30)
    return database

def consulta_concorrente(matriculas):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futuros = [executor.submit(get_record_by_id, matricula) for matricula in matriculas]
        resultados = [futuro.result() for futuro in concurrent.futures.as_completed(futuros)]
    return resultados

matriculas_para_consultar = [12345, 23456, 34567, 45678, 56789]
resultados = consulta_concorrente(matriculas_para_consultar)

for matricula, (nome, nota) in zip(matriculas_para_consultar, resultados):
    print(f"Matricula: {matricula}, Nome: {nome}, Nota: {nota}")

nota_media = sum(nota for _, nota in resultados) / len(resultados)
print(f"Nota média: {nota_media}")

def consulta_assincrona():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futuro_all_records = executor.submit(get_all_records)
        time.sleep(1)
        resultado_unico = get_record_by_id(12345)
        print(f"Consulta a uma matrícula: {resultado_unico}")
        futuro_all_records.cancel()

consulta_assincrona()