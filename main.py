#Higher lower game 
import random
from art import logo, vs
from game_data import data
from utils import clear
# the player must guess which celebrity has more number of instagram followers 
def get_account():
    """Get random account from data"""
    return random.choice(data)

def format_account(account):
    """Gives the information about the celebrity or account owner's information"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} from {country}"

def comparison(guess, a_account_followers, b_account_followers):
    """Checks the followers of the two accounts and tells which one has more followers"""
    if a_account_followers > b_account_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(logo)
    score = 0
    game_should_continue = True
    A_account = get_account()
    B_account = get_account()

    while game_should_continue:
        A_account = B_account
        B_account = get_account()
        
        while A_account == B_account:
            B_account = get_account()
        
        print(f"Compare A: {format_account(A_account)}")
        print(vs)
        print(f"Against B: {format_account(B_account)}")
        
        guess = input("Who has more followers on Instagram? Type 'A' or 'B': ").lower()
        a_followers = A_account["follower_count"]
        b_followers = B_account["follower_count"]
        is_correct = comparison(guess, a_followers, b_followers)
        
        clear()
        if is_correct:
            score += 1
            print(f"You are correct! The current score = {score}")
        else:
            print(f"Sorry you are wrong. The current score = {score}")
            game_should_continue = False

game()
