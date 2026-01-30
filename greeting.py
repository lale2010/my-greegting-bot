import random
def main():
    # Список пожеланий на английском
    wishes = [
        "Have a wonderful and productive day! 🚀",
        "Success is in your hands today! ✨",
        "Keep smiling and do your best! 😊",
        "You are capable of amazing things! 🔥",
        "Enjoy every moment of your work! 🌟"
    ]

    # Список цветов (синий, зеленый, желтый, красный, розовый)
    colors = ["\033[94m", "\033[92m", "\033[93m", "\033[91m", "\033[95m"]
    reset = "\033[0m"

    # 1. Спрашиваем имя (на английском)
    name = input("What is your name? ")

    # 2. Выбираем случайное пожелание и случайный цвет
    random_wish = random.choice(wishes)
    random_color = random.choice(colors)

    # 3. Красивый вывод результата
    print("\n" + "=" * 30)
    print(f"Hello, {name}!")
    print(f"{random_color}{random_wish}{reset}")
    print("=" * 30)

if __name__ == "__main__":
    main()
