import flet 
from flet import Page, IconButton, Row, TextField, icons, Text
from flet.ref import Ref

def main(page: Page):
    page.title = "Zwa9 Page"
    page.vertical_alignment = "spaceEvenly"    # like axe oy : 'start', 'end', 'center', 'spaceBetween', 'spaceAround', or 'spaceEvenly'.
    page.horizontal_alignment = "center"   # 'start', 'end', 'center', 'stretch', or 'baseline'.

    page.add(Row([
        Text(value="We are in Zwa9 Page"),
        Text(value="We are in Zwa9 Page")
    ], alignment="end") # 'start', 'end', 'center', 'spaceBetween', 'spaceAround', or 'spaceEvenly'. 
    )
    

if __name__ == "__main__":
    flet.app(target=main)