#include <string>
#include <fstream>
#include <iostream>

using namespace std;

int main()
{
    int x;
    char c;
    int n = 50;
    string line;
    int code = 0;
    
    ifstream file("input.txt");
    
    while (getline(file, line))
    {
        c = line[0];
        x = stoi(line.substr(1));
        if (c == 'R')
        {
            code += (n + x) / 100;
            n = (n + x) % 100;
        }
        else
        {
            code += ((n - x) / 100) * (n < x ? -1 : 1);
            n = (n - x) % 100;
            n = n < 0 ? 100 + n : n;
        }
        code += n == 0;
    }

    cout << "code : " << code << '\n';

    file.close();
}