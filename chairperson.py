#!/bin/python3
from datetime import datetime
import time
from motion import motion
m = motion()

class chairperson:
    #def __init__(self):
##    def rolecall(self, ):
##        return '
    
    def session(self, option):
        '''
        Chooses the session type.
        @parameter: Option of opening session, resuming session, closing session or suspending session
        @return: hints for the chairperson, messages for members
        '''
        current = datetime.now()
        # dd/mm/YY
        # H:M:S
        d_string = current.strftime("%d/%m/%Y")
        t_string = current.strftime("%H:%M:%S")
        if option == 'open':
            hint = 'Role Call'
            message = 'Session is opened on ' + d_string + ' at ' + t_string + '.'
        elif option == 'suspend':
            hint = ''
            message = 'Session is suspended on ' + d_string + ' at ' + t_string + ' till further notice. '   
        elif option == 'resume':
            
##            hint = 'Current Motion is ' + 
            message = 'Session is resumed on ' + d_string + ' at ' + t_string + '.'
        elif option == 'close':
            hint = ''
            message = 'Session is closed on ' + d_string + ' at ' + t_string + '.'       
        return hint, message
    
    def open_session(self):
        return session('open')
    def close_session(self):
        return session('close')
    def resume_session(self):
        return session('resume')
    def suspend_session(self):
        return session('suspend')

    def agenda_floor(self, state):
        '''
        Floor for selecting motions.
        @parameter: State if the floor is to open or close.
        '''
        current = datetime.now()
        # H:M:S
        t_string = current.strftime("%H:%M:%S")
        if state == 'open':
            hint = 'Close floor.'
            message = 'Floor is now open. Floor opened at  ' + t_string
        elif state == 'close':
            hint = 'Proceed with procedural voting.'
            message = 'Floor is now closed. Floor closed at ' + t_string

        return hint, message
    
    def unmoderated_floor(self, state):
        '''
        FLoor state during caucus.
        @parameter: State if the floor is to open or close.
        '''
        current = datetime.now()
        # H:M:S
        t_string = current.strftime("%H:%M:%S")
        if state == 'open':
            hint = 'Close floor. '
            message = 'Floor is now open. Floor opened at  ' + t_string
        elif state == 'close':
            hint = 'Proceed with next motion.'
            message = 'Floor is now closed. Floor closed at ' + t_string

        return hint, message        

    def open_floor(self):
        return agenda_floor('open')
    
    def close_floor(self):
        return agenda_floor('close')
    
    def del_motion(self, index):
        motion.delete(index)
    
    def countdown(self, t):
        '''
        Countdown timer.
        @parameter: seconds to start the countdown from.
        '''
        t = int(t)
        while t:
            mins, secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            if mins == 1:
                print("Time left: " + timeformat)
            elif mins == 0 and secs == 30:
                print("Time left: " + timeformat)
            elif mins == 0 and secs == 10:
                print("Time left: " + timeformat)
            if t < 10:
                print("Time left", timeformat, end='\n')
            time.sleep(1)
            t -= 1
        print('Times up!')

    def set_agenda(self, string):
        return ' '
    def close_agenda(self):
        return ' '


	


