

from src.Aspect_of_ChangeState import Judge_if_change_state, Execute


class FSMInterpreter(object):

    def __init__(self,input=0,typeNumber=0):
        self.statesList = []  # all states list
        self.stateNum = 0  # now  state
        self.input = input # remaining_time is a Integer  means time
        self.output = 0
        self.typeNum=typeNumber# typeNumber means which test
        # traffic light=1  find longest word=2
        self.state_history = []

    def add_state(self, state_node):

        self.statesList.append(state_node)

    def changeState(self):
        judgeObject = Judge_if_change_state(FSM=self)

        if self.typeNum==1:  #traffic light question
            flag=judgeObject.traffic_light_Judge()

        elif self.typeNum==2: # find longest word quesion
            flag=judgeObject.find_longest_word_Judge()


        return flag
        #flag means if change state



    def execute(self):
        execute = Execute(FSM=self)
        if self.typeNum==1:    #traffic light
            return execute.traffic_light()

        elif self.typeNum==2:  #find_longest_word
            return execute.find_longest_word()
    #will return output

    def showHistory(self):
        print("state_history")
        for x in self.state_history:
            print(x)

    def clear(self):
        self.input=0
        self.output=0
        self.stateNum=0


class stateNode(object):
    def __init__(self,name="",rule="",state=[]):
        self.name = name
        self.rule = rule #rule is a String , means a jugde code ,if ture ,change state
        self.state = state
        self.state_history = []



