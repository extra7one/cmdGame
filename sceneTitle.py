from scene import invalid_choice

class SceneTitle:
    def execute(self, context):
        print("CmdGame\n"
              "1) New game\n"
              "2) Load game\n"
              "3) Exit\n")
        choice = input("Your choice: ")
        function = self.choices.get(int(choice), invalid_choice)
        function(self, context)
    def new_game(self, context):
        print("New game")
        input()
    def load_game(self, context):
        print("Load game")
        input()
    def exit(self, context):
        context.popScene()
    choices = {
        1: new_game,
        2: load_game,
        3: exit
    }