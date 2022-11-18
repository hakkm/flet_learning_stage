import flet 
from flet import Checkbox, ElevatedButton, Row, TextField, Page

def main(page: Page):
    def add_clicked(e):
        page.add(Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        add_btn.text = "Another"
        new_task.disabled = True
        page.update()

    new_task = TextField(hint_text="What's need to be done?")
    add_btn = ElevatedButton(text="add", on_click=add_clicked)
    page.add(Row([new_task, add_btn]))


if __name__=="__main__":
    flet.app(target=main)