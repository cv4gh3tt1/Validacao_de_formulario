def gerar_contrato(e, page, dict_values, campos_do_formulario):

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
    dict_values["contratante"] = contratante.value or ""
    dict_values["contratante"] = contratante.value or ""
    dict_values["medida_judicial"] = medida_judicial.value or ""
    dict_values["outra_parte"] = outra_parte.value or ""
    dict_values["prolabore"] = prolabore.value or ""
    dict_values["exito"] = exito.value or ""
    dict_values["foro"] = foro.value or ""
    dict_values["data"] = data.value or ""
