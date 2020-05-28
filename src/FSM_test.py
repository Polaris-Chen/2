import unittest
from src.FSM_interpreter import *


class FSMTest(unittest.TestCase):

    def test_light(self):
        fsm = FSMInterpreter(typeNumber=1)
        list = [
            stateNode(name="A:Green B:Red", rule="input-25>=0 ",
                      state=[{'Red': False, 'Yellow': False, 'Green': True},
                             {'Red': True, 'Yellow': False,'Green': False}])

            , stateNode(name="A:blinking Green B:Red", rule=" input-30>=0 ",
                        state=[{'Red': False, 'Yellow': False, 'Green': True},
                               {'Red': True, 'Yellow': False, 'Green': False}])
            , stateNode(name="A:Yellow B:Red", rule="input-35>=0  ",
                        state=[{'Red': False, 'Yellow': True, 'Green': False},
                               {'Red': True, 'Yellow': False, 'Green': False}])
            ,
            stateNode(name="A:Red B:Green", rule="input-60>=0 ",
                      state=[{'Red': True, 'Yellow': False, 'Green': False},
                               {'Red': False, 'Yellow': False, 'Green': True}])
            , stateNode(name="A:Red B:blinking Green", rule="input-65>=0 ",
                        state=[{'Red': True, 'Yellow': False, 'Green': False},
                               {'Red': False, 'Yellow': False, 'Green': True}])
            ,
            stateNode(name="A:Red B:Yellow", rule="input-70>=0 ",
                      state=[{'Red': True, 'Yellow': False, 'Green': False},
                               {'Red': False, 'Yellow': True,'Green': False}])
        ]

        for x in list:
            fsm.add_state(x)

        test_data = [
            5, 10, 30, 40, 60, 65, 70, 95
        ]

        result_data = [
            [{'Red': False, 'Yellow': False, 'Green': True}, {'Red': True, 'Yellow': False, 'Green': False}],
            [{'Red': False, 'Yellow': False, 'Green': True}, {'Red': True, 'Yellow': False, 'Green': False}],
            [{'Red': False, 'Yellow': True, 'Green': False}, {'Red': True, 'Yellow': False, 'Green': False}],
            [{'Red': True, 'Yellow': False, 'Green': False}, {'Red': False, 'Yellow': False, 'Green': True}],
            [{'Red': True, 'Yellow': False, 'Green': False}, {'Red': False, 'Yellow': False, 'Green': True}],
            [{'Red': True, 'Yellow': False, 'Green': False}, {'Red': False, 'Yellow': True, 'Green': False}],
            [{'Red': False, 'Yellow': False, 'Green': True}, {'Red': True, 'Yellow': False, 'Green': False}],
            [{'Red': False, 'Yellow': False, 'Green': True}, {'Red': True, 'Yellow': False, 'Green': False}]
        ]
        
        for x in range(len(test_data)):
            fsm.clear()
            fsm.input = test_data[x]%70
            self.assertEqual(fsm.execute().state,result_data[x])


    def test_find_longest_word(self):
        list = [
            stateNode(name="INIT", rule="input.isalpha()"),
            stateNode(name="JUDGE", rule="input.isalpha()"),
            stateNode(name="TERMINATE", rule="input.isalpha()"),
        ]
        fsm = FSMInterpreter(typeNumber=2)
        for x in list:
            fsm.add_state(x)

        test_data = [
            "word23key241interpreter",
            "word312",
            "123123keyword123123",
            "hi",
            "howareyou1the2a4hi3"
        ]

        result_data=[11,4,7,2,9]

        for x in range(len(test_data)):
            fsm.clear()
            fsm.input = test_data[x]
            #print(fsm.input)
            self.assertEqual(fsm.execute(),result_data[x])