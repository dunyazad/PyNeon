// This is the main DLL file.

#include "stdafx.h"

#include "libNeonCLR.h"

namespace ArtificialNature {

	NeonCLR::NeonCLR()
	{
		m_pNative = new Neon();
	}

	NeonCLR::~NeonCLR()
	{
		AN_DELETE(m_pNative);
	}

	NeonCLR::!NeonCLR()
	{
		AN_DELETE(m_pNative);
	}

	void NeonCLR::Setup(System::IntPtr hWnd, int width, int height)
	{
		m_pNative->Setup((HWND)hWnd.ToPointer(), width, height);
	}

	void NeonCLR::Resize(int width, int height)
	{
		m_pNative->Resize(width, height);
	}

	int NeonCLR::Frame()
	{
		return m_pNative->Frame();
	}

}

namespace ArtificialNature {

	void UserControl_NeonCLR::OnLoad(EventArgs^ e)
	{
		this->Dock = DockStyle::Fill;

		this->SetStyle(ControlStyles::OptimizedDoubleBuffer, true);

		if (!this->DesignMode)
		{
			this->neon->Setup(this->Handle, this->Width, this->Height);

			renderingTimer->Tick += gcnew System::EventHandler(this, &UserControl_NeonCLR::OnTick);
			renderingTimer->Interval = 1;
			renderingTimer->Start();
		}
	}

	void UserControl_NeonCLR::OnTick(System::Object ^sender, System::EventArgs ^e)
	{
		if (!this->DesignMode)
		{
			this->neon->Frame();
		}
	}

	void UserControl_NeonCLR::OnPaint(PaintEventArgs^ e)
	{
		if (!this->DesignMode)
		{
			this->neon->Frame();
		}
	}

	void UserControl_NeonCLR::OnPaintBackground(PaintEventArgs^ e)
	{
		// not doing anything here avoids flicker
	}

	void UserControl_NeonCLR::OnSizeChanged(EventArgs^ e)
	{
		if (!this->DesignMode)
		{
			this->neon->Resize(this->Width, this->Height);
		}
	}
}
