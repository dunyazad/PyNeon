#pragma once

#include <iostream>
#include <string>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <vector>

#include <algorithm>
#include <chrono>
#ifndef _M_CEE
#include <thread>
#endif
using namespace std;

#include <Windows.h>
#ifdef _M_CEE
#pragma comment(lib, "user32.lib")
#pragma comment(lib, "Gdi32.lib")
#endif

#include <GL/glew.h>
#ifdef _DEBUG
#pragma comment(lib, "glew/glew32d.lib")
#else
#pragma comment(lib, "glew/glew32.lib")
#endif

#ifndef _M_CEE
#include <gl/gl.h>
#include <gl/glu.h>

#pragma comment(lib, "opengl32.lib")
#pragma comment(lib, "glu32.lib")

#include <glm/glm.hpp>

#include <FTGL/ftgl.h>
#ifdef _DEBUG
#pragma comment(lib, "ftgl_D.lib")
#else
#pragma comment(lib, "ftgl.lib")
#endif
#endif

typedef unsigned char byte;






#define AN_DELETE(x) if(nullptr != x) { delete x; x = nullptr; }