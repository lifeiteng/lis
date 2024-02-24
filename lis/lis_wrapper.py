import ctypes
import numpy as np
import os

# Get the path to the shared object file
file_dir = os.path.dirname(os.path.abspath(__file__))
so_file = os.path.join(file_dir, '../build/lib.linux-x86_64-cpython-310/lis/_liblis.cpython-310-x86_64-linux-gnu.so')

# Load the shared object file
_liblis = ctypes.CDLL(so_file)

# Define function prototypes
_liblis.longestIncreasingSubsequence.restype = ctypes.POINTER(ctypes.c_int)
_liblis.longestIncreasingSubsequence.argtypes = [np.ctypeslib.ndpointer(dtype=np.int32), ctypes.c_int]

def longestIncreasingSubsequence(X):
    # Convert Python list to NumPy array
    X_np = np.array(X, dtype=np.int32)
    N = len(X)
    
    # Call the C/C++ function
    result_ptr = _liblis.longestIncreasingSubsequence(X_np, N)
    
    # Convert the result from C pointer to Python list
    result = [result_ptr[i] for i in range(N)]
    
    # Free the memory allocated in C/C++ side
    _liblis.free(result_ptr)
    
    return result

# Expose the function under the lis module
lis = {
    'longestIncreasingSubsequence': longestIncreasingSubsequence
}