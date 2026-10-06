import numpy as np

def mk_cube():
    verts = np.array([
        [-0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5],
        [-0.5, -0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5],
        [-0.5, -0.5, -0.5, -0.5, 0.5, 0.5, 0.5, 0.5]
    ])
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]
    return verts, edges


axes = np.array([[0, 0, 0], [1.1, 0, 0], [0, 1.1, 0], [0, 0, 1.1]]).T


def rx(angle):
    c = np.cos(angle)
    s = np.sin(angle)
    return np.array([
        [1.0, 0.0, 0.0],
        [0.0, c, -s],
        [0.0, s, c]
    ])


def ry(angle):
    c = np.cos(angle)
    s = np.sin(angle)
    return np.array([
        [c, 0.0, s],
        [0.0, 1.0, 0.0],
        [-s, 0.0, c]
    ])


def rz(angle):
    c = np.cos(angle)
    s = np.sin(angle)
    return np.array([
        [c, -s, 0.0],
        [s, c, 0.0],
        [0.0, 0.0, 1.0]
    ])


def project(vertices, center, scale=210):
    center_x, center_y = center
    x = vertices[0, :]
    y = vertices[1, :]
    
    screen_x = center_x + x * scale
    screen_y = center_y - y * scale
    
    return np.column_stack((screen_x, screen_y))
