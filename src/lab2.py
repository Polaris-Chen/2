
#There are two traffic lights A,B at an intersection
#The red light lasts for 35 seconds, the green light lasts for 30 seconds,
#the green light will blink in the last five seconds,
# and the yellow light lasts for 5 seconds
class DiscreteEvent(object):

    def __init__(self,input=0):

        self.states=[]   #all states list
        self.statenum=0  #now in which state
        self.input=input #input is a Integer  means time
        self.output=[]   #output a dict to display light color
        self.state_history = []
        self.event_history = []

    #bencause moore FSM 's state is independent with input,so we can create all state nodes
    def create_state(self):
        nodes = []
##
        #A:Green B:Red
        nodes.append(Node(name="A:Green B:Red", time=25, colorA={'Red': False, 'Yellow': False, 'Green': True},
                      colorB={'Red': True, 'Yellow': False, 'Green': False}))

        #A:blinking Green B:Red
        nodes.append(Node(name="A:blinking Green B:Red", time=5, colorA={'Red': False, 'Yellow': False, 'Green': True},
                      colorB={'Red': True, 'Yellow': False, 'Green': False}))

        #A:Yellow B:Red
        nodes.append(Node(name="A:Yellow B:Red", time=5, colorA={'Red': False, 'Yellow': True, 'Green': False},
                      colorB={'Red': True, 'Yellow': False, 'Green': False}))

        #A:Red B:Green
        nodes.append(Node(name="A:Red B:Green", time=25, colorA={'Red': True, 'Yellow': False, 'Green': False},
                      colorB={'Red': False, 'Yellow': False, 'Green': True}))

        #A:Red B:blinking Green
        nodes.append(Node(name="A:Red B:blinking Green", time=5, colorA={'Red': True, 'Yellow': False, 'Green': False},
                      colorB={'Red': False, 'Yellow': False, 'Green': True}))

        #A:Red B:Yellow
        nodes.append(Node(name="A:Red B:Yellow", time=5, colorA={'Red': True, 'Yellow': False, 'Green': False},
                      colorB={'Red': False, 'Yellow': True, 'Green': False}))

        self.states=nodes


    #From one state to another state
    def change(self):

        # if input time is less than the now state's length_of_time
        # means the result state will be this state
        if self.input<self.states[self.statenum].length_of_time:

            self.output.append(self.states[self.statenum].colorA)
            self.output.append(self.states[self.statenum].colorB)
            self.state_history.append(self.states[self.statenum].name)
            self.event_history.append(self.states[self.statenum])
            self.input=-1
            return
        # if input time is more than the now state's length_of_time
        # means should change to another state
        newstatenum=(self.statenum+1)%6
        # print(newstatenum)
        self.input -= self.states[self.statenum].length_of_time
        self.statenum=newstatenum


    def execute(self):
        self.create_state()
        while self.input>=0:
            self.change()




class Node():
    # node have properties
    # name: means what this state's name
    # colorA : A light color in this state
    # colorB : B light color in this state
    # length_of_time:how much time this state will over
    def __init__(self, name="State", time=0, colorA={'Red': False, 'Yellow': False,
                                                     'Green': False},
                 colorB={'Red': False, 'Yellow': False, 'Green': False}):
        self.name = name
        self.colorA = colorA
        self.colorB = colorB
        self.length_of_time = time


