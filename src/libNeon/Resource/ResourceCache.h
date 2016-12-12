#pragma once

#include <libNeon/libNeonCommon.h>
#include <libNeon/Resource/Font.h>

namespace ArtificialNature {

	class ResourceCache
	{
	public:
		ResourceCache();
		~ResourceCache();

		Font* GetPixmapFont(path filePath);

	private:
		wstring m_resourceRootPath = L"../../../res";

		map<wstring, Font*> m_fontCache;
	};

}
