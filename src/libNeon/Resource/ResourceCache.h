#pragma once

#include <libNeon/libNeonCommon.h>
#include <libNeon/Resource/Font.h>

namespace ArtificialNature {

	class ResourceCache
	{
	public:
		static void Terminate();
		static Font* GetPixmapFont(path filePath);

	private:
		static ResourceCache* s_pInstance;
		ResourceCache();
		~ResourceCache();
		
		static wstring s_resourceRootPath;

		static map<path, Font*> s_fontCache;
	};

}
