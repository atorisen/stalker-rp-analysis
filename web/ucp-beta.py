import requests

head = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0"}

def ajax_request(form):
    req = requests.post("https://beta.stalker-rp.net/account/register/ajax", headers=head, data=form)
    return req.json()

def main():
    login = input("enter login: ")
    email = input("enter email: ")
    password = input("enter password: ")
    
    form = {
        "login": login,
        "email": email,
        "password": password,
        "repeatpassword": password
    }
    request = ajax_request(form)
    print("\nserver returned:\n", request)
