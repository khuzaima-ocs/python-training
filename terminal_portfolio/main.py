my_info = {
    "name": "Khuzaima Ahmed",
    "designation": "Associate Software Engineer",
    "University": "PUCIT, Lahore",
    "Skills": [
        "MERN Stack Developer",
        "Python, C/C++, Java, JavaScript",
        "Git, Figma, Canva",
        "Flutter React-Native",
        "MySQL, SQLite, MongoDB"
    ],
    'connects': [
        {
            "platform": "Facebook",
            "URL": "https://www.facebook.com/khuzaima"
        },
        {
            "platform": "Instagram",
            "URL": "https://www.instagram.com/khuzaima"
        },
        {
            "platform": "Github",
            "URL": "https://github.com/khuzaima"
        },
        {
            "platform": "GMail",
            "URL": "khuzaima@gmail.com"
        }
    ]
}

help = """
Usage: tell [flags]

-h              Help
-info           Ask about Khuzaima
-skills         Ask for his skills
-con            How you can connect with Khuzaima
-q              Quit
"""

info = f"""
Name:           {my_info["name"]}
University:     {my_info["University"]}
Designation:    {my_info['designation']}
"""

connects = "You can connect with Khuzaima here:\n\n" + "\n".join(
    map(lambda c: f"{c['platform']}:       {c['URL']}", my_info['connects'])
)

while True:
    print("C:\\Khuzaima> ", end="")
    command: str = input()

    if not command.lower().startswith("tell"):
        print(f"The command [{command}] is not recognized..")
        print(f"Sample Command: [tell -h]\n")
        continue

    command = command.split('-')
    if len(command) > 1:
        command = "-" + command[1]
    else:
        print(f"The command [{command[0]}] is not recognized..")
        print(f"Sample Command: [tell -h]\n")
        continue

    match command:
        case "-h":
            print(help)

        case "-q":
            print("Thank you..!!")
            print()
            break

        case "-info":
            print(info)

        case "-con":
            print(connects)
            print()

        case "-skills":
            print()
            for skill in my_info["Skills"]:
                print(skill)
            print()

        case _:
            print("Invalid flag. Run [tell -h] to see valid commands\n")