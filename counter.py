import flet 
from flet import Page, IconButton, Row, TextField, icons
from flet.ref import Ref

def main(page: Page):
    text_number = Ref[TextField]()

    def minus_click(e):
        text_number.current.value = f"{int(text_number.current.value) - 1}"
        page.update()

    def plus_click(e):
        text_number.current.value = f"{int(text_number.current.value) + 1}"
        page.update()

    page.add(Row([
                IconButton(
                    icon=icons.REMOVE, on_click=minus_click
                    ),
                TextField(ref=text_number, value="0"),
                IconButton(icon=icons.ADD, on_click=plus_click),
                ]
                )
            )

if __name__ == "__main__":
    flet.app(target=main)