#include <libNeon/libNeon.h>
#include <libNeon/GraphicsDevice.h>

namespace ArtificialNature {

	Neon::Neon()
	{
	}

	Neon::~Neon()
	{
		ResourceCache::Terminate();
	}

	//FTGLPixmapFont font("C:\\Windows\\Fonts\\gulim.ttc");
	void Neon::Setup(HWND hWnd, int width, int height)
	{
		m_pGraphicsDevice = new GraphicsDevice(hWnd, width, height);
		this->Resize(width, height);




		Font* pFont = ResourceCache::GetPixmapFont("C:\\Windows\\Fonts\\gulim.ttc");
		pFont->SetFaceSize(12);


		//if (p1.compare(p2))
		//	cout << "OK" << endl;
		//else
		//	cout << "No" << endl;
		
	}

	void Neon::Resize(int width, int height)
	{
		if(m_pGraphicsDevice) m_pGraphicsDevice->Resize(width, height);
	}

	float m_fRotationAngle = 0.0f;
	int Neon::Frame()
	{
		if (!m_pGraphicsDevice) return 0;

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




		Font* pFont = ResourceCache::GetPixmapFont("C:\\Windows\\Fonts\\gulim.ttc");
		wstringstream wss;
		wss << L"한글 입력, " << m_fRotationAngle;

		if (pFont)
		{
			//pFont->Render(L"한글 입력", -1, 100, 100);
			pFont->Render(wss.str(), -1, 100, 100);
		}
		




		m_pGraphicsDevice->Present();

		m_fRotationAngle += 1.0f;

		return 16;
	}
}
