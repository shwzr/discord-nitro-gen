import random
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

for i in range(100000):
    first = ''.join((random.choice(chars) for i in range(16)))
    result = "https://discord.gift/" + first
    output = open("tokens.txt", "a")
    output.write(result + "\n")

