#pragma once
#include<string>
#include<vector>
using namespace std;
std::string GetSuffix(std::string Name);
void GetAllCsvFileFromPath(const string& srcPath, vector<string>& srcCSVs, string Version, bool recursive = true);