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
		m_pFTGLPixmapFont->FaceSize(72);
	}

	Font::~Font()
	{
		AN_DELETE(m_pFTGLPixmapFont);
	}

	void Font::SetFaceSize(int faceSize)
	{
		m_pFTGLPixmapFont->FaceSize(faceSize);
	}

	void Font::Render(const std::wstring& text, int length,
		int positionX, int positionY,
		int spacingX, int spacingY,
		int renderMode)
	{
		m_pFTGLPixmapFont->Render(text.c_str(), length, FTPoint(positionX, positionY), FTPoint(spacingX, spacingY), renderMode);
	}
}