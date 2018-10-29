#include<string>
#include<vector>
#include<algorithm>
#include<io.h>
#include<tchar.h>
#include<windows.h>
//--------------------
#include"Common.h"

using namespace std;




void ListFiles(const string dir, vector<string>&Address, vector<string>sType)
{
	//auto Suffix;
	for (auto Suffix : sType)
	{
		transform(Suffix.begin(), Suffix.end(), Suffix.begin, ::tolower);
	}
	string DirNew;
	DirNew = dir + "\\*.*";


	//----------------------------------
	//intptr_t   _findfirst _findnext  _findclose 可以用在linux上，windows也可以



	intptr_t handle;
	_finddata_t findData;      
	handle = _findfirst(DirNew.c_str(), &findData);
	if (handle == -1)
		return;
	do
	{
		if (findData.attrib&_A_SUBDIR)  //subdirectory
		{
			if (strcmp(findData.name, ".") == 0 || strcmp(findData.name, "..") == 0)
				continue;
			DirNew = dir + "\\" + findData.name;
			ListFiles(DirNew, Address, sType);
		}
		else
		{
			for (auto Suffix : sType)
			{
				if (GetSuffix(findData.name) == Suffix)   //当后缀符合时
				{
					string TempDirStr = dir + "\\" + findData.name;
					Address.push_back(TempDirStr);					
				}
			}
		}
	} while (_findnext(handle, &findData) ==0);
	_findclose(handle); //关闭搜索句柄
}


//HANDLE handle;
//WIN32_FIND_DATA findData;
//handle = FindFirstFile(DirNew.c_str(), &findData);
//if (handle == INVALID_HANDLE_VALUE)
//return;
//do
//{
//	if (findData.dwFileAttributes&)
//
//}
