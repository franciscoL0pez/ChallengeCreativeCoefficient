import unittest

# Count the number of greetings that will occur in based on the given move secuence
# The function recieve a string with the moves iterate and count the number of greetings
# - Args: moves (str): string with the moves
# - Returns: int: number of greetings


def greeting_numbers(moves:str) -> int:
    greetings = 0
    for i in range(len(moves)):
        if moves[i] == '>':
            for j in range(i+1, len(moves)):
                if moves[j] == '<':
                    greetings += 2
    
    return greetingsnce 
def greeting_numbers(moves:str) -> int:
    greetings = 0
    for i in range(len(moves)):
        if moves[i] == '>':
            for j in range(i+1, len(moves)):
                if moves[j] == '<':
                    greetings += 2
    
    return greetings



class TestGreetings(unittest.TestCase):

    def test_one_meeting_without_empty_spaces(self):
        self.assertEqual(greeting_numbers('><'), 2)

    def test_one_meeting_with_empty_space(self):
        self.assertEqual(greeting_numbers('<---<--->----<'), 2)

    def test_two_meetings(self):
        self.assertEqual(greeting_numbers('-->--<--<--'), 4)

    def test_four_meetings(self):
        self.assertEqual(greeting_numbers(' >----->-----<--<'), 8)


    def test_no_meetings(self):
        self.assertEqual(greeting_numbers('--<-<-'), 0)



if __name__ == "__main__":
    unittest.main()