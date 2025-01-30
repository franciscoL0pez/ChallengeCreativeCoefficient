# boxes = [1,7,8] This is a list of boxes in the factory
# my task is Rearrange the boxes in the factory to form stacks of equal height.

# boxInClaw = 0 if the arm is empty
# boxInClaw = 1 if the arm is holding a box
# Commands: right, left, pick, place
# Limit moves = 80
# I supose is not neccesary save the commands in a list, just print the commands
import unittest

def expectedStacks(stackHeight: int, numStacks: int, extraBoxes:int) -> list:
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
            command =  'PLACE'


        else:
            #Other form is to use a for loop and break to stop... 
            target = next((i for i in range(numStacks) if stacks[i] < expectedStacksList[i]), None)

            if target != None:

                if clawPos < target:
                    clawPos += 1
                    command =  'RIGHT'

                else:
                    clawPos -= 1
                    command =  'LEFT'

        
                

    else:  

        if stacks[clawPos] > expectedStacksList[clawPos]:
            stacks[clawPos] -= 1
            boxInClaw = 1
            command =  'PICK'


        else:
            target = next((i for i in range(numStacks) if stacks[i] > expectedStacksList[i]), None)

            if target != None:

                if clawPos < target:
                    clawPos += 1
                    command =  'RIGHT'

                else:
                    clawPos -= 1
                    command =  'LEFT'
           

    return command
        

class TestAutomatedFactory(unittest.TestCase):

    def test_return_pick(self):
        self.assertEqual(solve(2, [1,7,8], 0), 'PICK')

    def test_return_right(self):
        self.assertEqual(solve(0, [1,7,8], 0), 'RIGHT')

    def test_return_left(self):
        self.assertEqual(solve(1, [1,6,8], 1), 'LEFT')
    
    def test_return_place(self):
        self.assertEqual(solve(0, [1,6,8], 1), 'PLACE')

    def test_return_nothing(self):
        self.assertEqual(solve(0, [1,1,1], 0), '')

    def test_move_and_place_one_box(self):
        self.assertEqual(solve(0, [1,2], 0), 'RIGHT')
        self.assertEqual(solve(1, [1,2], 0), 'PICK')
        self.assertEqual(solve(1, [1,1], 1), 'LEFT')
        self.assertEqual(solve(0, [1,1], 1), 'PLACE')


if __name__ == "__main__":
    unittest.main()




        
        


            

    






