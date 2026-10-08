import numpy as np

axes = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]]).T

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

def project(vertices, center, scale=300):
    center_x, center_y = center
    x = vertices[0, :]
    y = vertices[1, :]
    
    screen_x = center_x + x * scale
    screen_y = center_y - y * scale
    
    return np.column_stack((screen_x, screen_y))
