import flet as f 

#colori
def main(page: f.Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'
    page.window_width=600
    page.window_height=850
    page.scroll = "auto"
    page.icon = "icona.png"
    page.update()
    
#pagina 1 con le slide
    create_task_view = f.Container(
        content = f.Container(
            height = 40,
            width =40,
            content=f.Text('x'),
            on_click=lambda _: page.go('/'),
            
        )
    )

#pagina 2 con il quiz
    create_task_view2 = f.Container(
        content = f.Container(
            height = 40,
            width =40,
            content=f.Text('x'),
            on_click=lambda _: page.go('/'),
            
        )
    )

#pagina 3 con lo shop
    create_task_view3 = f.Container(
        content = f.Container(
            height = 40,
            width =40,
            content=f.Text('x'),
            on_click=lambda _: page.go('/'),
            
        )
    )

#se voglio creare una colonna di cose nella pagina principale
    tasks = f.Column()

#scrollo le categorie
    categories_card = f.Row(
        scroll= 'auto'
    )
    categories = ['Leggi','Gioca','Shop']

#creo la prima vignetta
    categories_card.controls.append(
            f.Container(
                bgcolor=BG,
                height=120,
                width=150,
                border_radius=20,
                padding=15,
                content=f.Column(
                    controls=[
                        f.Text(categories[0]),
                        f.FloatingActionButton(
                            icon = f.icons.ADD, on_click=lambda _: page.go('/create_task'),
                        ),
                    ]
                )

            )
        )

#creo la seconda vignetta
    categories_card.controls.append(
            f.Container(
                bgcolor=BG,
                height=120,
                width=150,
                border_radius=20,
                padding=15,
                content=f.Column(
                    controls=[
                        f.Text(categories[1]),
                        f.FloatingActionButton(
                            icon = f.icons.SEARCH, on_click=lambda _: page.go('/create_task2'),
                        ),
                    ]
                )

            )
        )

#creo la terza vignetta
    categories_card.controls.append(
            f.Container(
                bgcolor=BG,
                height=120,
                width=150,
                border_radius=20,
                padding=15,
                content=f.Column(
                    controls=[
                        f.Text(categories[2]),
                        f.FloatingActionButton(
                            icon = f.icons.MENU, on_click=lambda _: page.go('/create_task3'),
                        ),
                    ]
                )

            )
        )

#content della home
    home_page_contents = f.Container(
        content=f.Column(
            controls=[
                f.Row(alignment='spaceBetween',
                    controls=[
                        f.Container(
                            content=f.Icon(
                                f.icons.MENU)),

                        f.Row(
                            controls=[
                                f.Icon(f.icons.SEARCH)
                            ]
                        )
                    ]
                ),
                f.Text(value="Ciao"),
                f.Text(value="CATEGORIES"),
                f.Container(
                    padding=f.padding.only(
                        top=10,
                        bottom=20,
                    ),
                    content = categories_card
                )
                
            ],
        ),
    )
#funziamento e granezza pagine
    page_2 = f.Row(
        controls=[
            f.Container(
                width=360,
                height=850,
                bgcolor=FG,
                border_radius= 20,
                padding=f.padding.only(
                    top=45,
                    left=20,
                    right=30,
                    bottom=5
                ),
                content=f.Column(
                    controls=[
                        home_page_contents
                    ]
                )
            )
        ]
    )
    slide = f.Row(
        controls=[
            f.Container(
                width=360,
                height=850,
                bgcolor=FG,
                border_radius=20,
                padding=f.padding.only(
                    top=55,
                    left=20,
                    right= 30,
                    bottom=5
                ),
                content=f.Column(
                    controls=[
                        create_task_view
                    ]
                )
            )
        ]
    )
    game = f.Row(
        controls=[
            f.Container(
                width=360,
                height=850,
                bgcolor=FG,
                border_radius=20,
                padding=f.padding.only(
                    top=55,
                    left=20,
                    right=30,
                    bottom=5
                ),
                content=f.Column(
                    controls=[
                        create_task_view2
                    ]
                )
            )
        ]
    )
    shop = f.Row(
        controls=[
            f.Container(
                width=360,
                height=850,
                bgcolor=FG,
                border_radius=20,
                padding=f.padding.only(
                    top=55,
                    left=20,
                    right=30,
                    bottom=5
                ),
                content=f.Column(
                    controls=[
                        create_task_view3
                    ]
                )
            )
        ]
    )
#sfondo home
    container = f.Container(
        width=360,
        height=800,
        bgcolor=BG,
        border_radius=20,
        content=f.Stack(
            controls=[
                page_2,
            ]  
        )
    )

#sfondo slide
    container_slide = f.Container(
        width=360,
        height=800,
        bgcolor=BG,
        border_radius=20,
        content=f.Stack(
            controls=[
                slide,
            ]  
        )
    )
#sfondo mini-game
    container_game = f.Container(
        width=360,
        height=800,
        bgcolor=BG,
        border_radius=20,
        content=f.Stack(
            controls=[
                game,
            ]  
        )
    )
#sfondo shop
    container_shop = f.Container(
        width=360,
        height=800,
        bgcolor=BG,
        border_radius=20,
        content=f.Stack(
            controls=[
                shop,
            ]  
        )
    )

#dizionari per muoversi nelle pagine
    pages = {
        '/': f.View(
            "/",
            [
                container
            ],
        ),
        '/create_task': f.View(
            "/create_task",
            [
                container_slide
            ],
        ),

        '/create_task2': f.View(
            "/create_task2",
            [
                container_game
            ],
        ),
        '/create_task3': f.View(
            "/create_task3",
            [
                container_shop
            ],
        ),
    }
    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )
    page.on_route_change = route_change
    page.go(page.route)

f.app(target=main)
