user_name=(input("Enter your name: "))
if user_name:
    with open("user_info.txt", "a") as file:
        file.write(user_name + "\n")
show_info=(input("Do you want to see your name (y  for Yes/n  for No): "))
if show_info.lower() == 'y':
    try:
        with open("user_info.txt", "r") as file:
            content=file.readlines()
    except Exception as e:
        print(e,type(e))
    else:
        for line in content:
            print(f" {line.rstrip()}")