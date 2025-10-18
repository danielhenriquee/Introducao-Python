# Daniel Henrique da Silva   - Código de pessoa: 8109346 - Número de matrícula: 23.2.2001
# Guilherme Melo             - Código de pessoa: 8576076 - Número de matrícula: 26.1.0379
# Leonardo Pinheiro de Souza - Código de pessoa: 8557802 - Número de matrícula: 25.2.7332

alunos: dict[str, dict[str, str]] = {}
disciplinas: dict[str, dict[str, int]] = {}
matriculas: list[dict[str, str]] = []

def validar_matricula(matricula: str) -> bool:
    return len(matricula) == 7 and matricula.isdigit() and 1900 <= int(matricula[:4]) <= 2100

def validar_codigo_disciplina(codigo: str) -> bool:
    return len(codigo) == 5 and codigo[:2].isalpha() and codigo[:2].isupper() and codigo[2:].isdigit()

def validar_vagas(vagas: str) -> bool:
    return vagas.isdigit() and int(vagas) >= 0

def input_matricula(prompt: str, existe: bool | None = None) -> str:
    while True:
        matricula = input(prompt).strip()
        if not validar_matricula(matricula):
            print("Matrícula inválida. Deve ter 7 dígitos e os 4 primeiros formam o ano.")
            continue
        if existe is True and matricula not in alunos:
            print("Matrícula não cadastrada.")
            continue
        if existe is False and matricula in alunos:
            print("Matrícula já cadastrada.")
            continue
        return matricula

def input_codigo_disciplina(prompt: str, existe: bool | None = None) -> str:
    while True:
        codigo = input(prompt).strip()
        if not validar_codigo_disciplina(codigo):
            print("Código inválido. Deve ser LLNNN (ex: PY001).")
            continue
        if existe is True and codigo not in disciplinas:
            print("Disciplina não cadastrada.")
            continue
        if existe is False and codigo in disciplinas:
            print("Código já cadastrado.")
            continue
        return codigo

def input_vagas(prompt: str) -> int:
    while True:
        vagas = input(prompt).strip()
        if not validar_vagas(vagas):
            print("Vagas inválidas. Digite um inteiro >= 0.")
            continue
        return int(vagas)

def input_codigo_matricula(prompt: str, matricula: str) -> str:
    while True:
        codigo = input_codigo_disciplina(prompt, existe=True)
        if esta_inscrito(matricula, codigo):
            print("Aluno já inscrito nesta disciplina.")
            continue
        if disciplinas[codigo]["vagas"] <= 0:
            print("Não há vagas disponíveis.")
            continue
        return codigo
    
def cadastrar_aluno(matricula: str, nome: str) -> tuple[bool, str]:
    if matricula in alunos:
        return False, "Matrícula já cadastrada."
    alunos[matricula] = {"nome": nome}
    return True, "Aluno cadastrado com sucesso."

def listar_alunos() -> list[dict[str, str]]:
    return sorted([{"matricula": m, "nome": d["nome"]} for m, d in alunos.items()], key = lambda x: x["matricula"])

def buscar_aluno(matricula: str) -> dict[str, str] | None:
    return alunos.get(matricula)

def cadastrar_disciplina(codigo: str, nome: str, vagas: int) -> tuple[bool, str]:
    if codigo in disciplinas:
        return False, "Código já cadastrado."
    disciplinas[codigo] = {"nome": nome, "vagas": vagas}
    return True, "Disciplina cadastrada com sucesso."

def listar_disciplinas() -> list[dict[str, str | int]]:
    return sorted([{"codigo": c, "nome": d["nome"], "vagas": d["vagas"]} for c, d in disciplinas.items()], key = lambda x: x["codigo"])

def buscar_disciplina(codigo: str) -> dict[str, str | int] | None:
    return disciplinas.get(codigo)

def esta_inscrito(matricula: str, codigo: str) -> bool:
    for i in matriculas:
        if i["matricula"] == matricula and i["codigo"] == codigo:
            return True
    return False

def realizar_inscricao(matricula: str, codigo: str) -> tuple[bool, str]:
    if esta_inscrito(matricula, codigo):
        return False, "Aluno já inscrito nesta disciplina."
    if disciplinas[codigo]["vagas"] <= 0:
        return False, "Não há vagas disponíveis."
    matriculas.append({"matricula": matricula, "codigo": codigo})
    disciplinas[codigo]["vagas"] -= 1
    return True, "Inscrição realizada com sucesso."

def listar_inscricoes() -> list[dict[str, str]]:
    return [dict(i) for i in matriculas] 

def listar_alunos_por_disciplina(codigo: str) -> list[dict[str, str]] | None:
    if codigo not in disciplinas:
        return None
    return sorted([{"matricula": m, "nome": alunos[m]["nome"]} for m in [i["matricula"] for i in matriculas if i["codigo"] == codigo]], key = lambda x: x["matricula"])

def listar_disciplinas_por_aluno(matricula: str) -> list[dict[str, str]] | None:
    if matricula not in alunos:
        return None
    return sorted([{"codigo": c, "nome": disciplinas[c]["nome"]} for c in [i["codigo"] for i in matriculas if i["matricula"] == matricula]], key = lambda x: x["codigo"])

def listar_disciplinas_vagas_esgotadas() -> list[dict[str, str]]:
    return [{"codigo": c, "nome": d["nome"]} for c, d in disciplinas.items() if d["vagas"] <= 0]

def menu_gestao_alunos():
    while True:
        print("\n--- Gestão de Alunos ---")
        print("[1] Cadastrar Aluno\n[2] Listar Alunos\n[3] Buscar Aluno por Matrícula\n[4] Voltar")
        op = input("Escolha: ").strip()
        if op == "1":
            matricula = input_matricula("Matrícula (7 dígitos e os 4 primeiros formam o ano): ", existe=False)
            while True:
                nome = input("Nome: ").strip()
                if not nome:
                    print("Nome não pode ser vazio.")
                    continue
                break
            ok, msg = cadastrar_aluno(matricula, nome)
            print(msg)
        elif op == "2":
            lista = listar_alunos()
            if not lista:
                print("Nenhum aluno cadastrado.")
            else:
                print(f"{'Matrícula':<10} | {'Nome':<30}")
                print("-"*43)
                for aluno in lista:
                    print(f"{aluno['matricula']:<10} | {aluno['nome']:<30}")
        elif op == "3":
            matricula = input_matricula("Matrícula: ", existe = True)
            aluno = buscar_aluno(matricula)
            print(f"Matrícula: {matricula} | Nome: {aluno['nome']}" if aluno else "Aluno não encontrado.")
        elif op == "4":
            return
        else:
            print("Opção inválida. Digite 1-4.")

def menu_gestao_disciplinas():
    while True:
        print("\n--- Gestão de Disciplinas ---")
        print("[1] Cadastrar Disciplina\n[2] Listar Disciplinas\n[3] Buscar Disciplina por Código\n[4] Voltar")
        op = input("Escolha: ").strip()
        if op == "1":
            codigo = input_codigo_disciplina("Código (LLNNN): ", existe=False)
            while True:
                nome = input("Nome da disciplina: ").strip()
                if not nome:
                    print("Nome da disciplina não pode ser vazio.")
                    continue
                break
            vagas = input_vagas("Vagas (inteiro >= 0): ")
            ok, msg = cadastrar_disciplina(codigo, nome, vagas)
            print(msg)
        elif op == "2":
            lista = listar_disciplinas()
            if not lista:
                print("Nenhuma disciplina cadastrada.")
            else:
                print(f"{'Código':<8} | {'Nome':<30} | {'Vagas':<5}")
                print("-"*46)
                for d in lista:
                    print(f"{d['codigo']:<8} | {d['nome']:<30} | {d['vagas']:<5}")
        elif op == "3":
            codigo = input_codigo_disciplina("Código: ", existe=True)
            disciplina = buscar_disciplina(codigo)
            if disciplina:
                print(f"{'Código':<8} | {'Nome':<30} | {'Vagas':<5}")
                print("-"*46)
                print(f"{codigo:<8} | {disciplina['nome']:<30} | {disciplina['vagas']:<5}")
            else:
                print("Disciplina não encontrada.")
        elif op == "4":
            return
        else:
            print("Opção inválida. Digite 1-4.")

def menu_gestao_matriculas():
    while True:
        print("\n--- Gestão de Matrículas ---")
        print("[1] Realizar Inscrição\n[2] Listar Inscrições\n[3] Voltar")
        op = input("Escolha: ").strip()
        if op == "1":
            matricula = input_matricula("Matrícula do aluno: ", existe=True)
            codigo = input_codigo_matricula("Código da disciplina: ", matricula)
            ok, msg = realizar_inscricao(matricula, codigo)
            print(msg)
        elif op == "2":
            inscricoes = listar_inscricoes()
            if not inscricoes:
                print("Nenhuma inscrição realizada.")
            else:
                print(f"{'Matrícula':<10} | {'Código':<8} | {'Nome Aluno':<30} | {'Nome Disciplina':<30}")
                print("-"*86)
                for i in inscricoes:
                    print(f"{i['matricula']:<10} | {i['codigo']:<8} | {alunos[i['matricula']]['nome']:<30} | {disciplinas[i['codigo']]['nome']:<30}")
        elif op == "3":
            return
        else:
            print("Opção inválida. Digite 1-3.")

def menu_relatorios():
    while True:
        print("\n--- Geração de Relatórios ---")
        print("[1] Listar Alunos por Disciplina\n[2] Listar Disciplinas por Aluno\n[3] Listar Disciplinas com Vagas Esgotadas\n[4] Voltar")
        op = input("Escolha: ").strip()
        if op == "1":
            codigo = input_codigo_disciplina("Código da disciplina: ", existe=True)
            retorno = listar_alunos_por_disciplina(codigo)
            if not retorno:
                print("Nenhum aluno inscrito nesta disciplina.")
            else:
                print(f"{'Matrícula':<10} | {'Nome':<30}")
                print("-"*43)
                for r in retorno:
                    print(f"{r['matricula']:<10} | {r['nome']:<30}")
        elif op == "2":
            matricula = input_matricula("Matrícula do aluno: ", existe=True)
            retorno = listar_disciplinas_por_aluno(matricula)
            if not retorno:
                print("Aluno não inscrito em nenhuma disciplina.")
            else:
                print(f"{'Código':<8} | {'Nome':<30}")
                print("-"*40)
                for r in retorno:
                    print(f"{r['codigo']:<8} | {r['nome']:<30}")
        elif op == "3":
            esgotadas = listar_disciplinas_vagas_esgotadas()
            if not esgotadas:
                print("Nenhuma disciplina com vagas esgotadas.")
            else:
                print(f"{'Código':<8} | {'Nome':<30}")
                print("-"*40)
                for d in esgotadas:
                    print(f"{d['codigo']:<8} | {d['nome']:<30}")

        elif op == "4":
            return
        else:
            print("Opção inválida. Digite 1-4.")

while True:
    print("\n====== Sistema de Gestão Acadêmica - Universidade Python ======")
    print("[1] Gestão de Alunos\n[2] Gestão de Disciplinas\n[3] Gestão de Matrículas\n[4] Geração de Relatórios\n[5] Sair")
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
        print("Opção inválida. Digite 1-5.")