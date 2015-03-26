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
    def test_euler_xz(self):
        q = quaternion.fromEuler( x=arrays.pi, z = arrays.pi/2 )
        ac(q.XYZR(), (2**.5/2, -2**.5/2, 0, arrays.pi))
    def test_euler_xy(self):
        q = quaternion.fromEuler( x=arrays.pi, y = arrays.pi/2 )
        ac(q.XYZR(), (2**.5/2, 0, 2**.5/2, arrays.pi))
    def test_euler_yz(self):
        q = quaternion.fromEuler( z=arrays.pi, y = arrays.pi/2 )
        ac(q.XYZR(), (2**.5/2, 0, 2**.5/2, arrays.pi))
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
    def test_inverse_null(self):
        first = quaternion.fromXYZR( 0,1,0,0 )
        second = first.inverse()
        assert arrays.allclose( first.internal,second.internal ), (first, second)
    def test_inverse_angle(self):
        first = quaternion.fromXYZR( 0,1,0,arrays.pi/2 )
        second = first.inverse()
        expected = quaternion.fromXYZR( 0,1,0,-arrays.pi/2)
        assert arrays.allclose( second.internal, expected.internal ), (second,expected )

    def test_quaternion_dot(self):
        q = quaternion.fromXYZR( 0, 1, 0, arrays.pi )
        v = arrays.array([1, 0, 0, 0], dtype='f')
        transformed = q*v
        ac(transformed, [-1, 0, 0, 0])
    def test_quaternion_dot_2(self):
        q = quaternion.fromXYZR( 0, 1, 0, arrays.pi/2 )
        v = arrays.array([1, 0, 0, 0], dtype='f')
        transformed = q*v
        ac(transformed, [0, 0, -1, 0])
    
