import os
import pickle

def save_user(email, password):
    new_user = (email, password)

    os.makedirs("client", exist_ok=True)
    
    with open("client/user.dat", "wb") as f:
        pickle.dump(new_user, f)

def load_user():
    if not os.path.exists("client/user.dat"):
        return False
    with open("client/user.dat", "rb") as f:
        return pickle.load(f)

def get_email():
    user = load_user()
    return user[0]

def get_password():
    user = load_user()
    return user[1]
    
