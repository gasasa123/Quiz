class Game:
    def __init__(self,user_name,num_round=0):
        self.user_name = user_name
        self.num_round = num_round
    def getUserName(self):
        return self.user_name
    def getNum_round(self):
        return self.num_round

    def setUserName(self,new_username):
        forbidden = ['@', '#', '!', '$', '^', '%', '&', '*', '(', ')', '-', '+', '=', '~', '`', '.', '/', '\\', ]
        if new_username in forbidden:
            print("Invalid Characters! please")
        else:
            self.user_name = new_username

    def setNumRound(self,num_round):
        self.num_round = num_round