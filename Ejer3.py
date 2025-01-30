# boxes = [1,7,8] This is a list of boxes in the factory
# my task is Rearrange the boxes in the factory to form stacks of equal height.

# boxInClaw = 0 if the arm is empty
# boxInClaw = 1 if the arm is holding a box
# Commands: right, left, pick, place
# Limit moves = 80
# I supose is not neccesary save the commands in a list, just return the command

import unittest

def expectedStacks(stackHeight: int, numStacks: int, extraBoxes: int) -> list:
    expectedStacks = []

    for _ in range(numStacks):
        if extraBoxes > 0:
            expectedStacks.append(stackHeight + 1)
            extraBoxes -= 1
        else:
            expectedStacks.append(stackHeight)

    return expectedStacks


def solve(clawPos: int, stacks: list, boxInClaw: int) -> str:
    # Add box in claw to the total boxes
    totalBoxes = sum(stacks) + boxInClaw
    numStacks = len(stacks)
    extraBoxes = totalBoxes % numStacks
    stackHeight = totalBoxes // numStacks
    command = ''
    expectedStacksList = expectedStacks(stackHeight, numStacks, extraBoxes)

    if boxInClaw == 1:
        if stacks[clawPos] < expectedStacksList[clawPos]:
            stacks[clawPos] += 1
            boxInClaw = 0
            command = 'PLACE'

        else:
            # Other form is to use a for loop and break to stop...
            target = next((i for i in range(numStacks)
                          if stacks[i] < expectedStacksList[i]), None)

            if target != None:

                if clawPos < target:
                    clawPos += 1
                    command = 'RIGHT'

                else:
                    clawPos -= 1
                    command = 'LEFT'

    else:

        if stacks[clawPos] > expectedStacksList[clawPos]:
            stacks[clawPos] -= 1
            boxInClaw = 1
            command = 'PICK'

        else:
            target = next((i for i in range(numStacks)
                          if stacks[i] > expectedStacksList[i]), None)

            if target != None:

                if clawPos < target:
                    clawPos += 1
                    command = 'RIGHT'

                else:
                    clawPos -= 1
                    command = 'LEFT'

    return command

# The only moment when solve return '' is when the stacks are already sorted
def sortStacks(clawPos: int, stacks: list, boxInClaw: int) -> str:
    limitCommands = 80


    while limitCommands > 0:
        command = solve(clawPos, stacks, boxInClaw)
        limitCommands -= 1

        if command == 'RIGHT':
            clawPos += 1

        elif command == 'LEFT':
            clawPos -= 1

        elif command == 'PICK':
            boxInClaw = 1

        elif command == 'PLACE':
            boxInClaw = 0

        else:
            return 'Victory'

    return 'Lose'


class TestAutomatedFactory(unittest.TestCase):

    def test_return_pick(self):
        self.assertEqual(solve(2, [1, 7, 8], 0), 'PICK')

    def test_return_right(self):
        self.assertEqual(solve(0, [1, 7, 8], 0), 'RIGHT')

    def test_return_left(self):
        self.assertEqual(solve(1, [1, 6, 8], 1), 'LEFT')

    def test_return_place(self):
        self.assertEqual(solve(0, [1, 6, 8], 1), 'PLACE')

    def test_return_nothing(self):
        self.assertEqual(solve(0, [1, 1, 1], 0), '')

    def test_move_and_place_one_box(self):
        self.assertEqual(solve(0, [1, 2], 0), 'RIGHT')
        self.assertEqual(solve(1, [1, 2], 0), 'PICK')
        self.assertEqual(solve(1, [1, 1], 1), 'LEFT')
        self.assertEqual(solve(0, [1, 1], 1), 'PLACE')

    def test_move_and_pick_two_boxes(self):
        self.assertEqual(solve(2, [1, 1, 3], 0), 'PICK')
        self.assertEqual(solve(2, [1, 1, 2], 1), 'LEFT')
        self.assertEqual(solve(1, [1, 1, 2], 1), 'PLACE')
        self.assertEqual(solve(0, [1, 2, 2], 0), 'RIGHT')
        self.assertEqual(solve(2, [1, 2, 2], 0), 'PICK')
        self.assertEqual(solve(2, [1, 1, 2], 1), 'LEFT')
        self.assertEqual(solve(1, [1, 2, 1], 1), 'LEFT')
        self.assertEqual(solve(0, [1, 2, 1], 1), 'PLACE')
        self.assertEqual(solve(0, [2, 2, 1], 0), '')

    def test_move_and_pick_one_box_in_8_stacks(self):
        self.assertEqual(solve(4, [0,0,0,0,0,0,0,1], 0), 'RIGHT')
        self.assertEqual(solve(5, [0,0,0,0,0,0,0,1], 0), 'RIGHT')
        self.assertEqual(solve(6, [0,0,0,0,0,0,0,1], 0), 'RIGHT')
        self.assertEqual(solve(7, [0,0,0,0,0,0,0,1], 0), 'PICK')
        self.assertEqual(solve(7, [0,0,0,0,0,0,0,0], 1), 'LEFT')
        self.assertEqual(solve(6, [0,0,0,0,0,0,0,0], 1), 'LEFT')
        self.assertEqual(solve(5, [0,0,0,0,0,0,0,0], 1), 'LEFT')
        self.assertEqual(solve(4, [0,0,0,0,0,0,0,0], 1), 'LEFT')
        self.assertEqual(solve(3, [0,0,0,0,0,0,0,0], 1), 'LEFT')
        self.assertEqual(solve(2, [0,0,0,0,0,0,0,0], 1), 'LEFT')
        self.assertEqual(solve(1, [0,0,0,0,0,0,0,0], 1), 'LEFT')
        self.assertEqual(solve(0, [0,0,0,0,0,0,0,0], 1), 'PLACE')
        self.assertEqual(solve(0, [1,0,0,0,0,0,0,0], 0), '')
     

    def test_excess_number_of_commands(self):
        self.assertEqual(sortStacks(0, [16,0,0,0,0,0,0,0], 0), 'Lose')


    def test_victory_without_moving_boxes(self):
        self.assertEqual(sortStacks(0, [1, 1, 1], 0), 'Victory')
    
    def test_victory_moving_boxes(self):
        self.assertEqual(sortStacks(0, [1, 2,4,6], 0), 'Victory')

if __name__ == "__main__":
    unittest.main()
