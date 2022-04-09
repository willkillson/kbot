from src.kbot.modules.ActionModule import ActionModule


class MalahHeal(ActionModule):
    name = None

    def __init__(self, name):
        super().__init__()
        self.name = name;
        return