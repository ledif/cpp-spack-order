all:
	$(CXX) -std=c++11 -I./extern/include -I ./tools/libstdc++/4.9.3/  main.cpp -o main
