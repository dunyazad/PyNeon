#include <libNeon/Resource/Font.h>

#include <FTGL/ftgl.h>
#ifdef _DEBUG
#pragma comment(lib, "ftgl_D.lib")
#else
#pragma comment(lib, "ftgl.lib")
#endif

namespace ArtificialNature {

	Font::Font(path fontFilePath) : m_fontFilePath(fontFilePath)
	{
		m_pFTGLPixmapFont = new FTGLPixmapFont(wcs_to_mbs(m_fontFilePath).c_str());
		//m_pFTGLPixmapFont->FaceSize()
	}

	Font::~Font()
	{
		AN_DELETE(m_pFTGLPixmapFont);
	}
}