#include <string>
#include <vector>
#include <ctype.h>
#include <cstdlib>
#include <fstream>
#include <iostream>

int main()
{
	size_t	i;
	size_t	j;
	size_t	k;
	size_t	m;
	int		l;
	int		c1;
	int		c2;
	int		c3;
	int		count;

	std::string	line;
	std::vector<std::string> words;
	
	std::ifstream input("input.txt");

	if (!input.is_open())
	{
		std::cerr << "cannot open input.txt" << std::endl;
		return (1);
	}

	while (getline(input, line))
		words.push_back(line);

	i = 0;
	count = 0;
	while (i < words.size())
	{
		j = 0;
		while (j < words[i].length())
		{
			if (words[i][j] == 'X')
			{
				if (words[i].substr(j, 4) == "XMAS" || (j > 2 && words[i].substr(j - 3, 4) == "SAMX"))
				{
					count++;
				}
				if (i > 3)
				{
					c1 = c2 = c3 = 0;
					k = i;
					l = j;
					m = j;
					while (k > i - 4)
					{
						if (words[k][j] == "XMAS"[i - k])
							c1++;
						if (l >= 0 && words[k][l] == "XMAS"[i - k])
							c2++;
						if (m < words[k].length() && words[k][m] == "XMAS"[i - k])
							c3++;
						l--;
						m++;
						k--;
					}
					count += (c1 == 4) + (c2 == 4) + (c3 == 4);
				}
				if (i + 3 < words.size())
				{
					c1 = c2 = c3 = 0;
					k = i;
					l = j;
					m = j;
					while (k < i + 4)
					{
						if (words[k][j] == "XMAS"[k - i])
							c1++;
						if (l >= 0 && words[k][l] == "XMAS"[k - i])
							c2++;
						if (m < words[k].length() && words[k][m] == "XMAS"[k - i])
							c3++;
						l--;
						m++;
						k++;
					}
					count += (c1 == 4) + (c2 == 4) + (c3 == 4);
				}
			}
			j++;
		}
		i++;
	}

	std::cout << "count: " << count << std::endl;

	input.close();

}

// 4435 too high
// 2503 too low
