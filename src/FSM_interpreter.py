class FSMInterpreter(object):

    def __init__(self,input=0):
        self.statesList = []  # all states list
        self.stateNum = 0  # now  state
        self.input = input  # remaining_time is a Integer  means time
        self.output = []
        self.state_history = []

    def add_state(self, state_node):
        self.statesList.append(state_node)

    def changeState(self):
        now_state = self.statesList[self.stateNum]
        if self.input < now_state.time:
            self.output = now_state
            self.input = -1
        else:
            self.input -= now_state.time
            self.stateNum = (self.stateNum + 1) % len(self.statesList)
        self.state_history.append(now_state)

    def execute(self):
        while self.input >= 0:
            self.changeState()
        #print(self.output.name)
        return self.output

    def showHistory(self):
        print("state_history")
        for x in self.state_history:
            print(x)

    def clear(self):
        self.input=0
        self.output=[]
        self.stateNum=0


class stateNode(object):
    def __init__(self,name="",time=0,state=[]):
        self.name = name
        self.time = time
        self.state = state
        self.state_history = []

