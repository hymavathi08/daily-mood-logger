import datetime
import random

# Motivational quotes based on mood
quotes = {
    "happy": [
        "Keep spreading your joy! 🌟",
        "Happiness is contagious. Share it! 😄",
        "You're shining bright today! ☀️"
    ],
    "sad": [
        "Tough times don't last, tough people do. 💪",
        "Every day may not be good, but there's good in every day. 🌈",
        "Hang in there. Better days are coming. 🕊️"
    ],
    "angry": [
        "Take a deep breath. Let go of what you can't control. 🧘",
        "Peace begins with a smile. 🙂",
        "Anger doesn't solve problems, calm does. 💡"
    ],
    "stressed": [
        "You’ve got this. One step at a time. 🛤️",
        "Breathe. Rest. Reset. 💆",
        "Difficult roads often lead to beautiful destinations. 🌄"
    ],
    "default": [
        "Believe in yourself and all that you are. 🌟",
        "Each day is a new beginning. Start fresh. 🌼",
        "Your future is created by what you do today. 🚀"
    ]
}

def get_quote(mood):
    mood = mood.lower()
    return random.choice(quotes.get(mood, quotes["default"]))

def log_mood(mood):
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    quote = get_quote(mood)

    entry = f"{today} - Mood: {mood.capitalize()} - Quote: \"{quote}\"\n"

    with open("mood_logs.txt", "a") as file:
        file.write(entry)

    print("\n✅ Mood logged successfully!")
    print(f"💬 Your quote: {quote}")

def view_logs():
    print("\n📔 Mood Log History:")
    try:
        with open("mood_logs.txt", "r") as file:
            content = file.read()
            print(content if content else "No logs found yet.")
    except FileNotFoundError:
        print("No logs found yet.")

def main():
    while True:
        print("\n--- Daily Mood & Motivation Logger ---")
        print("1. Log today's mood")
        print("2. View mood history")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            mood = input("Enter your mood today: ")
            log_mood(mood)
        elif choice == "2":
            view_logs()
        elif choice == "3":
            print("Goodbye! Take care 💖")
            break
        else:
            print("Invalid input. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
