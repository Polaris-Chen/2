from collections import OrderedDict, namedtuple


class DiscreteEvent(object):

    def __init__(self,input=0):
        self.states=[]
        self.statenum=0
        self.input=input
        self.output=[]
        self.state_history = []
        self.event_history = []


    def create_state(self):
        nodes = []

        nodes.append(Node(name="A:Green B:Red", time=25, colorA={'Red': False, 'Yellow': False, 'Green': True},
                      colorB={'Red': True, 'Yellow': False, 'Green': False}))

        nodes.append(Node(name="A:blinking Green B:Red", time=5, colorA={'Red': False, 'Yellow': False, 'Green': True},
                      colorB={'Red': True, 'Yellow': False, 'Green': False}))

        nodes.append(Node(name="A:Yellow B:Red", time=5, colorA={'Red': False, 'Yellow': True, 'Green': False},
                      colorB={'Red': True, 'Yellow': False, 'Green': False}))

        nodes.append(Node(name="A:Red B:Green", time=25, colorA={'Red': True, 'Yellow': False, 'Green': False},
                      colorB={'Red': False, 'Yellow': False, 'Green': True}))

        nodes.append(Node(name="A:Red B:blinking Green", time=5, colorA={'Red': True, 'Yellow': False, 'Green': False},
                      colorB={'Red': False, 'Yellow': False, 'Green': True}))

        nodes.append(Node(name="A:Red B:Yellow", time=5, colorA={'Red': True, 'Yellow': False, 'Green': False},
                      colorB={'Red': False, 'Yellow': True, 'Green': False}))

        self.states=nodes

    def change(self):
        if self.input<self.states[self.statenum].length_of_time:

            self.output.append(self.states[self.statenum].colorA)
            self.output.append(self.states[self.statenum].colorB)
            self.state_history.append(self.states[self.statenum].name)
            self.event_history.append(self.states[self.statenum])
            self.input=-1
            return
        newstatenum=(self.statenum+1)%6
        # print(newstatenum)
        self.input -= self.states[self.statenum].length_of_time
        self.statenum=newstatenum

        # time=self.states[newstatenum].length_of_time
        # # print(time)
        # if time<self.input:
        #     self.statenum=newstatenum
        #     self.input-=time
        #     print("time still")
        # else:
        #     self.input -= time
        #     self.output.append(self.states[newstatenum].colorA)
        #     self.output.append(self.states[newstatenum].colorB)

    def execute(self):
        self.create_state()
        while self.input>=0:
            self.change()

        self.visualize()
        #self.back()
    #     print("A lightcolor is:" )
    #     print(self.output[0])
    #     print("B lightcolor is:" )
    #     print(self.output[1])
    #
    # def back(self):
    #     self.__init__(input=0)


class Node():
    def __init__(self, name="State", time=0, colorA={'Red': False, 'Yellow': False,
                                                     'Green': False},
                 colorB={'Red': False, 'Yellow': False, 'Green': False}):
        self.name = name
        self.colorA = colorA
        self.colorB = colorB
        self.length_of_time = time

test = DiscreteEvent(input=60)
test.execute()
