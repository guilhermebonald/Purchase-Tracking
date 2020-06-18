from selenium import webdriver
import smtplib
from email.mime.text import MIMEText
from time import sleep

#Coleta de dados.

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45')

wd = webdriver.Chrome(options= options)
wd.get('https://portal.patrus.com.br/tracking/cli/e/Tracking/Info.aspx?CGC=&TRACKINGNUMBER=ML024158533855030047936739QXD&TIPO=R')
sleep(10)

pack_state = wd.find_element_by_xpath('//div[@class="timeline"]').text
sleep(2)

#Envio de Email.
def email(pack_state):
    conexao_host = 'smtp.gmail.com'
    conexao_port = 465

    #email e senha para login.
    username = 'fxflat16@gmail.com' 
    password = 'gui35452609'

    #from / to
    from_email = 'fxflat16@gmail.com'
    to_email = 'guilhermebonald@hotmail.com'

    msg = MIMEText(pack_state)
    msg['subject'] = 'Vidro camera LG G6. Status de entrega.'
    msg['from'] = from_email
    msg['to'] = to_email

    server = smtplib.SMTP_SSL(conexao_host, conexao_port)

    server.login(username, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

email(pack_state)
wd.quit()