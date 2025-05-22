import flet as ft
import contrato_utils


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
    dict_values = {
        "contratante": "",
        "medida_judicial": "",
        "outra_parte": "",
        "prolabore": "",
        "exito": "",
        "foro": "",
        "data": "",
    }

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

    campos_do_formulario = [
        contratante,
        medida_judicial,
        outra_parte,
        prolabore,
        exito,
        foro,
        data,
    ]

    def on_gerar_contrato(e):
        contrato_utils.gerar_contrato(e, campos_do_formulario, dict_values, page)

    btn_gerar = ft.FilledButton(
        text="Gerar Contrato",
        icon=ft.Icons.SAVE,
        on_click=on_gerar_contrato,
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
