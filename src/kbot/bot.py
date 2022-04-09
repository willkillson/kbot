
# collapse all code hotkey
# Ctrl + (K => 0) (zero) on Windows and Linux

from vision import Vision
from time import sleep
from src.kbot.vision.hsvfilter import HsvFilter
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
    
    loot_sense = 0.46
    
    currentLostAttempt = 0
    maxLostAttempt = 5
    
    currentHealAttempt = 0
    maxHealAttempt = 5
    
    currentAttackAttempt = 0
    maxAttackAttempt = 5
    
    totalRunTime = None
    BOT_STATE = None
    # Based on state, this is our current place we should be.
    # Will will need to determine where this is often, 
    # otherwise we will be lost and need to figure where we are at.
    movementNeedle = None
    # Current attack targets
    targetNeedles = []
    # Elapsed time since last move.
    elapsedTime = 0
    
    
    #filters for finding items quickly
    hsv_filter_rare = HsvFilter(26, 122, 0, 39, 170, 255, 3, 16, 0, 0)
    hsv_filter_unique = HsvFilter(17, 71, 166, 27, 118, 203, 11, 24, 0, 0)
    
    vision_unique_a = Vision('../../images/needle/items/unique_a.jpg')
    vision_unique_e = Vision('../../images/needle/items/unique_e.jpg')
    vision_unique_i = Vision('../../images/needle/items/unique_i.jpg')
    vision_unique_u = Vision('../../images/needle/items/unique_u.jpg')
    
    vision_rare_e = Vision('../../images/needle/items/rare_e.jpg')


    vision_login_a1 = Vision('../../images/needle/login/login_a1.jpg')
    vision_login_a2 = Vision('../../images/needle/login/login_a2.jpg')
    vision_login_a3 = Vision('../../images/needle/login/login_a3.jpg')
    vision_login_a4 = Vision('../../images/needle/login/login_a4.jpg')
    vision_login_a5 = Vision('../../images/needle/login/login_a5.jpg')
    
    vision_a5_start = Vision('../../images/needle/a5/a5_start.jpg')


    vision_a5_wp= Vision('../../images/needle/a5/a5_wp.jpg')
    
    movementIndex = 0
    movementList = []
    
    eldritch_movementList = []
    eldritch_movePoints = []
    
    malah = Vision('../../images/needle/malah.jpg')
    malah_movePoints = []
    
    sleep_scale = 0.85
    
    

    def __init__(self):
        self.totalRunTime = 0
        self.BOT_STATE = BotState()
        self.BOT_STATE.BOT_ACTION_STATE = BotActionState.INITIALIZING
        self.BOT_STATE.BOT_ACT_STATE = ActState.UNK
        
        self.movementList.append(Vision('../../images/needle/a5/a5_stairs1.jpg'))
        self.movementList.append(Vision('../../images/needle/a5/a5_midstairs2.jpg'))
        self.movementList.append(Vision('../../images/needle/a5/a5_stairs2.jpg'))
        self.movementList.append(Vision('../../images/needle/a5/a5_wp.jpg'))
        
        self.eldritch_movementList.append(Vision('../../images/needle/eldritch/eldritch_1.jpg'))
        self.eldritch_movementList.append(Vision('../../images/needle/eldritch/eldritch_2.jpg'))
        
        self.eldritch_movePoints.append((1300,55))
        self.eldritch_movePoints.append((1200,55))
        
        self.malah_movePoints.append((755,575))
        self.malah_movePoints.append((820,430))
                
        # self.eldritch_movementList.append(Vision('./images/needle/eldritch/eldritch_3.jpg'))
        
        
    def updateState(self, currentFrame):
        if self.BOT_STATE.BOT_ACTION_STATE == BotActionState.INITIALIZING:
            self.findLoginPlace(currentFrame)   
            # self.setStateEldritchLoot(currentFrame)   
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
        print("setStateInitiailized")
        self.BOT_STATE.BOT_ACTION_STATE = BotActionState.INITIALZED 
    
    def setStateMoving(self, currentFrame):
        print("setStateMoving")
    
    def setStateLost(self, currentFrame):
        print("setStateLost")
        self.BOT_STATE.BOT_ACTION_STATE = BotActionState.LOST
        self.currentLostAttempt = 0        
    
    def setStateEldritchFight(self, currentFrame):
        print("setStateEldritchFight")
        self.BOT_STATE.BOT_ACTION_STATE = BotActionState.ELDRITCH_FIGHT
        self.currentAttackAttempt = 0
    
    def setStateEldritchMove(self, currentFrame):
        print("setStateEldritchMove")
        self.BOT_STATE.BOT_ACTION_STATE = BotActionState.ELDRITCH_MOVE
        self.movementIndex = 0
    
    def setStateEldritchLoot(self, currentFrame):
        print("setStateEldritchLoot")
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
        print("setStateHealAct5Malah")
        self.BOT_STATE.BOT_ACTION_STATE = BotActionState.HEAL_ACT_5_MALAH      
        self.currentHealAttempt = 0

    # Move Act 5 Malah
    def setStateMoveHealAct5Malah(self, currentFrame):
        print("setStateMoveHealAct5Malah")
        self.movementIndex = 0
        self.BOT_STATE.BOT_ACTION_STATE = BotActionState.MOVE_HEAL_ACT_5_MALAH   
        
    def setStateWp(self, currentFrame):
        print("setStateWp")
        self.BOT_STATE.BOT_ACTION_STATE = BotActionState.WP
        
    def setStateExit(self,currentFrame):
        print("setStateExit")
        self.BOT_STATE.BOT_ACTION_STATE = BotActionState.EXIT
        
    def setMenuState(self, currentFrame):
        print("setMenuState")
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
        rectangles = self.movementList[currentIndex].find(currentFrame,0.5)
        clickPoints = self.vision_a5_start.get_click_points(rectangles)
        print("handleMoving: {}".format(clickPoints))
        if len(clickPoints) > 0:
            point = clickPoints[0]
            pyautogui.moveTo(point[0], point[1]);
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
            
            pyautogui.moveTo(1300, 5)
            
            pyautogui.press("f1")
            pyautogui.click(button='right') 
            pyautogui.press("f3")
            pyautogui.mouseDown(button='right')
            sleep(2)
            pyautogui.mouseUp(button='right')
            
            self.setStateEldritchLoot(currentFrame)
    
    def handleEldritchLoot(self, currentFrame):
        print("handleEldritchLoot")
        
        ##TODO this is a hack because my vision thinks pots are items at times.
        pyautogui.press("1")
        pyautogui.press("2")
        pyautogui.press("3")
        pyautogui.press("4")
        
        pyautogui.keyDown("alt")
        # points for unique
        unique_filter = self.vision_unique_e.apply_hsv_filter(currentFrame,self.hsv_filter_unique)
        rare_filter = self.vision_unique_e.apply_hsv_filter(currentFrame,self.hsv_filter_rare)
        rarPoints = self.vision_rare_e.find(rare_filter, self.loot_sense)
        uniPoints = self.vision_unique_e.find(unique_filter, self.loot_sense)        

        #Go get the loot
        if len(uniPoints) > 0:
            point = uniPoints[0]
            y_offset = 40
            x_offset = 5
            print("UniqueLootFound!: {}".format(uniPoints))
            pyautogui.moveTo(point[0]+x_offset, point[1]+y_offset);
            pyautogui.mouseDown(button='left')
            pyautogui.mouseUp(button='left')
            return
        # if len(rarPoints) > 0:
        #     point = rarPoints[0]
        #     y_offset = 40
        #     x_offset = 5
        #     print("RareLootFound!: {}".format(rarPoints))
        #     pyautogui.moveTo(point[0]+x_offset, point[1]+y_offset);
        #     pyautogui.mouseDown(button='left')
        #     pyautogui.mouseUp(button='left')
        #     return
        pyautogui.keyUp("alt")
        self.setStateExit(currentFrame)   
             
    # Will trigger BOT_ACTION_STATE to INITIALZED 
    def findLoginPlace(self, currentFrame):
        point = None
        point = self.vision_login_a1.find(currentFrame, 0.5)
        if len(point) == 0:
            point = self.vision_login_a2.find(currentFrame, 0.5)
            if len(point) == 0:
                point = self.vision_login_a3.find(currentFrame, 0.5)
                if len(point) == 0:
                    point = self.vision_login_a4.find(currentFrame, 0.5)
                    if len(point) == 0:
                        point = self.vision_login_a5.find(currentFrame, 0.5)
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



