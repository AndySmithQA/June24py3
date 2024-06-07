#Question 1
import os
import sys



def end_timer(txt='End time'):
    """...
    """
    global start_time
    if start_time is None:
        raise SystemError(
            "end_timer() called without a start_timer()")
    end_time = os.times()[:2]
    print("{0:<12}: {1:01.3f} seconds".
          format(txt, end_time - start_time))

    start_time = None
    return

#Question 2 - Debugging the error
#you will need to import mytimer for this to work

from mytimer import end_timer
try:
    end_timer()
except SystemError as err:
    print("end_timer error:", err, file=sys.stderr)
