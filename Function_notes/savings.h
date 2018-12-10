#pragma once
#ifndef savings
#define savings
class Savings
{
public:
	Savings(unsigned accNo, float balan = 0.0);
	unsigned AccountNo();
	float AcntBalan();
	static Savings* First();
	Savings* Next();
	static int NoAccounts();
	void Display();
	void Deposit(float amount);
	void Withdrawal(float amount);
protected:
	static Savings* pFirst;
	Savings* pNext;
	static int count;
	unsigned acntNumber;
	float balance;
};

#endif