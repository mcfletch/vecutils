'''Simple utility functions that should really be in a C module'''
from .arrays import (
    asarray, zeros, 
    dot, reshape, sometrue, compress, 
    allclose, 
)
from . import vectorutilities

def crossProduct( first, second ):
    """Given 2 4-item vectors, return the cross product as a 4-item vector"""
    x,y,z = vectorutilities.crossProduct( first[:3], second[:3] )[0]
    return [x,y,z,0]
def magnitude( vector ):
    """Given a 3 or 4-item vector, return the vector's magnitude"""
    return vectorutilities.magnitude( vector[:3] )[0]
def normalise( vector ):
    """Given a 3 or 4-item vector, return a 3-item unit vector"""
    return vectorutilities.normalise( vector[:3] )[0]

def pointNormal2Plane( point, normal ):
    """Create parametric equation of plane from point and normal
    """
    point = asarray(point,'f')
    normal = normalise(normal)
    result = zeros((4,),'f')
    result[:3] = normal
    result[3] = - dot(normal, point)
    return result

def plane2PointNormal( plane ):
    """Get a point and normal from a plane equation"""
    (a,b,c,d) = plane
    return asarray((-d*a,-d*b,-d*c),'f'), asarray((a,b,c),'f')

def combineNormals( normals, weights=None ):
    """Given set of N normals, return (weighted) combination"""
    normals = asarray( normals,'d')
    if weights:
        weights = reshape(asarray( weights, 'f'),(len(weights),1))
        final = sum(normals*weights, 0)
    else:
        final = sum(normals,0)
    x,y,z = final
    if x == y == z == 0.0:
        x,y,z = normals[0]
        if x or y:
            x,y,z = -x,-y,z
        else:
            x,y,z = -x,y,-z
    return normalise( (x,y,z) )

def coplanar( points ):
    """Determine if points are coplanar

    All sets of points < 4 are coplanar
    Otherwise, take the first two points and create vector
    for all other points, take vector to second point,
    calculate cross-product where the cross-product is
    non-zero (not colinear), if the normalised cross-product
    is all equal, the points are collinear...
    """
    points = asarray( points, 'f' )
    if len(points) < 4:
        return True
    a,b = points[:2]
    vec1 = reshape(b-a,(1,3))
    rest = points[2:] - b
    vecs = vectorutilities.crossProduct(
        rest,
        vec1,
    )
    vecsNonZero = sometrue(vecs,1)
    vecs = compress(vecsNonZero, vecs,0)
    if not len(vecs):
        return True
    vecs = vectorutilities.normalise(vecs)
    return allclose( vecs[0], vecs )
