#include <map>
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

	std::string line;
	std::string last;
	std::string first;
	std::vector<int> lst1;
	std::vector<int> lst2;
	std::map<int, int> count;

	std::vector<int>::iterator vit;
	std::map<int, int>::iterator it;

	std::ifstream input("input.txt");

	if (!input.is_open())
	{
		std::cout << "cannot open input.txt" << std::endl;
		return (1);
	}

	while (getline(input, line))
	{
		i = 0;
		while (line[i] && isdigit(line[i]))
			i++;
		
		first = line.substr(0, i);

		while (line[i] && !isdigit(line[i]))
			i++;

		j = i;
		while (line[i] && isdigit(line[i]))
			i++;
		
		last = line.substr(j, i - j);

		lst1.push_back(atoi(first.c_str()));
		lst2.push_back(atoi(last.c_str()));

		it = count.find(lst2.back());

		if (it == count.end())
			count[lst2.back()] = 1;
		else
			count[it->first]++;
	}

	i = 0;

	vit = lst1.begin();
	while (vit != lst1.end())
	{
		it = count.find(*vit);

		if (it != count.end())
			i += *vit * it->second;

		vit++;
	}

	std::cout << "similarity score = " << i << std::endl;

	input.close();
}
