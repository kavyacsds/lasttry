import random
import logo_art
import database
print(logo_art.game_logo)

score=0

def display_accountinfo(account):
    name=account["name"]
    description=account["description"]
    country=account["country"]

    return f"{name}, a {description},from {country}"
def check_answer(guess,followers_1,followers_2):
    if followers_1>followers_2:
        if guess==1:
            return False
        else:
            return True
    else:
        if guess==1: 
            return True
        else:
            return False 
continue_flag=True
while continue_flag:                          
    account_1=random.choice(database.data)
    account_2=random.choice(database.data)
    # print(account_1)
    # print(account_2)
    print(f"compare 1: {display_accountinfo(account_1)}")
    print(logo_art.vs)
    print(f"compare 2: {display_accountinfo(account_2)}")
    # display_accountinfo(account_1)
    # display_accountinfo(account_2)
    guess=int(input("who has more followers? tyoe 1 or 2 :"))
    follower_count_1=account_1["follower_count"]
    follower_count_2=account_2["follower_count"]
    print(follower_count_1)
    print(follower_count_2)
    is_correct=check_answer(guess,follower_count_1,follower_count_2)
    if is_correct:
        score +=1
        print(f"you are right.. you score is :{score}" )
    else:
        print(f"you are wrong.. your final score is:{score}")
        continue_flag=False