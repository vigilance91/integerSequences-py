from time import time as now
#
class Timer:
    """Class representing a timer which can be started, stopped, reset,
    for use to time function call execution time, frame ticks, or for firing events"""    
    INV_MS = 1.0 / 1000.0   #inverse milliseconds, for use in conversion from milliseconds to seconds
    INV_M = 1.0 / 60.0   #inverse minutes, for use in conversion from seconds to minutes
    INV_D = 1.0 / 24.0
    #
    @staticmethod
    def now():
        #returns the time in Seconds since the unix epoch as a floating point number
        return now()
    
    @staticmethod
    def nowMS():
        #returns the time in Seconds since the unix epoch as a floating point number
        return now() * 1000
        
    @staticmethod
    def nowM():
        #returns the time in Minutes since the unix epoch as a floating point number
        return now() * Timer.INV_M
        
    @staticmethod
    def nowH():
        #returns the current time in Hours since the unix epoch as a floating point number
        return now() * Timer.INV_M
        
    @staticmethod
    def nowD():
        #returns the time in Days since the unix epoch as a floating point number
        return now() * Timer.INV_D
    #@staticmethod
    # //def getScriptExecTimeNano():
        # //returns the current time (relative to the call) since the script's request in nanoseconds
        # //return Timer.getScriptExecTimeS() * 1000000000
    
    #@staticmethod
    # //def getScriptExecTimeMicro(){
        # //returns the current time (relative to the call) since the script's request in microseconds
        # //return Timer.getScriptExecTimeS() * 1000000;
    
    #@staticmethod
    # def getScriptExecTimeMS()
        # //returns the current time (relative to the call) since the script's request in milliseconds
        # return Timer.getScriptExecTimeS() * 1000
        
    #@staticmethod
    # def getScriptExecTimeS():
        # //returns the current time (relative to the call) since the script's request in seconds
        # return microtime(true) - $_SERVER['REQUEST_TIME_FLOAT']

    #@staticmethod
    # def getScriptExecTimeM():
        # //returns the current time (relative to the call) since the script's request in minutes
        # return Timer.getScriptExecTimeS() * Timer.INV_M

    #@staticmethod
    # //def getScriptExecTimeH():
        # //returns the current time (relative to the call) since the script's request in hours
        # //return Timer.getScriptExecTimeM() * Timer.INV_M
    
    def __init__(self, reset = False):
        #if reset is true, will start timer as soon as init has completed
        #default behaviour is the timer is stopped and must be manually started with a call to start
        self._start = 0.0   #time when timer started
        #self._prev = 0.0   #time since last tick
        self._end = 0.0 #time when timer stopped
        self._dt = 0.0  #delta time between start and stop calls
        self._pauseStart = 0.0
        #self._pausedTime = 0.0
        self._isStopped = True
        
        if reset:
            self.reset()
    
    def start(self):
        if self._isStopped:
            if self._pauseStart > 0.0:
                #timer is paused, so reset
                t = now()
                self._start = t
                #self._prev = 0.0
                self._pauseStart = 0.0
                #self._pauseEnd = t
            else:
                #timer has been stopped but not paused,
                #so just set start time
                #t = now()
                self._start = now()
                #self._prevTime = t

            self._isStopped = False
        #else:
            #print('notice: attempting to start after previously being started, call does nothing')

    def pause(self):
        if self._start > 0.0 and not self._isStopped:
            self._isStopped = True
            self._pauseStart = now()
        #else:
            #print('timer has not been started, stop does nothing')
    
    def isPaused(self):
        return self._isStopped and self._pauseStart > 0.0

    def end(self):
        if self._start > 0.0 and not self._isStopped:
            self._isStopped = True
            self._end = now()
            self._pauseStart = 0.0
            #self._pauseEnd = 0.0
            self._dt = self._end - self._start
        #else:
            #timer has not been started, stop does nothing

    # def #getPauseDelta(self):
        # #return self._isStopped ? self.pauseDelta : Timer.now() - self._pauseStart
    
    #def getTickDelta(self):
        # #returns delta in seconds between now and previous update if timer is stopped,
        # #otherwise returns 0.0
        #return 0.0 if self._isStopped else now() - self._prev

    #def getTotalDelta(self):
    def getDelta(self):
        # #returns delta in seconds between _start and _end if timer is stopped,
        # #otherwise returns difference between start and the current time
        return self._dt if self._isStopped else now() - self._start

    #def tick(self):
        #if self._isStopped:
            #self._dt = 0.0
            #return
            
        #t = now()
        #self._prevTime = self._curTime
        
        #if self._dt < 0.0:
            #self._dt = 0.0
            
            
        
    #def getCurrentTime(self):
        #if not self._isStopped:
            #(self._stopTime - self._startTime) * _secondsPerCount
        #else:
            #return (self._currTime - self._pausedTime) - self._baseTime
            
    # def getDeltaMS(self):
        # #returns delta in milliseconds
        # return self.getDelta() * 1000
    
    # def getDeltaM(self):
        # //returns delta in minutes
        # return self.getDelta() * Timer.INV_M
        
    # def getDeltaH(self):
        # //returns delta in minutes
        # return self.getDeltaM() * Timer.INV_M

    def reset(self):
        if not self._isStopped:
            self._end = 0.0
            self._dt = 0.0
            self._pauseStart = 0.0
            #self._pauseEnd = 0.0
            self._isStopped = True
        
        self.start()

def timeCall(callable): #**kwargs
    """decorator for timing the execution of a generic function"""
    #returns the time taken to execute function callable, in seconds
    def dec(*args, **kwargs):
        t = Timer(True)
        
        ret = callable(*args, **kwargs)
        
        t.end()
        dt = t.getDelta()
        
        print("execution time:{DT}".format(DT=dt))
        
        return ret
  
    return dec
    
