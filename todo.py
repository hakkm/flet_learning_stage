import flet 
from flet import Page, Checkbox, Text
from flet.ref import Ref


def main(page: Page):
    page.horizontal_alignment = "baseline"   # 'start', 'end', 'center', 'stretch', or 'baseline'.
    
    
    text = Ref[Text]()
    todo_check = Ref[Checkbox]()


    def checkbox_change(e):
        text.current.value = f"Learn how make a TextField on focus: {todo_check.current.value}"
        page.update()

    page.add(
        Checkbox(
            ref=todo_check,
            label="ToDo: Learn how make a TextField on focus.",
            value=False,
            on_change=checkbox_change
            ),
        Text(ref=text)
        )


flet.app(target=main)