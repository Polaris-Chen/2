import unittest
from src.FSM import *


class FSMTest(unittest.TestCase):

    def test_execute(self):
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
            #

            test = FSM(remaining_time=test_data[x])

            test.execute()
            print(test.outputColor)

            # you can use test.state_history to see the states of FSM
            # print(test.state_history)

            self.assertEqual(test.outputColor[0], result_data[x][0])
            self.assertEqual(test.outputColor[1], result_data[x][1])

    def test_add_state(self):
        test = FSM()
        test.add_state(state_name="A:Green B:Red", length_of_time=25,
                       colorA={'Red': False, 'Yellow': False, 'Green': True}
                       , colorB={'Red': True, 'Yellow': False, 'Green': False})
        self.assertEqual(test.states[0].colorA, {'Red': False, 'Yellow': False, 'Green': True})

    def test_create_all_states(self):
        test = FSM()
        test.create_all_states()
        test_data = []
        self.assertEqual(test.states[0].name, "A:Green B:Red")
        self.assertEqual(test.states[1].length_of_time, 5)
        self.assertEqual(test.states[2].colorA, {'Red': False, 'Yellow': True, 'Green': False})
        self.assertEqual(test.states[3].colorB, {'Red': False, 'Yellow': False, 'Green': True})

    def test_Node(self):
        self.assertEqual(Node().name, "State")
        self.assertEqual(Node().length_of_time, 0)
        self.assertEqual(Node().colorA, {'Red': False, 'Yellow': False, 'Green': False})
        self.assertEqual(Node(length_of_time=500).length_of_time, 500)
