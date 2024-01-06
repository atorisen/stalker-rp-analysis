import requests, uuid, subprocess, random
from time import sleep

def generate_username():
    chars = "1234567890abcdef"
    username = ''
    for i in range(20):
        username += random.choice(chars)
    return username

def auth(ucp, hwid, usr):
    params = {
        "nicknamu": ucp,
        "machinu": hwid,
        "hashu": usr
    }
    req = requests.get("https://files.stalker-rp.net/launcher/api/register.php", params=params)
    if req.status_code != 200:
        return False
    return True

def start(usr, samp):
    subprocess.Popen(f"\"{samp}\\samp.exe\" -c -n {usr} -h 103.214.68.49 -p 7777", cwd=samp)
    return

def main():
    # Путь к папке stalker-rp, содержащей samp.exe
    samp_path = "C:\\Program Files (x86)\\STALKER-RP-NET\\content\\game"

    # Это ваш идентификатор, который админы используют для бана по железу
    # Я сделал его случайным, но админы могут заметить это, и вы будете забанены
    # Вы можете заменить его своим собственным значением GUID
    machine_uuid = str(uuid.uuid4())

    # Это ваш временный ник для входа на сервер
    username = generate_username()

    ucp_login = input("enter your ucp login: ")

    auth_result = auth(ucp_login, machine_uuid, username)
    if not auth_result: print("auth failed"); return

    print("auth success\nstarting game")
    start(username, samp_path)

main()
sleep(5)
