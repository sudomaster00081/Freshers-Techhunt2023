import os
import time
import os
import time
import threading
import webbrowser

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def won():
    s1 = []
    a = r"""
    
  _____                                    _           _         _    _                                
 /  __ \                                  | |         | |       | |  (_)                               
 | /  \/  ___   _ __    __ _  _ __   __ _ | |_  _   _ | |  __ _ | |_  _   ___   _ __   ___             
 | |     / _ \ | '_ \  / _` || '__| / _` || __|| | | || | / _` || __|| | / _ \ | '_ \ / __|            
 | \__/\| (_) || | | || (_| || |   | (_| || |_ | |_| || || (_| || |_ | || (_) || | | |\__ \ _  _  _  _ 
  \____/ \___/ |_| |_| \__, ||_|    \__,_| \__| \__,_||_| \__,_| \__||_| \___/ |_| |_||___/(_)(_)(_)(_)
                        __/ |                                                                          
                       |___/                                                                           
 __   __                _   _                       _    _                                             
 \ \ / /               | | | |                     | |  | |                                            
  \ V /   ___   _   _  | |_| |  __ _ __   __  ___  | |  | |  ___   _ __                                
   \ /   / _ \ | | | | |  _  | / _` |\ \ / / / _ \ | |/\| | / _ \ | '_ \                               
   | |  | (_) || |_| | | | | || (_| | \ V / |  __/ \  /\  /| (_) || | | | _  _  _  _  _                
   \_/   \___/  \__,_| \_| |_/ \__,_|  \_/   \___|  \/  \/  \___/ |_| |_|(_)(_)(_)(_)(_)               
                                                                                                       

        """
    s1.append(a)
    b = r"""
    
     _____                                    _           _         _    _                                
    /  __ \                                  | |         | |       | |  (_)                               
    | /  \/  ___   _ __    __ _  _ __   __ _ | |_  _   _ | |  __ _ | |_  _   ___   _ __   ___             
    | |     / _ \ | '_ \  / _` || '__| / _` || __|| | | || | / _` || __|| | / _ \ | '_ \ / __|            
    | \__/\| (_) || | | || (_| || |   | (_| || |_ | |_| || || (_| || |_ | || (_) || | | |\__ \ _  _  _  _ 
    \____/ \___/ |_| |_| \__, ||_|    \__,_| \__| \__,_||_| \__,_| \__||_| \___/ |_| |_||___/(_)(_)(_)(_)
                            __/ |                                                                          
                        |___/                                                                           
    __   __                _   _                       _    _                                             
    \ \ / /               | | | |                     | |  | |                                            
    \ V /   ___   _   _  | |_| |  __ _ __   __  ___  | |  | |  ___   _ __                                
    \ /   / _ \ | | | | |  _  | / _` |\ \ / / / _ \ | |/\| | / _ \ | '_ \                               
    | |  | (_) || |_| | | | | || (_| | \ V / |  __/ \  /\  /| (_) || | | | _  _  _  _  _                
    \_/   \___/  \__,_| \_| |_/ \__,_|  \_/   \___|  \/  \/  \___/ |_| |_|(_)(_)(_)(_)(_)               
                                                                                                        

        """
    s1.append(b)
    c = r"""
    
        _____                                    _           _         _    _                                
        /  __ \                                  | |         | |       | |  (_)                               
        | /  \/  ___   _ __    __ _  _ __   __ _ | |_  _   _ | |  __ _ | |_  _   ___   _ __   ___             
        | |     / _ \ | '_ \  / _` || '__| / _` || __|| | | || | / _` || __|| | / _ \ | '_ \ / __|            
        | \__/\| (_) || | | || (_| || |   | (_| || |_ | |_| || || (_| || |_ | || (_) || | | |\__ \ _  _  _  _ 
        \____/ \___/ |_| |_| \__, ||_|    \__,_| \__| \__,_||_| \__,_| \__||_| \___/ |_| |_||___/(_)(_)(_)(_)
                                __/ |                                                                          
                            |___/                                                                           
        __   __                _   _                       _    _                                             
        \ \ / /               | | | |                     | |  | |                                            
        \ V /   ___   _   _  | |_| |  __ _ __   __  ___  | |  | |  ___   _ __                                
        \ /   / _ \ | | | | |  _  | / _` |\ \ / / / _ \ | |/\| | / _ \ | '_ \                               
        | |  | (_) || |_| | | | | || (_| | \ V / |  __/ \  /\  /| (_) || | | | _  _  _  _  _                
        \_/   \___/  \__,_| \_| |_/ \__,_|  \_/   \___|  \/  \/  \___/ |_| |_|(_)(_)(_)(_)(_)               
                                                                                                            
        
        """
    s1.append(c)
    while True:
        for art in s1:
            print(art)
            time.sleep(.5)
            clear_screen()


def play_video():
    webbrowser.open("https://cdn.dribbble.com/users/311928/screenshots/6574034/congrats1.png")

def success():
    clear_screen()
    won_thread = threading.Thread(target=won)
    time.sleep(3)
    video_thread = threading.Thread(target=play_video)
        
    won_thread.start()
    video_thread.start()
        
    won_thread.join()
    video_thread.join()

def is_close_answer(user_answer, correct_answer):
    return user_answer in correct_answer or ("ai" in correct_answer and "ai" in user_answer)

def get_hint(correct_answer, user_answer):
    if any(char.isalpha() for char in correct_answer):
        if "artificial intelligence" in user_answer:
            success()
        if "ai" in user_answer:
            return "You're closer! The answer is a combination of two words."
        return "You're closer!"
    return "The answer is a number."

def ask_question_with_hints(question, correct_answer):
    while True:
        user_answer = input("Your Answer: ").lower()
        if user_answer == correct_answer:
            print("Correct!\n")
            return True
        elif is_close_answer(user_answer, correct_answer):
            hint = get_hint(correct_answer, user_answer)
            print("Close, but not quite. Hint:", hint)
        else:
            print("Incorrect. Try again!")

def main():
    input("Press Enter key to start the Questionnaire...")
    clear_screen()
    
    print(r"""
  

 ______                            _                            _             __   _____      
 |  _  \                          | |                          | |           / _| /  __ \     
 | | | |  ___  _ __    __ _  _ __ | |_  _ __ ___    ___  _ __  | |_    ___  | |_  | /  \/ ___ 
 | | | | / _ \| '_ \  / _` || '__|| __|| '_ ` _ \  / _ \| '_ \ | __|  / _ \ |  _| | |    / __|
 | |/ / |  __/| |_) || (_| || |   | |_ | | | | | ||  __/| | | || |_  | (_) || |   | \__/\\__ \
 |___/   \___|| .__/  \__,_||_|    \__||_| |_| |_| \___||_| |_| \__|  \___/ |_|    \____/|___/
              | |                                                                             
              |_|                                                                             


    
    """)
    
    questions = [
        
        "If a book has 450 pages and it takes 5 minutes to read each page, how long will it take to read the entire book (in minutes)?",
        "If a shirt costs 2250 after a 25% discount, what was the original price of the shirt?",
        'Introducing a boy, a girl said, "He is the son of the daughter of the father of my uncle." How is the boy related to the girl?',
        "A clock strikes once at 1 o'clock, twice at 2 o'clock, and so on. How many times will it strike in 24 hours?",
        "\"Something that becomes a part of your life, even after you leave Here. What is it?\""
    ]
    
    answers = [
        
        "2250",
        "3000",
        "brother",
        "156",
        "artificial intelligence, ai"
    ]
    
    num_questions = len(questions)
    correct_count = 0
    
    print("\nWelcome to the Questionnaire!\n")
    
    for i in range(num_questions):
        question = questions[i]
        correct_answer = answers[i]
        
        print("Question", i + 1)
        print(question)
        
        if ask_question_with_hints("", correct_answer):
            correct_count += 1
    
    clear_screen()
    
    if correct_count == num_questions:
        success()
        print("Congratulations! You answered all questions correctly.")

    else:
        print("Questionnaire incomplete. You answered", correct_count, "out of", num_questions, "questions correctly.")

if __name__ == "__main__":
    
    main()
