class timer():
    def __init__(self, maxTime, framerate):
        self.maxTime = self.secondsToFrames(maxTime, framerate)
        self.currTime = self.secondsToFrames(maxTime, framerate)
        self.stopped = 0
        self.framerate = framerate

    def resume(self):
        self.stopped=False

    def halt(self):
        self.stopped=True

    def resetTime(self, seconds, framerate):
        self.currTime = seconds*framerate

    def isFinished(self):
        if(self.currTime<=0):
            return 1 #If return 1 the game is over
        return 0 #If return 0 the game is still going

    def decrement(self):
        if(self.stopped==0):
            self.currTime-=1

    def increment(self):
        if (self.stopped == 0):
            self.currTime+=1

    def secondsToFrames(self, seconds, framerate):
        return seconds*framerate

    def getTime(self):
        return self.currTime

    def getTimeSeconds(self):
        return int(self.currTime/self.framerate)