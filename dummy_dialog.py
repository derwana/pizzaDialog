import random

def rand_greeting():
    greetings = ['Guten Morgen', 'Hallo']
    question = [', was kann ich für Sie tun?', '!']
    return (random.choice(greetings) + random.choice(question))

def rand_farewell():
    farewells = ['Ihre Pizza wird in 5 Minuten geliefert!', 'Gut, kommt.', 'Die Pizza wird Ihnen in 5 Minuten geliefert.']
    return random.choice(farewells)

# def check_sorte():
#    if !sorte:
#        aks = ['Welche Pizza hätten Sie denn gerne?', 'Was für eine?']
#        input (sst)
#        check_sorte()
#    else:
#       return True

def main():
    # random greeting
    print(rand_greeting())

    # do-while
        # first input (stt)
        # cut stopwords
        # analysing input (create and fill class)

        # check if sorte
        # ask belag
        # ask boden

        # ask "noch etwas" (second pizza)
    # while "noch etwas"

    # random bye
    print(rand_farewell())

# run Main Function
main()