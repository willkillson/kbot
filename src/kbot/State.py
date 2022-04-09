# from src.kbot.vision.vision import Vision
#
#
# class ActionModuleQueue:
#     modules = []
#
#     def __init__(self):
#         malahHealModule = MalahHeal("poop")
#         self.modules.append(malahHealModule)
#         return
#
#     # Will handle 1 frame call
#     def update(self):
#         module = self.modules.pop()
#
#         print("updating")
#
# class Bot:
#
#     actionModuleQueue = ActionModuleQueue()
#
#     def __init__(self):
#         return
#
#     def update(self):
#         # Get the current game frame, and pass it into update
#         self.actionModuleQueue.update()
#
#
# bot = Bot()
#
# vision_malah = Vision('./malah/malah_filtered.jpg')
# vision_malah2 = Vision('./malah/malah_filtered_2.jpg')
# vision_malah3 = Vision('./malah/malah_filtered_3.jpg')
# vision_malah4 = Vision('./malah/malah_filtered_4.jpg')
#
# while(True):
#     bot.update()
#
