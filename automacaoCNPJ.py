# No que consiste a automação:
# abrir um arquivo TXT com vários CNPJ,
# consultar cada CNPJ na API do Invertexto
# salvar o resultado da consulta no banco de dados
# Só devem ser consultados os novos dados inseridos
import re
from idlelib.debugger_r import restart_subprocess_debugger

import pymysql
import requests
from consultaCNPJ import response
from tokenCNPJ import API_TOKEN
# Conexão com o banco de dados MySQL

def conectar_banco():
   conn = pymysql.connect(
        host='localhost',
        user='root',
        password='admin',
        port=3306,
        database='cnpjs'
   )
   conn_cursor = conn.cursor()
   return conn, conn_cursor

def consultar_cadastro(cnpj_procurado):
    conexao_consulta, cursor_consulta = conectar_banco()
    query = '''
    SELECT COUNT(*) FROM cnpjs WHERE cnpj = %s;
    '''
    cursor_consulta.execute(query,(cnpj_corrigido,))
    resultado = int(cursor_consulta.fetchone()[0]) > 0
    cursor_consulta.close()
    conexao_consulta.close()
    return resultado

# Lê todos os CNPJs do arquivo TXT
cnpjs = (open(r'C:\Users\75955\Desktop\automacoes em python\cnpj.txt', 'r')
        .read().splitlines())
for cnpj in cnpjs:
    cnpj_corrigido = re.sub(r'\D', '', cnpj)  # Remove pontuação e mantém só os números
    if consultar_cadastro(cnpj_corrigido):
        print(f'cnpj {cnpj} já cadastrado')
        continue
    url = f'https://api.invertexto.com/v1/cnpj/{cnpj_corrigido}?token={API_TOKEN}'
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        razao_social = dados['razao_social']
        data_inicio = dados['data_inicio']

        # Insere os dados no banco de dados
        conexao, cursor = conectar_banco()
        query = 'INSERT INTO cnpjs (cnpj, razaoSocial, dataInicio) VALUES (%s, %s, %s);'
        valores = (cnpj_corrigido, razao_social, data_inicio)
        cursor.execute(query, valores)
        conexao.commit()
        cursor.close()
        conexao.close()
        continue

    if response.status_code == 422:
        print(f'CNPJ {cnpj} não foi encontrado')
        continue