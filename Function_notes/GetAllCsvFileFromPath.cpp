#include<string>
#include<io.h>
#include<vector>
#include<iostream>
#include<fstream>
#include<tchar.h>
#include<sstream>
#include<windows.h>

using namespace std;








void GetAllCsvFileFromPath(const string& srcPath, vector<string>& srcCSVs, string Version, bool recursive = true)
{
	TCHAR szSearchPath[_MAX_PATH] = { 0 };
	wsprintf(szSearchPath, "%s\\*.*", srcPath.c_str());
	//wsprintf c_str
	WIN32_FIND_DATA ff;
	//printf("%s", szSearchPath);
	HANDLE curFile = FindFirstFile(szSearchPath, &ff);
	if (curFile != INVALID_HANDLE_VALUE)
	{
		do
		{
			BOOL bDirectory = ((ff.dwFileAttributes&FILE_ATTRIBUTE_DIRECTORY) == FILE_ATTRIBUTE_DIRECTORY);//directory of file																									
			if (bDirectory)
			{
				if (_tcsstr(_T(".."), ff.cFileName))//exit ".." in filename
													//if (_tcsstr(_T(".."), ff.cFileName))//exit ".." in filename
				{
					continue;
				}
				else//if not,continue
				{
					if (recursive)//if recursive
					{
						string tmppath = srcPath + ff.cFileName + "\\";
						GetAllCsvFileFromPath(tmppath, srcCSVs, Version, recursive);
					}
					else
						continue;
				}

			}
			else//if file
			{
				TCHAR szFilePath[MAX_PATH] = { 0 };
				string tmpext = ff.cFileName;
				int iVersionStringLength_1 = Version.length();
				size_t pos = tmpext.find_last_of('.');//find index of the last '.'
				if (((int)pos - iVersionStringLength_1 - 1) < 0)
				{
					continue;
				}





				string tempPos = tmpext.substr(pos - iVersionStringLength_1 - 1);
				if (pos != string::npos)
					//if(pos!=string::npos)
				{
					tmpext = tmpext.substr(pos);
					for (int i = 0; i < tmpext.length(); ++i)
					{
						tmpext[i] = tolower(tmpext[i]);
					}
					if (tempPos == (Version + "_.csv"))//image or not
					{
						wsprintf(szFilePath, "%s%s", srcPath.c_str(), ff.cFileName);
						srcCSVs.push_back(szFilePath);//add to vector
					}
				}
			}
		} while (FindNextFile(curFile, &ff));
		//FindNextFile(curFile, &ff));
		FindClose(curFile);
	}
	return;

}