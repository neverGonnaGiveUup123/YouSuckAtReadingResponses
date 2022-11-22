import trafilatura, re, requests, os, json
from googlesearch import lucky
from main import textName

url = lucky(textName)
print(url)

r = requests.get(url)

if str(r.status_code)[0] == "2":
    
    downloaded = trafilatura.fetch_url(url)
    text = trafilatura.extract(downloaded)

    with open("extractedContent.txt", "w", encoding="utf-8") as file:
        file.write(text)
    os.replace(f"{os.getcwd()}\\extractedContent.txt", f"{os.getcwd()}\\data\\extractedContent.txt")

    splitText = text.split("|")

    with open("eee.txt", "w", encoding="utf-8") as file:
        checkCommit = False
        for i in splitText:
            if checkCommit == False:
                if len(i) > 200:
                    file.write(str(i).split(".")[0] + ".")
                    checkCommit = True

    os.replace(f"{os.getcwd()}\\eee.txt", f"{os.getcwd()}\\data\\eee.txt")

    listedText = text.split(" ")
    testList = []

    with open("ee.txt", "w", encoding='utf-8') as file:
        checkCommit = False
        for i in listedText:
            if  re.search("Characters", i) != None:
                # if re.search(listedText[i.index() + 1], []):
                #     pass
                print("EEEEEEEEEEEEEEEEEEE")
                testList.append(i)
                if checkCommit == False:
                    for j in range(listedText.index(i), listedText.index(i) + 10):
                        print(listedText[j])
                        checkCommit = True

        with open("test.json", "w", encoding="utf-8") as testFile:
            json.dump(str(testList),testFile)

        file.write(str(listedText))
    os.replace(f"{os.getcwd()}\\ee.txt", f"{os.getcwd()}\\data\\ee.txt")




else:
    print("Problem accessing website")
print(os.getcwd())
