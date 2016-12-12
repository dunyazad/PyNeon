#pragma once

#pragma warning(disable: 4819)

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

#include <filesystem>
using namespace std::tr2::sys;

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
#endif

typedef unsigned char byte;







std::string wcs_to_mbs(const std::wstring& wstr);
std::wstring mbs_to_wcs(const std::string& astr);
std::wstring mbs_to_wcs2(std::string const& str, std::locale const& loc = std::locale());
std::string wcs_to_mbs2(std::wstring const& str, std::locale const& loc = std::locale());




#define AN_DELETE(x) if(nullptr != x) { delete x; x = nullptr; }
