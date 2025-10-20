# Daniel Henrique da Silva   - Código de pessoa: 8109346 - Número de matrícula: 23.2.2001
# Guilherme Melo             - Código de pessoa: 8576076 - Número de matrícula: 26.1.0379
# Leonardo Pinheiro de Souza - Código de pessoa: 8557802 - Número de matrícula: 25.2.7332

alunos: dict[str, dict[str, str]] = {}
disciplinas: dict[str, dict[str, int]] = {}
matriculas: list[dict[str, str]] = []


def validar_matricula(matricula: str) -> bool:
    """Valida uma matrícula.

    Verifica se uma matrícula esta no formato correto:
    - 7 Dígitos;
    - 4 Primeiros dígitos são o ano de ingresso.

    Args:
        matricula: a matricula a ser validada.

    Returns:
        True se a matrícula é válida, False se não for.
    """
    return (
        len(matricula) == 7
        and matricula.isdigit()
        and 1900 <= int(matricula[:4]) <= 2100
    )


def validar_codigo_disciplina(codigo: str) -> bool:
    """Valida um código de disciplina.

    Verifica se um código de disciplina esta no formato correto:
    - 5 Dígitos;
    - LLNNN.

    Args:
        codigo: Código de matrícula a ser validado.

    Returns:
        True se o código for válido, False se não for.
    """
    return (
        len(codigo) == 5
        and codigo[:2].isalpha()
        and codigo[:2].isupper()
        and codigo[2:].isdigit()
    )


def validar_vagas(vagas: str) -> bool:
    """Valida quantidade de vagas.

    Verifica se o input de vagas é valido:
    - Apenas dígitos;
    - Maior ou igual a 0.

    Args:
        vagas: Input de vagas a ser validado.

    Returns:
        True se a(s) vaga(s) for(em) valída(s), false se não for(em).
    """
    return vagas.isdigit() and int(vagas) >= 0


def input_matricula(prompt: str, existe: bool | None = None) -> str:
    """Pede uma matrícula para o usuário.

    Pede uma matrícula para o usúario, valida e verifica se ela já foi
    cadastrada ou não, pedindo outra matrícula caso alguma verificação falhe.

    Args:
        prompt: Mensagem para mostrar ao úsuario.
        existe: True se a matricula a ser digitada deve já existir,
            False caso contrário.

    Returns:
        A mátricula digitada pelo úsuario.
    """
    while True:
        matricula = input(prompt).strip()
        if not validar_matricula(matricula):
            print(
                "Matrícula inválida. Deve ter 7 dígitos e os 4 primeiros formam o ano."
            )
            continue
        if existe is True and matricula not in alunos:
            print("Matrícula não cadastrada.")
            continue
        if existe is False and matricula in alunos:
            print("Matrícula já cadastrada.")
            continue
        return matricula


def input_codigo_disciplina(prompt: str, existe: bool | None = None) -> str:
    """Pede um código de disciplina para o usuário.

    Pede um código de disciplina para o usúario, valida e verifica se ele já foi
    cadastrado ou não, pedindo outro código de matrícula caso alguma
    verificação falhe.

    Args:
        prompt: Mensagem para mostrar ao úsuario.
        existe: True se o código de disciplina a ser digitado deve já existir,
            False caso contrário.

    Returns:
        O código de disciplina digitado pelo úsuario.
    """
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
    """Pede a quantidade de vagas para o usuário.

    Pede a quantidade de vagas para o usuário e valida,
    pedindo outra caso alguma verificação falhe.

    Args:
        prompt: Mensagem para mostrar ao usuário.

    Returns:
        A quantidade de vagas digitada pelo usuário.
    """
    while True:
        vagas = input(prompt).strip()
        if not validar_vagas(vagas):
            print("Vagas inválidas. Digite um inteiro >= 0.")
            continue
        return int(vagas)


def input_codigo_matricula(prompt: str, matricula: str) -> str:
    """Pede um código de disciplina para o usuário.

    Pede um código de disciplina para o usuário valida, e verifica
    se a matrícula passada esta inscrita nesta disciplina,
    pedindo outro código caso alguma verificação falhe.

    Args:
        prompt: Mensagem para mostrar ao usuário.
        matricula: Matrícula para verificar se já está inscrita na disciplina.

    Returns:
        O código de disciplina digitado.
    """
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
    """Cadastra um aluno.

    Coloca um aluno na lista de alunos, primeiro verificando se a matricula
    já foi cadastrada.

    Args:
        matricula: Matrícula do aluno a ser cadastrado.
        nome: Nome do aluno a ser cadastrado.

    Returns:
        Uma tupla com True e "Aluno cadastrado com sucesso" caso não tenha
        falhado nenhuma verificação, False e "Matrícula já cadastrada"
        caso contrário.
    """
    if matricula in alunos:
        return False, "Matrícula já cadastrada."
    alunos[matricula] = {"nome": nome}
    return True, "Aluno cadastrado com sucesso."


def alunos_ordenados() -> list[dict[str, str]]:
    """Ordena a lista de alunos.

    Ordena a lista de alunos em ordem alfábetica.

    Returns:
        A lista de alunos ordenada.
    """
    return sorted(
        [{"matricula": m, "nome": d["nome"]} for m, d in alunos.items()],
        key=lambda x: x["matricula"],
    )


def buscar_aluno(matricula: str) -> dict[str, str] | None:
    """Pesquisa um aluno.

    Pesquisa um aluno pela matrícula.

    Args:
        matricula: Matrícula do aluno a ser pesquisado.

    Returns:
        O aluno que possui a matrícula passada ou None caso não exista.
    """
    return alunos.get(matricula)


def cadastrar_disciplina(codigo: str, nome: str, vagas: int) -> tuple[bool, str]:
    """Cadastra uma disciplina.

    Coloca uma discplina na lista de disciplinas, verificando antes se o código
    de disciplina já foi cadastrado.

    Args:
        codigo: Código de disciplina a ser cadastrado.
        nome: Nome da disciplina a ser cadastrada.
        vagas: vagas disponíveis para a disciplina a ser cadastrada.

    Returns:
        Uma tupla com True e "Disciplina cadastrada com sucesso." caso não
        tenha falhado nenhuma verificação, False e "Código já cadastrado." caso
        contrário.
    """
    if codigo in disciplinas:
        return False, "Código já cadastrado."
    disciplinas[codigo] = {"nome": nome, "vagas": vagas}
    return True, "Disciplina cadastrada com sucesso."


def disciplinas_ordenadas() -> list[dict[str, str | int]]:
    """Ordena a lista de disciplinas.

    Ordena a lista de disciplinas em ordem alfabética.

    Returns:
        A lista de disciplinas ordenada.
    """
    return sorted(
        [
            {"codigo": c, "nome": d["nome"], "vagas": d["vagas"]}
            for c, d in disciplinas.items()
        ],
        key=lambda x: x["codigo"],
    )


def buscar_disciplina(codigo: str) -> dict[str, str | int] | None:
    """Busca uma disciplina.

    Pesquisa uma discplina pelo código de disciplina.

    Args:
        codigo: Código da disciplina a ser buscada.

    Returns:
        A disciplina se for encontrada ou None se não for.
    """
    return disciplinas.get(codigo)


def esta_inscrito(matricula: str, codigo: str) -> bool:
    """Verifica se um aluno está inscrito em certa disciplina.

    Verifica se uma certa matrícula está cadastrada em uma certa disciplina.

    Args:
        matricula: Matrícula do aluno.
        codigo: Código da disciplina a procurar a matrícula.

    Returns:
        True caso o aluno esteja cadastrado na disciplina, False caso não.
    """
    for i in matriculas:
        if i["matricula"] == matricula and i["codigo"] == codigo:
            return True
    return False


def inscrever_aluno_disciplina(matricula: str, codigo: str) -> tuple[bool, str]:
    """Inscreve um aluno em uma discplina.

    Cadastra um aluno em uma disciplina, verificando antes e o aluno já foi
    inscrito e se ainda há vagas disponíveis.

    Args:
        matricula: Matrículo do aluno a ser inscrito.
        codigo: Código da disciplina que o aluno será cadastrado.

    Returns:
        Uma tupla com True e "Inscrição realizada com sucesso." caso tenha
        passado todas as verificações, False e "Aluno já inscrito nesta
        disciplina." ou "Não há vagas disponíveis." caso contrário.
    """
    if esta_inscrito(matricula, codigo):
        return False, "Aluno já inscrito nesta disciplina."
    if disciplinas[codigo]["vagas"] <= 0:
        return False, "Não há vagas disponíveis."
    matriculas.append({"matricula": matricula, "codigo": codigo})
    disciplinas[codigo]["vagas"] -= 1
    return True, "Inscrição realizada com sucesso."


def listar_inscricoes() -> bool:
    """Lista as incrições realizadas.

    Listagem formatada dos alunos incritos em alguma disciplina.

    Returns:
        False caso não existam incrições, True caso contrário.
    """
    if not matriculas:
        return False
    else:
        print(
            f"{'Matrícula':<10} | {'Código':<8} | {'Nome Aluno':<30} | {'Nome Disciplina':<30}"
        )
        print("-" * 86)
        for i in matriculas:
            print(
                f"{i['matricula']:<10} | {i['codigo']:<8} | {alunos[i['matricula']]['nome']:<30} | {disciplinas[i['codigo']]['nome']:<30}"
            )
    return True


def ordenar_alunos_por_disciplina(codigo: str) -> list[dict[str, str]] | None:
    """Ordena a lista de incrições de uma certa disciplina.

    Ordena lista de incrições de uma disciplina informada pelo código.

    Args:
        codigo: Código da disciplina a ser ordenada.

    Returns:
        A lista de alunos inscritos na disciplina ordenados alfabéticamente
        ou None caso o código não exista.
    """
    if codigo not in disciplinas:
        return None
    return sorted(
        [
            {"matricula": m, "nome": alunos[m]["nome"]}
            for m in [i["matricula"] for i in matriculas if i["codigo"] == codigo]
        ],
        key=lambda x: x["matricula"],
    )


def ordenar_disciplinas_por_aluno(matricula: str) -> list[dict[str, str]] | None:
    """Ordena as disciplinas de um aluno.

    Ordena alfabéticamente as disciplina em que um aluno está cadastrado.

    Args:
        matricula: Matrícula do aluno.

    Returns:
        A lista de disciplinas que o aluno está cadastrado ordenada ou None
        caso a matrícula não exista.
    """
    if matricula not in alunos:
        return None
    return sorted(
        [
            {"codigo": c, "nome": disciplinas[c]["nome"]}
            for c in [i["codigo"] for i in matriculas if i["matricula"] == matricula]
        ],
        key=lambda x: x["codigo"],
    )


def disciplinas_com_vagas_esgotadas() -> list[dict[str, str]]:
    """Lista de disciplinas com vagas esgotadas.

    Faz a listagem das disciplinas com vagas esgotadas.

    Returns:
        Lista com as disciplinas com vagas já esgotadas.
    """
    return [
        {"codigo": c, "nome": d["nome"]}
        for c, d in disciplinas.items()
        if d["vagas"] <= 0
    ]


def menu_gestao_alunos():
    """Menu de gestão de alunos.

    Emprime na tela um menu com opções relacionadas a gestão de alunos:
        - Cadastro de novo aluno;
        - Listagem dos alunos;
        - Busca de aluno.
    """
    while True:
        print("\n--- Gestão de Alunos ---")
        print(
            "[1] Cadastrar Aluno\n[2] Listar Alunos\n[3] Buscar Aluno por Matrícula\n[4] Voltar"
        )
        op = input("Escolha: ").strip()
        if op == "1":
            matricula = input_matricula(
                "Matrícula (7 dígitos e os 4 primeiros formam o ano): ", existe=False
            )
            while True:
                nome = input("Nome: ").strip()
                if not nome:
                    print("Nome não pode ser vazio.")
                    continue
                break
            ok, msg = cadastrar_aluno(matricula, nome)
            print(msg)
        elif op == "2":
            lista = alunos_ordenados()
            if not lista:
                print("Nenhum aluno cadastrado.")
            else:
                print(f"{'Matrícula':<10} | {'Nome':<30}")
                print("-" * 43)
                for aluno in lista:
                    print(f"{aluno['matricula']:<10} | {aluno['nome']:<30}")
        elif op == "3":
            matricula = input_matricula("Matrícula: ", existe=True)
            aluno = buscar_aluno(matricula)
            print(
                f"Matrícula: {matricula} | Nome: {aluno['nome']}"
                if aluno
                else "Aluno não encontrado."
            )
        elif op == "4":
            return
        else:
            print("Opção inválida. Digite 1-4.")


def menu_gestao_disciplinas():
    """Menu de gestão de disciplinas.

    Emprime na tela um menu com opções relacionadas a gestão de disciplinas:
        - Cadastro de nova disciplina;
        - Listagem de disciplinas;
        - Busca de disciplina.
    """
    while True:
        print("\n--- Gestão de Disciplinas ---")
        print(
            "[1] Cadastrar Disciplina\n[2] Listar Disciplinas\n[3] Buscar Disciplina por Código\n[4] Voltar"
        )
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
            lista = disciplinas_ordenadas()
            if not lista:
                print("Nenhuma disciplina cadastrada.")
            else:
                print(f"{'Código':<8} | {'Nome':<30} | {'Vagas':<5}")
                print("-" * 46)
                for d in lista:
                    print(f"{d['codigo']:<8} | {d['nome']:<30} | {d['vagas']:<5}")
        elif op == "3":
            codigo = input_codigo_disciplina("Código: ", existe=True)
            disciplina = buscar_disciplina(codigo)
            if disciplina:
                print(f"{'Código':<8} | {'Nome':<30} | {'Vagas':<5}")
                print("-" * 46)
                print(
                    f"{codigo:<8} | {disciplina['nome']:<30} | {disciplina['vagas']:<5}"
                )
            else:
                print("Disciplina não encontrada.")
        elif op == "4":
            return
        else:
            print("Opção inválida. Digite 1-4.")


def menu_gestao_matriculas():
    """Menu de gestão de matrículas.

    Emprime na tela um menu com opções relacionadas a gestão de matrículas:
        - Incrição de um aluno em alguma disciplina;
        - Listagem de disciplinas.
    """
    while True:
        print("\n--- Gestão de Matrículas ---")
        print("[1] Realizar Inscrição\n[2] Listar Inscrições\n[3] Voltar")
        op = input("Escolha: ").strip()
        if op == "1":
            matricula = input_matricula("Matrícula do aluno: ", existe=True)
            codigo = input_codigo_matricula("Código da disciplina: ", matricula)
            ok, msg = inscrever_aluno_disciplina(matricula, codigo)
            print(msg)
        elif op == "2":
            if not listar_inscricoes():
                print("Nenhuma inscrição realizada.")
        elif op == "3":
            return
        else:
            print("Opção inválida. Digite 1-3.")


def menu_relatorios():
    """Menu de relatórios.

    Emprime na tela um menu com opções de geração de relatórios:
        - Listar alunos por disciplina;
        - Listar disciplinas por aluno;
        - Listar disciplinas com vagas esgotadas.
    """
    while True:
        print("\n--- Geração de Relatórios ---")
        print(
            "[1] Listar Alunos por Disciplina\n[2] Listar Disciplinas por Aluno\n[3] Listar Disciplinas com Vagas Esgotadas\n[4] Voltar"
        )
        op = input("Escolha: ").strip()
        if op == "1":
            codigo = input_codigo_disciplina("Código da disciplina: ", existe=True)
            retorno = ordenar_alunos_por_disciplina(codigo)
            if not retorno:
                print("Nenhum aluno inscrito nesta disciplina.")
            else:
                print(f"{'Matrícula':<10} | {'Nome':<30}")
                print("-" * 43)
                for r in retorno:
                    print(f"{r['matricula']:<10} | {r['nome']:<30}")
        elif op == "2":
            matricula = input_matricula("Matrícula do aluno: ", existe=True)
            retorno = ordenar_disciplinas_por_aluno(matricula)
            if not retorno:
                print("Aluno não inscrito em nenhuma disciplina.")
            else:
                print(f"{'Código':<8} | {'Nome':<30}")
                print("-" * 40)
                for r in retorno:
                    print(f"{r['codigo']:<8} | {r['nome']:<30}")
        elif op == "3":
            esgotadas = disciplinas_com_vagas_esgotadas()
            if not esgotadas:
                print("Nenhuma disciplina com vagas esgotadas.")
            else:
                print(f"{'Código':<8} | {'Nome':<30}")
                print("-" * 40)
                for d in esgotadas:
                    print(f"{d['codigo']:<8} | {d['nome']:<30}")

        elif op == "4":
            return
        else:
            print("Opção inválida. Digite 1-4.")


while True:
    print("\n====== Sistema de Gestão Acadêmica - Universidade Python ======")
    print(
        "[1] Gestão de Alunos\n[2] Gestão de Disciplinas\n[3] Gestão de Matrículas\n[4] Geração de Relatórios\n[5] Sair"
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
