# Python 2.7 utility to kill off a named program/programs
import os, time, sys

def usage():
    print """
    kill_prog {-D,-d,--delay time_in_seconds} program1 program2 ...
    
    note: default delay is 1 second, if you override with a value less than 1, the
    kill will only run once.
    """
    sys.exit(0)
    
def kill_program(pname):
    cmd = 'taskkill /f /im %s' % pname
    os.system(cmd)

def kill_daemon(programs, delay_seconds = 1):
    """
    kill_daemon(programs, delay_seconds)
    intent: runs a program that will attempt to kill off a single or list of programs
    programs = single program name or python list of names
    delay_seconds - amount of wait time in between kill attempts
    """
    DEBUG = False
    if type(programs) == type('str'):
        programs = [programs]
    
    done = False    
    while not done:
        for this_program in programs:
            try:
                kill_program(this_program)
            except Exception, e:
                if DEBUG:
                    print str(e)
                    print 'Error thrown killing <%s>' % this_program
                else:
                    pass
            if delay_seconds > 0:
                time.sleep(delay_seconds)
            else:
                done = True
            
def test_program():
    while True:
        # test
        try:
            kill_program("putty.exe")
        except:
            pass
        time.sleep(1)
        
if __name__ == '__main__':
    programs = []
    if len(sys.argv) > 1:
        delay_flag = False
        delay_time = 1
        for arg in sys.argv:
            if delay_flag:
                # see if user is overriding the default delay of 1 second
                try:
                    delay_time = int(arg)
                    delay_flag = False
                except:
                    print 'Delay value must be integer'
                    usage()
                    
            elif arg in ['-d','-D','--delay']:
                delay_flag = True
            elif arg == sys.argv[0]:
                pass
            else:
                programs.append(arg)
    else:
        usage()
        
    kill_daemon(programs,delay_time)
                
                
    
    