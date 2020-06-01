class Judge_if_change_state():
    def __init__(self, FSM=None):
        self.FSM = FSM

    def traffic_light_Judge(self):
        nowState = self.FSM.statesList[self.FSM.stateNum]
        input = self.FSM.input
        flag = eval(nowState.rule)
        if flag:
            self.FSM.stateNum = (self.FSM.stateNum + 1) % 6

        else:
            self.FSM.output = nowState

        self.FSM.state_history.append(nowState)
        return flag

    def find_longest_word_Judge(self):
        nowState = self.FSM.statesList[self.FSM.stateNum]
        input = self.FSM.input
        flag = eval(nowState.rule)
        return flag


class Execute():
    def __init__(self, FSM=None):
        self.FSM = FSM

    def traffic_light(self):
        flag = True
        while flag:
            flag = self.FSM.changeState()
        return self.FSM.output

    def find_longest_word(self):
        self.FSM.stateNum += 1
        length = len(self.FSM.input)
        maxLength = 0
        str = self.FSM.input
        flag = True
        for x in range(length):  # look all char of a string
            self.FSM.input = str[x]
            flag = self.FSM.changeState()

            if flag:
                maxLength += 1
                # print(maxLength)
            else:
                if self.FSM.output < maxLength:

                    self.FSM.output = maxLength
                    maxLength = 0
                else:
                    maxLength = 0

        if maxLength > 0:
            self.FSM.output = maxLength

        return self.FSM.output