class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom, high, low = 0, len(matrix) - 1, len(matrix[0]) - 1, 0

        # Binary search the rows as a whole to 
        # determine which row could even possible contain the target
        # Then binary search the correct row

        correctRow = 0
        while top <= bottom:
            mid = (top + bottom) // 2

            if target > matrix[mid][high]:
                top = mid + 1
            elif target < matrix[mid][low]:
                bottom = mid - 1
            elif target <= matrix[mid][high] and target >= matrix[mid][low]:
                correctRow = mid
                break
                # If no such row exists, the number is not in the matrix
            else:
                return False

        while low <= high:
            mid = (low + high) // 2

            if target > matrix[correctRow][mid]:
                low = mid + 1
            elif target < matrix[correctRow][mid]:
                high = mid - 1
            else:
                return True
        return False