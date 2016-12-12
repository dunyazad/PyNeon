#pragma once

#include <libNeon/libNeonCommon.h>

namespace ArtificialNature {

	class GraphicsDevice
	{
	public:
		GraphicsDevice(HWND hWnd, int width, int height);
		~GraphicsDevice();

		HRESULT Initialize(HWND hWnd, int width, int height);
		void Terminate();

		void Clear(float r = 0.0f, float g = 0.125f, float b = 0.3f, float a = 1.0f);
		void Present();

		void Resize(int width, int height);

	private:
		HWND	m_hWnd;
		HDC		m_hDC;
		HGLRC	m_hRC;

		int m_width;
		int m_height;
	};

}