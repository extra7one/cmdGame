from context import Context
from sceneTitle import SceneTitle

context = Context()
gameRunning = True

context.pushScene(SceneTitle())

while gameRunning:
    gameRunning = context.execute()