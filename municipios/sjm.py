import pandas as pd
from dotenv import load_dotenv
import os 

load_dotenv()

from procedimentos import (
    carregar_audiometria_tonal,
    carregar_biopsia_mama,
    carregar_biopsia_prostata,
    carregar_cirurgia_oftalmologica,
    carregar_colposcopia,
    carregar_consulta_cardio_com_eletro,
    carregar_consulta_especializadas,
    carregar_consulta_oftalmologia,
    carregar_desintometria,
    carregar_ecocardiografia_transtoracica,
    carregar_eletroencefalograma,
    carregar_eletroneuromiografia,
    carregar_endoscopias_digestivas,
    carregar_espirometria,
    carregar_exames_laboratoriais,
    carregar_fisioterapia_atendimento,
    carregar_fisioterapia_consulta,
    carregar_fornecimento_oculos,
    carregar_ginecologia_citopatologico,
    carregar_holter_24h,
    carregar_mapa,
    carregar_mamografia,
    carregar_polissonografia,
    carregar_potencial_evocado_auditivo,
    carregar_proc_oftalmologico,
    carregar_protese_dentaria,
    carregar_radiografia,
    carregar_ressonancia_magnetica,
    carregar_teste_esforco,
    carregar_tomografia,
    carregar_ultrassonografia,
    carregar_us_doppler,
    carregar_vectoeletronistagmografia,
    carregar_videohisteroscopia,
    carregar_videolaringoscopia,
    carregar_todos_procedimentos
)

def analisar_procedimentos_sjm():
    arquivo = os.getenv("arquivo")
    
    try:
        # carregar listas de procedimentos
        ultrassonografias = carregar_ultrassonografia()
        doppler = carregar_us_doppler()
        audiometria_tonal = carregar_audiometria_tonal()
        biopsia_mama = carregar_biopsia_mama()
        biopsia_prostata = carregar_biopsia_prostata()
        cirurgia_oftalmologica = carregar_cirurgia_oftalmologica()
        colposcopia = carregar_colposcopia()
        consulta_cardio_com_eletro = carregar_consulta_cardio_com_eletro()
        consulta_especializadas = carregar_consulta_especializadas()
        consulta_oftalmologia = carregar_consulta_oftalmologia()
        desintometria = carregar_desintometria()
        ecocardiografia_transtoracica = carregar_ecocardiografia_transtoracica()
        eletroencefalograma = carregar_eletroencefalograma()
        eletroneuromiografia = carregar_eletroneuromiografia()
        endoscopias_digestivas = carregar_endoscopias_digestivas()
        espirometria = carregar_espirometria()
        exames_laboratoriais = carregar_exames_laboratoriais()
        fisioterapia_atendimento = carregar_fisioterapia_atendimento()
        fisioterapia_consulta = carregar_fisioterapia_consulta()
        fornecimento_oculos = carregar_fornecimento_oculos()
        ginecologia_citopatologico = carregar_ginecologia_citopatologico()
        holter_24h = carregar_holter_24h()
        mapa = carregar_mapa()
        mamografia = carregar_mamografia()
        polissonografia = carregar_polissonografia()
        potencial_evocado_auditivo = carregar_potencial_evocado_auditivo()
        proc_oftalmologico = carregar_proc_oftalmologico()
        protese_dentaria = carregar_protese_dentaria()
        radiografia = carregar_radiografia()
        ressonancia_magnetica = carregar_ressonancia_magnetica()
        teste_esforco = carregar_teste_esforco()
        tomografia = carregar_tomografia()
        vectoeletronistagmografia = carregar_vectoeletronistagmografia()
        videohisteroscopia = carregar_videohisteroscopia()
        videolaringoscopia = carregar_videolaringoscopia()
        todos_procedimentos = carregar_todos_procedimentos()
        
        tabela = pd.read_excel(arquivo)

        coluna_procedimento = 'São Joao de Meriti'
        coluna_quantidade = 'Quantidade São Joao de Meriti'

        if coluna_procedimento not in tabela.columns:
            print(f"Coluna '{coluna_procedimento}' não encontrada!")
            return
        
        if coluna_quantidade not in tabela.columns:
            print(f"Coluna '{coluna_quantidade}' não encontrada!")
            return
        
        resultados = {}
        
        def process_group(procedimentos):
            total = 0
            for procedimento in procedimentos:
                mask = tabela[coluna_procedimento].astype(str) == procedimento
                quantidade = tabela.loc[mask, coluna_quantidade].sum()  # type: ignore
                if not pd.isna(quantidade) and quantidade > 0:
                    resultados[procedimento] = quantidade
                    total += quantidade
            return total
        
        grupos = {
            "audiometria_tonal": audiometria_tonal,
            "biopsia_mama": biopsia_mama,
            "biopsia_prostata": biopsia_prostata,
            "cirurgia_oftalmologica": cirurgia_oftalmologica,
            "colposcopia": colposcopia,
            "consulta_cardio_com_eletro": consulta_cardio_com_eletro,
            "consulta_especializadas": consulta_especializadas,
            "consulta_oftalmologia": consulta_oftalmologia,
            "desintometria": desintometria,
            "ecocardiografia_transtoracica": ecocardiografia_transtoracica,
            "eletroencefalograma": eletroencefalograma,
            "eletroneuromiografia": eletroneuromiografia,
            "endoscopias_digestivas": endoscopias_digestivas,
            "espirometria": espirometria,
            "exames_laboratoriais": exames_laboratoriais,
            "fisioterapia_atendimento": fisioterapia_atendimento,
            "fisioterapia_consulta": fisioterapia_consulta,
            "fornecimento_oculos": fornecimento_oculos,
            "ginecologia_citopatologico": ginecologia_citopatologico,
            "holter_24h": holter_24h,
            "mapa": mapa,
            "mamografia": mamografia,
            "polissonografia": polissonografia,
            "potencial_evocado_auditivo": potencial_evocado_auditivo,
            "proc_oftalmologico": proc_oftalmologico,
            "protese_dentaria": protese_dentaria,
            "radiografia": radiografia,
            "ressonancia_magnetica": ressonancia_magnetica,
            "teste_esforco": teste_esforco,
            "tomografia": tomografia,
            "ultrassonografia": ultrassonografias,
            "doppler": doppler,
            "vectoeletronistagmografia": vectoeletronistagmografia,
            "videohisteroscopia": videohisteroscopia,
            "videolaringoscopia": videolaringoscopia,
        }
        
        totais = {}
        for nome, lista in grupos.items():
            totais[nome] = process_group(lista or [])
            procedimentoMunicipio = {
                coluna_procedimento: totais.keys(),
                coluna_quantidade: totais.values(),
            }

        df = pd.DataFrame(procedimentoMunicipio)
        df.to_excel("./relatorio-criado-municipio/sjm/{}.xlsx".format(coluna_procedimento), index=False)

        print("=== RESULTADOS {} ===".format(coluna_procedimento))
        for nome, total in totais.items():
            print(f"{nome.replace('_', ' ').title()} Total: {total}")
        soma_total = sum(totais.values())
        print(f"Soma Total: {soma_total}")
        
        print("\n")
        
        todos_procedimentos_conhecidos = []
        for lista in grupos.values():
            todos_procedimentos_conhecidos.extend(lista or [])
        
        todos_procedimentos_conhecidos = list(set([p for p in todos_procedimentos_conhecidos if p and str(p).strip()]))
        
        procedimentos_na_coluna = tabela[coluna_procedimento].dropna().unique()
        procedimentos_na_coluna = [p for p in procedimentos_na_coluna if p and str(p).strip()]
        
        # Encontrar procedimentos que estão na coluna mas não nas listas
        procedimentos_nao_mapeados = {}
        for procedimento in procedimentos_na_coluna:
            if procedimento not in todos_procedimentos_conhecidos:
                mask = tabela[coluna_procedimento].astype(str) == str(procedimento)
                quantidade = tabela.loc[mask, coluna_quantidade].sum()
                if not pd.isna(quantidade) and quantidade > 0:
                    procedimentos_nao_mapeados[procedimento] = quantidade

        procedimentos_nao_mapeados = dict(sorted(procedimentos_nao_mapeados.items(), key=lambda x: x[1], reverse=True))

        if procedimentos_nao_mapeados:
            print(f"\nEncontrados {len(procedimentos_nao_mapeados)} procedimentos não mapeados:")
            total_nao_mapeado = 0
            for procedimento, quantidade in procedimentos_nao_mapeados.items():
                print(f"  '{procedimento}': {quantidade}")
                total_nao_mapeado += quantidade

        procedimentoNaoListado = {
            "Procedimento Nao listados": procedimentos_nao_mapeados.keys(),
            "Quantidade Nao listados": procedimentos_nao_mapeados.values(),
        }

        df = pd.DataFrame(procedimentoNaoListado)
        df.to_excel("./relatorio-criado-municipio/sjm/{}.xlsx".format("Nao-listados"), index=False)
        
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado!")
        return {}, []
    except Exception as e:
        print(f"Erro: {e}")
        return {}, []

