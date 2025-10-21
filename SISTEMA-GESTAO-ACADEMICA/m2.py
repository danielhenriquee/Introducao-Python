# Daniel Henrique da Silva   - Código de pessoa: 8109346 - Número de matrícula: 23.2.2001
# Guilherme Melo             - Código de pessoa: 8576076 - Número de matrícula: 26.1.0379
# Leonardo Pinheiro de Souza - Código de pessoa: 8557802 - Número de matrícula: 25.2.7332

alunos: dict[str, dict[str, str]] = {}
disciplinas: dict[str, dict[str, int]] = {}
matriculas: list[dict[str, str]] = []


def input_matricula(prompt: str, existe: bool | None = None) -> str | None:
    """Pede uma matrícula para o usuário.

    Pede uma matrícula para o usuário, valida e verifica se ela já foi
    cadastrada ou não, pedindo outra matrícula caso alguma verificação falhe.

    Args:
        prompt: Mensagem para mostrar ao úsuario.
        existe: True se a matricula deve existir, False caso contrário.
        None para quando for apenas validar o formato

    Returns:
        A matrícula digitada pelo úsuario.
        None caso usuário decida voltar.
    """
    while True:
        matricula = input(prompt).strip()
        if matricula == "-1":
            return None
        if (
            len(matricula) == 7
            and matricula.isdigit()
            and 1900 <= int(matricula[:4]) <= 2100
        ):
            if existe is True and matricula not in alunos:
                print("Matrícula não cadastrada.")
                continue
            if existe is False and matricula in alunos:
                print("Matrícula já cadastrada.")
                continue
            else:
                break
        else:
            print(
                "Matrícula inválida, deve ter 7 dígitos com os 4 primeiros sendo o ano de ingresso."
            )
    return matricula


def input_codigo_disciplina(prompt: str, existe: bool | None = None) -> str | None:
    """Pede um código de disciplina para o usuário.

    Pede um código de disciplina para o usuário, valida e verifica se ele já foi
    cadastrado ou não, pedindo outro código de matrícula caso alguma
    verificação falhe.

    Args:
        prompt: Mensagem para mostrar ao usuário.
        existe: True se o código de disciplina deve existir, False caso contrário.

    Returns:
        O código de disciplina digitado pelo usuário.
        None caso usuário decida voltar.
    """
    while True:
        codigo = input(prompt).strip()
        if codigo == "-1":
            return None
        if (
            len(codigo) == 5
            and codigo[:2].isalpha()
            and codigo[:2].isupper()
            and codigo[2:].isdigit()
        ):
            if existe is True and codigo not in disciplinas:
                print("Disciplina não cadastrada.")
                continue
            if existe is False and codigo in disciplinas:
                print("Código já cadastrado.")
                continue
            else:
                break
        else:
            print("Código inválido, deve ser no formato LLNNN (L = letra, N = número)")
    return codigo


def input_vagas(prompt: str) -> int | None:
    """Pede a quantidade de vagas para o usuário.

    Pede a quantidade de vagas para o usuário e valida,
    pedindo outra caso alguma verificação falhe.

    Args:
        prompt: Mensagem para mostrar ao usuário.

    Returns:
        A quantidade de vagas digitada pelo usuário.
        None caso usuário decida voltar.
    """
    while True:
        vagas = input(prompt).strip()
        if vagas == "-1":
            return None
        if vagas.isdigit() and int(vagas) >= 0:
            break
        else:
            print("Vagas inválidas. Digite um inteiro >= 0.")
    return int(vagas)


def cadastrar_aluno(matricula: str, nome: str) -> None:
    """Cadastra um aluno.

    Adiciona um aluno na lista de alunos, verificando se a matrícula
    já foi cadastrada.

    Args:
        matricula: Matrícula do aluno a ser cadastrado.
        nome: Nome do aluno a ser cadastrado.

    Notes:
        Se a matrícula já existir, imprime mensagem de erro.
        Caso contrário, cadastra o aluno e imprime mensagem de sucesso.
    """
    if matricula in alunos:
        print("Matrícula já cadastrada.")
        return
    alunos[matricula] = {"nome": nome}
    print("Aluno cadastrado com sucesso.")


def alunos_ordenados() -> list[dict[str, str]]:
    """Retorna a lista de alunos ordenada por matrícula.

    Gera uma lista de dicionários contendo todos os alunos cadastrados,
    cada um com sua matrícula e nome, ordenados pela matrícula.

    Returns:
        list[dict[str, str]]: Lista de alunos ordenados por matrícula,
        cada aluno representado como um dicionário com as chaves:
        'matricula' e 'nome'.
    """
    alunos_list = [
        {"matricula": m, "nome": d["nome"]}
        for m, d in alunos.items()
    ]
    return sorted(alunos_list, key = lambda x: x["matricula"])


def buscar_aluno(matricula: str) -> None:
    """Exibe o nome de um aluno a partir da matrícula.

    Args:
        matricula: Matrícula do aluno a ser pesquisado.
    """
    aluno = alunos.get(matricula)
    print(f"Nome: {aluno['nome']}")


def cadastrar_disciplina(codigo: str, nome: str, vagas: int) -> None:
    """Cadastra uma disciplina.

    Adiciona uma disciplina na lista de disciplinas, verificando se o código
    já foi cadastrado.

    Args:
        codigo: Código de disciplina a ser cadastrado.
        nome: Nome da disciplina a ser cadastrada.
        vagas: vagas disponíveis para a disciplina a ser cadastrada.

    Notes:
        Se o código já existir, imprime mensagem de erro.
        Caso contrário, cadastra a disciplina e imprime mensagem de sucesso.
    """
    if codigo in disciplinas:
        print("Código já cadastrado.")
        return
    disciplinas[codigo] = {"nome": nome, "vagas": vagas}
    print("Disciplina cadastrada com sucesso.")


def disciplinas_ordenadas() -> list[dict[str, str | int]]:
    """Retorna a lista de disciplinas ordenadas por código.

    Gera uma lista de dicionários contendo todas as disciplinas cadastradas,
    cada uma com seu código, nome e quantidade de vagas, ordenadas pelo código.

    Returns:
        list[dict[str, str | int]]: Lista de disciplinas ordenadas por código,
        cada disciplina representada como um dicionário com as chaves:
        'codigo', 'nome' e 'vagas'.
    """
    disciplinas_list = [
        {"codigo": c, "nome": d["nome"], "vagas": d["vagas"]}
        for c, d in disciplinas.items()
    ]
    return sorted(disciplinas_list, key = lambda x: x["codigo"])


def buscar_disciplina(codigo: str) -> None:
    """Exibe informações de uma disciplina a partir do código.

    Args:
        codigo: Código da disciplina a ser buscada.
    
    Notes:
        Imprime o código, nome e número de vagas da disciplina correspondente.
    """
    disciplina = disciplinas.get(codigo)
    print(f"{'Código':<8} | {'Nome':<30} | {'Vagas':<5}")
    print("-" * 46)
    print(f"{codigo:<8} | {disciplina['nome']:<30} | {disciplina['vagas']:<5}")


def esta_inscrito(matricula: str, codigo: str) -> bool:
    """Verifica pela matrícula se um aluno está inscrito em uma disciplina.

    Args:
        matricula: Matrícula do aluno.
        codigo: Código da disciplina.

    Returns:
        bool: True se o aluno estiver inscrito na disciplina, False caso contrário.
    """
    for i in matriculas:
        if i["matricula"] == matricula and i["codigo"] == codigo:
            return True
    return False


def inscrever_aluno_disciplina(matricula: str, codigo: str) -> None:
    """Inscreve um aluno em uma discplina.

    Verifica se o aluno já está inscrito e se há vagas disponíveis
    antes de realizar a inscrição.

    Args:
        matricula: Matrícula do aluno a ser inscrito.
        codigo: Código da disciplina na qual o aluno será inscrito.

    Notes:
        Se o aluno já estiver inscrito ou não houver vagas, imprime mensagem
        de erro. Caso contrário, adiciona a inscrição e decrementa a vaga.
    """
    if esta_inscrito(matricula, codigo):
        print("Aluno já inscrito nesta disciplina.")
        return
    if disciplinas[codigo]["vagas"] <= 0:
        print("Não há vagas disponíveis.")
        return
    matriculas.append({"matricula": matricula, "codigo": codigo})
    disciplinas[codigo]["vagas"] -= 1
    print("Inscrição realizada com sucesso.")


def listar_inscricoes() -> None:
    """Lista todas as incrições realizadas.

    Imprime uma tabela com matrícula do aluno, código da disciplina,
    nome do aluno e nome da disciplina.
    """
    if not matriculas:
        print("Nenhuma inscrição realizada.")
        return
    
    print(f"Matrícula | Código | {'Nome Aluno':<30} | {'Nome Disciplina':<30}")
    print("-" * 83)
    for i in matriculas:
        print(
            f"{i['matricula']:<9} | {i['codigo']:<6} | {alunos[i['matricula']]['nome']:<30} | {disciplinas[i['codigo']]['nome']:<30}"
        )


def ordenar_alunos_por_disciplina(codigo: str) -> list[dict[str, str]] | None:
    """Retorna os alunos inscritos em uma disciplina, ordenados por matrícula.

    Gera uma lista de dicionários contendo os alunos inscritos na disciplina
    informada, cada um com sua matrícula e nome, ordenados pela matrícula.

    Args:
        codigo (str): Código da disciplina a ser ordenada.

    Returns:
        list[dict[str, str]] | None: Lista de alunos ordenados ou None se
        o código da disciplina não existir. Cada aluno é representado como
        um dicionário com as chaves 'matricula' e 'nome'.
    """
    if codigo not in disciplinas:
        return None
    return sorted(
        [
            {"matricula": m, "nome": alunos[m]["nome"]}
            for m in [i["matricula"] for i in matriculas if i["codigo"] == codigo]
        ],
        key = lambda x: x["matricula"],
    )


def ordenar_disciplinas_por_aluno(matricula: str) -> list[dict[str, str]] | None:
    """Retorna as disciplinas em que um aluno está inscrito, ordenadas por código.

    Gera uma lista de dicionários contendo as disciplinas em que o aluno
    informado está inscrito, cada uma com seu código e nome, ordenadas pelo código.

    Args:
        matricula (str): Matrícula do aluno.

    Returns:
        list[dict[str, str]] | None: Lista de disciplinas ordenadas ou None
        se a matrícula não existir. Cada disciplina é representada como um
        dicionário com as chaves 'codigo' e 'nome'.
    """
    if matricula not in alunos:
        return None
    return sorted(
        [
            {"codigo": c, "nome": disciplinas[c]["nome"]}
            for c in [i["codigo"] for i in matriculas if i["matricula"] == matricula]
        ],
        key = lambda x: x["codigo"],
    )


def disciplinas_com_vagas_esgotadas() -> list[dict[str, str]]:
    """Retorna uma lista de disciplinas com todas as vagas esgotadas.

    Gera uma lista de dicionários contendo apenas as disciplinas cujas
    vagas disponíveis são zero.

    Returns:
        list[dict[str, str]]: Lista de disciplinas com vagas esgotadas,
        cada uma representada como um dicionário com as chaves 'codigo' e 'nome'.
    """
    return [
        {"codigo": c, "nome": d["nome"]}
        for c, d in disciplinas.items()
        if d["vagas"] <= 0
    ]


def menu_gestao_alunos():
    """Exibe o menu de gestão de alunos.

    Permite ao usuário:
        - Cadastrar um novo aluno;
        - Listar todos os alunos cadastrados;
        - Buscar um aluno por matrícula;
        - Voltar ao menu principal.
    """
    while True:
        print("\n--- Gestão de Alunos ---")
        print(
            "[1] Cadastrar Aluno\n"
            "[2] Listar Alunos\n"
            "[3] Buscar Aluno por Matrícula\n"
            "[4] Voltar"
        )
        op = input("Escolha: ").strip()
        if op == "1":
            matricula = input_matricula(
                "Matrícula (7 dígitos e os 4 primeiros formam o ano) [-1 para voltar]: ", existe = False
            )
            if matricula is None:
                continue
            while True:
                nome = input("Nome [-1 para voltar]: ").strip()
                if nome == "-1":
                    break
                if not nome:
                    print("Nome não pode ser vazio.")
                    continue
                cadastrar_aluno(matricula, nome)
                break
        elif op == "2":
            lista = alunos_ordenados()
            if not lista:
                print("Nenhum aluno cadastrado.")
            else:
                print(f"Matrícula | {'Nome':<30}")
                print("-" * 43)
                for aluno in lista:
                    print(f"{aluno['matricula']:<9} | {aluno['nome']:<30}")
        elif op == "3":
            matricula = input("Matrícula [-1 para voltar]: ", existe = True)
            buscar_aluno(matricula)
        elif op == "4":
            return
        else:
            print("Opção inválida. Digite 1-4.")


def menu_gestao_disciplinas():
    """Exibe o menu de gestão de disciplinas.

    Permite ao usuário:
        - Cadastrar uma nova disciplina;
        - Listar todas as disciplinas cadastradas;
        - Buscar uma disciplina pelo código;
        - Voltar ao menu principal.
    """
    while True:
        print("\n--- Gestão de Disciplinas ---")
        print(
            "[1] Cadastrar Disciplina\n"
            "[2] Listar Disciplinas\n"
            "[3] Buscar Disciplina por Código\n"
            "[4] Voltar"
        )
        op = input("Escolha: ").strip()
        if op == "1":
            codigo = input_codigo_disciplina("Código (LLNNN) [-1 para voltar]: ", existe = False)
            if codigo is None:
                continue
            while True:
                nome = input("Nome da disciplina [-1 para voltar]: ").strip()
                if nome == "-1":
                    break
                if not nome:
                    print("Nome da disciplina não pode ser vazio.")
                    continue
                vagas = input_vagas("Vagas (inteiro >= 0) [-1 para voltar]: ")
                if vagas is None:
                    break
                cadastrar_disciplina(codigo, nome, vagas)
                break
            
        elif op == "2":
            lista = disciplinas_ordenadas()
            if not lista:
                print("Nenhuma disciplina cadastrada.")
            else:
                print(f"Código | {'Nome':<30} | Vagas")
                print("-" * 48)
                for d in lista:
                    print(f"{d['codigo']:<6} | {d['nome']:<30} | {d['vagas']:<5}")
        elif op == "3":
            codigo = input_codigo_disciplina("Código [-1 para voltar]: ", existe = True)
            buscar_disciplina(codigo)
        elif op == "4":
            return
        else:
            print("Opção inválida. Digite 1-4.")


def menu_gestao_matriculas():
    """Exibe o menu de gestão de matrículas.

    Permite ao usuário:
        - Realizar a inscrição de um aluno em uma disciplina;
        - Listar todas as inscrições realizadas;
        - Voltar ao menu principal.
    """
    while True:
        print("\n--- Gestão de Matrículas ---")
        print(
            "[1] Realizar Inscrição\n"
            "[2] Listar Inscrições\n"
            "[3] Voltar"
        )
        op = input("Escolha: ").strip()
        if op == "1":
            while True:
                matricula = input_matricula("Matrícula do aluno [-1 para voltar]: ", existe = None)
                if matricula is None:
                    break
                if matricula not in alunos:
                    print("Matrícula não cadastrada.")
                    continue
                codigo = input_codigo_disciplina("Código da disciplina [-1 para voltar]: ", existe = True)
                if codigo is None:
                    break
                inscrever_aluno_disciplina(matricula, codigo)
                break
            
        elif op == "2":
            listar_inscricoes()
        elif op == "3":
            return
        else:
            print("Opção inválida. Digite 1-3.")


def menu_relatorios():
    """Exibe o menu de relatórios acadêmicos.

    Permite ao usuário:
        - Listar alunos por disciplina;
        - Listar disciplinas por aluno;
        - Listar disciplinas com vagas esgotadas;
        - Voltar ao menu principal.
    """
    while True:
        print("\n--- Geração de Relatórios ---")
        print(
            "[1] Listar Alunos por Disciplina\n"
            "[2] Listar Disciplinas por Aluno\n"
            "[3] Listar Disciplinas com Vagas Esgotadas\n"
            "[4] Voltar"
        )
        op = input("Escolha: ").strip()
        if op == "1":
            codigo = input_codigo_disciplina("Código da disciplina [-1 para voltar]: ", existe = True)
            if codigo is None:
                continue
            retorno = ordenar_alunos_por_disciplina(codigo)
            if not retorno:
                print("Nenhum aluno inscrito nesta disciplina.")
            else:
                print(f"Matrícula | {'Nome':<30}")
                print("-" * 43)
                for r in retorno:
                    print(f"{r['matricula']:<9} | {r['nome']:<30}")
        elif op == "2":
            matricula = input_matricula("Matrícula do aluno [-1 para voltar]: ", existe = True)
            if matricula is None:
                continue
            retorno = ordenar_disciplinas_por_aluno(matricula)
            if not retorno:
                print("Aluno não inscrito em nenhuma disciplina.")
            else:
                print(f"Código | {'Nome':<30}")
                print("-" * 40)
                for r in retorno:
                    print(f"{r['codigo']:<6} | {r['nome']:<30}")
        elif op == "3":
            esgotadas = disciplinas_com_vagas_esgotadas()
            if not esgotadas:
                print("Nenhuma disciplina com vagas esgotadas.")
            else:
                print(f"Código | {'Nome':<30}")
                print("-" * 40)
                for d in esgotadas:
                    print(f"{d['codigo']:<6} | {d['nome']:<30}")

        elif op == "4":
            return
        else:
            print("Opção inválida. Digite 1-4.")


while True:
    print("\n====== Sistema de Gestão Acadêmica - Universidade Python ======")
    print(
        "[1] Gestão de Alunos\n"
        "[2] Gestão de Disciplinas\n"
        "[3] Gestão de Matrículas\n"
        "[4] Geração de Relatórios\n"
        "[5] Sair"
    )
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
