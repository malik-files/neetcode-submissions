class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def isListUnique(values):
            setOfValues = set(values)
            for x in setOfValues:
                if values.count(x) > 1 and x != ".":
                    return False
            return True

        #Check all the rows are different
        for i in range(9):
            if not isListUnique(board[i]):
                print("from checking the rows")
                return False

        #Check all the colums are different
        for j in range(9):
            listForComparison = list()
            for i in range(9):
                listForComparison.append(board[i][j])
            if not isListUnique(listForComparison):
                print("from checking the columns")
                return False
        
        #Check 3 x 3 
        places = [0,3,6]
        comparison = list()
        for rows in places:
            for columns in places:
                for add in range(3):
                    for num in range(3):
                        comparison.append(board[rows+add][columns+num])
                if not isListUnique(comparison):
                    print("from checking the 3x3")
                    return False
                comparison = list()

        return True

