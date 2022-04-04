from vision import Vision
from time import sleep, time
import pyautogui

class BotActionState:
    INITIALIZING = 0
    INITIALZED = 1
    LOOTING = 2
    MOVING = 3
    KILLING = 4
    LOST = 5
    WP = 6
    ELDRITCH_MOVE = 7
    ELDRITCH_FIGHT = 8
    EXIT = 9
    MENU = 10
    ELDRITCH_LOOT = 11

class ActState:
    UNK = 0
    ACT_1 = 1
    ACT_2 = 2
    ACT_3 = 3
    ACT_4 = 4
    ACT_5 = 5

class BotState:
    BOT_ACTION_STATE = BotActionState.INITIALIZING
    BOT_ACT_STATE = None
class kbot:
    
    currentLostAttempt = 0
    maxLostAttempt = 10
    
    currentAttackCount = 0
    attackCount = 10
    totalRunTime = None
    BOT_STATE = None
    # Based on state, this is our current place we should be.
    # Will will need to determine where this is often, 
    # otherwise we will be lost and need to figure where we are at.
    movementNeedle = None;
    # Current attack targets
    targetNeedles = []
    # Elapsed time since last move.
    elapsedTime = 0

    vision_login_a1 = Vision('./images/needle/login/login_a1.jpg')
    vision_login_a2 = Vision('./images/needle/login/login_a2.jpg')
    vision_login_a3 = Vision('./images/needle/login/login_a3.jpg')
    vision_login_a4 = Vision('./images/needle/login/login_a4.jpg')
    vision_login_a5 = Vision('./images/needle/login/login_a5.jpg')
    
    vision_a5_start = Vision('./images/needle/a5/a5_start.jpg')


    vision_a5_wp= Vision('./images/needle/a5/a5_wp.jpg')
    
    movementIndex = 0
    movementList = []
    
    eldritch_movementList = []
    
    

    def __init__(self):
        self.totalRunTime = 0
        self.BOT_STATE = BotState()
        self.BOT_STATE.BOT_ACTION_STATE = BotActionState.INITIALIZING
        self.BOT_STATE.BOT_ACT_STATE = ActState.UNK
        
        self.movementList.append(Vision('./images/needle/a5/a5_stairs1.jpg'))
        self.movementList.append(Vision('./images/needle/a5/a5_midstairs2.jpg'))
        self.movementList.append(Vision('./images/needle/a5/a5_stairs2.jpg'))
        self.movementList.append(Vision('./images/needle/a5/a5_wp.jpg'))      
        
        self.eldritch_movementList.append(Vision('./images/needle/eldritch/eldritch_1.jpg'))
        self.eldritch_movementList.append(Vision('./images/needle/eldritch/eldritch_2.jpg'))
        # self.eldritch_movementList.append(Vision('./images/needle/eldritch/eldritch_3.jpg'))
        
        
    def updateState(self, currentFrame):
        if self.BOT_STATE.BOT_ACTION_STATE == BotActionState.INITIALIZING:
            print("State: INITIALIZING")
            self.findLoginPlace(currentFrame)
        elif self.BOT_STATE.BOT_ACTION_STATE == BotActionState.INITIALZED:
            print("State: INITIALZED")
            self.BOT_STATE.BOT_ACTION_STATE = BotActionState.MOVING
            # Set out movement index to 0
            # we should also set up our movement list, but lets just default to a5 
            self.movementIndex = 0
            self.movementNeedle = self.vision_a5_start
        elif self.BOT_STATE.BOT_ACTION_STATE == BotActionState.LOOTING:
            print("State: LOOTING")
        elif self.BOT_STATE.BOT_ACTION_STATE == BotActionState.MOVING:
            currentIndex = self.movementIndex
            point = self.movementList[currentIndex].find(currentFrame,0.5)
            print("State: MOVING {}".format(point))
            if len(point) == 1:
                print(point)
                pyautogui.moveTo(point[0][0], point[0][1]);
                pyautogui.click();
                sleep(2)
                self.movementIndex = self.movementIndex + 1
                if self.movementIndex >= len(self.movementList):
                    #we are done moving
                    self.BOT_STATE.BOT_ACTION_STATE = BotActionState.WP
            else:
                # we are lost
                self.BOT_STATE.BOT_ACTION_STATE = BotActionState.LOST
                self.currentLostAttempt = 0        
        elif self.BOT_STATE.BOT_ACTION_STATE == BotActionState.KILLING:
            print("State: KILLING")
        elif self.BOT_STATE.BOT_ACTION_STATE == BotActionState.LOST:
            print("State: LOST")
            self.findLoginPlace(currentFrame)
            self.currentLostAttempt = self.currentLostAttempt + 1
            if self.currentLostAttempt > self.maxLostAttempt:
                self.BOT_STATE.BOT_ACTION_STATE = BotActionState.EXIT
        elif self.BOT_STATE.BOT_ACTION_STATE == BotActionState.WP:
            print("State: WP")
            #going to frigid
            pyautogui.moveTo(517, 475);
            pyautogui.click();
            self.BOT_STATE.BOT_ACTION_STATE = BotActionState.ELDRITCH_MOVE
            self.movementIndex = 0
            sleep(5)
        elif self.BOT_STATE.BOT_ACTION_STATE == BotActionState.ELDRITCH_MOVE:
            #fighting eldritch
            currentIndex = self.movementIndex
            point = self.eldritch_movementList[currentIndex].find(currentFrame,0.5)
            print("State: ELDRITCH_MOVE {}".format(point))
            if len(point) == 1:
                print(point)
                pyautogui.moveTo(point[0][0], point[0][1]);
                pyautogui.click();
                sleep(1)
                self.movementIndex = self.movementIndex + 1
                if self.movementIndex >= len(self.eldritch_movementList):
                    #we are done moving time to attack
                    self.BOT_STATE.BOT_ACTION_STATE = BotActionState.ELDRITCH_FIGHT
                    self.currentAttackCount = 0
            else:
                # we are lost
                self.BOT_STATE.BOT_ACTION_STATE = BotActionState.LOST
                self.currentLostAttempt = 0
        elif self.BOT_STATE.BOT_ACTION_STATE == BotActionState.ELDRITCH_FIGHT:
            print("State: ELDRITCH_FIGHT")
            pyautogui.moveTo(1300, 5)
            pyautogui.rightClick()
            self.currentAttackCount = self.currentAttackCount + 1
            sleep(1)
            if self.currentAttackCount >= self.attackCount:
                self.BOT_STATE.BOT_ACTION_STATE = BotActionState.EXIT
        elif self.BOT_STATE.BOT_ACTION_STATE == BotActionState.EXIT:
            print("State: EXIT")
            pyautogui.press("esc")
            sleep(2)
            pyautogui.moveTo(2560/2, 1440/2-50)
            pyautogui.click()
            self.BOT_STATE.BOT_ACTION_STATE = BotActionState.MENU
        elif self.BOT_STATE.BOT_ACTION_STATE == BotActionState.MENU:
            print("State: MENU")
            sleep(5)
            #Play button
            pyautogui.moveTo(1050, 1300)
            sleep(1)
            pyautogui.click()
            sleep(2)
            #nightmare button
            pyautogui.moveTo(1250, 700)
            sleep(1)
            pyautogui.click()
            sleep(2)
            self.BOT_STATE.BOT_ACTION_STATE = BotActionState.INITIALIZING
                

            
    # Will trigger BOT_ACTION_STATE to INITIALZED 
    def findLoginPlace(self, currentFrame):
        point = None
        point = self.vision_login_a1.find(currentFrame, 0.5, 'rectangles')
        if len(point) == 0:
            point = self.vision_login_a2.find(currentFrame, 0.5, 'rectangles')
            if len(point) == 0:
                point = self.vision_login_a3.find(currentFrame, 0.5, 'rectangles')
                if len(point) == 0:
                    point = self.vision_login_a4.find(currentFrame, 0.5, 'rectangles')
                    if len(point) == 0:
                        point = self.vision_login_a5.find(currentFrame, 0.5, 'rectangles')
                        if len(point) == 0:
                            self.BOT_STATE.BOT_ACT_STATE = ActState.UNK
                        else:
                            self.BOT_STATE.BOT_ACTION_STATE = BotActionState.INITIALZED
                            self.BOT_STATE.BOT_ACT_STATE = ActState.ACT_5
                    else:
                        self.BOT_STATE.BOT_ACTION_STATE = BotActionState.INITIALZED
                        self.BOT_STATE.BOT_ACT_STATE = ActState.ACT_4
                else:
                    self.BOT_STATE.BOT_ACTION_STATE = BotActionState.INITIALZED
                    self.BOT_STATE.BOT_ACT_STATE = ActState.ACT_3
            else:
                self.BOT_STATE.BOT_ACTION_STATE = BotActionState.INITIALZED
                self.BOT_STATE.BOT_ACT_STATE = ActState.ACT_2
        else:
            self.BOT_STATE.BOT_ACTION_STATE = BotActionState.INITIALZED
            self.BOT_STATE.BOT_ACT_STATE = ActState.ACT_1



