import requests
terms = ["exit","quit","EXIT","QUIT","bye","Bye","BYE"]
spacer = " "*2
star = "*"*40
print(f"{star}\n{spacer}Instagram Account Existence Checker{spacer}\n{star}".upper())
print("                   CODED BY MayankNCodes\n")
vall = "0"
debug = False
while vall=="0":
    val = input("Enter the Username:")
    url = 'https://www.instagram.com/{}/'.format(val)
    send = requests.get(url)
    response = send.content
    strr = response.decode('utf-8')
    lenn = len(strr)
    if debug==True:
        if val in terms:
            print("Exiting...")
            vall=1
        else:
            if lenn<300000:
                print('\n[-] {} ACCOUNT DOES NOT EXIST\nRESPONSE LENGTH: {}\n'.format(val,lenn))
            if lenn>300000:
                print('\n[+] {} ACCOUNT EXISTS\nRESPONSE LENGTH: {}\n'.format(val,lenn))
    if debug==False:
        if val in terms:
            print("Exiting...")
            vall=1
        else:
            if lenn<300000:
                print(f'\n[-] {val} ACCOUNT DOES NOT EXIST\n')
            if lenn>300000:
                print(f'\n[+] {val} ACCOUNT EXISTS\n')
    
