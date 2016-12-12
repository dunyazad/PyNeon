#include <libNeon/libNeon.h>
#include <libNeon/GraphicsDevice.h>

namespace ArtificialNature {

	Neon::Neon()
	{
	}

	Neon::~Neon()
	{
	}

	FTGLPixmapFont font("C:\\Windows\\Fonts\\gulim.ttc");
	void Neon::Setup(HWND hWnd, int width, int height)
	{
		m_pGraphicsDevice = new GraphicsDevice(hWnd, width, height);
		this->Resize(width, height);






		
	}

	void Neon::Resize(int width, int height)
	{
		if(m_pGraphicsDevice) m_pGraphicsDevice->Resize(width, height);
	}

	float m_fRotationAngle = 0.0f;
	int Neon::Frame()
	{
		if (!m_pGraphicsDevice) return 0;

		cout << "Frame()" << endl;

		m_pGraphicsDevice->Clear();

		//for (auto& kvp : m_sceneMap)
		//{
		//	if (kvp.second)
		//	{
		//		kvp.second->Render(pGraphicsDevice);
		//	}
		//}

		glMatrixMode(GL_PROJECTION);
		glLoadIdentity();
		glOrtho(-1.0, 1.0, -1.0, 1.0, 1.0, 100.0);
		// gluPerspective( 67.5, ((double)(iWidth) / (double)(iHeight)), 1.0, 500.0);
		glMatrixMode(GL_MODELVIEW);
		glLoadIdentity();

		glTranslatef(0.0f, 0.0f, -2.6f);
		glRotatef(m_fRotationAngle, 0.0f, 1.0f, 0.0f);

		glBegin(GL_TRIANGLES);
		glColor3f(1.0f, 0.0f, 0.0f);	glVertex3f(-1.0f, -1.0f, 0.0f);
		glColor3f(0.0f, 1.0f, 0.0f);	glVertex3f( 0.0f,  1.0f, 0.0f);
		glColor3f(0.0f, 0.0f, 1.0f);	glVertex3f( 1.0f, -1.0f, 0.0f);
		glEnd();





		// Create a pixmap font from a TrueType file.


		// If something went wrong, bail out.
		if (font.Error())
			return 16;

		// Set the font size and render a small text.
		font.FaceSize(72);
		font.Render(L"한글 입력", -1, FTPoint(100, 100));






		glFlush();

		m_pGraphicsDevice->Present();

		m_fRotationAngle += 1.0f;

		return 16;
	}
}
