from pyscript import display, document

def account_authenticator(e):

    document.getElementById('output').innerHTML = ""

    username = document.getElementById('username').value
    password = document.getElementById('password').value

#character counter
    user_count = 0
    for letter in username:
        user_count += 1

    if user_count >= 7:
        pass_count = 0
        for letter in password:
            pass_count += 1

        if pass_count >= 10:
            has_letter = False
            has_number = False

    #password requirements
            for letter in password:
                if letter.isalpha():
                    has_letter = True
                if letter.isdigit():
                    has_number = True

            if has_letter:
                if has_number:
                    display("Account Created!", target="output")
                else:
                    display("Password MUST contain at least ONE NUMBER.", target="output")
            else:
                display("Password MUST contain at least ONE LETTER.", target="output")

    #character requirements
        else:
            display("Password must be at least 10 characters long.", target="output")

    else:
        display("Username must be at least 7 characters long.", target="output")

