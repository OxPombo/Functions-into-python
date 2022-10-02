def greetings (weekday, person = 'Person', greet = 'Hello'):
    
    print(f"{greet.title()} {person.title()}, how are you in this {weekday}?")



greetings('Monday', person = 'Andrei', greet = 'Hi')  
greetings('Tuesday', person = 'Jorge', greet = 'Yoooo')