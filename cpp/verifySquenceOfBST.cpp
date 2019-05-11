class Solution {
public:
	bool verifySequenceOfBST(int sequence[])
	{
		int length = sizeof(sequence) / sizeof(int);
		if (length == 0)
		{
			return false;
		}
		return isResult(sequence, 0, length - 1);
	}
	bool isResult(int sequence[], int start, int end)
	{
		if (end <= start)
			return true;
		int i = start;
		for (; i < end; i++)
		{
			if (sequence[i] > sequence[end])
				break;
		}
		int j = i;
		for (; j < end; j++)
		{
			if (sequence[j] < sequence[end])
				return false;
		}
		return isResult(sequence, start, i - 1) && isResult(sequence, i, end - 1);

	}
};

