from cryptography.fernet import Fernet
"""def write_key():
    key = Fernet.generate_key()
    with open('key.key' , 'wb') as key_file:
        key_file.write(key)
write_key()"""
def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for lines in f.readlines():
            data = lines.rstrip()
            user , pasw = data.split('|')
            print('username: ', user, '| password: ', fer.decrypt(pasw.encode()).decode() )

def add():
    account = input('enter Account name: ')
    pwd = input('enter password: ')
    
    with open('passwords.txt', 'a') as f:
        f.write(account + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input('do u wanna add a password or view the existing ones? or enter q to quit (view / add / q) ').lower()
    if mode == 'q':
        break
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode!')
        continue