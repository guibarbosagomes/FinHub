#%%
from os import getenv

import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

from datetime import datetime, time

import pandas as pd
#%%

load_dotenv("../../Env/.env")

#%%
def enviar_email_registro( destinatario, nome_completo, dt_nascimento, usuario, email, dt_cadastro):

    # Crie a mensagem de e-mail
    smtp_server = getenv("SMTP_SERVER")
    port = getenv("SMTP_PORT")
    sender_email = getenv("SMTP_EMAIL_SENDER")
    password = getenv("SMTP_EMAIL_PASSWORD")
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = destinatario
    msg['Subject'] = "Cadastro FinHub"


    # Bom dia ou boa tarde
    if datetime.now().time() < time(12, 00):
        bom_dia_tarde = "Olá, bom dia !"
    else:
        bom_dia_tarde = "Olá, boa tarde !"

    # Estilização da tabela
    css_style = """
                <style>
                    body {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                    }
                    table {
                        width: 50%;
                        border-collapse: collapse;
                        margin: auto;
                    }
                    th, td {
                        padding: 8px;
                        text-align: left;
                        border: 1px solid #ddd;
                    }
                    tr:nth-child(even) {
                        background-color: #f2f2f2;
                    }
                    th {
                        background-color: #4CAF50;
                        color: white;
                    }
                    .bold {
                        font-weight: bold;
                        background-color: #f5f5f5;
                    }
                </style>  
        """

    # Corpo do e-mail em HTML
    html_content = f"""
        <!DOCTYPE html>
            <html lang="pt-BR">
            <head>
                <meta charset="UTF-8">
                {css_style}
            </head>
            <body>
            <p>{bom_dia_tarde}</p>
            </br>
            </br>
                <table>
                    <tr>
                        <td class="bold">Nome Completo</td>
                        <td>{nome_completo}</td>
                    </tr>
                    <tr>
                        <td class="bold">Data de Nascimento</td>
                        <td>{dt_nascimento}</td>
                    </tr>
                    <tr>
                        <td class="bold">Nome do Usuário</td>
                        <td>{usuario}</td>
                    </tr>
                    <tr>
                        <td class="bold">Email</td>
                        <td>{email}</td>
                    </tr>
                    <tr>
                        <td class="bold">Data do Cadastro</td>
                        <td>{dt_cadastro}</td>
                    </tr>
                </table>
            </br>
            </br>
            <p>Atenciosamente, equipe FP&A</p>
            </body>
            </html>
            """

    # Anexe o corpo do e-mail
    msg.attach(MIMEText(html_content, 'html'))

    # Envie o e-mail
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, destinatario, msg.as_string())
#%%


def enviar_email_rec_senha( destinatario, codigo):

    # Crie a mensagem de e-mail
    smtp_server = getenv("SMTP_SERVER")
    port = getenv("SMTP_PORT")
    sender_email = getenv("SMTP_EMAIL_SENDER")
    password = getenv("SMTP_EMAIL_PASSWORD")
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = destinatario
    msg['Subject'] = "Recuperar Senha FinHub"


    # Bom dia ou boa tarde
    if datetime.now().time() < time(12, 00):
        bom_dia_tarde = "Olá, bom dia !"
    else:
        bom_dia_tarde = "Olá, boa tarde !"

    # Estilização da tabela
    css_style = """
                <style>
                    body {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                    }
                    table {
                        width: 50%;
                        border-collapse: collapse;
                        margin: auto;
                    }
                    th, td {
                        padding: 8px;
                        text-align: left;
                        border: 1px solid #ddd;
                    }
                    tr:nth-child(even) {
                        background-color: #f2f2f2;
                    }
                    th {
                        background-color: #4CAF50;
                        color: white;
                    }
                    .bold {
                        font-weight: bold;
                        background-color: #f5f5f5;
                    }
                </style>  
        """


    # Corpo do e-mail em HTML
    html_content = f"""
        <!DOCTYPE html>
            <html lang="pt-BR">
            <head>
                <meta charset="UTF-8">
                {css_style}
            </head>
            <body>
            <p>{bom_dia_tarde}</p>
            <p>Para alterar a senha, utilize o codigo abaixo no <a href= "http://localhost:8502/alterar_senha"> Link </a> para recuperar sua senha.</p></br>
            </br>
                <table>
                    <tr>
                        <td class="bold">Código secreto</td>
                        <td>{codigo}</td>
                    </tr>
                    
                </table>
            </br>
            </br>
            <p>Atenciosamente, equipe FP&A</p>
            </body>
            </html>
            """

    # Anexe o corpo do e-mail
    msg.attach(MIMEText(html_content, 'html'))

    # Envie o e-mail
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, destinatario, msg.as_string())