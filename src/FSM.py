# There are two traffic lights A,B at an intersection
# The red light lasts for 35 seconds, the green light lasts for 30 seconds,
# the green light will blink in the last five seconds,
# and the yellow light lasts for 5 seconds


class FSM(object):

    def __init__(self, remaining_time=0):

        self.states = []  # all states list
        self.statenum = 0  # now in which state
        self.remaining_time = remaining_time  # remaining_time is a Integer  means time
        self.outputColor = []  # outputColor a dict to display light color
        self.state_history = []


    #
    def add_state(self, state_name, length_of_time, colorA, colorB):
        state = Node(name=state_name, length_of_time=length_of_time, colorA=colorA, colorB=colorB)
        self.states.append(state)

    def create_all_states(self):

        # A:Green B:Red
        self.add_state(state_name="A:Green B:Red", length_of_time=25,
                       colorA={'Red': False, 'Yellow': False, 'Green': True},
                       colorB={'Red': True, 'Yellow': False, 'Green': False})

        # A:blinking Green B:Red
        self.add_state(state_name="A:blinking Green B:Red", length_of_time=5,
                       colorA={'Red': False, 'Yellow': False, 'Green': True},
                       colorB={'Red': True, 'Yellow': False, 'Green': False})

        # A:Yellow B:Red
        self.add_state(state_name="A:Yellow B:Red", length_of_time=5,
                       colorA={'Red': False, 'Yellow': True, 'Green': False},
                       colorB={'Red': True, 'Yellow': False, 'Green': False})

        # A:Red B:Green
        self.add_state(state_name="A:Red B:Green", length_of_time=25,
                       colorA={'Red': True, 'Yellow': False, 'Green': False},
                       colorB={'Red': False, 'Yellow': False, 'Green': True})

        # A:Red B:blinking Green
        self.add_state(state_name="A:Red B:blinking Green", length_of_time=5,
                       colorA={'Red': True, 'Yellow': False, 'Green': False},
                       colorB={'Red': False, 'Yellow': False, 'Green': True})

        # A:Red B:Yellow
        self.add_state(state_name="A:Red B:Yellow", length_of_time=5,
                       colorA={'Red': True, 'Yellow': False, 'Green': False},
                       colorB={'Red': False, 'Yellow': True, 'Green': False})

    # From one state to another state
    def changeState(self):

        # if remaining_time time is less than the now state's length_of_time
        # means the result state will be this state
        if self.remaining_time < self.states[self.statenum].length_of_time:
            self.outputColor.append(self.states[self.statenum].colorA)
            self.outputColor.append(self.states[self.statenum].colorB)
            self.state_history.append(self.states[self.statenum].name)

            # self.event_history.append(self.states[self.statenum])
            self.remaining_time = -1
            return

        # if remaining_time time is more than the now state's length_of_time
        # means should change to next state
        self.state_history.append(self.states[self.statenum].name)
        newstatenum = (self.statenum + 1) % 6
        # print(newstatenum)
        self.remaining_time -= self.states[self.statenum].length_of_time
        self.statenum = newstatenum

    def execute(self):
        self.create_all_states()
        while self.remaining_time >= 0:
            self.changeState()

    def showHistory(self):
        print("state_history")
        for x in self.state_history:
            print(x)


class Node():
    # node have properties
    # name: means what this state's name
    # colorA : A light color in this state
    # colorB : B light color in this state
    # length_of_time:how much time this state will over
    def __init__(self, name="State", length_of_time=0,
                 colorA={'Red': False, 'Yellow': False, 'Green': False},
                 colorB={'Red': False, 'Yellow': False, 'Green': False}):
        self.name = name
        self.colorA = colorA
        self.colorB = colorB
        self.length_of_time = length_of_time
