

from src.Aspect_of_ChangeState import Judge_if_change_state


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
        if self.typeNum==1:    #traffic light
            flag=True
            while flag:
                flag=self.changeState()
            return self.output

        elif self.typeNum==2:  #find_longest_word

            self.stateNum+=1
            length=len(self.input)
            maxLength=0
            str=self.input
            flag=True
            for x in range(length): #look all char of a string
                self.input=str[x]
                flag=self.changeState()

                if flag:
                    maxLength+=1
                    #print(maxLength)
                else:
                    if self.output<maxLength:

                        self.output=maxLength
                        maxLength=0
                    else :
                        maxLength=0

            if maxLength > 0 :
                 self.output=maxLength

            return self.output



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



