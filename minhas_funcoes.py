
"""
#=========================================================
# 👓 01. SOBRE
#=========================================================

MÓDULO DE FUNÇÕES PARA O MINI-PROJETO 1 (Vínculo)
=========================================================
MINI-PROJETO: Pipeline de ETL com Python Puro
=========================================================
Aqui você encontrará a estrutura das funções preparadas 
para serem utilizadas no módulo principal (sanitizacao.ipynb).
Utilizamos apenas Python puro, e as bibliotecas básicas 
listadas abaixo.
"""
import re                                  # Biblioteca padrão para expressões regulares, usada para manipulação de strings.
import csv                                 # Biblioteca padrão para leitura e escrita de arquivos CSV. 
from datetime import datetime              # Biblioteca padrão para manipulação de datas e horas.  
from typing import List, Dict, Any, Union  # Biblioteca padrão para dicas de tipo (type hints), usada para melhorar a legibilidade e manutenção do código.

"""
#=========================================================
# 💡 02. LEMBRETES
#=========================================================

01. Type Hints (dicas de tipo) para melhorar a legibilidade e manutenção do código.

    A explicitação dos tipos de variáveis e parâmetros em funções no Python é chamada de Type Hints (dicas de tipo) ou
    Type Annotations (anotações de tipo). Essa prática (introduzida pelo PEP 484) permite definir o tipo esperado para
    cada argumento da função e o tipo do dado que ela vai retornar

02. Cores:

    Estilo/Cor	Código
    Negrito	    \033[1m
    Vermelho	\033[31m
    Verde	    \033[32m
    Amarelo	    \033[33m
    Azul	    \033[34m
    Reset	    \033[0m

    Ex: ERRO = "\033[1;31m" 
        RESET = "\033[0m"
        print(f"{ERRO}ERRO CRÍTICO:{RESET} O arquivo não foi encontrado.")

 """
#=========================================================
# 💡 03. VARIÁVEIS DE AMBIENTE
#=========================================================

TERMOS_NULOS: tuple = (
    '', 'null', 'none', 'undefined', 'nan', 'nulo', 
    'vazio', 'na', 'n/a', '-', '--', '.', '?'
)

NEGRITO = "\033[1m"
ERRO = "\033[1;31m"
RESET = "\033[0m"
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"

#=========================================================
# 📆 04. FUNÇÕES PARA DATAS
#=========================================================

def FormatarData(data: str) -> str:
    """
    Objetivo: Converter string de data para o formato 'DD/MM/YYYY'.
    """
    if not data:
        return ""   
    data_br = (datetime.strptime(data, "%Y-%m-%d %H:%M:%S")).strftime("%d/%m/%Y")
    return data_br

def CalcularMedianaDataColuna(base_dados: List[Dict[str, Any]], coluna_alvo: str) -> str:
    """
    Calcula a mediana de uma coluna de datas (formato americano com hora)
    e retorna apenas a data formatada no padrão brasileiro (DD/MM/YYYY).
    """
    datas_existentes: List[datetime] = []    
    for linha in base_dados:
        valor_texto = str(linha.get(coluna_alvo, '')).strip()        
        if valor_texto.lower() not in TERMOS_NULOS:  
            try:
                # 1. Lê a string no formato americano com hora (ex: "2026-05-30 14:35:20")
                # Se o formato usar "T" (ex: 2026-05-30T14:35:20), mude o espaço por 'T' abaixo
                dt_objeto = datetime.strptime(valor_texto, "%Y-%m-%d %H:%M:%S")
                datas_existentes.append(dt_objeto)
            except ValueError:
                # Caso a string não esteja no formato esperado, pula a linha
                continue                
    # 2. Ordena as datas da mais antiga para a mais recente
    datas_existentes.sort()
    qtd_elementos: int = len(datas_existentes)    
    if qtd_elementos == 0:
        return "" # Ou uma string padrão, ex: "00/00/0000"        
    # 3. Lógica da Mediana
    if qtd_elementos % 2 == 1:
        # Se for ímpar, pega o elemento do meio exatamente
        data_mediana = datas_existentes[qtd_elementos // 2]
    else:
        # Se for par, calcula o ponto médio entre as duas datas centrais
        meio1 = datas_existentes[(qtd_elementos // 2) - 1]
        meio2 = datas_existentes[qtd_elementos // 2]        
        # Tirando a média usando a diferença de tempo (timestamp)
        timestamp_medio = (meio1.timestamp() + meio2.timestamp()) / 2
        data_mediana = datetime.fromtimestamp(timestamp_medio)    
    # 4. Retorna apenas a data simples formatada no padrão brasileiro
    return data_mediana.strftime("%d/%m/%Y")

#=========================================================
# 🖍 05. FUNÇÕES PARA STRINGS
#=========================================================

def RetirarCaracteresEspeciais(texto: Any) -> str:
    if not texto: 
        return ""
    return re.sub(r'[^\w\s]', '', str(texto))

def RetirarEspacosExtras(texto: Any) -> str:
    if not texto: 
        return ""
    return re.sub(r'\s+', ' ', str(texto)).strip()

def NormalizarString(valor_original: Any, substituir: str, letras: str = "original") -> str:
    """
    Remove espaços, valida valores nulos/vazios e padroniza a string.
    Retorna o valor do parâmetro 'substituir' caso seja nulo, ou o texto limpo.
    """
    if not valor_original:
        return substituir        
    valor_texto = str(valor_original).strip()
    if valor_texto.lower() in TERMOS_NULOS:
        return substituir
    texto_limpo = RetirarCaracteresEspeciais(valor_texto)
    texto_limpo = RetirarEspacosExtras(texto_limpo)
    formatos: Dict[str, str] = {
        "minusculas": texto_limpo.lower(),
        "maiusculas": texto_limpo.upper(),
        "iniciais_maiusculas": texto_limpo.title()
    }    
    return formatos.get(letras, texto_limpo)

def NormalizarValorDecimal(valor_original: Any) -> float:
    if not valor_original:
        return 0.0    
    texto_limpo = RetirarEspacosExtras(str(valor_original))
    texto_limpo = texto_limpo.replace(',', '.')    
    try:
        return float(texto_limpo)
    except ValueError:
        return 0.0
    
def NormalizarValorInteiro(valor_original: Any) -> int:
    if not valor_original:
        return 0        
    texto_limpo = RetirarEspacosExtras(str(valor_original))
    texto_limpo = texto_limpo.replace(',', '.')       
    try:
        return int(float(texto_limpo))
    except ValueError:
        return 0

#=========================================================
# 🔍 06. FUNÇÕES PARA ANÁLISE DE DADOS
#=========================================================

def ExibirDados(mensagem: str,dados: List[Dict[str, Any]], qtd_linhas: int) -> None:
    print(mensagem)
    for linha in dados[:qtd_linhas]:
        print(list(linha.values()))
    print("-" * 100)
    return

def ContarValoresNulos(base_dados: List[Dict[str, Any]], coluna: str, exibir: str) -> int:
    qtd_nulo: int = 0   
    for linha in base_dados:
        # Garante que estamos acessando o dicionário corretamente
        if isinstance(linha, dict) and coluna in linha:
            valor = linha[coluna]
            if valor is None or str(valor).lower() == 'nan':
                qtd_nulo += 1
            elif str(valor).strip().lower() in TERMOS_NULOS:
                qtd_nulo += 1
        else:
            qtd_nulo += 1           
    if exibir != "":
        # Se qtd_nulo for maior que zero, aplica o vermelho negrito senão exibe normal
        print(f"{exibir}: {NEGRITO}{VERMELHO}{qtd_nulo:,}{RESET}".replace(",", ".") if qtd_nulo > 0 else f"{exibir}: {qtd_nulo}")        
    return qtd_nulo

def CalcularMedianaColuna(base_dados: List[Dict[str, Any]], coluna_alvo: str) -> int:
    """
    Calcula e retorna a mediana de uma coluna específica da lista de dicionários.
    """
    valores_existentes: List[int] = []
    for linha in base_dados:
        valor_texto = str(linha.get(coluna_alvo, '')).strip()
        if valor_texto.lower() not in TERMOS_NULOS:  
            try:
                valores_existentes.append(int(float(valor_texto)))
            except ValueError:
                continue                
    valores_existentes.sort()
    qtd_elementos: int = len(valores_existentes)    
    if qtd_elementos == 0:
        return 0
    elif qtd_elementos % 2 == 1:
        return valores_existentes[qtd_elementos // 2]
    else:
        meio1 = valores_existentes[(qtd_elementos // 2) - 1]
        meio2 = valores_existentes[qtd_elementos // 2]
        return (meio1 + meio2) // 2

#=========================================================
# 📂 07. FUNÇÕES PARA ARQUIVOS
#=========================================================

def GerarArquivoCSV(dados: List[Dict[str, Any]], nome_arq_saida: str) -> None:   
    try:
        # Pegar as chaves (colunas) do primeiro registro da lista
        # Como o primeiro já passou pelo laço, ele já possui as colunas novas (flags)
        cabecalho_saida = list(dados[0].keys())
        print(f"Novo cabeçalho gerado com {NEGRITO}{VERDE}{len(cabecalho_saida)}{RESET} colunas: {cabecalho_saida}")
        print(f"Iniciando a gravação do arquivo: {nome_arq_saida}...")  
        # Abre o arquivo em modo de escrita ('w') garantindo o padrão UTF-8 e quebra de linhas correta
        # O caminho "dados_limpos/" foi criado para uma boa organização dos arquivos gerados, evitando misturar com os dados originais.
        with open("dados_limpos/" + nome_arq_saida, mode='w', encoding='utf-8', newline='') as arquivo_csv:       
            # Cria o escritor de dicionários mapeando as colunas definidas
            escritor = csv.DictWriter(arquivo_csv, fieldnames=cabecalho_saida)
            # Grava a primeira linha do arquivo com os nomes das colunas
            escritor.writeheader()
            # Grava todas as linhas da lista 'dados' de uma só vez
            escritor.writerows(dados)
        print(f"{NEGRITO}{VERDE}✓ Sucesso! Arquivo gerado com {len(dados):,} linhas.{RESET}".replace(",", "."))
    except Exception as erro:
        print(f"{NEGRITO}{VERMELHO}❌Erro ao tentar gravar o arquivo CSV: {erro}{RESET}")
    return