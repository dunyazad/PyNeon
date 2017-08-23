#pragma once

#include <libNeon/libNeonCommon.h>
#include <libNeon/Resource/ResourceCache.h>
#include <libNeon/Scene/Scene.h>

namespace ArtificialNature {

	class GraphicsDevice;

	class Neon
	{
	public:
		Neon();
		~Neon();

		void Setup(HWND hWnd, int width, int height);
		void Resize(int width, int height);
		int Frame();

	private:
		GraphicsDevice* m_pGraphicsDevice = nullptr;


	};

}