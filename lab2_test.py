import unittest
from lab2 import *


class DiscreteEventTest(unittest.TestCase):

    def test_execute(self):
        test_data = [
            5, 10, 20, 40, 60, 65,70,95
        ]
        result_data = [
            [{'Red': False, 'Yellow': False, 'Green': True}, {'Red': True, 'Yellow': False, 'Green': False}],
            [{'Red': False, 'Yellow': False, 'Green': True}, {'Red': True, 'Yellow': False, 'Green': False}],
            [{'Red': False, 'Yellow': False, 'Green': True}, {'Red': True, 'Yellow': False, 'Green': False}],
            [{'Red': True, 'Yellow': False, 'Green': False}, {'Red': False, 'Yellow': False, 'Green': True}],
            [{'Red': True, 'Yellow': False, 'Green': False}, {'Red': False, 'Yellow': False, 'Green': True}],
            [{'Red': True, 'Yellow': False, 'Green': False}, {'Red': False, 'Yellow': True, 'Green': False}],
            [{'Red': False, 'Yellow': False, 'Green': True}, {'Red': True, 'Yellow': False, 'Green': False}],
            [{'Red': False, 'Yellow': False, 'Green': True}, {'Red': True, 'Yellow': False, 'Green': False}]
        ]
        for x in range(len(test_data)):


            test = DiscreteEvent(input=test_data[x])

            test.execute()
            print(test.output)

            self.assertEqual(test.output[0], result_data[x][0])
            self.assertEqual(test.output[1], result_data[x][1])
