#include <libNeon/Resource/ResourceCache.h>

namespace ArtificialNature {

	ResourceCache* ResourceCache::s_pInstance = new ResourceCache();
	wstring ResourceCache::s_resourceRootPath = L"../../../res";
	map<path, Font*> ResourceCache::s_fontCache;

	ResourceCache::ResourceCache()
	{
	}

	ResourceCache::~ResourceCache()
	{
	}

	void ResourceCache::Terminate()
	{
		for (auto& kvp : s_fontCache)
		{
			AN_DELETE(kvp.second);
		}
	}

	Font * ResourceCache::GetPixmapFont(path filePath)
	{
		auto canonical = std::tr2::sys::canonical(filePath);
		auto i = s_fontCache.find(canonical);
		if (i == s_fontCache.end()) {
			auto pFont = new Font(filePath);
			s_fontCache[canonical] = pFont;
			return pFont;
		}
		else {
			return (*i).second;
		}
	}

}
