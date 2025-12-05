import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "My first app"
    greeting_text = ft.Text(value="Hello world", color=ft.Colors.RED)
    greeting_history = []  
    history_text = ft.Text("History of greetings:\n")

    def one_button_click(e):
        name = name_input.value.strip()
        timestamp = datetime.now()

        if name:
            record = f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} | {name}"
            greeting_text.value = f"Hello, {name}!"
            greeting_text.color = None
            name_input.value = ""

            greeting_history.append(record)

            if len(greeting_history) > 5:
                greeting_history.pop(0)

            history_text.value = "History:\n" + "\n".join(greeting_history)
        else:
            greeting_text.value = "Enter correct name"
            greeting_text.color = ft.Colors.RED

        page.update()

    def filter_morning(e):
        filtered = []  
        for record in greeting_history:
            time_str = record.split(" | ")[0].split(" ")[1]  
            hour = int(time_str.split(":")[0])  

            if hour < 12:  
                filtered.append(record)

        history_text.value = "Morning greetings:\n" + "\n".join(filtered)
        page.update()

    def filter_evening(e):
        filtered = []  
        for record in greeting_history:
            time_str = record.split(" | ")[0].split(" ")[1]  
            hour = int(time_str.split(":")[0])  
            if hour >= 12:  
                filtered.append(record)

        history_text.value = "Evening greetings:\n" + "\n".join(filtered)
        page.update()

    name_input = ft.TextField(label="Enter your name", on_submit=one_button_click)
    button_send = ft.ElevatedButton("Send", on_click=one_button_click)
    button_morning = ft.ElevatedButton("Show morning greetings", on_click=filter_morning)
    button_evening = ft.ElevatedButton("Show evening greetings", on_click=filter_evening)

    
    page.add(
        greeting_text,
        ft.Row([name_input, button_send]),
        ft.Row([button_morning, button_evening]),
        history_text
    )

ft.app(target=main)