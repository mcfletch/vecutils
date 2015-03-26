from vecutils import arrays, utilities, vectorutilities
import unittest

class TestUtilities( unittest.TestCase ):
    """Tests for generic atlas algorithms"""
    def test_plane2PointNormal( self ):
        for p,n in [
            ([0,1,0], [0,-1,0]),
            ([1,0,0], [1,0,0]),
            ([0,0,1], [0,0,1]),
        ]:
            plane = utilities.pointNormal2Plane(p,n)
            p1,n1 = utilities.plane2PointNormal(plane)
            assert arrays.allclose( p, p1)
            assert arrays.allclose(n, n1)
    def test_coplanar( self ):
        assert utilities.coplanar( [[0,0,1],[0,1,1],[0,1,2],[0,1,3],[0,0,1],[0,1,1]] )
        assert not utilities.coplanar( [[0,0,1],[0,1,1],[0,1,2],[0,1,3],[0,0,1],[1,1,1]] )
        assert not utilities.coplanar( [[0,0,1],[1,1,1],[0,1,2],[0,1,3],[0,0,1],[0,1,1]] )
        assert not utilities.coplanar( [[0,0,1.005],[1,1,1],[0,1,2],[0,1,3],[0,0,1],[0,1,1]] )

    def test_magnitude( self ):
        data = arrays.array( [
            [0,0,0],[1,0,0],[0,1,0],
            [1,0,0],[0,0,0],[0,1,0],
        ],'f')
        mag = vectorutilities.magnitude( data )
        assert arrays.allclose( mag, [0,1,1,1,0,1] ), mag
    def test_normalize( self ):
        data = arrays.array( [
            [2,0,0],[0,2,0],[0,0,2],
            [1,1,0],[-1,1,0],
        ], 'f')
        norms = vectorutilities.normalise( data )
        
        self._allclose( norms, arrays.array([
            [1,0,0],[0,1,0],[0,0,1],
            [1/arrays.sqrt(2),1/arrays.sqrt(2),0],[-1/arrays.sqrt(2),1/arrays.sqrt(2),0],
        ],'f') )
    def test_normalize_zero( self ):
        data = arrays.array( [[ 0,0,0 ]],'f')
        result = vectorutilities.normalise( data )
        assert arrays.allclose( result, [[0,0,0]] )
    def test_crossProduct( self ):
        data = arrays.array([
            [0,1,0],[1,0,0],[0,0,1],
            [1,1,0],
        ],'f')
        cps = vectorutilities.crossProduct( data, [-1,0,0] )
        expected = arrays.array([
            [0,0,1],[0,0,0],[0,-1,0],
            [0,0,1],
        ],'f')
        self._allclose( cps, expected )
    def test_crossProduct4( self ):
        data = arrays.array([
            [0,1,0,1],[1,0,0,1],[0,0,1,1],
            [1,1,0,1],
        ],'f')
        cps = vectorutilities.crossProduct4( data, [-1,0,0,1] )
        expected = arrays.array([
            [0,0,1,1],[0,0,0,1],[0,-1,0,1],
            [0,0,1,1],
        ],'f')
        self._allclose( cps, expected )
    def _allclose( self, target, expected ):
        for a,b in zip( target, expected ):
            assert arrays.allclose( a,b),(a,b)
        
    def test_orientToXYZR( self ):
        """Can we do an orientation-to-xyzr rotation properly?"""
        a = (0,0,-1 )
        b = (1,0,0 )
        expected = [(0,1,0,-arrays.pi/2),(0,-1,0,arrays.pi/2)]
        xyzr = vectorutilities.orientToXYZR( a,b )
        found = False 
        for e in expected:
            if arrays.allclose( e, xyzr ):
                found = True 
                break 
        assert found, xyzr
    
