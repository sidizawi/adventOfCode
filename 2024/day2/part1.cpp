#include <vector>
#include <string>
#include <ctype.h>
#include <cstdlib>
#include <fstream>
#include <iostream>

int main()
{
    size_t i;
    size_t j;
    int count;

    bool	dec;
    std::string nbr;
    std::string line;
    std::vector<int> vec;

    std::ifstream input("input.txt");

    if (!input.is_open())
    {
        std::cout << "cannot open input.txt" << std::endl;
        return (1);
    }

    count = 0;
    while (getline(input, line))
    {
		if (line.empty())
			continue ;

        i = 0;
        while (line[i])
        {
            j = i;
            while (line[i] && isdigit(line[i]))
                i++;

            if (j != i)
			{
				nbr = line.substr(j, i - j);
	            vec.push_back(atoi(nbr.c_str()));
			}
			if (line[i])
				i++;
        }

        dec = vec[0] < vec[1];

        count++;

        for (i = 1; i < vec.size(); i++)
        {
			j = abs(vec[i] - vec[i - 1]);
			if ((vec[i - 1] < vec[i]) != dec || !(j >= 1 && j <= 3))
			{
				count--;
				break ;
			}
        }

        vec.clear();
    }

	std::cout << "safe reports: " << count << std::endl;

    input.close();
}
