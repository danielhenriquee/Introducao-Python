# Daniel Henrique da Silva   - Código de pessoa: 8109346 - Número de matrícula: 23.2.2001
# Guilherme Melo             - Código de pessoa: 8576076 - Número de matrícula: 26.1.0379
# Leonardo Pinheiro de Souza - Código de pessoa: 8557802 - Número de matrícula: 25.2.7332

from typing import List, Dict, Optional

alunos: Dict[str, Dict[str, str]] = {}
disciplinas: Dict[str, Dict[str, int]] = {}
matriculas: List[Dict[str, str]] = []

def validar_matricula(matricula: str) -> bool:
    if len(matricula) != 7 or not matricula.isdigit():
        return False
    ano = int(matricula[:4])
    return 1900 <= ano <= 2100

def validar_codigo_disciplina(codigo: str) -> bool:
    if len(codigo) != 5:
        return False
    letra0, letra1 = codigo[0], codigo[1]
    numeros = codigo[2:]
    return letra0.isalpha() and letra1.isalpha() and letra0.isupper() and letra1.isupper() and numeros.isdigit()

def cadastrar_aluno(matricula: str, nome: str) -> bool:
    if not validar_matricula(matricula):
        print("\nFormato inválido. Matrícula deve ter 7 dígitos e os 4 primeiros formam o ano.")
        return False
    if matricula in alunos:
        print("\nMatrícula já cadastrada.")
        return False
    alunos[matricula] = {"nome": nome}
    print("\nAluno cadastrado com sucesso.")
    return True

def listar_alunos() -> List[Dict[str, str]]:
    if not alunos:
        return []
    return [{"matricula": m, "nome": n["nome"]} for m, n in alunos.items()]

def buscar_aluno(matricula: str) -> Optional[Dict[str, str]]:
    return alunos.get(matricula)

def cadastrar_disciplina(codigo: str, nome: str, vagas: int) -> bool:
    if not validar_codigo_disciplina(codigo):
        print("\nFormato inválido. Código deve ser LLNNN (ex: PY001).")
        return False
    if codigo in disciplinas:
        print("\nCódigo já cadastrado.")
        return False 
    try:
        vagas_int = int(vagas)
    except:
        print("\nVagas deve ser número inteiro >= 0.")
        return False
    if vagas_int < 0:
        print("\nVagas deve ser >= 0.")
        return False
    disciplinas[codigo] = {"nome": nome, "vagas": vagas_int}
    print("\nDisciplina cadastrada com sucesso.")
    return True

def listar_disciplinas() -> List[Dict[str, object]]:
    if not disciplinas:
        return []
    return [{"codigo": c, "nome": d["nome"], "vagas": d["vagas"]} for c, d in disciplinas.items()]

def buscar_disciplina(codigo: str) -> Optional[Dict[str, object]]:
    return disciplinas.get(codigo)

def esta_inscrito(matricula: str, codigo: str) -> bool:
    for i in matriculas:
        if i["matricula"] == matricula and i["codigo"] == codigo:
            return True
    return False

def realizar_inscricao(matricula: str, codigo: str) -> bool:
    if not validar_codigo_disciplina(codigo):
        print("\nCódigo de disciplina inválido. Deve ser LLNNN (ex: PY001).")
        return False
    if matricula not in alunos:
        print("\nAluno não cadastrado.")
        return False
    if codigo not in disciplinas:
        print("\nDisciplina não cadastrada.")
        return False
    if esta_inscrito(matricula, codigo):
        print("\nAluno já inscrito nesta disciplina.")
        return False
    if disciplinas[codigo]["vagas"] <= 0:
        print("\nNão há vagas disponíveis.")
        return False 
    matriculas.append({"matricula": matricula, "codigo": codigo})
    disciplinas[codigo]["vagas"] -= 1
    print("\nInscrição realizada com sucesso.")
    return True

def listar_inscricoes() -> List[Dict[str, str]]:
    return [dict(i) for i in matriculas] 

def listar_alunos_por_disciplina(codigo: str) -> Optional[List[Dict[str, str]]]:
    if codigo not in disciplinas:
        return None
    inscritos = [i["matricula"] for i in matriculas if i["codigo"] == codigo]
    return [{"matricula": m, "nome": alunos[m]["nome"]} for m in inscritos]

def listar_disciplinas_por_aluno(matricula: str) -> Optional[List[Dict[str, str]]]:
    if matricula not in alunos:
        return None
    codigos = [i["codigo"] for i in matriculas if i["matricula"] == matricula]
    return [{"codigo": c, "nome": disciplinas[c]["nome"]} for c in codigos]

def listar_disciplinas_vagas_esgotadas() -> List[Dict[str, str]]:
    return [{"codigo": c, "nome": d["nome"]} for c, d in disciplinas.items() if d["vagas"] <= 0]

def leia_inteiro(prompt: str) -> int:
    while True:
        i = input(prompt).strip()
        if i.isdigit():
            return int(i)
        print("Entrada inválida. Digite um número inteiro.")

def menu_gestao_alunos():
    while True:
        print("\n--- Gestão de Alunos ---")
        print("[1] Cadastrar Aluno")
        print("[2] Listar Alunos")
        print("[3] Buscar Aluno por Matrícula")
        print("[4] Voltar")
        op = input("Escolha: ").strip()
        
        if op == "1":
            while True:
                matricula = input("Matrícula (7 dígitos): ").strip()
                if not validar_matricula(matricula):
                    print("Matrícula inválida. Digite novamente.")
                    continue
                if matricula in alunos:
                    print("Matrícula já cadastrada. Digite outra.")
                    continue
                break
            
            nome = input("Nome: ").strip()
            cadastrar_aluno(matricula, nome)
        
        elif op == "2":
            lista = listar_alunos()
            if not lista:
                print("Nenhum aluno cadastrado.")
            else:
                print("Matrícula | Nome")
                for aluno in lista:
                    print(f"{aluno['matricula']} | {aluno['nome']}")
        
        elif op == "3":
            matricula = input("Matrícula: ").strip()
            aluno = buscar_aluno(matricula)
            if aluno:
                print(f"Matrícula: {matricula} | Nome: {aluno['nome']}")
            else:
                print("Aluno não encontrado.")
        
        elif op == "4":
            return
        else:
            print("Opção inválida. Digite 1, 2, 3 ou 4.")

def menu_gestao_disciplinas():
    while True:
        print("\n--- Gestão de Disciplinas ---")
        print("[1] Cadastrar Disciplina")
        print("[2] Listar Disciplinas")
        print("[3] Buscar Disciplina por Código")
        print("[4] Voltar")
        op = input("Escolha: ").strip()
        
        if op == "1":
            while True:
                codigo = input("Código (LLNNN): ").strip()
                if not validar_codigo_disciplina(codigo):
                    print("Código inválido. Digite novamente.")
                    continue
                if codigo in disciplinas:
                    print("Código já cadastrado. Digite outro.")
                    continue
                break
            
            nome = input("Nome: ").strip()
            
            while True:
                vagas = input("Vagas (inteiro >= 0): ").strip()
                if not vagas.isdigit() or int(vagas) < 0:
                    print("Vagas inválidas. Digite novamente.")
                    continue
                break
            
            cadastrar_disciplina(codigo, nome, vagas)
        
        elif op == "2":
            lista = listar_disciplinas()
            if not lista:
                print("Nenhuma disciplina cadastrada.")
            else:
                print("Código | Nome | Vagas")
                for disciplina in lista:
                    print(f"{disciplina['codigo']} | {disciplina['nome']} | {disciplina['vagas']}")
        
        elif op == "3":
            codigo = input("Código: ").strip()
            disciplina = buscar_disciplina(codigo)
            if disciplina:
                print(f"Código: {codigo} | Nome: {disciplina['nome']} | Vagas: {disciplina['vagas']}")
            else:
                print("Disciplina não encontrada.")
        
        elif op == "4":
            return
        else:
            print("Opção inválida. Digite 1, 2, 3 ou 4.")

def menu_gestao_matriculas():
    while True:
        print("\n--- Gestão de Matrículas ---")
        print("[1] Realizar Inscrição")
        print("[2] Listar Inscrições")
        print("[3] Voltar")
        op = input("Escolha: ").strip()
        if op == "1":
            while True:
                matricula = input("Matrícula do aluno: ").strip()
                if not validar_matricula(matricula) or matricula not in alunos:
                    print("Matrícula inválida ou não cadastrada. Digite novamente.")
                    continue
                break

            while True:
                codigo = input("Código da disciplina: ").strip()
                if not validar_codigo_disciplina(codigo) or codigo not in disciplinas:
                    print("Código inválido ou disciplina não cadastrada. Digite novamente.")
                    continue
                if esta_inscrito(matricula, codigo):
                    print("Aluno já inscrito nesta disciplina.")
                    continue
                if disciplinas[codigo]["vagas"] <= 0:
                    print("Não há vagas disponíveis.")
                    continue
                break

            realizar_inscricao(matricula, codigo)
        elif op == "2":
            inscricao = listar_inscricoes()
            if not inscricao:
                print("Nenhuma inscrição realizada.")
            else:
                print("Matrícula | Código | Nome Aluno | Nome Disciplina")
                for i in inscricao:
                    nome_aluno = alunos[i["matricula"]]["nome"]
                    nome_disciplina = disciplinas[i["codigo"]]["nome"]
                    print(f"{i['matricula']} | {i['codigo']} | {nome_aluno} | {nome_disciplina}")
        elif op == "3":
            return
        else:
            print("Opção inválida. Digite 1, 2 ou 3.")

def menu_relatorios():
    while True:
        print("\n--- Geração de Relatórios ---")
        print("[1] Listar Alunos por Disciplina")
        print("[2] Listar Disciplinas por Aluno")
        print("[3] Listar Disciplinas com Vagas Esgotadas")
        print("[4] Voltar")
        op = input("Escolha: ").strip()
        if op == "1":
            codigo = input("Código da disciplina: ").strip()
            while not validar_codigo_disciplina(codigo):
                print("Código inválido. Digite novamente.")
                codigo = input("Código da disciplina: ").strip()
            retorno = listar_alunos_por_disciplina(codigo)
            if retorno is None:
                print("Disciplina não cadastrada.")
            elif not retorno:
                print("Nenhum aluno inscrito nesta disciplina.")
            else:
                print("Matrícula | Nome")
                for r in retorno:
                    print(f"{r['matricula']} | {r['nome']}")
        elif op == "2":
            matricula = input("Matrícula do aluno: ").strip()
            while not validar_matricula(matricula):
                print("Matrícula inválida. Digite novamente.")
                matricula = input("Matrícula do aluno: ").strip()
            retorno = listar_disciplinas_por_aluno(matricula)
            if retorno is None:
                print("Aluno não cadastrado.")
            elif not retorno:
                print("Aluno não inscrito em nenhuma disciplina.")
            else:
                print("Código | Nome")
                for r in retorno:
                    print(f"{r['codigo']} | {r['nome']}")
        elif op == "3":
            disciplinas_esgotadas = listar_disciplinas_vagas_esgotadas()
            if not disciplinas_esgotadas:
                print("Nenhuma disciplina com vagas esgotadas.")
            else:
                print("Código | Nome")
                for disciplina in disciplinas_esgotadas:
                    print(f"{disciplina['codigo']} | {disciplina['nome']}")
        elif op == "4":
            return
        else:
            print("Opção inválida. Digite 1, 2, 3 ou 4.")

while True:
    print("\n====== Sistema de Gestão Acadêmica - Universidade Python ======")
    print("[1] Gestão de Alunos")
    print("[2] Gestão de Disciplinas")
    print("[3] Gestão de Matrículas")
    print("[4] Geração de Relatórios")
    print("[5] Sair")
    print("==============================================================")
    escolha = input("Escolha: ").strip()
    if escolha == "1":
        menu_gestao_alunos()
    elif escolha == "2":
        menu_gestao_disciplinas()
    elif escolha == "3":
        menu_gestao_matriculas()
    elif escolha == "4":
        menu_relatorios()
    elif escolha == "5":
        print("Encerrando programa.")
        break
    else:
        print("Opção inválida. Digite 1, 2, 3, 4 ou 5.")