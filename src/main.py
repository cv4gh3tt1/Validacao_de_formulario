import flet as ft


def main(page: ft.Page):
    page.title = "Gerador de Contrato"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    titulo = ft.Text(
        value="Gerador de Contrato de Prestação de Serviços Advocatícios",
        size=30,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_900,
        text_align=ft.TextAlign.CENTER,
    )
    # Definindo o dicionário para armazenar os valores dos campos do formulário
    dict_values = {
        "contratante": "",
        "medida_judicial": "",
        "outra_parte": "",
        "prolabore": "",
        "exito": "",
        "foro": "",
        "data": "",
    }

    # Função para gerar o contrato
    def gerar_contrato(e):
        # Lista de campos para verificar se o campo está preenchido
        campos_do_formulario = [
            contratante,
            medida_judicial,
            outra_parte,
            prolabore,
            exito,
            foro,
            data,
        ]

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

    contratante = ft.TextField(
        label="Nome do Contratante",
        autofocus=True,
        hint_text="Nome do Contratante",
    )
    medida_judicial = ft.TextField(label="Medida Judicial")
    outra_parte = ft.TextField(label="Outra Parte")
    prolabore = ft.TextField(label="Prolabore", prefix_text="R$ ")
    exito = ft.TextField(label="Exito", suffix_text="%")
    foro = ft.TextField(label="Foro")
    data = ft.TextField(label="Data")

    btn_gerar = ft.FilledButton(
        text="Gerar Contrato", icon=ft.Icons.SAVE, on_click=gerar_contrato
    )

    page.add(
        ft.Column(
            controls=[
                titulo,
                contratante,
                medida_judicial,
                outra_parte,
                prolabore,
                exito,
                foro,
                data,
                btn_gerar,
            ],
            width=500,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


ft.app(main)
