class Judge_if_change_state():
    def __init__(self,FSM=None):
        self.FSM=FSM

    def traffic_light_Judge(self):
        nowState = self.FSM.statesList[self.FSM.stateNum]
        input=self.FSM.input
        flag=eval(nowState.rule)
        if flag:
            self.FSM.stateNum = (self.FSM.stateNum + 1) % 6

        else:
            self.FSM.output=nowState


        self.FSM.state_history.append(nowState)
        return flag

    def find_longest_word_Judge(self):
        nowState = self.FSM.statesList[self.FSM.stateNum]
        input = self.FSM.input
        flag = eval(nowState.rule)
        return flag





