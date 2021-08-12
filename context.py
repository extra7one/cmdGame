import os

class Context:
    _sceneList = []
    def pushScene(self, scene):
        self._sceneList.append(scene)
    def popScene(self):
        self._sceneList.pop(0)
    def execute(self):
        cls()
        if len(self._sceneList) > 0:
            self._sceneList[-1].execute(self)
            return True
        else:
            return False

def cls():
    os.system('cls' if os.name=='nt' else 'clear')