
class Player:
    def __init__(self, name : str, wins : int):
        self.name = name
        self.wins = wins

    def get_name(self):
        return self.name
    
    def get_wins(self):
        return self.wins

# def create_player():
#     print("Hello Player, what is your name?")
#     name = input("Name: ")
#     wins = 0
#     return_player = Player(name, wins)
#     return return_player

def add_players():
    players = []
    wins = 0
    player_count = int(input("How many players are going to play the quiz?\nAmount: "))
    for _ in range(player_count):
        pn = input("Name: ")
        players.append(pn)
        Player(pn, wins)
    return players

class CQuestion:
   
    def __init__(self, inquiry : str, answer : str, category: str):
        self.inquiry = inquiry
        self.answer = answer
        self.category = category
    
    def get_question(self):
        return self.inquiry

    def get_answer(self):
        return self.answer
    
    def get_category(self):
        return self.category

class Question:

    def __init__(self, inquiry : str, answer : str):
        self.inquiry = inquiry
        self.answer = answer
    
    def get_question(self):
        return self.inquiry

    def get_answer(self):
        return self.answer

class Quiz:
    def __init__(self, questions : list, players : list, winner):
    
        self.questions = questions
        self.players = players
        self.winner = winner

    def get_questions(self):
        return self.questions
        
    def get_players(self):
        return self.players

    def get_winner(self):
        return self.winner

