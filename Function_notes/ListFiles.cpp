#include<string>
#include<vector>
#include<algorithm>
#include<io.h>
#include<tchar.h>
#include<windows.h>
#include<iostream>
#include"Common.h"

//--------------------

using namespace std;




void ListFiles(const string dir, vector<string>&Address, vector<string>sType)
{
	//auto Suffix;
	for (auto Suffix : sType)
	{
		transform(Suffix.begin(), Suffix.end(), Suffix.begin(), ::tolower);
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
		if (findData.attrib & _A_SUBDIR)  //subdirectory
		{
			if (strcmp(findData.name, ".") == 0 || strcmp(findData.name, "..") == 0) //directory
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



void WinListFile(const string Dir, vector<string>Address, vector<string>stype)
{
	HANDLE handle;
	WIN32_FIND_DATA findData;
	string dirNew;
	handle = FindFirstFile(Dir.c_str(), &findData);

	for (string Suffix : stype)
	{
		transform(Suffix.begin(), Suffix.end(), Suffix.begin(), ::tolower);//transform CASE and case
	}

	//----------------------------------------
	//for example
	/*
	int nmatrix[10] = { 1,2,3,4,5,6,7,8,9,10 };   //In this example,the variable item holds the current value from the numbers array.
	for (int a : nmatrix)
	{
		cout << "Count is:" << a << endl;
	}
	*/

	dirNew = Dir + "\\*.*";

	if (handle == INVALID_HANDLE_VALUE)
		return;
	do
	{
		bool bDirectory = (findData.dwFileAttributes&FILE_ATTRIBUTE_DIRECTORY) == FILE_ATTRIBUTE_DIRECTORY;
		if (bDirectory)
		{
			if (strcmp(findData.cFileName, ".") == 0 || strcmp(findData.cFileName, "..") == 0)
				continue;
			dirNew = Dir + "\\" + findData.cFileName;
			WinListFile(Dir, Address, stype);
		}
		else
		{
			for (string Suffix : stype)
			{
				if (GetSuffix(findData.cFileName) == Suffix)
				{
					string TempDirStr = Dir + "\\" + findData.cFileName;
					Address.push_back(TempDirStr);
				}
			}
		}

	} while (FindNextFile(handle, &findData));
	FindClose(handle);
}