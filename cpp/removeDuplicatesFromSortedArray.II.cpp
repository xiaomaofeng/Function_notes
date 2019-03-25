class Solution {
public:
	int removeDuplicates(vector<int>& nums) {
		if (nums.size() <= 2)
			return nums.size();
		int i = 0;
		int j = 1;
		bool changeFlag = 0;
		while (j < nums.size())
		{

			if (nums[i] == nums[j])
			{
				if (changeFlag == 0)
				{
					nums[++i] = nums[j];
					changeFlag = 1;
				}
				else
				{
					j++;
				}
			}
			else
			{
				nums[++i] = nums[j++];
				changeFlag = 0;
			}
		}
		return i + 1;
	}
};