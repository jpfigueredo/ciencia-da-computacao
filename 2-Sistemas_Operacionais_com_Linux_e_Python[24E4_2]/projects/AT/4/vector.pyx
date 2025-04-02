from cython.parallel import prange
import cython

@cython.boundscheck(False)
@cython.wraparound(False)
def vector_by_scalar(double[:] vec, double scalar):
    cdef int i
    cdef int n = vec.shape[0]
    with nogil:
        for i in prange(n):
            vec[i] *= scalar
