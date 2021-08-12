class Context:
    _sceneList = []
    def pushScene(self, scene):
        self._sceneList.append(scene)
    def popScene(self, scene):
        self._sceneList.pop(0)
    def execute(self):
        if len(self._sceneList) > 0:
            self._sceneList[-1].execute(self)
            return True
        else:
            return False