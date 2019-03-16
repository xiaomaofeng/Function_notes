#pragma once
#ifndef TABTENN1_H_
#define TABTENN1_H_
#include <string>
using std::string
//simple base class
class TableTennisPlalyer
{
private:
	string firstname;
	string lastname;
	bool hasTable;
public:
	TableTennisPlalyer(const string & fn = "none", const string & ln = "none", bool ht = false);
	void Name() const;
	bool HasTable() const { return hasTable }
	void ResetTable{ bool v } {hasTable = v; };
};

//simple derived class
class RatedPlayer :public TableTennisPlalyer
{
private:
	unsigned int rating;
public:
	RatedPlayer(unsigned int r = 0, const string & fn = "none", const string & ln = "none", bool ht = false);
	RatedPlayer(unsighed int r, const TableTennisPlayer & tp);
	unsighed int Rating() const { return rating; }
	void ResetRating(unsigned int r) { rating = r; }
};
#endif




