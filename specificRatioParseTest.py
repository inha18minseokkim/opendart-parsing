import unittest
import re

def testCase(text):
    # Sample Korean text
    #text = "미래에셋대우㈜의 일반청약자 청약증거금율은 50%입니다."

    # Regular expression pattern to match the percentage value
    pattern = r'(\d+)%'

    # Using re.search to find the pattern in the text
    match = re.search(pattern, text)

    # Extracting the percentage value if a match is found
    if match:
        percentage_value = int(match.group(1))
        print(text , percentage_value)
        return percentage_value  # Output: 50
    else:
        print("No percentage value found in the text.")


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(testCase("미래에셋대우㈜의 일반청약자 청약증거금율은 50%입니다."), 50)  # add assertion here
        self.assertEqual(testCase("나는 50%입니다."), 50)
        self.assertEqual(testCase("우야호오옹 100%입니다."), 100)
        self.assertEqual(testCase("미래에셋증권㈜의 일반청약자 청약증거금율은 50%입니다."), 50)



if __name__ == '__main__':
    unittest.main()
