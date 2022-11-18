import flet
from flet import Dropdown, ElevatedButton, Page, Text, dropdown


def main(page: Page):
    def button_clicked(e):
        output_text.value = f"Dropdown value is:  {color_dropdown.value}"
        page.update()

    output_text = Text()
    submit_btn = ElevatedButton(text="Submit", on_click=button_clicked)
    color_dropdown = Dropdown(
        width=100,
        label="shortcuts",
        options=[
            dropdown.Option("Red"),
            dropdown.Option("Green"),
            dropdown.Option("Blue"),
        ],
    )
    page.add(color_dropdown, submit_btn, output_text)

flet.app(target=main)