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
    HEAL_ACT_5_MALAH = 12
    MOVE_HEAL_ACT_5_MALAH = 13

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
    maxLostAttempt = 5
    
    currentHealAttempt = 0
    maxHealAttempt = 5
    
    currentAttackAttempt = 0
    maxAttackAttempt = 10
    
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
    eldritch_movePoints = []
    
    malah = Vision('./images/needle/malah.jpg')
    malah_movePoints = []
    
    sleep_scale = 0.85
    
    

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
        
        self.eldritch_movePoints.append((1300,55))
        self.eldritch_movePoints.append((1200,55))
        
        self.malah_movePoints.append((755,575))
        self.malah_movePoints.append((820,430))
                
        # self.eldritch_movementList.append(Vision('./images/needle/eldritch/eldritch_3.jpg'))
        
        
    def updateState(self, currentFrame):
        if self.BOT_STATE.BOT_ACTION_STATE == BotActionState.INITIALIZING:
            self.findLoginPlace(currentFrame)   
        elif self.BOT_STATE.BOT_ACTION_STATE == BotActionState.INITIALZED:
            self.setStateMoving(currentFrame)
        elif self.BOT_STATE.BOT_ACTION_STATE == BotActionState.LOOTING:
            print("UNUSED")
        elif self.BOT_STATE.BOT_ACTION_STATE == BotActionState.MOVING:
            self.handleMoving(currentFrame)
        elif self.BOT_STATE.BOT_ACTION_STATE == BotActionState.KILLING:
            print("UNUSED")
        elif self.BOT_STATE.BOT_ACTION_STATE == BotActionState.LOST:
            self.handleLost(currentFrame)
        elif self.BOT_STATE.BOT_ACTION_STATE == BotActionState.WP:
            self.handleWp(currentFrame)
        elif self.BOT_STATE.BOT_ACTION_STATE == BotActionState.ELDRITCH_MOVE:
            self.handleEldritchMove(currentFrame)
        elif self.BOT_STATE.BOT_ACTION_STATE == BotActionState.ELDRITCH_FIGHT:
            self.handleEldritchFight(currentFrame)
        elif self.BOT_STATE.BOT_ACTION_STATE == BotActionState.ELDRITCH_LOOT:
            self.handleEldritchLoot(currentFrame)
        elif self.BOT_STATE.BOT_ACTION_STATE == BotActionState.EXIT:
            self.handleExit(currentFrame)
        elif self.BOT_STATE.BOT_ACTION_STATE == BotActionState.MENU:
            self.handleMenu(currentFrame)
        elif self.BOT_STATE.BOT_ACTION_STATE == BotActionState.HEAL_ACT_5_MALAH:
            self.handleHealAct5Malah(currentFrame)
        elif self.BOT_STATE.BOT_ACTION_STATE == BotActionState.MOVE_HEAL_ACT_5_MALAH:
            self.handleMoveAct5Malah(currentFrame)
           
        
    ##############################
    # State Transitions
    ##############################  
    
    def setStateInitiailized(self, currentFrame):
        self.BOT_STATE.BOT_ACTION_STATE = BotActionState.INITIALZED 
    
    def setStateMoving(self, currentFrame):
        print("setStateMoving")
    
    def setStateLost(self, currentFrame):
        print("setStateLost")
        self.BOT_STATE.BOT_ACTION_STATE = BotActionState.LOST
        self.currentLostAttempt = 0        
    
    def setStateEldritchFight(self, currentFrame):
        print("setStateEldritchMove")
        self.BOT_STATE.BOT_ACTION_STATE = BotActionState.ELDRITCH_FIGHT
        self.currentAttackAttempt = 0
    
    def setStateEldritchMove(self, currentFrame):
        print("setStateEldritchMove")
        self.BOT_STATE.BOT_ACTION_STATE = BotActionState.ELDRITCH_MOVE
        self.movementIndex = 0
    
    def setStateEldritchLoot(self, currentFrame):
        print("setStateEldritchMove")
        self.BOT_STATE.BOT_ACTION_STATE = BotActionState.ELDRITCH_LOOT
    
    def setStateMoving(self, currentFrame):
        print("setStateMoving")
        self.BOT_STATE.BOT_ACTION_STATE = BotActionState.MOVING
        # Set out movement index to 0
        # we should also set up our movement list, but lets just default to a5 
        self.movementIndex = 0
        self.movementNeedle = self.vision_a5_start

    # Heal Act5 Malah
    def setStateHealAct5Malah(self, currentFrame):
        self.BOT_STATE.BOT_ACTION_STATE = BotActionState.HEAL_ACT_5_MALAH      
        self.currentHealAttempt = 0

    # Move Act 5 Malah
    def setStateMoveHealAct5Malah(self, currentFrame):
        self.movementIndex = 0
        self.BOT_STATE.BOT_ACTION_STATE = BotActionState.MOVE_HEAL_ACT_5_MALAH   
        
    def setStateWp(self, currentFrame):
        self.BOT_STATE.BOT_ACTION_STATE = BotActionState.WP
        
    def setStateExit(self,currentFrame):
        self.BOT_STATE.BOT_ACTION_STATE = BotActionState.EXIT
        
    def setMenuState(self, currentFrame):
        self.BOT_STATE.BOT_ACTION_STATE = BotActionState.MENU
        
    ##############################
    # Handles
    ##############################
    
    def handleMenu(self, currentFrame):
        print("handleMenu")
        sleep(3*self.sleep_scale)
        #Play button
        pyautogui.moveTo(1050, 1300)
        sleep(1*self.sleep_scale)
        pyautogui.click()
        sleep(1*self.sleep_scale)
        #nightmare button
        pyautogui.moveTo(1250, 700)
        sleep(1*self.sleep_scale)
        pyautogui.click()
        sleep(1*self.sleep_scale)
        self.setStateInitiailized(currentFrame)
    
    def handleExit(self, currentFrame):
        print("handleExit")
        pyautogui.press("esc")
        sleep(1*self.sleep_scale)
        pyautogui.moveTo(2560/2, 1440/2-50)
        pyautogui.click()
        self.setMenuState(currentFrame)
           
    def handleMoving(self, currentFrame):
        
        currentIndex = self.movementIndex
        point = self.movementList[currentIndex].find(currentFrame,0.5)
        print("handleMoving: {}".format(point))
        if len(point) == 1:
            print(point)
            pyautogui.moveTo(point[0][0], point[0][1]);
            pyautogui.click();
            sleep(1*self.sleep_scale)
            self.movementIndex = self.movementIndex + 1
            if self.movementIndex >= len(self.movementList):
                self.setStateWp(currentFrame)
        else:
            # we are lost
            self.setStateLost(currentFrame)
    
    def handleLost(self, currentFrame):
        print("handleLost")
        self.findLoginPlace(currentFrame)
        self.currentLostAttempt = self.currentLostAttempt + 1
        if self.currentLostAttempt > self.maxLostAttempt:
            self.setStateExit(currentFrame)
            
    def handleWp(self, currentFrame):
        print("handleWp")
        #going to frigid
        pyautogui.moveTo(517, 475);
        pyautogui.click();
        self.setStateEldritchMove(currentFrame)
        sleep(3*self.sleep_scale)
        
    # Move Act 5 Malah
    def handleMoveAct5Malah(self,currentFrame):
        print("handleHealAct5Malah")
        #fighting eldritch
        point = self.malah_movePoints[self.movementIndex]
        print("State: MALAH_MOVE {}".format(point))
        pyautogui.moveTo(point[0], point[1]);
        pyautogui.click(button='left')
        sleep(1*self.sleep_scale)
        self.movementIndex = self.movementIndex + 1
        if self.movementIndex >= len(self.malah_movePoints):
            self.setStateHealAct5Malah(currentFrame)
              
    # Heal Act5 Malah
    def handleHealAct5Malah(self, currentFrame):
        point = self.malah.find(currentFrame,0.5)
        print("State: HEALING {}".format(point))
        if len(point) == 1:
            print(point)
            pyautogui.moveTo(point[0][0], point[0][1]);
            pyautogui.click();
            sleep(1*self.sleep_scale)
            self.movementIndex = self.movementIndex + 1
            if self.movementIndex >= len(self.movementList):
                #we are done moving
                self.setStateWp(currentFrame)
        else:
            self.currentHealAttempt = self.currentHealAttempt + 1
            if self.currentHealAttempt > self.maxHealAttempt:
                # TODO: needs to path back, perhaps we can set up a circular pathing system in the towns 
                # so we will always know where we are in the world
                self.setStateInitiailized(currentFrame)
                
    def handleEldritchMove(self,currentFrame):
        #fighting eldritch
        currentIndex = self.movementIndex
        point = self.eldritch_movePoints[currentIndex]
        print("State: ELDRITCH_MOVE {}".format(point))
        pyautogui.moveTo(point[0], point[1]);
        pyautogui.click(button='left')
        sleep(1*self.sleep_scale)
        self.movementIndex = self.movementIndex + 1
        if self.movementIndex >= len(self.eldritch_movePoints):
            #we are done moving time to attack
            self.setStateEldritchFight(currentFrame)
            
    def handleEldritchFight(self, currentFrame):
        pyautogui.moveTo(1300, 5)
        pyautogui.mouseDown(button='right')
        
        self.currentAttackAttempt = self.currentAttackAttempt + 1
        sleep(1*self.sleep_scale)
        if self.currentAttackAttempt >= self.maxAttackAttempt:
            pyautogui.mouseUp(button='right')
            self.setStateEldritchLoot(currentFrame)
    
    def handleEldritchLoot(self, currentFrame):
        print("handleEldritchLoot")
        pyautogui.moveTo(1300, 5)
        pyautogui.press("f1")
        sleep(0.5*self.sleep_scale)
        pyautogui.click(button='right')
        sleep(0.5*self.sleep_scale)
        pyautogui.press("f3")
        sleep(0.5*self.sleep_scale)
        pyautogui.keyDown("alt")
        sleep(10)
        pyautogui.keyUp("alt")
        self.setStateExit(currentFrame)
        
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
                            self.setStateInitiailized(currentFrame)
                            self.BOT_STATE.BOT_ACT_STATE = ActState.ACT_5
                    else:
                        self.setStateInitiailized(currentFrame)
                        self.BOT_STATE.BOT_ACT_STATE = ActState.ACT_4
                else:
                    self.setStateInitiailized(currentFrame)
                    self.BOT_STATE.BOT_ACT_STATE = ActState.ACT_3
            else:
                self.setStateInitiailized(currentFrame)
                self.BOT_STATE.BOT_ACT_STATE = ActState.ACT_2
        else:
            self.setStateInitiailized(currentFrame)
            self.BOT_STATE.BOT_ACT_STATE = ActState.ACT_1



