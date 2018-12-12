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
	string tempFilePath;
	vector<string>tempString;
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
						bool firstInput = srcCSVs.size() == 0;
						if (firstInput)
						{
							srcCSVs.push_back(szFilePath);
							continue;
						}
						bool bifSameFlag = false;
						for (int k = 0; k < srcCSVs.size(); k++)
						{
							size_t tempPos;
							tempFilePath = srcCSVs[k];
							tempPos = tempFilePath.find_last_of('\\') + 1;
							string tempFileName = tempFilePath.substr(tempPos);
							tempString.push_back(tempFileName);
							
						}
						if (!firstInput)
						{
							for (int j = 0; j < srcCSVs.size(); j++)
							{
								if (ff.cFileName == tempString[j])
								{
									bifSameFlag = true;
									break;
								}
							}
							if (!bifSameFlag)
							{
								srcCSVs.push_back(szFilePath);
							}
							else
							{
								continue;
							}
						}
					}
				}
			}
		} while (FindNextFile(curFile, &ff));
		//FindNextFile(curFile, &ff));
		FindClose(curFile);
	}
	return;

}

void ExtractFileName(vector<string>&srcCSVs, vector<string>&tempAtlasName)
{
	string atlasName;
	string filePath;
	string fileName;
	size_t tempPos;
	size_t pointPos;
	for (int i = 0; i < srcCSVs.size(); i++)
	{
		filePath = srcCSVs[i];
		tempPos = filePath.find_last_of('\\') + 1;
		fileName = filePath.substr(tempPos);
		pointPos = fileName.find_first_of('.csv') - 3;
		atlasName = fileName.substr(0, pointPos);
		tempAtlasName.push_back(atlasName);
	}
}
void SynchronizeFilesCount(vector<string>&srcCSVs, vector<string>&tempSrcCSVs)
{
	vector<string>tempAtlasName;
	vector<string>AtlasName;
	vector<string>srcCSVsCopy;
	srcCSVsCopy = srcCSVs;
	ExtractFileName(srcCSVs, tempAtlasName);
	ExtractFileName(tempSrcCSVs, AtlasName);
	for (int j = 0; j < srcCSVs.size(); j++)
	{
		for (int k = 0; k < AtlasName.size(); k++)
		{
			bool sameFileNameFlag = false;
			if (tempAtlasName[j] == AtlasName[k])
			{
				sameFileNameFlag = true;
				srcCSVsCopy.push_back(tempSrcCSVs[k]);
				break;
			}
			if (!sameFileNameFlag)
			{
				continue;
			}
		}
	}
	srcCSVs = srcCSVsCopy;

}



