import flet 
from flet import Page, ElevatedButton, TextField, Text
from flet.ref import Ref

def main(page: Page):
    page.title = "Greeter"


    name = Ref[TextField]()
    hello_name = Ref[Text]()

    def say_hello(e):
        if not name.current.value:
            name.current.value = "Please enter your name"
        
        else:
            hello_name.current.value = "Hello " + name.current.value

        page.update()

    page.add(
        TextField(ref=name, hint_text="Your name"),
        ElevatedButton(text="Say Hello!", on_click=say_hello),
        Text("", ref=hello_name)
    )


if __name__ == "__main__":
    flet.app(target=main)