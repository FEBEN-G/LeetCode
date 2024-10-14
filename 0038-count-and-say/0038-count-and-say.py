class Solution:
    def countAndSay(self, n: int) -> str:

        def recursion(x,times):
            if times == n:
                return x
            string = x[0]
            count = 1
            answer = ""
            for i in range(1,len(x)):
                if x[i] == string[0]:
                    count += 1
                else:
                    answer += str(count)+string
                    string = x[i]
                    count = 1
            answer += str(count)+string
            return recursion(answer,times+1)
        return recursion("1",1)
        