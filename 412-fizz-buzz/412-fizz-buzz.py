class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            match [i % 3 == 0, i % 5 == 0]:
                case [True, True]:
                    ans.append("FizzBuzz")
                case [True, False]:
                    ans.append("Fizz")
                case [False, True]:
                    ans.append("Buzz")
                case [False, False]:
                    ans.append(str(i))
        return ans