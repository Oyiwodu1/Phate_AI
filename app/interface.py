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
                        bgcolor="#202B49",
                        padding=15,
                        border_radius=12,
                        shadow=ft.BoxShadow(
                        blur_radius=15,
                        color="#604B9B",
                        offset=ft.Offset(4, 5)
                        ),
                        gradient=ft.LinearGradient(
                            colors=["#293B68", "#161F3D"],
                            begin=ft.Alignment.TOP_LEFT,
                            end=ft.Alignment.BOTTOM_RIGHT
                        ),
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
                    bgcolor="#30234F",
                    padding=15,
                    border_radius=12
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            expand=True
        )
    )
    messages_column.update()
   
def main(page: ft.Page):
    page.title = "Echo"
    page.window.width = 1100
    page.window.height = 750

    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0B1026"
    
    message_input = ft.TextField(
        hint_text="Message Echo...",
        width=600,
        border_radius=15,
        bgcolor="#161F3D",
        hint_style=ft.TextStyle(color="#A0AEC0"),
        text_style=ft.TextStyle(color="#FFFFFF")
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
        bgcolor="#111A33",
        padding=15,
        border_radius=20
    )


    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "Hello, I'm Echo.",
                    size=40,
                    weight=ft.FontWeight.BOLD,
                    color="#FFFFFF"
                ),

                    ft.Text(
                        "Listen.  Think.  Assist.",
                        size=22,
                        color="#A78BFA"
                    ),
                 
                    ft.Text(
                        "Your intelligent companion, ready to help you think, create and get things done.",
                        size=16,
                        italic=True,
                        color="#B8C0D9",
                    ),
                    
                    message_input,

                    chat_area,

                    ft.Button(
                        content="Send",
                        on_click=lambda e: send_message(e, message_input, messages, messages_column)
                    )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True
        )
    )
    echo_message("Hello! I'm Echo. How can I help you?", messages_column)

        