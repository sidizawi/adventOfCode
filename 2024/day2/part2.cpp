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
    int     count;

    bool	inc;
    bool    removed;
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

        inc = vec[0] < vec[1];

        i = 1;
        count++;
        removed = false;
        while (i < vec.size())
        {
			j = abs(vec[i] - vec[i - 1]);
			if ((vec[i - 1] < vec[i]) != inc || ((i + 1) < vec.size() && (vec[i] < vec[i + 1]) != inc) || !(j >= 1 && j <= 3))
			{
                std::cout << "i " << i << std::endl;
                if (removed)
                {
                    std::cout << std::endl << line << std::endl;
                    count--;
                    break ;
                }
                removed = true;
			}
            i++;
        }
        vec.clear();
    }

	std::cout << "safe reports: " << count << std::endl;

    input.close();
}
