import itertools
import string
import time
from zipfile import ZipFile, ZIP_STORED


## Richtigkeit des Passwortes überprüfen
def is_password_correct(zip_path, output_path, str_password):
    try:
        with ZipFile(zip_path, mode='r', compression=ZIP_STORED, allowZip64=True) as zip_file:
            zip_file.setpassword(bytes(str_password, "utf-8"))
            zip_file.extractall(path=output_path)
            return True
    except Exception as e:
        pass
    return False


## Brute-Force
def brute_force(zip_path, output_path):
    letters = string.ascii_letters + string.digits + string.punctuation

    print("===== Passwort wird ermittelt (Brute-Force) =====")
    for i in range(1, 1000):
        start = time.time()
        for password in map("".join, itertools.product(letters, repeat=i)):
            if is_password_correct(zip_path, output_path, password):
                return password

        end = time.time()
        print(str(i) + "er Buchstabenkombinationen {:5.3f}s".format(end-start))


## Dictionary
def dictionary(zip_path, output_path, passwordlist_path):
    passwordlist = open(passwordlist_path, "r")

    print("===== Passwort wird ermittelt (Dictionary) =====")
    for line in passwordlist:
        password = line.rstrip()
        if is_password_correct(zip_path, output_path, password):
            passwordlist.close()
            return password
    passwordlist.close()
    return None


zip_path = "files/mama.zip"
output_path = "files/temp"
passwordlist_path = "passwordlist.txt"
password = ""
start = 0
end = 0


try:
    with ZipFile(zip_path, mode='r', compression=ZIP_STORED, allowZip64=True) as zip_file:
        zip_file.extractall(output_path)
except Exception as e:
    start = time.time()

    password = dictionary(zip_path, output_path, passwordlist_path)
    if password == None:
        password = brute_force(zip_path, output_path)
    end = time.time()
finally:
    print()
    if password == None:
        print("===== Es konnte kein Passwort ermittelt werden =====")
    elif password == "":
        print("===== ZIP-Datei hat kein Passwort =====")
    else:
        print("===== Paswort gefunden: " + password + " =====")
        print("===== Dauer: {:5.3f}s =====".format(end - start))
