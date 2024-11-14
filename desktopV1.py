import flet as ft

# Função da página principal
def main(page: ft.Page):
    page.bgcolor = "#000000"
    # Variável de estado para controlar a aba ativa
    active_tab = "inicio"  # Iniciar com a aba "INÍCIO" ativa

    # Função para trocar a aba
    def change_tab(tab_name: str):
        nonlocal active_tab  # Modifica a variável active_tab
        active_tab = tab_name  # Atualiza a aba ativa
        update_tabs()  # Atualiza as abas
        page.update()  # Atualiza a página para refletir a mudança

    # Barra de navegação lateral
    nav_bar = ft.Container(
        content=ft.Column(
            controls=[
                # Botões da navbar que alteram a aba ativa
                ft.TextButton("INÍCIO", style=ft.ButtonStyle(color="green"), on_click=lambda e: change_tab("inicio")),
                ft.TextButton("MONITORAMENTO", style=ft.ButtonStyle(color="green"), on_click=lambda e: change_tab("monitoramento")),
                ft.TextButton("ESPORTES", style=ft.ButtonStyle(color="green"), on_click=lambda e: change_tab("esportes")),
                ft.TextButton("CONFIGURAÇÕES", style=ft.ButtonStyle(color="green"), on_click=lambda e: change_tab("configuracoes")),
            ],
            alignment="start",  # Alinha os itens ao topo da barra lateral
            spacing=20,
        ),
        bgcolor="#4F4F4F",  # Cor de fundo da barra lateral
        padding=ft.padding.all(20),
        width=200,  # Largura da barra lateral
        height=page.vertical_alignment,  # A altura da barra lateral será igual à altura da página, independente da orientação.
        border_radius=ft.border_radius.all(10)  # Bordas arredondadas
    )

    # Conteúdo das diferentes abas
    inicio_content = ft.Column(
        controls=[
            ft.Text("Bem-vindo à aba INÍCIO!", size=24, weight="bold", color="lightblue"),
            ft.Text("Aqui você verá informações iniciais.", size=18, color="lightblue"),
        ],
        visible=True  # Inicialmente exibido
    )

    acompanhamento_content = ft.Column(
        controls=[
            ft.Text("Bem-vindo à aba MONITORAMENTO!", size=24, weight="bold", color="lightblue"),
            ft.Text("Aqui você pode acompanhar dados e métricas.", size=18, color="lightblue"),
        ],
        visible=False  # Inicialmente oculto
    )

    esportes_content = ft.Column(
        controls=[
            ft.Text("Bem-vindo à aba ESPORTES!", size=24, weight="bold", color="lightblue"),
            ft.Text("Aqui você encontra notícias e atualizações sobre esportes.", size=18, color="lightblue"),
        ],
        visible=False  # Inicialmente oculto
    )

    configuracoes_content = ft.Column(
        controls=[
            ft.Text("Bem-vindo à aba CONFIGURAÇÕES!", size=24, weight="bold", color="lightblue"),
            ft.Text("Aqui você pode ajustar suas preferências.", size=18, color="lightblue"),
        ],
        visible=False  # Inicialmente oculto
    )

    # Adiciona todos os componentes à página
    page.add(
        ft.Row(
            controls=[
                nav_bar,  # Barra lateral
                ft.Column(
                    controls=[
                        inicio_content,
                        acompanhamento_content,
                        esportes_content,
                        configuracoes_content,
                    ],
                    expand=True  # Preenche o restante da tela
                ),
            ],
            expand=True  # Expande a linha para preencher a página
        )
    )

    # Função para atualizar a visibilidade com base na aba ativa
    def update_tabs():
        # Oculta todos os conteúdos
        inicio_content.visible = False
        acompanhamento_content.visible = False
        esportes_content.visible = False
        configuracoes_content.visible = False
        
        # Exibe o conteúdo da aba ativa
        if active_tab == "inicio":
            inicio_content.visible = True
        elif active_tab == "monitoramento":
            acompanhamento_content.visible = True
        elif active_tab == "esportes":
            esportes_content.visible = True
        elif active_tab == "configuracoes":
            configuracoes_content.visible = True

    # Chama a função de atualização de abas
    update_tabs()

# Executa a aplicação
ft.app(target=main)
