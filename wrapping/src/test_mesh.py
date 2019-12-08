#!/usr/bin/env python

from os import path as path
import openmeeg as om
import numpy as np
from optparse import OptionParser

data_path = path.dirname(path.abspath(__file__))
parser = OptionParser()
parser.add_option("-p", "--path", dest="data_path",
                  help="path to data folder", metavar="FILE", default=data_path)

options, args = parser.parse_args()
data_path = options.data_path


def test_mesh(name, Vs, Ts, ExpectedResult):
    try:
        mesh = om.Mesh(Vs, Ts)
        mesh.update()
        mesh.info()
    except:
        if ExpectedResult:
            print("Test", name, "--> Failed")
            assert False
        else:
            print("Test", name, "--> Expected failure")
        return
    if not ExpectedResult:
        print("Test", name, "--> Unexpected success")
        assert False
    print("Test", name, "--> Expected success")

vertices = np.array([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0],
                     [1.0, 1.0, 0.0], [0.0, 1.0, 0.0]])
triangles = np.array([[1, 2, 3], [2, 3, 0]])

bad_vertices = np.array([[0.0, 0.0], [1.0, 0.0, 0.0],
                        [1.0, 1.0, 0.0], [0.0, 1.0, 0.0]])
bad_triangles = np.array([[1, 2], [0, 1, 2]])

test_mesh("1", vertices, triangles, True)
test_mesh("2", np.array([0.0, 0.0, 0.0]), triangles, False)
test_mesh("3", vertices, np.array([0, 1, 2]), False)
test_mesh("4", bad_vertices, triangles, False)
test_mesh("5", vertices, bad_triangles, False)

bad_vertices = np.array([0.0, 0.0])
test_mesh("6", bad_vertices, triangles, False)

bad_triangles = np.array([1, 2, 3])
test_mesh("7", vertices, bad_triangles, False)

triangles = np.array([[1, 2, 3], [2, 3, 0]], dtype=np.uint64)
test_mesh("8", vertices, triangles, True)

triangles = np.array([[1, 2, 3], [2, 3, 0]], dtype=np.int64)
test_mesh("9", vertices, triangles, True)

# test X -> should be OK
# TODO: Does not work if not jls....
data_file = path.join(data_path, "Head1", "Head1.tri")
mesh_X = om.Mesh()
mesh_X.load(data_file)
mesh_X.update()

# test Y -> redo with np.array()
V_Y = mesh_X.vertices()
#T6 = mesh_6.triangles()
#mesh_7 = om.Mesh(V6, T6)
# mesh_7.info()

# TODO
#
# mesh_6.nb_vertices()  == mesh_7.nb_vertices()
# mesh_6.nb_triangles() == mesh_7.nb_triangles()
# V7 = mesh_6.vertices()
# T7 = mesh_6.triangles()
# V6 == V7
# T6 == T7
