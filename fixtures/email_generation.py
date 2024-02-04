import string
import requests

from random import choice


API = 'https://www.1secmail.com/api/v1/'


def generate_email():
    domains = ["1secmail.com", "1secmail.org", "1secmail.net"]
    email = f"{''.join(choice(string.ascii_lowercase + string.digits) for i in range(10))}@{choice(domains)}'"
    return email


def get_message(generate_email):
    api_wait_message = f'{API}?action=getMessages&login={generate_email.split("@")[0]}&domain={generate_email.split("@")[1]}'
    response = requests.get(api_wait_message).json()
    return len(response)
