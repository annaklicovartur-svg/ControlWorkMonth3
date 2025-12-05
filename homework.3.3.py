# Homework 1

import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Homework 3.3"
    
    name_input = ft.TextField(label="Введите ваше имя")
    result = ft.Text(value="", color=ft.Colors.BLUE)
    
    def on_submit(e):
        name = name_input.value.strip()
        timestamp = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")
        
        if name:
            result.value = f"{timestamp} - Привет, {name}!"
            result.color = ft.Colors.GREEN
        else:
            result.value = "Пожалуйста, введите ваше имя!"
            result.color = ft.Colors.RED
        
        page.update()
    
    name_input.on_submit = on_submit
    
    page.add(name_input, result)

ft.app(target=main, view=ft.WEB_BROWSER)


# ДЗ номер 2 (Инструкция по запуску: один екст закоментировать, и нужный запускать)
import flet as ft

def main(page: ft.Page):
    page.title = 'Button_change'
    page.theme_mode = ft.ThemeMode.DARK

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    def button_click(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        
        page.update()
    
    button_elevated = ft.ElevatedButton(text='Change theme', on_click=button_click)
    
    page.add(button_elevated)

ft.app(target=main, view=ft.WEB_BROWSER)