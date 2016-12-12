#pragma once

#include <libNeon/libNeonCommon.h>

class FTPixmapFont;

namespace ArtificialNature {

	class Font
	{
	public:
		Font(path fontFilePath);
		~Font();



	private:
		path m_fontFilePath;
		FTPixmapFont* m_pFTGLPixmapFont = nullptr;
		int m_size = -1;
	};

}