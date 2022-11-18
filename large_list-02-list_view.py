import flet 
from flet import Page, Text, ListView
from flet.ref import Ref

def main(page: Page):
    lv =  Ref[ListView]()
    for line in range(101):
        lv.current.controls.append(Text(f"Line {line}"))
    page.add(ListView(ref=lv, expand=True, spacing=10)) # spacing: space between rows (lines)

flet.app(target=main)