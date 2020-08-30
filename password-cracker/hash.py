import hashlib

## Rainbowtable
def gen_rainbowtable(passwordlist_path, rainbowtable_path):
    passwordlist = open(passwordlist_path, "r")
    rainbowtable = open(rainbowtable_path, "w")

    print("===== Rainbowtable wird erstellt =====")
    for line in passwordlist:
        password = line.rstrip()
        hash = hashlib.sha512(bytes(password, "utf-8"))
        rainbowtable.write(hash.hexdigest() + "#" + password + "\n")
    rainbowtable.close()
    passwordlist.close()

def crack_hash(hash, rainbowtable_path):
    rainbowtable = open(rainbowtable_path, "r")

    print("===== Hash wird ermittelt =====")
    for line in rainbowtable:
        hash_password = line.rstrip().split("#", 1)
        if hash == hash_password[0]:
            rainbowtable.close()
            return hash_password[1]
    rainbowtable.close()
    return None

## Initalisierung der Werte
passwordlist_path = "passwordlist.txt"
rainbowtable_path = "rainbowtable.txt"

def get_password_with_encryption():
    gen_rainbowtable(passwordlist_path, rainbowtable_path)
    password = crack_hash("eab9c07645dc3b67333e3a8e1547ec41a1e46fc3e3446838afa43bcb2c8026621ddc982bb2c159019ac6e51eb398f61761136cc50f5175a2724057fce4511f6d", rainbowtable_path)
    print("===== Passwort gefunden: " + password + " =====")