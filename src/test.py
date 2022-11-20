import trafilatura, re, requests, os
from googlesearch import lucky
from main import textName

url = lucky(textName)
print(url)

r = requests.get(url)
if r.status_code >= 200 and r.status_code < 300:
    downloaded = trafilatura.fetch_url(url)
    text = trafilatura.extract(downloaded)


    with open("e.txt","w", encoding="utf-8") as file:
        file.write(text)
    os.replace(f"{os.getcwd()}\\e.txt", f"{os.getcwd()}\\data\\e.txt")

    splitText = text.split("|")

    with open("eee.txt", "w", encoding="utf-8") as file:
        checkCommit = False
        for i in splitText:
            if checkCommit == False:
                if len(i) > 200:
                    file.write(str(i).split(".")[0] + ".")
                    checkCommit = True

    os.replace(f"{os.getcwd()}\\eee.txt", f"{os.getcwd()}\\data\\eee.txt")

else:
    print("Problem accessing website")
print(os.getcwd())