class BotState:
    INITIALIZING = 0
    LOOTING = 1
    MOVING = 2
    KILLING = 3
    LOST = 4


class kbot:
    totalRunTime = None
    state = None
    # Based on state, this is our current place we should be.
    # Will will need to determine where this is often, 
    # otherwise we will be lost and need to figure where we are at.
    movementNeedle = None;
    # Current attack targets
    targetNeedles = []
    # Elapsed time since last move.
    elapsedTime = 0

    def __init__(self):
        self.totalRunTime = 0