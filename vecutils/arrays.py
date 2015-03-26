from numpy import *
try:
    from . import tmatrixaccel
except ImportError as err:
    tmatrixaccel = None
# why did this get taken out?  Is divide now safe?
amin = amin 
amax = amax
divide_safe = divide 
# Now deal with differing numpy APIs...
ArrayType = ndarray # alias removed in later versions
# Take's API changed from Numeric, we've updated to 
# always provide axis now...
try:
    # PyVRML97 is from before numpy printed errors, we explicitly do not care 
    # about the divide-by-zero, which commonly happens in mesh data processing
    # TODO: likely should rework the mesh processing to check manually and remove 
    # this sledge-hammer approach
    seterr(all='ignore')
except Exception as err:
    pass
    
def contiguous( a ):
    """Force to a contiguous array"""
    return array( a, a.dtype )
