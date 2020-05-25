import unittest
from src.FSM_interpreter import *


class FSMTest(unittest.TestCase):

    def test_FSM(self):
        fsm = FSMInterpreter()
        list = [
            stateNode(name="A:Green B:Red", time=25, state=[{'Red': False, 'Yellow': False, 'Green': True},
                                                        {'Red': True, 'Yellow': False, 'Green': False}])
            , stateNode(name="A:blinking Green B:Red", time=5, state=[{'Red': False, 'Yellow': False, 'Green': True},
                                                                  {'Red': True, 'Yellow': False, 'Green': False}])
            , stateNode(name="A:Yellow B:Red", time=5, state=[{'Red': False, 'Yellow': True, 'Green': False},
                                                          {'Red': True, 'Yellow': False, 'Green': False}])
            , stateNode(name="A:Red B:Green", time=25, state=[{'Red': True, 'Yellow': False, 'Green': False},
                                                          {'Red': False, 'Yellow': False, 'Green': True}])
            , stateNode(name="A:Red B:blinking Green", time=5, state=[{'Red': True, 'Yellow': False, 'Green': False},
                                                                  {'Red': False, 'Yellow': False, 'Green': True}])
            , stateNode(name="A:Red B:Yellow", time=5, state=[{'Red': True, 'Yellow': False, 'Green': False},
                                                          {'Red': False, 'Yellow': True, 'Green': False}])
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
            fsm.input = test_data[x]
            self.assertEqual(fsm.execute().state,result_data[x])


