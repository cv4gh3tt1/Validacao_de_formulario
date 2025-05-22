def validar_numero_decimal(campo, page):
    valor = campo.value
    novo_valor = ""
    separador_encontrado = False

    for char in valor:
        if char.isdigit():
            novo_valor += char
        elif char == "." and not separador_encontrado:
            novo_valor += char
            separador_encontrado = True

    if valor != novo_valor:
        campo.value = novo_valor
        page.update()


def padronizar_decimal(campo, page):
    valor = campo.value
    if valor:
        if "." not in valor:
            campo.value = f"{valor}.00"
        elif valor.endswith("."):
            campo.value = f"{valor}00"
        else:
            partes = valor.split(".")
            if len(partes) == 2:
                decimais = partes[1][:2]  # pega no máximo 2 dígitos
                if len(decimais) < 2:
                    decimais = decimais.ljust(2, "0")  # completa com zero se faltar
                campo.value = f"{partes[0]}.{decimais}"
        page.update()


def gerar_contrato(e, campos_do_formulario, dict_values, page):
    # 1. Limpar erros de validações anteriores de todos os campos
    for campo in campos_do_formulario:
        campo.error_text = None

    # 1.1 Variável para armazenar o primeiro campo com erro
    primeiro_campo_com_erro = None

    # 1.2 Variável para verificar se houve erro na validação
    houve_erro_na_validacao = False

    # 2 Validar cada campo do formulário
    for campo in campos_do_formulario:
        if not campo.value:  # Verifica se o valor do campo é vazio ou None
            campo.error_text = f"O campo '{campo.label}' é obrigatório."
            houve_erro_na_validacao = True
            if (
                primeiro_campo_com_erro is None
            ):  # Guarda o primeiro campo com erro para dar foco
                primeiro_campo_com_erro = campo

    # Se houver erro na validação, não prosseguir
    # 2.1 Se houver erro na validação, dar foco no primeiro campo com erro
    if houve_erro_na_validacao:
        if primeiro_campo_com_erro:
            primeiro_campo_com_erro.focus()
        page.update()  # Atualiza a página para mostrar os erros e o foco
        return

    # 3. Se todos os campos estiverem válidos, popular o dict_values.
    dict_values["contratante"] = campos_do_formulario[0].value or ""
    dict_values["medida_judicial"] = campos_do_formulario[1].value or ""
    dict_values["outra_parte"] = campos_do_formulario[2].value or ""
    dict_values["campo"] = campos_do_formulario[3].value or ""
    dict_values["exito"] = campos_do_formulario[4].value or ""
    dict_values["foro"] = campos_do_formulario[5].value or ""
    dict_values["data"] = campos_do_formulario[6].value or ""
    page.update()

    print("gerando contrato...")
