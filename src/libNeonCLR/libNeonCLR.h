// libNeonCLR.h

#pragma once

#include <libNeon/libNeon.h>
#pragma comment(lib, "libNeon.lib")

using namespace System;
using namespace System::Drawing;
using namespace System::Windows::Forms;

namespace ArtificialNature {

	public ref class NeonCLR
	{
	public:
		NeonCLR();
		~NeonCLR();
		!NeonCLR();

		void Setup(System::IntPtr hWnd, int width, int height);
		void Resize(int width, int height);
		int Frame();

	private:
		Neon* m_pNative = nullptr;
	};
}

namespace ArtificialNature {
	public ref class UserControl_NeonCLR : UserControl
	{
	public:
		void OnLoad(EventArgs^ e) override;
		void OnTick(System::Object ^sender, System::EventArgs ^e);
		virtual void OnPaint(PaintEventArgs^ e) override;
		virtual void OnPaintBackground(PaintEventArgs^ e) override;
		virtual void OnSizeChanged(EventArgs^ e) override;

	private:
		NeonCLR^ neon = gcnew NeonCLR();
		Timer^ renderingTimer = gcnew Timer();
	};
}
