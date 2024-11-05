import flet as ft


class Place(ft.Container):
    def __init__(self, name_place: tuple[str, str], loc_place: str, rate: str, place: str) -> None:
        self.name_place = name_place
        self.loc_place = loc_place
        self.rate = rate
        self.place = place
        super().__init__()
        self.width, self.height = 380-160, 330
        self.bgcolor = "red"
        self.border_radius = ft.border_radius.all(value=20)
        self.shadow = ft.BoxShadow(
            blur_radius=19,
            color=ft.colors.with_opacity(opacity=0.1, color=ft.colors.BLACK),
            offset=ft.Offset(x=0.1, y=0)
        )
        self.image_src = self.place
        self.image_fit = ft.ImageFit.FIT_HEIGHT
        self.on_click = self.send



        self.heart = ft.Container(
            margin=ft.margin.only(left=165, top=14),
            width=44, height=44,
            bgcolor="#999999",
            border_radius=ft.border_radius.all(value=180),
            content=ft.Icon(
                name=ft.icons.FAVORITE_OUTLINE,
                color="#FBFBFB",
            ),
            on_click=self.clicked

        )

        self.location = ft.Container(
            margin=ft.margin.only(left=15, top=170),
            width=190, height=75,
            bgcolor=ft.colors.with_opacity(opacity=0.80, color="#1D1D1D"),
            border_radius=ft.border_radius.all(value=15),
            content=ft.Column(
                controls=[
                    ft.Divider(color=ft.colors.TRANSPARENT, height=2),
                    ft.Text(
                        value=f"    {self.name_place[0]}, ",
                        color=ft.colors.WHITE,
                        font_family="Roboto",
                        weight=ft.FontWeight.W_200,
                        spans=[
                            ft.TextSpan(
                                text=self.name_place[1],
                                style=ft.TextStyle(
                                    size=12,
                                    color="#D9D9D9",
                                )
                            )
                        ]
                    ),
                    ft.Row(
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=2,
                        controls=[
                            ft.Icon(
                                name=ft.icons.LOCATION_ON,
                                size=25,
                                color="#D9D9D9"
                            ),
                            ft.Text(
                                value=self.loc_place,
                                color=ft.colors.WHITE,
                                font_family="Roboto",
                                weight=ft.FontWeight.W_200,
                                size=12,
                            ),
                            ft.Row(
                                spacing=-5,
                                controls=[
                                    ft.Icon(
                                        name=ft.icons.STAR_BORDER,
                                        color="#D9D9D9",
                                        size=14
                                    ),
                                    ft.Text(
                                        value=self.rate,
                                        color=ft.colors.WHITE,
                                        font_family="Roboto",
                                        weight=ft.FontWeight.W_200,
                                        size=14,
                                    )
                                ]
                            )
                        ]
                    )
                ]
            )

        )

        self.content = ft.Column(
            controls=[
                self.heart,
                self.location
            ]
        )

    def clicked(self, e: ft.ControlEvent) -> None:
        if e.control.content.name == ft.icons.FAVORITE_OUTLINE:
            e.control.content.name = ft.icons.FAVORITE
            e.page.snack_bar = ft.SnackBar(ft.Text("Add to Favorite"))
            e.page.snack_bar.open = True
            e.page.session.set(f"fav_{''.join(self.name_place)}", {
                "name": self.name_place[0],
                "place": self.place,
                "loc": self.loc_place,
                "rate": self.rate
            })
            e.page.session.set("place", {
                "name": self.name_place[0],
                "place": self.place,
                "loc": self.loc_place
            })
        else:
            e.control.content.name = ft.icons.FAVORITE_OUTLINE
            e.page.snack_bar = ft.SnackBar(ft.Text("Delete from Favorite"))
            e.page.snack_bar.open = True
            e.page.session.remove(f"fav_{"".join(self.name_place)}")
            e.page.session.remove("place")
        e.page.update()

    def send(self, e: ft.ControlEvent) -> None:
        e.page.go("/place")
        e.page.session.set("place", {
            "name": self.name_place[0],
            "place": self.place,
            "loc": self.loc_place
        })


class ViewAll(ft.View):
    def __init__(self):
        super().__init__()
        self.padding = ft.padding.only(top=30, left=5)
        self.bgcolor = ft.colors.WHITE
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER


        self.content_column = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
            height=700,
            controls=[
                Place(
                    name_place=("Aîn Draham", "Jendouba"),
                    loc_place="Jendouba, Tunisie",
                    rate="4.8",
                    place="3ain_drahom.jpg"
                ),
                Place(
                    name_place=("Galite Islands", "Bizerte"),
                    loc_place="Bizerte, Tunisie",
                    rate="4.2",
                    place="la-galite.jpg"
                ),
                Place(
                    name_place=("Aîn Draham", "Jendouba"),
                    loc_place="Jendouba, Tunisie",
                    rate="4.8",
                    place="3ain_drahom.jpg"
                ),
                Place(
                    name_place=("Galite Islands", "Bizerte"),
                    loc_place="Bizerte, Tunisie",
                    rate="4.2",
                    place="la-galite.jpg"
                )
            ]
        )

        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    width=35, height=35,
                    bgcolor="#999999",
                    border_radius=ft.border_radius.all(value=180),
                    content=ft.Icon(
                        name=ft.icons.ARROW_BACK_IOS_SHARP,
                        color="#FBFBFB",
                        size=15
                    ),
                    on_click=lambda e: e.page.go("/home")
                ),
                self.content_column
            ]
        )

        self.controls = [self.content]

class Home(ft.Container):
    def __init__(self):
        super().__init__()
        self.padding = ft.padding.only(top=30, left=5)
        self.bgcolor = ft.colors.WHITE


        self.hi = ft.Text(
            value="Hi, Omar👋",
            font_family="Montserrat",
            size=25,
            weight=ft.FontWeight.BOLD,
            color="#2F2F2F",
            offset=ft.Offset(x=0.1, y=0)
        )

        self.explore = ft.Text(
            value="Explore The World",
            font_family="Inter",
            size=15,
            weight=ft.FontWeight.W_400,
            color="#888888",
            style=ft.TextStyle(letter_spacing=0.5),
            offset=ft.Offset(x=0.1, y=0)
        )

        self.avatar = ft.Container(
            content=ft.Image(
                src=r"faces\omar.png",
                width=100, height=80.24 * 1.2
            ),
            width=50, height=50,
            bgcolor=ft.colors.RED,
            border_radius=180,
            offset=ft.Offset(x=5.7, y=-1.4)
        )

        self.search = ft.Container(
            offset=ft.Offset(x=0.06, y=-1),
            content=ft.SearchBar(
                width=311, height=45,
                expand=True,
                bar_bgcolor=ft.colors.WHITE,
                # bar_leading=ft.Icon(name=ft.icons.SEARCH, color=ft.colors.BLACK),
                bar_trailing=[
                    ft.Row(
                        spacing=5,
                        controls=[
                            ft.Image(src="icons/line.png", color="#888888", width=30, height=21.6),
                            ft.Image(src="icons/settings.png", color="#888888", width=24, height=21.6),
                            ft.Text("    ")
                        ]
                    )
                ],
                divider_color=ft.colors.BLACK,
                bar_hint_text="   Search Places",
            )
        )

        self.popular_places = ft.Text(
            value="Popular Places",
            font_family="Montserrat",
            weight=ft.FontWeight.W_400,
            size=16,
            color=ft.colors.BLACK,
            offset=ft.Offset(x=0.1, y=-1)
        )

        self.view_all = ft.TextButton(
            offset=ft.Offset(x=3, y=-1.8),
            style=ft.ButtonStyle(overlay_color=ft.colors.TRANSPARENT),
            content=ft.Text(
                value="View all",
                font_family="Montserrat",
                weight=ft.FontWeight.W_400,
                size=16,
                color="#888888"
            ),
            on_click=lambda e: e.page.go("/view_all")
        )

        self.most_viewed = ft.Container(
            width=115, height=49.34,
            bgcolor="#2F2F2F",
            border_radius=ft.border_radius.all(value=20),
            alignment=ft.alignment.center,
            data="most",
            shadow=ft.BoxShadow(
                blur_radius=19,
                color=ft.colors.with_opacity(opacity=0.19, color=ft.colors.BLACK),
                offset=ft.Offset(x=0, y=9)
            ),
            animate=500,
            content=ft.Text(
                value="Most Viewed",
                color=ft.colors.WHITE,
                font_family="Montserrat",
                size=14,
                weight=ft.FontWeight.W_400
            ),
            on_click=self.clicked
        )

        self.nearby = ft.Container(
            width=84, height=49.34,
            bgcolor="#FBFBFB",
            border_radius=ft.border_radius.all(value=20),
            alignment=ft.alignment.center,
            data="nearby",
            animate=500,
            content=ft.Text(
                value="Nearby",
                color="#C5C5C5",
                font_family="Montserrat",
                size=14,
                weight=ft.FontWeight.W_400
            ),
            on_click=self.clicked
        )

        self.latest = ft.Container(
            width=84, height=49.34,
            bgcolor="#FBFBFB",
            border_radius=ft.border_radius.all(value=20),
            alignment=ft.alignment.center,
            data="latest",
            animate=500,
            content=ft.Text(
                value="Latest",
                color="#C5C5C5",
                font_family="Montserrat",
                size=14,
                weight=ft.FontWeight.W_400
            ),
            on_click=self.clicked
        )

        self.places = ft.Row(
            width=350, height=330,
            offset=ft.Offset(x=0.02, y=-0.1),
            spacing=19,
            scroll=ft.ScrollMode.HIDDEN,
            controls=[
                Place(
                    name_place=("Aîn Draham", "Jendouba"),
                    loc_place="Jendouba, Tunisie",
                    rate="4.8",
                    place="3ain_drahom.jpg"
                ),
                Place(
                    name_place=("Galite Islands", "Bizerte"),
                    loc_place="Bizerte, Tunisie",
                    rate="4.2",
                    place="la-galite.jpg"
                ),
                Place(
                    name_place=("Aîn Draham", "Jendouba"),
                    loc_place="Jendouba, Tunisie",
                    rate="4.8",
                    place="3ain_drahom.jpg"
                ),
                Place(
                    name_place=("Galite Islands", "Bizerte"),
                    loc_place="Bizerte, Tunisie",
                    rate="4.2",
                    place="la-galite.jpg"
                )
            ]
        )


        self.controls = [
            self.hi,
            self.explore, self.avatar,
            self.search,
            self.popular_places, self.view_all,
            ft.Row(
                offset=ft.Offset(x=-0.04, y=-1),
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                controls=[self.most_viewed, self.nearby, self.latest]
            ),
            self.places
        ]
        self.content = ft.Column(controls=self.controls)


    def clicked(self, e: ft.ControlEvent) -> None:
        print(e.control.data)
        if e.control.data == "most":
            self.most_viewed.width = 115
            self.most_viewed.bgcolor = "#2F2F2F"
            self.most_viewed.content.color = ft.colors.WHITE
            self.most_viewed.content.size = 14
            self.most_viewed.shadow = ft.BoxShadow(
                blur_radius=19,
                color=ft.colors.with_opacity(opacity=0.19, color=ft.colors.BLACK),
                offset=ft.Offset(x=0, y=9)
            )

            self.latest.width = 84
            self.latest.bgcolor = "#FBFBFB"
            self.latest.shadow = None
            self.latest.content.color = "#C5C5C5"

            self.nearby.width = 84
            self.nearby.bgcolor = "#FBFBFB"
            self.nearby.shadow = None
            self.nearby.content.color = "#C5C5C5"


        elif e.control.data == "nearby":
            self.nearby.width = 115
            self.nearby.bgcolor = "#2F2F2F"
            self.nearby.content.color = ft.colors.WHITE
            self.nearby.shadow = ft.BoxShadow(
                blur_radius=19,
                color=ft.colors.with_opacity(opacity=0.19, color=ft.colors.BLACK),
                offset=ft.Offset(x=0, y=9)
            )

            self.latest.width = 84
            self.latest.bgcolor = "#FBFBFB"
            self.latest.shadow = None
            self.latest.content.color = "#C5C5C5"

            self.most_viewed.width = 84
            self.most_viewed.bgcolor = "#FBFBFB"
            self.most_viewed.shadow = None
            self.most_viewed.content.color = "#C5C5C5"
            self.most_viewed.content.size = 12


        if e.control.data == "latest":
            self.latest.width = 121
            self.latest.bgcolor = "#2F2F2F"
            self.latest.content.color = ft.colors.WHITE
            self.latest.shadow = ft.BoxShadow(
                blur_radius=19,
                color=ft.colors.with_opacity(opacity=0.19, color=ft.colors.BLACK),
                offset=ft.Offset(x=0, y=9)
            )

            self.most_viewed.width = 84
            self.most_viewed.bgcolor = "#FBFBFB"
            self.most_viewed.shadow = None
            self.most_viewed.content.color = "#C5C5C5"
            self.most_viewed.content.size = 12


            self.nearby.width = 85
            self.nearby.bgcolor = "#FBFBFB"
            self.nearby.content.color = "#C5C5C5"
            self.nearby.shadow = None

        e.page.update()


class Destination(ft.NavigationBarDestination):
    def __init__(self, icon: str):
        self.__icon = icon
        super().__init__()
        #self.label = "."
        self.icon = self.__icon
        self.bgcolor = ft.colors.TRANSPARENT
        #self.selected_icon = self.__icon[:self.__icon.find("_")]
        self.selected_icon_content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=3,
            controls=[
                ft.Icon(name=self.__icon[:self.__icon.find("_")]),
                ft.Icon(name=ft.icons.CIRCLE, color=ft.colors.RED, size=7),

            ]
        )


class Timer(ft.Container):
    def __init__(self):
        super().__init__()
        self.alignment = ft.alignment.center
        self.margin = ft.margin.only(top=250)
        self.content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Icon(
                    name=ft.icons.TIMER_OUTLINED,
                    size=100,
                    color=ft.colors.GREEN
                ),
                ft.Text(
                    value="timer",
                    size=70,
                    font_family="NotoSerifOriya",
                    weight=ft.FontWeight.W_200

                )
            ]
        )


class Favorite(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.alignment = ft.alignment.center
        self.padding = ft.padding.only(top=30)
        self.content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    image_src=page.session.get(i).get("place"),
                    image_fit=ft.ImageFit.FIT_WIDTH,
                    width=300, height=75,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.with_opacity(opacity=0.80, color="#1D1D1D"),
                    border_radius=ft.border_radius.all(value=15),
                    content=ft.Text(
                        value=page.session.get(i).get("name"),
                        color=ft.colors.WHITE,
                        font_family="Roboto",
                        weight=ft.FontWeight.W_200,
                    ),
                    on_click=lambda e: e.page.go("/place")

                )
                for i in page.session.get_keys() if "fav" in i
            ]
        )


class Person(ft.Container):
    def __init__(self):
        super().__init__()
        self.alignment = ft.alignment.center
        self.margin = ft.margin.only(top=250)
        self.content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Icon(
                    name=ft.icons.PERSON,
                    size=100,
                    color=ft.colors.GREEN
                ),
                ft.Text(
                    value=ft.icons.PERSON,
                    size=70,
                    font_family="NotoSerifOriya",
                    weight=ft.FontWeight.W_200

                )
            ]
        )


class HomeScreen(ft.View):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(
            route="/home",
            padding=0,
        )
        self.bgcolor = ft.colors.WHITE
        #self.bottom_appbar = BottomAppBar()
        self.navigation_bar = ft.NavigationBar(
            height=40,
            bgcolor=ft.colors.TRANSPARENT,
            indicator_color=ft.colors.TRANSPARENT,
            overlay_color=ft.colors.TRANSPARENT,
            label_behavior=ft.NavigationBarLabelBehavior.ONLY_SHOW_SELECTED,
            animation_duration=200,
            destinations=[
                Destination(ft.icons.HOME_OUTLINED),
                Destination(ft.icons.TIMER_OUTLINED),
                Destination(ft.icons.FAVORITE_BORDER),
                Destination(ft.icons.PERSON_OUTLINED)
            ],
            on_change=self.switched
        )

        self.switch = ft.AnimatedSwitcher(
            content=Home(),
            transition=ft.AnimatedSwitcherTransition.SCALE,
            duration=500,
            reverse_duration=100,
            switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
            switch_out_curve=ft.AnimationCurve.BOUNCE_IN
        )

        self.controls = [
            self.switch
        ]

    def switched(self, e: ft.ControlEvent) -> None:
        if e.data == "0":
            self.switch.content = Home()
        elif e.data == "1":
            self.switch.content = Timer()
        elif e.data == "2":
            self.switch.content = Favorite(self.page)
        elif e.data == "3":
            self.switch.content = Person()
        self.switch.update()
