import pandas as pd

def carregar(procedimento):
    arquivo_excel = "Procedimento  Marque fácil.xlsx"
    tabela = pd.read_excel(arquivo_excel)
    coluna = [x for x in tabela[procedimento].to_list() if pd.notna(x) and x not in [None, '']] 
    return coluna

def carregar_audiometria_tonal():
    return carregar("AUDIOMETRIA TONAL LIMIAR IMPED e LOGOAUDOMETRIA (LDV-IRF-LRF)")

def carregar_biopsia_mama():
    return carregar("BIÓPSIA MAMA")

def carregar_biopsia_prostata():
    return carregar("BIÓPSIA PRÓSTATA")

def carregar_cirurgia_oftalmologica():
    return carregar("CIRURGIA OFTALMOLOGICA")

def carregar_colposcopia():
    return carregar("COLPOSCOPIA COM BIOPSIA E RESULTADO DA BIOPSIA")

def carregar_consulta_cardio_com_eletro():
    return carregar("CONSULTAS CARDIO C/ ELETRO")

def carregar_consulta_especializadas():
    return carregar("CONSULTAS ESPECIALIZADAS")

def carregar_consulta_oftalmologia():
    return carregar("CONSULTAS OFTALMOLOGIA")

def carregar_desintometria():
    return carregar("DESINTOMETRIA")

def carregar_ecocardiografia_transtoracica():
    return carregar("ECOCARDIOGRAFIA TRANSTORACICA")

def carregar_eletroencefalograma():
    return carregar("ELETROENCEFALOGRAMA")

def carregar_eletroneuromiografia():
    return carregar("ELETRONEUROMIOGRAFIA")

def carregar_endoscopias_digestivas():
    return carregar("ENDOSCOPIAS DIGESTIVAS (ALTA E BAIXA)")

def carregar_espirometria():
    return carregar("ESPIROMETRIA")

def carregar_exames_laboratoriais():
    return carregar("EXAMES LABORATORIAIS")

def carregar_fisioterapia_atendimento():
    return carregar("FISIOTERAPIA ATENDIMENTO (SESSÕES)")

def carregar_fisioterapia_consulta():
    return carregar("FISIOTERAPIA CONSULTA")

def carregar_fornecimento_oculos():
    return carregar("FORNECIMENTO DE ÓCULOS DE GRAU, INCLUINDO A ARMAÇÃO E AS LENTES CORRETIVAS CONFORME INDICAÇÃO MEDICA")

def carregar_ginecologia_citopatologico():
    return carregar("GINECOLOGIA E COLETA MATERIAL EXAME CITOPATOLOGICO COLO UTERINO C/ RESULTADO E CONSULTA DE RETORNO GINECOLOGIA")

def carregar_holter_24h():
    return carregar("HOLTER 24H(3 CANAIS)")

def carregar_mapa():
    return carregar("M.A.P.A.")

def carregar_mamografia():
    return carregar("MAMOGRAFIA")

def carregar_polissonografia():
    return carregar("POLISSONOGRAFIA")

def carregar_potencial_evocado_auditivo():
    return carregar("POTENCIAL EVOCADO AUDITIVO PARA TRIAGEM AUDITIVA (TESTE DA ORELHINHA)")

def carregar_proc_oftalmologico():
    return carregar("PROC. OFTALMOLOGICO")

def carregar_protese_dentaria():
    return carregar("PROTESE DENTARIA")

def carregar_radiografia():
    return carregar("RADIOGRAFIA")

def carregar_ressonancia_magnetica():
    return carregar("RESSONANCIA MAGNETICA")

def carregar_teste_esforco():
    return carregar("TESTE DE ESFORCO / TESTE ERGOMETRICO")

def carregar_tomografia():
    return carregar("TOMOGRAFIA")

def carregar_ultrassonografia():
    return carregar("ULTRASSONOGRAFIA")

def carregar_us_doppler():
    return carregar("US DOPPLER")

def carregar_vectoeletronistagmografia():
    return carregar("VECTOELETRONISTAGMOGRAFIA/ testes vestibulares")

def carregar_videohisteroscopia():
    return carregar("VIDEOHISTEROSCOPIA")

def carregar_videolaringoscopia():
    return carregar("VIDEOLARINGOSCOPIA")

def carregar_todos_procedimentos():
    procedimentos = [
        "AUDIOMETRIA TONAL LIMIAR IMPED e LOGOAUDOMETRIA (LDV-IRF-LRF)",
        "BIÓPSIA MAMA",
        "BIÓPSIA PRÓSTATA",
        "CIRURGIA OFTALMOLOGICA",
        "COLPOSCOPIA COM BIOPSIA E RESULTADO DA BIOPSIA",
        "CONSULTAS CARDIO C/ ELETRO",
        "CONSULTAS ESPECIALIZADAS",
        "CONSULTAS OFTALMOLOGIA",
        "DESINTOMETRIA",
        "ECOCARDIOGRAFIA TRANSTORACICA",
        "ELETROENCEFALOGRAMA",
        "ELETRONEUROMIOGRAFIA",
        "ENDOSCOPIAS DIGESTIVAS (ALTA E BAIXA)",
        "ESPIROMETRIA",
        "EXAMES LABORATORIAIS",
        "FISIOTERAPIA ATENDIMENTO (SESSÕES)",
        "FISIOTERAPIA CONSULTA",
        "FORNECIMENTO DE ÓCULOS DE GRAU, INCLUINDO A ARMAÇÃO E AS LENTES CORRETIVAS CONFORME INDICAÇÃO MEDICA",
        "GINECOLOGIA E COLETA MATERIAL EXAME CITOPATOLOGICO COLO UTERINO C/ RESULTADO E CONSULTA DE RETORNO GINECOLOGIA",
        "HOLTER 24H(3 CANAIS)",
        "M.A.P.A.",
        "MAMOGRAFIA",
        "POLISSONOGRAFIA",
        "POTENCIAL EVOCADO AUDITIVO PARA TRIAGEM AUDITIVA (TESTE DA ORELHINHA)",
        "PROC. OFTALMOLOGICO",
        "PROTESE DENTARIA",
        "RADIOGRAFIA",
        "RESSONANCIA MAGNETICA",
        "TESTE DE ESFORCO / TESTE ERGOMETRICO",
        "TOMOGRAFIA",
        "ULTRASSONOGRAFIA",
        "US DOPPLER",
        "VECTOELETRONISTAGMOGRAFIA/ testes vestibulares",
        "VIDEOHISTEROSCOPIA",
        "VIDEOLARINGOSCOPIA"
    ]
    
    todos_dados = {}
    for procedimento in procedimentos:
        nome_funcao = procedimento.lower().replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "").replace(",", "").replace(".", "")
        todos_dados[nome_funcao] = carregar(procedimento)
    
    return todos_dados

if __name__ == "__main__":
    ultrassonografias = carregar_ultrassonografia()
    for ultrassonografia in ultrassonografias:
        print(ultrassonografia)