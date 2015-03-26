from vecutils import arrays, quaternion
import unittest

def ac(x, y):
    assert arrays.allclose(x, y), x

class TestQuaternions( unittest.TestCase ):
    def test_euler_x(self):
        rot = quaternion.fromEuler( arrays.pi/2 ).XYZR()
        ac( rot, (1, 0, 0, arrays.pi/2))
    def test_euler_y(self):
        rot = quaternion.fromEuler( y = arrays.pi/2 ).XYZR()
        ac( rot, (0, 1, 0, arrays.pi/2))
    def test_euler_z(self):
        rot = quaternion.fromEuler( z = arrays.pi/2 ).XYZR()
        ac( rot, (0, 0, 1, arrays.pi/2))
    def test_euler_y_flip(self):
        q = quaternion.fromEuler( y=arrays.pi*2 )
        rot = q.XYZR()
        assert arrays.allclose(rot[-1]%(arrays.pi*2), 0)
        matrix = q.matrix()
        ac(matrix, arrays.identity(4))
    def test_slerp(self):
        first = quaternion.fromXYZR( 0,1,0,0 )
        second = quaternion.fromXYZR( 0,1,0,arrays.pi )
        for fraction in arrays.arange( 0.01, 1.0, .01 ):
            rot = first.slerp( second, fraction ).XYZR()
            assert arrays.allclose( rot, (0, 1, 0, arrays.pi*fraction ), 0.001)
#    first = fromXYZR( 0,1,0,0 )
#    second = first.inverse()
#    assert allclose( first.internal,second.internal ), (first, second)
#    first = fromXYZR( 0,1,0,pi/2 )
#    second = first.inverse()
#    expected = fromXYZR( 0,1,0,-pi/2)
#    assert allclose( second.internal, expected.internal ), (second,expected )
