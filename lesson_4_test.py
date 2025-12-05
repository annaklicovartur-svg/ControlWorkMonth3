# Part first: LESSON_4

import flet as ft 
from datetime import datetime

def main(page: ft.Page):
    page.tite = 'My first app'
    greeting_text = ft.Text(value='Hello wrold', color=ft.Colors.RED)
    
    greeting_history = []
    history_text = ft.Text("History of greetings: ")

    def one_button_click(_):
        
        name = name_input.value.strip()

        timestamp = datetime.now().strftime("%y:%m:%d - %H:%M:%S") 
        if name:
            greeting_text.value  = f'{timestamp} Hello {name}'
            greeting_text.color = None
            name_input.value = None   

            greeting_history.append(f"{timestamp} - {greeting_history} - {name}")
            print(greeting_history)
            history_text.value = f"History\n" + "\n".join(greeting_history)
        else:
            greeting_text.value = 'Enter correct name'
            greeting_text.color = ft.Colors.RED
        
        page.update()

    name_input = ft.TextField(label='enter your name', on_submit=one_button_click, expand=True)
    button_text = ft.TextButton(text='Send', on_click=one_button_click)
    button_elevated = ft.ElevatedButton(text='Send', on_click=one_button_click)
    button_icon = ft.IconButton(icon=ft.Icons.SEND, on_click=one_button_click)

    def clear_history(e):
        greeting_history.clear()
        history_text.value = "History of greeting"
        page.update()

    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    # page.add(greeting_text, name_input, button_text, button_elevated, button_icon, history_text)

    view_greeting_text = ft.Row([greeting_text], alignment=ft.MainAxisAlignment.CENTER)

    page.add(view_greeting_text, greeting_text, ft.Row([name_input, button_elevated, clear_button]), history_text)

    
ft.app(target=main, view=ft.WEB_BROWSER)