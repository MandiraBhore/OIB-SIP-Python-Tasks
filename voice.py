import webbrowser
import datetime

def assistant():
    print("Hello! Main aapka Python Assistant hoon.")
    while True:
        query = input("Main kya kar sakta hoon? (time/google/exit): ").lower()

        if 'time' in query:
            waqt = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Abhi waqt ho raha hai: {waqt}")
        
        elif 'google' in query:
            search = input("Kya search karna hai? ")
            webbrowser.open(f"https://www.google.com/search?q={search}")
        
        elif 'exit' in query:
            print("Goodbye!")
            break
        else:
            print("Option select karein: time, google, ya exit.")

assistant()