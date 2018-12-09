git submodule update --init --recursive
mkdir perception/apriltag
cd perception/apriltag
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j4
cd ../../..
touch perception/apriltag/__init__.py #to allow top-level imports
touch perception/apriltag/python/__init__.py

