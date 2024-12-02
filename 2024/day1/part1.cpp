#include <vector>
#include <string>
#include <ctype.h>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <algorithm>

int main()
{
	int	i;
	int	j;
	int	len;

	std::string line;
	std::string last;
	std::string first;
	std::vector<int> lst1;
	std::vector<int> lst2;

	std::ifstream input("input.txt");

	if (!input.is_open())
	{
		std::cout << "cannot open input.txt" << std::endl;
		return (1);
	}

	len = 0;
	while (getline(input, line))
	{
		i = 0;
		while (line[i] && isdigit(line[i]))
			i++;
		
		first = line.substr(0, i);

		while (line[i] && !isdigit(line[i]))
			i++;

		last = line.substr(i);

		lst1.push_back(atoi(first.c_str()));
		lst2.push_back(atoi(last.c_str()));

		len++;
	}

	std::sort(lst1.begin(), lst1.end());
	std::sort(lst2.begin(), lst2.end());

	i = 0;
	j = 0;
	while (i < len)
	{
		j += abs(lst1[i] - lst2[i]);
		i++;
	}

	std::cout << "total distance = " << j << std::endl;

	input.close();
}
