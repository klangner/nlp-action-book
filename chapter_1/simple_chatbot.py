import re


# List of possible chatbot names.
# Can be used in phrases as 'Hello Rose'
MY_NAMES = {'rosa', 'rose', 'chatty', 'chatbot', 'bot', 'chatterbot'}

# It is also possible to use those names, but chatbot doesn't really like them
CURT_NAMES = {'hal', 'you', 'u'}

# Our chatbot is rule based, and the rules are based on regular expression.
# The following pattern checks if the phrase use a greeting.
# If it is, then we expect that the last group will contain name given to the chatbot
GREETING_PATTERN = re.compile(
    r"[^a-z]*([y]o|hi|[h']?ello|ok|hey|(good[ ])?(morn[gin']{0,3}|afternoon|even[gin']{0,3}))[\s,;:]{1,3}([a-z]{1,20})",
    flags=re.IGNORECASE)

# This pattern will check if the phrase ends conversation lie 'bye'
LEAVE_PATTERN = re.compile(r"bye.*", flags=re.IGNORECASE)


# Main loop:
#   * We read the text from the console
#   * Based on entered phrase give answer
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


# Start app
main()
