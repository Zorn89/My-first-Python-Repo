import random # importier random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors'] # Diese Funktion erstellt eine Liste mit den möglichen Auswahlmöglichkeiten: 
    return random.choice(choices) #Mit der Funktion  wird zufällig eine Wahl aus dieser Liste getroffen, die dann als Rückgabewert der Funktion dient.

def get_user_choice(): # Diese Funktion fragt den Benutzer nach seiner Wahl
    while True:
        user_choice = input("Enter rock, paper, or scissors: ").lower() #Es wird überprüft, ob die Eingabe des Benutzers einer der gültigen Optionen entspricht. 
        if user_choice in ['rock', 'paper', 'scissors']: 
            return user_choice
        else:
            print("Invalid input. Please choose rock, paper, or scissors.") # Wenn die Eingabe ungültig ist, wird der Benutzer aufgefordert, erneut zu wählen, bis eine gültige Eingabe erfolgt.

def determine_winner(user_choice, computer_choice): # Diese Funktion bestimmt den Gewinner, indem sie die Auswahl des Benutzers mit der des Computers vergleicht.
    if user_choice == computer_choice: # Wenn die beiden Auswahlen gleich sind, gibt die Funktion "It's a tie!"  zurück.
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"  # Wenn der Benutzer gewinnt, also die Wahl des Benutzers gegen die des Computers gemäß den Regeln (Rock > Scissors, Paper > Rock, Scissors > Paper) gewinnt, gibt die Funktion "You win!" zurück.
    else:
        return "Computer wins!" # gewinnt der Computer, und es wird "Computer wins!" zurückgegeben.

def play_game():
    print("Welcome to Rock, Paper, Scissors!") # Begrüßungsnachricht
    
    while True:
        user_choice = get_user_choice() #  die Wahl des Benutzers erhalten
        computer_choice = get_computer_choice() # Wahl des Computers.
        
        print(f"You chose: {user_choice}") # Ausgabe Lösung
        print(f"Computer chose: {computer_choice}") # Ausgabe Lösung
        
        result = determine_winner(user_choice, computer_choice)
        print(result) # Ermittlung Gewinner und Ausgabe
        
        play_again = input("Do you want to play another round? (yes/no): ").lower() # Nachfrage ob erneut gespielt werden möchte
        if play_again != 'yes':
            print("Thanks for playing!") # Verabschiedung
            break

# Run the game
if __name__ == "__main__":
    play_game()


