class LengthOfNumber():
      length = 0
      def __init__(self, number):
        self.number = number

      def findLength(self):
        tempLength = 0
        
        for i in str(self.number):
          tempLength += 1
        
        self.length = tempLength
        print("The length of the number is {}".format(tempLength))