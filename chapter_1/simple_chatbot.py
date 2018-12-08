import re


MY_NAMES = {'rosa', 'rose', 'chatty', 'chatbot', 'bot', 'chatterbot'}

CURT_NAMES = {'hal', 'you', 'u'}

GREETING_PATTERN = re.compile(
    r"[^a-z]*([y]o|hi|[h']?ello|ok|hey|(good[ ])?(morn[gin']{0,3}|afternoon|even[gin']{0,3}))[\s,;:]{1,3}([a-z]{1,20})",
    flags=re.IGNORECASE)

LEAVE_PATTERN = re.compile(r"bye.*", flags=re.IGNORECASE)


def main():
    greeter_name = None
    while True:
        text = input("you: ")
        if LEAVE_PATTERN.match(text):
            print('Rosa: bye.')
            break
        else:
            match = GREETING_PATTERN.match(text)
            if match:
                at_name = match.groups()[-1]
                if at_name in CURT_NAMES:
                    print("Good one.")
                elif at_name.lower() in MY_NAMES:
                    print("Hi {}, How are you?".format(greeter_name or ''))
            else:
                print("Rosa: Sorry I don't understand")


main()
