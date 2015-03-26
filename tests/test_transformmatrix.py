import unittest,sys
from vecutils.transformmatrix import transMatrix, rotMatrix, scaleMatrix, perspectiveMatrix, DEGTORAD
from vecutils.arrays import allclose,dot, pi, array

class TestTransformMatrix( unittest.TestCase ):
    def test_calculations( self ):
        for (matrix,point, expected, name) in self.TEST_DATA:
            try:
                result = dot( point,matrix)
            except TypeError as err:
                sys.stderr.write("""\nF (TypeError):\n\tpoint=%(point)s\n\t%(matrix)s\n"""%(locals()))
            else:
                assert allclose( result, expected, 0, 0.000001 ),(name,matrix,point,expected,result)
    TEST_DATA = [
        (transMatrix( (1,0,0) )[0], (0, 0,0,1), (1,0,0,1), "Simple translation"),
        (transMatrix( (-1,-1,-1) )[0], (1, 1,1,1), (0,0,0,1), "Simple translation"),
        (transMatrix( (0,0,1) )[0], (0, 0,0,1), (0,0,1,1), "Simple translation"),
        (rotMatrix( (0,1,0,pi) )[0], (1, 0,0,1), (-1,0,0,1), "Simple rotation"),
        (rotMatrix( (0,1,0,pi/2) )[0], (1, 0,0,1), (0,0,-1,1), "Simple rotation"),
        (rotMatrix( (0,0,1,pi/2) )[0], (1, 0,0,1), (0,1,0,1), "Simple rotation"),
        (rotMatrix( (0,0,1,-(pi/2)) )[0], (1, 0,0,1), (0,-1,0,1), "Simple rotation"),
        (rotMatrix( (0,0,-1,-(pi/2)) )[0], (1, 0,0,1), (0,1,0,1), "Simple rotation"),
        (rotMatrix( (0,0,-2,-(pi/2)) )[0], (1, 0,0,1), (0,1,0,1), "Simple rotation (w/normalize)"),
        (rotMatrix( (1,0,0,-(pi/2)) )[0], (1, 0,0,1), (1,0,0,1), "Simple rotation"),
        (rotMatrix( (0,0,1,pi/2) )[0], (0,1,0,1), (-1,0,0,1), "Simple rotation"),
        (rotMatrix( (1,0,0,pi/2) )[0], (0,0,1,1), (0,-1,0,1), "Simple rotation"),
        (scaleMatrix( (1,1,2) )[0], (1, 1,1,1), (1,1,2,1), "Simple scale"),
        (scaleMatrix( (-1,1,2) )[0], (1, 1,1,1), (-1,1,2,1), "Simple scale"),
        (scaleMatrix( (-1,0,2) )[0], (1, 1,1,1), (-1,0,2,1), "Simple scale"),
        (scaleMatrix( (-1,0,0) )[0], (1, 1,1,1), (-1,0,0,1), "Simple scale"),
        (scaleMatrix( (0,0,0) )[0], (1, 1,1,1), (0,0,0,1), "Simple scale"),
        (rotMatrix([ 0.,0.,1., -0.515])[0], (1,0,0,1), (0.87029272,-0.49253485,0.,1.), "Make sure rotation uses float check for abs value" ),
    ]
        
    def test_perspectiveMatrix( self ):
        """Test that perspective matrix calculation matches expected values"""
        result = perspectiveMatrix(
            59.999999999999993*DEGTORAD, 1.0, 0.29999999999999999, 50000
        )
        inverse = perspectiveMatrix(
            59.999999999999993*DEGTORAD, 1.0, 0.29999999999999999, 50000, inverse=True,
        )
        
        expected = array([
            [ 1.73205081,  0.,          0.,          0.,        ],
            [ 0.,          1.73205081,  0.,          0.,        ],
            [ 0.,          0.,         -1.000012, -1.,        ],
            [ 0.,          0.,         -0.6000036,   0.,        ],],'f')
        assert allclose(result,expected), result
        
        test = array([ 20,8,5,1.0 ],'f')
        projected = dot( result, test )
        unprojected = dot( inverse, projected )
        assert allclose( unprojected, test ), (unprojected, test)
    
