

def new_password(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6:
        print("True")

    else:
        print(" False ")




oldpassword = (input(' Voer het oude wachtwoord in: '))
newpassword = (input(' Voer het nieuwe wachtwoord in: '))

new_password(oldpassword,newpassword)