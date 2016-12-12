#include <libNeon/libNeonCommon.h>

std::string wcs_to_mbs(const std::wstring& wstr)
{
	const wchar_t *str = wstr.c_str();
	char mbs[1024] = { 0 };
	mbstate_t shiftState = mbstate_t();
	setlocale(LC_ALL, "");
	wcsrtombs(mbs, &str, sizeof(mbs), &shiftState);
	return mbs;
}

std::wstring mbs_to_wcs(const std::string& astr)
{
	const char *str = astr.c_str();
	wchar_t wcs[1024] = { 0 };
	mbstate_t shiftState = mbstate_t();
	setlocale(LC_ALL, "");
	mbsrtowcs(wcs, &str, sizeof(wcs), &shiftState);
	return wcs;
}

std::wstring mbs_to_wcs2(std::string const& str, std::locale const& loc)
{
	typedef std::codecvt<wchar_t, char, std::mbstate_t> codecvt_t;
	codecvt_t const& codecvt = std::use_facet<codecvt_t>(loc);
	std::mbstate_t state = std::mbstate_t();
	std::vector<wchar_t> buf(str.size() + 1);
	char const* in_next = str.c_str();
	wchar_t* out_next = &buf[0];
	std::codecvt_base::result r = codecvt.in(state,
		str.c_str(), str.c_str() + str.size(), in_next,
		&buf[0], &buf[0] + buf.size(), out_next);
	if (r == std::codecvt_base::error)
		throw std::runtime_error("can't convert string to wstring");
	return std::wstring(&buf[0]);
}

std::string wcs_to_mbs2(std::wstring const& str, std::locale const& loc)
{
	typedef std::codecvt<wchar_t, char, std::mbstate_t> codecvt_t;
	codecvt_t const& codecvt = std::use_facet<codecvt_t>(loc);
	std::mbstate_t state = std::mbstate_t();
	std::vector<char> buf((str.size() + 1) * codecvt.max_length());
	wchar_t const* in_next = str.c_str();
	char* out_next = &buf[0];
	std::codecvt_base::result r = codecvt.out(state,
		str.c_str(), str.c_str() + str.size(), in_next,
		&buf[0], &buf[0] + buf.size(), out_next);
	if (r == std::codecvt_base::error)
		throw std::runtime_error("can't convert wstring to string");
	return std::string(&buf[0]);
}