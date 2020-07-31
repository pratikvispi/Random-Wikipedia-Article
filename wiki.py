import wikipedia , webbrowser

def getPage():
    wikipage = wikipedia.random(1)
    wikiload = wikipedia.page(wikipage)

    userchoice = input("Would you like to read the article? {} (y/n/q)".format(wikipage)).lower().strip()

    if userchoice == 'y' :
        print("\n Summary : \n -------------- \n")
        print(wikiload.summary)

        wikiopen = input("Want to open browser for more information : (y/n)").lower().strip()

        if wikiopen == 'y':
            webbrowser.open(wikiload.url , new =2)
        else:
            getPage()
        exit(0)
    elif(userchoice == 'q'):
        exit(0)
    else:
        getPage()

if __name__ == "__main__":
    getPage()
