
while True:
    textName = input("Enter the name of the text: ") + " book wikipedia"
    if input(f"Confirm \"{textName}\"? Y/N ").lower() == "y":
        break
    else:
        continue

