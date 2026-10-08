import h5py
import numpy

def load_shapes():
    global cedges, cverts, dedges, dverts, medges, mverts
    with h5py.File("shapes.h5", "r") as f:
        f = f["shapes"]
        cube = f["cube"]
        donut = f["donut"]
        monkey = f["monkey"]
        cverts, cedges = cube["vertices"][:], cube["edges"][:]
        dverts, dedges = donut["vertices"][:], donut["edges"][:]
        mverts, medges = monkey["vertices"][:], monkey["edges"][:]

        shapes = [(cverts, cedges), (dverts, dedges), (mverts, medges)]
        return shapes
