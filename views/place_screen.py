import flet as ft


class Custom(ft.Row):
    def __init__(self, icon: str, text: str) -> None:
        self.__icon = icon
        self.__text = text
        super().__init__()

        self.icon = ft.Container(
            bgcolor="#EDEDED",
            width=30, height=29,
            border_radius=ft.border_radius.all(value=10),
            content=ft.Icon(
                name=self.__icon,
                color="#3F3F3F",
                size=18
            )
        )

        self.text =ft.Text(
            value=self.__text,
            color="#888888",
            font_family="Roboto",
            weight=ft.FontWeight.W_200,
            size=16,
            style=ft.TextStyle(letter_spacing=0.6)
        )

        self.controls = [self.icon, self.text]


class PlaceScreen(ft.View):
    def __init__(self, page: ft.Page) -> None:
        super().__init__("/place", padding=ft.padding.only(top=30, left=10, bottom=10))
        self.bgcolor = "white"
        #print(page.session.get("place"))

        self.arch = ft.Container(
            width=35, height=35,
            offset=ft.Offset(x=7.79, y=-0.8),
            bgcolor="#999999",
            border_radius=ft.border_radius.all(value=180),
            content=ft.Icon(
                name=ft.icons.ARCHIVE_OUTLINED,
                color="#FBFBFB",
                size=25
            ),
            on_click=self.clicked
        )

        self.undo = ft.Container(
            width=35, height=35,
            offset=ft.Offset(x=0.4, y=0.4),
            bgcolor="#999999",
            border_radius=ft.border_radius.all(value=180),
            content=ft.Icon(
                name=ft.icons.ARROW_BACK_IOS_SHARP,
                color="#FBFBFB",
                size=15
            ),
            on_click=lambda e: e.page.go("/home")
        )

        self.location = ft.Container(
            width=280, height=80,
            offset=ft.Offset(x=0.08, y=1.8),
            bgcolor=ft.colors.with_opacity(opacity=0.80, color="#1D1D1D"),
            border_radius=ft.border_radius.all(value=15),
            content=ft.Column(
                controls=[
                    ft.Divider(color=ft.colors.TRANSPARENT, height=2),
                    ft.Text(
                        value=page.session.get("place").get("name"),
                        size=26,
                        offset=ft.Offset(x=0.09, y=-0.2),
                        color=ft.colors.WHITE,
                        font_family="Roboto",
                        weight=ft.FontWeight.W_200,
                    ),
                    ft.Text(
                        value="Price",
                        offset=ft.Offset(x=8, y=-2.2),
                        color=ft.colors.WHITE,
                        font_family="Roboto",
                        weight=ft.FontWeight.W_200,
                        size=12,
                    ),
                    ft.Icon(
                        name=ft.icons.LOCATION_ON,
                        offset=ft.Offset(x=0.3, y=-1.4),
                        size=30,
                        color="#D9D9D9"
                    ),
                    ft.Text(
                        value=page.session.get("place").get("loc"),
                        offset=ft.Offset(x=0.25, y=-2.6),
                        color=ft.colors.WHITE,
                        font_family="Roboto",
                        weight=ft.FontWeight.W_200,
                        size=20,
                    ),
                    ft.Text(
                        value="288",
                        offset=ft.Offset(x=4, y=-3.9),
                        color=ft.colors.WHITE,
                        font_family="Roboto",
                        weight=ft.FontWeight.W_200,
                        size=20,
                        spans=[
                            ft.TextSpan(
                                text="DT",
                                style=ft.TextStyle(
                                    color="#888888",
                                    font_family="Roboto",
                                    weight=ft.FontWeight.W_200,
                                    size=15,

                                )
                            )
                        ]
                    ),
                ]
            )
        )

        self.con = ft.Container(
            border_radius=ft.border_radius.all(value=20),
            width=323, height=330,
            offset=ft.Offset(x=0.022, y=0),
            bgcolor="red",
            image_src=page.session.get("place").get("place"),
            image_fit=ft.ImageFit.FIT_HEIGHT,
            content=ft.Column(
                controls=[
                    self.undo, self.arch,
                    self.location
                ]
            )
        )

        self.overview = ft.Text(
            value="Overview",
            offset=ft.Offset(x=0.2, y=0.3),
            color=ft.colors.BLACK,
            font_family="Roboto",
            weight=ft.FontWeight.W_200,
            size=32,
        )

        self.details = ft.Text(
            value="Details",
            offset=ft.Offset(x=4, y=-1.2),
            color="#888888",
            font_family="Roboto",
            weight=ft.FontWeight.W_200,
            size=16,
        )

        self.controls = [
            self.con,
            self.overview, self.details,
            ft.Row(
                offset=ft.Offset(x=0.08, y=0.3),
                spacing=18,
                controls=[
                    Custom(icon=ft.icons.TIMER, text="8 hours"),
                    Custom(icon=ft.icons.CLOUD, text="16 °C"),
                    Custom(icon=ft.icons.STAR, text="4.5")
                ]
            ),
            ft.ShaderMask(
                offset=ft.Offset(x=0.08, y=0.2),
                content=ft.Text(
                    value="This vast mountain range is renowned for its remarkable diversity in terms of topography and climate. It features towering peaks, active volcanoes, deep canyons, expansive plateaus, and lush valleys. The Andes are also home to ",
                    width=300,
                    color="#888888",
                    font_family="Roboto",
                    weight=ft.FontWeight.W_200,
                    size=14,
                ),
                width=350, height=200,
                shader=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=["#A5A5A5", ft.colors.with_opacity(opacity=0.1, color=ft.colors.WHITE)]
                )
            ),
            ft.Container(
                offset=ft.Offset(x=0.07, y=-1.4),
                height=44, width=300,
                bgcolor=ft.colors.BLACK,
                border_radius=ft.border_radius.all(value=10),
                alignment=ft.alignment.center,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value="Book Now",
                            color=ft.colors.WHITE,
                            font_family="Roboto",
                            weight=ft.FontWeight.W_200,
                            size=18,
                        ),
                        ft.Image(
                            src="icons/send icon.png",
                            color=ft.colors.WHITE,
                            width=23, height=23,
                        )
                    ]
                )
            )
        ]


    @staticmethod
    def clicked(e: ft.ControlEvent) -> None:
        if e.control.content.name == ft.icons.ARCHIVE_OUTLINED:
            e.control.content.name = ft.icons.ARCHIVE
            e.page.snack_bar = ft.SnackBar(ft.Text("Add to Archive"))
            e.page.snack_bar.open = True

        else:
            e.control.content.name = ft.icons.ARCHIVE_OUTLINED
            e.page.snack_bar = ft.SnackBar(ft.Text("Delete from Archive"))
            e.page.snack_bar.open = True
        e.page.update()
