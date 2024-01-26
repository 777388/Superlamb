import os
import sys
class supervised:
    def __init__(self, result, request): 
        self.result = result
        self.request = request

    def lambdlog(self):
        (lambda: os.popen("wsl sudo apt update;"))()
        (lambda: os.popen("wsl sudo apt upgrade;"))()
        (lambda: os.popen("wsl time time;"))()
        (lambda: os.popen(f'wsl sudo apt search {self.result}'))()
        (lambda: print({self.request}))()

    def lambdfilt(self):
        v = []
        for stuff in self.result:
            v.append(stuff)
        for otherstuff in self.request:
            v.append(otherstuff)
        list(filter(lambda: lambdlog(), v ))

class Commondeer(supervised):
    def __init__(self, result, request):
        super(Commondeer, self).__init__(result, request)

black = Commondeer(sys.argv[1], sys.argv[2])
black.lambdlog()