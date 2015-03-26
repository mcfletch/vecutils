from unittest import TestCase
from vecutils import arrays, triangleutilities, vectorutilities

class TriangleUtilityTests(TestCase):
    def setUp(self):
        self.triangles = arrays.array( [
            [0,0,0],[1,0,0],[0,1,0],
            [1,0,0],[0,0,0],[0,1,0],
        ],'f')
    def test_normal_per_face_ccw(self):
        normals = triangleutilities.normalPerFace( self.triangles )
        assert arrays.allclose(normals, [[0, 0, 1], [0, 0, -1]]), normals
    def test_normal_per_face_noccw(self):
        normals = triangleutilities.normalPerFace( self.triangles, ccw=False )
        assert arrays.allclose(normals, [[0, 0, -1], [0, 0, 1]]), normals
    def test_basis_vector_reshape(self):
        triangles = arrays.reshape(self.triangles, (2, 3, 3))
        normals = triangleutilities.normalPerFace( triangles )
        assert arrays.allclose(normals, [[0, 0, 1], [0, 0, -1]]), normals
    def test_centers(self):
        centers = triangleutilities.centers(self.triangles)
        assert arrays.allclose(centers, [
            [1/3., 1/3., 0], 
            [1/3., 1/3., 0], 
        ]), centers
        
class VectorUtilityTests(TestCase):
    def test_colinear(self):
        for points in [
            [[0, 1, 0], [0, 0, 0], [0, -1, 0]], 
            [[1, 0, 0], [2, 0, 0], [3, 0, 0]], 
            [[0, 0, 0], [23, 23, 0], [46, 46, 0]], 
        ]:
            colinear = vectorutilities.colinear(points)
            assert colinear is not None, points
    def test_orient_to_rotation(self):
        first = [0, 1, 0]
        second = [0, 0, -1]
        expected = [1, 0, 0, -arrays.pi/2], [-1, 0, 0, arrays.pi/2]
        produced = vectorutilities.orientToXYZR(first, second)
        found = False 
        for exp in expected:
            if arrays.allclose(produced, exp):
                found = True 
        assert found, produced
    def test_orient_to_rotation_null(self):
        first = [0, 1, 0]
        second = [0, 1.00000000000001,0]
        expected = [0, 1, 0, 0]
        produced = vectorutilities.orientToXYZR(first, second)
        assert arrays.allclose(produced, expected), produced
    def test_magnitude_reshape(self):
        tris = arrays.array( [
            [[0,0,0],[1,0,0],[0,1,0]],
            [[1,0,0],[0,0,0],[0,1,0]],
        ],'f')
        produced = vectorutilities.magnitude(tris)
        assert produced.shape == (6, ), produced
    
