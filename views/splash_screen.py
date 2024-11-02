import flet as ft


class Splash(ft.View):
    def __init__(self):
        super().__init__(
            route="/",
            padding=0,
        )

        self.splash = ft.Container(
            width=380, height=750,
            content=ft.Stack(
                controls=[
                    ft.Text(
                        value="Travel",
                        font_family="Lobster",
                        color=ft.colors.WHITE,
                        size=44,
                        top=300,
                        left=100
                    ),
                    ft.IconButton(
                        icon=ft.icons.PUBLIC,
                        icon_color=ft.colors.WHITE,
                        icon_size=45,
                        top=300,
                        left=257-37,
                        on_click=lambda e: e.page.go("/home")
                    ),
                    ft.Text(
                        value="  Find Your  Dream \nDestination With Us!",
                        font_family="Roboto",
                        color=ft.colors.WHITE,
                        size=20,
                        top=474-79,
                        left=90
                    )

                ]
            ),
            expand=True,
            gradient=ft.LinearGradient(
                colors=["#0172B2", "#001645"],
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center
            ),
        )

        self.controls = [
            self.splash
        ]
