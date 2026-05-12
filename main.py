import random


def get_card_value(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)


def calculate_score(cards):
    score = sum(get_card_value(card) for card in cards)
    aces_count = cards.count('A')
    while score > 21 and aces_count > 0:
        score -= 10
        aces_count -= 1
    return score


def get_random_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)


def main():
    player_cards = [get_random_card(), get_random_card()]

    print("Добро пожаловать в Блэкджек!")
    print(f"Ваши карты: {', '.join(player_cards)}")
    print(f"Очков: {calculate_score(player_cards)}")

    while True:
        command = input("\nВведите 'more' для новой карты или 'stop' для остановки: ").lower()

        if command == 'more':
            new_card = get_random_card()
            player_cards.append(new_card)
            print(f"Вы получили карту: {new_card}")
            print(f"Ваши карты: {', '.join(player_cards)}")
            score = calculate_score(player_cards)
            print(f"Очков: {score}")

            if score > 21:
                print("\nПеребор! Вы проиграли!")
                break
            elif score == 21:
                print("\nУ вас 21 очко! Поздравляю!")
                break

        elif command == 'stop':
            score = calculate_score(player_cards)
            print(f"\nИгра окончена. Ваши очки: {score}")

            if score == 21:
                print("Блэкджек! Вы выиграли!")
            elif score > 21:
                print("Перебор! Вы проиграли!")
            else:
                print("Игра завершена.")
            break
        else:
            print("Неверная команда. Введите 'more' или 'stop'")

main()