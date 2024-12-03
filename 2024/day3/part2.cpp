#include <string>
#include <ctype.h>
#include <cstdlib>
#include <fstream>
#include <iostream>

int main()
{
    int a;
    int b;
    int count;

    size_t  i;
    size_t  j;

    bool enable;

    std::string     nbr;
    std::string     line;
    std::ifstream   input("input.txt");

    if (!input.is_open())
    {
        std::cerr << "cannot open input.txt" << std::endl;
        return (1);
    }

    count = 0;
    enable = true;
    while (getline(input, line))
    {
        i = 0;
        while (i < line.length())
        {
            if (line.substr(i, 4) == "mul(" && enable)
            {
                i += 4;
                if (!isdigit(line[i]))
                    continue ;
                j = i;
                while (line[i] && isdigit(line[i]))
                    i++;
                if (i - j <= 3 && i != j)
                {
                    nbr = line.substr(j, i - j);
                    a = atoi(nbr.c_str());
                }
                else
                    continue ;
                if (line[i] == ',')
                    i++;
                else
                    continue ;
                j = i;
                if (!isdigit(line[i]))
                    continue ;
                while (line[i] && isdigit(line[i]))
                    i++;
                if (line[i] != ')')
                    continue ;
                if (i - j <= 3 && i != j)
                {
                    nbr = line.substr(j, i - j);
                    b = atoi(nbr.c_str());
                }
                else
                    continue ;
                count += a * b;
            }
            else if (line.substr(i, 4) == "do()")
            {
                i += 4;
                enable = true;
            }
            else if (line.substr(i, 7) == "don't()")
            {
                i += 7;
                enable = false;
            }
            else if (line[i])
                i++;
        }
    }

    std::cout << "count: " << count << std::endl;

    input.close();
}

// too low: 83493183
// too high: 86865767
// mul\([0-9]{1,3},[0-9]{1,3}\)     717     710
// do\(\)                           27      27
// don't\(\)                        38      38
