#pragma once

#include <libNeon/libNeonCommon.h>

class FTPixmapFont;

namespace ArtificialNature {

	class Font
	{
	public:
		Font(path fontFilePath);
		~Font();

		enum RenderMode
		{
			RENDER_FRONT = 0x0001,
			RENDER_BACK = 0x0002,
			RENDER_SIDE = 0x0004,
			RENDER_ALL = 0xffff
		};

		void SetFaceSize(int faceSize);
		void Render(const std::wstring& text, int length = -1,
			int positionX = 0, int positionY = 0,
			int spacingX = 0, int spacingY = 0,
			int renderMode = RenderMode::RENDER_ALL);
	private:
		path m_fontFilePath;
		FTPixmapFont* m_pFTGLPixmapFont = nullptr;
		int m_size = -1;
	};

}
