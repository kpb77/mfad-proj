# 3D Wireframe Viewer
## Mini Project for Mathematical Foundation for AI & Data Science (UE25MA242A)

### What?
* This is a simple and lightweight 3D Wireframe viewing tool
* Written in Python using pygame, numpy and h5py (with the help of open3d to generate matrices for 3D objects)

### Why?
* It is a simple demonstration of how 3D objects are represented mathematically in the form of matrices
* How they are projected on a 2D screen
* How they can be manipulated using rotation matrices and orthogonal projections

### How?
* Well, I would like to explain it file-by-file:
* __`math_engine.py`__: this has the core mathematical components, defines the origin and the 3 axes, rotation functionality is implemented using the functions `rx()`, `ry()`, and `rz()` which take in an angle and returns the respective rotation matrices, `project()` handles orthogonal projection which is basically converting 3D coordinates into 2D projections onto the screen, `project()` takes in vertices and the center coordinates of the screen and a scaling factor, the position of each 3D coordinate projected onto the screen is calculated by this simple formula: `screen_x = center_x + x * scale` and `screen_y = center_y - y * scale` where `x * scale` and `y * scale` handles the "zoom" or "magnification" and `center_x +` and `center_y -` handle the offsetting/shifting of the scaled coordinates wrt the center, these new set of coordinates are returned by the function for rendering onto the screen
* __`ui_engine.py`__: this has the code for the UI Button element
* __`readshapes.py` and `shapes.h5`__: `shapes.h5` uses is a file stored in the HDF5 format, which is a highly efficient way to store large data sets, in our case, we are storing the matrices (arrays in python) of the vertices and the edges of various shapes, like the cube, donut and the monkey, the cube and donut might be simple but the matrices for the monkey contains tens of thousands of individual elements which demands the usage of HDF5 for quick access and lesser resource consumption, `readshapes.py` reads `shapes.h5` and it basically extracts those matrices for the cube, donut and monkey and stores them in their respective arrays
* __`main.py`__: this is the main script used to bring all aspects together for a complete application, first of all the pygame window is being set up, the starting state of `rotation_matrix` which is an identity of order 3 is setup, a function `rotate_object()` is defined and what it does is quite simple, it calls the rotation function for the respective axis which we have defined in `math_engine.py` and cumulatively modifies `rotation_matrix` for the specific angle by multiplying the new transformation matrix with the accumulated previous one, we have a reset function which resets the `rotation_matrix` back to I₃, then we have implemented functions to autorotate, change the object and we have implemented various buttons to rotate by a certain angle in a certain axis, reset, autorotate and change shape, we have also implemented a live viewer of the rotation matrix to see how it changes for various values

### How do I test it out?
* Well, first of all this is the link to the repository: `https://github.com/kpb77/mfad-proj`
* You have to clone the repository locally using this command (you need to have Git installed): `git clone https://github.com/kpb77/mfad-proj`
* Next, navigate to the project directory: `cd mfad-proj`
* Setup a Python Virtual Environment (you need to have the Python stuff installed): `python3 -m venv venv`
* After this, activate the venv: `source venv/bin/activate`
* In the same terminal, use this command to install all the dependencies: `pip install -r requirements.txt`
* After the above steps, your terminal should look roughly like this:
  <img width="1255" height="670" alt="image" src="https://github.com/user-attachments/assets/82f5e5d1-1f5d-45d8-9c0e-fce62b6628d9" />
* Now, to run the application, in the same terminal, type: `python3 main.py`
* That's it! The application must be running by now. It would look something like this:
  <img width="1266" height="867" alt="image" src="https://github.com/user-attachments/assets/ca7946b3-6ba9-4822-a501-5132fdd354bb" />

### What all features does it have?
* The first feature we would like you to try is using the `WASD` or the `ARROW` keys to rotate the cube. You would see the cube rotating on holding the key and also the rotation matrix changing. If you prefer a step-wise increment in the rotation angles, there are 3 buttons in the `Transformation Controls` pane to do so in a 15° increment for the 3 axes, to bring it back to the original orientation, just press the `Reset` button, and to see it rotate automatically, press the `Auto Rotate` button
  <img width="1267" height="888" alt="image" src="https://github.com/user-attachments/assets/e0ffdeea-d25d-489a-bfa2-5f67ce7d9a96" />
* Next up, try changing the object! By pressing the `Object: X` button, you can toggle between 3 built-in objects: a cube, a donut and a monkey (the Blender Monkey, Suzanne) and try out the above functions on them
  <img width="1260" height="882" alt="image" src="https://github.com/user-attachments/assets/159778ed-fd74-45d7-8e92-4d95d954c7c0" />
* That's all for now!

### What can I do next?
* Well, you can try out changing the `shapes.h5` file to include the matrices for the object of your liking and modify the other respective files to accommodate them and try rendering them out.
