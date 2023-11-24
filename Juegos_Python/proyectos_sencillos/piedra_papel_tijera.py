import random

def is_win(player, opponent):
    if (player == "r" and opponent == "t") or (player == "t" and opponent == "p") or (player == "p" and opponent == "r"):
        return True
    return False

def play():
    user = input("r para roca, p para papel y t para tijeras:\n")
    computer = random.choice(["r", "p", "t"])

    if user == computer:
        return "Empate"

    if is_win(user, computer):
        return "Has ganado!"
    return "Has perdido!"

resultado = play()
print(resultado)
