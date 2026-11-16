from services.assistant import get_response
import flet as ft

def send_message(e, message_input, messages, messages_column):
    if message_input.value.strip():
        messages.append(message_input.value)
        messages_column.controls.append(
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(
                            message_input.value,
                            color="#FFFFFF",
                            size=16,
                            weight=ft.FontWeight.W_500
                        ),
                        bgcolor="#51403A",
                        padding=15,
                        border_radius=12,
                    )
                ],
                alignment=ft.MainAxisAlignment.END,
                expand=True
            )
        )
        messages_column.update()
        message_input.value = "" 
        message_input.update()
        response = get_response(messages[-1])
        echo_message(response, messages_column)


def echo_message(message, messages_column):
    messages_column.controls.append(
        ft.Row(
            controls=[
                ft.Container(
                    content=ft.Text(
                        message,
                        color="#FFFFFF",
                        size=16
                    ),
                    bgcolor="#6B352A",
                    padding=15,
                    border_radius=12
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            expand=True
        )
    )
    messages_column.update()

def new_chat(e, messages, messages_column):
    messages.clear()
    messages_column.controls.clear()
    echo_message("Hello! I'm Echo. How can I help you?", messages_column)
   
def main(page: ft.Page):
    page.title = "Echo"
    page.window.width = 1100
    page.window.height = 750

    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#242323"
    
    message_input = ft.TextField(
        hint_text="Message Echo...",
        width=600,
        border_radius=15,
        bgcolor="#393432",
        hint_style=ft.TextStyle(color="#D9C6B5"),
        text_style=ft.TextStyle(color="#F5EEE5")
    )


    messages = []
    messages_column = ft.Column(
        controls=[],
        scroll=ft.ScrollMode.AUTO,
        auto_scroll=True
    )
    chat_area = ft.Container(
        content=messages_column,
        width=700,
        height=400,
        bgcolor="#393432",
        padding=15,
        border_radius=20
    )

    sidebar = ft.Container(
    content=ft.Column(
        controls=[
            ft.Text(
                "Echo",
                size=28,
                weight=ft.FontWeight.BOLD,
                color="#FFF1A6"
            ),

            ft.Button(
                content="+ New Chat",
                bgcolor="#6B352A",
                color="#FFF1A6",
                on_click=lambda e: new_chat(e, messages, messages_column),
            ),

            ft.Text("WORKSPACE", color="#D9C6B5"),
            ft.Text("Chat History", color="#F5EEE5"),
            ft.Text("Projects", color="#F5EEE5"),
            ft.Text("Tasks", color="#F5EEE5"),

            ft.Text("Settings", color="#F5EEE5")
        ]
    ),
    width=220,
    height=650,
    bgcolor="#302723",
    padding=20,
    border_radius=15
    )

    chat_interface = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Icon(
                        ft.Icons.GRAPHIC_EQ,
                        color="#FFF1A6",
                            size=36
                    ),

                    ft.Text(
                        "Hello, I'm Echo.",
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        color="#F5EEE5"
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            

            
      
                ft.Text(
                    "Listen.  Think.  Assist.",
                    size=22,
                    color="#FFF1A6"
                ),
                 
                ft.Text(
                    "Your intelligent companion, ready to help you think, create and get things done.",
                    size=16,
                    italic=True,
                    color="#B8C0D9",
                ),
                    
                chat_area,

                ft.Row(
                    controls=[
                        message_input,
                        ft.Button(
                            content="Send",
                            on_click=lambda e: send_message(e, message_input, messages, messages_column),
                            bgcolor="#FFF1A6",
                            color="#6B352A"
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
        ],
        spacing=18,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True
    )

    page.add(
        ft.Row(
            controls=[
                sidebar,
                chat_interface
            ],
            expand=True
        )
    )

    
    echo_message("Hello! I'm Echo. How can I help you?", messages_column)

        