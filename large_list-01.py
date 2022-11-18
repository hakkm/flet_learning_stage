import flet 
from flet import Page, Text

def main(page: Page):
    for line in range(200):
        page.controls.append(Text(f"Line {line}"))
    page.scroll = "adaptive"  # True, False, 'none', 'auto', 'adaptive', 'always', or 'hidden'.
    page.update()

if __name__ == "__main__":
    flet.app(target=main)