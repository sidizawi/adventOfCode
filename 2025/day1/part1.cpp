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
        if (c == 'R') n += x;
        else n -= x;

        

        code += n == 0;
    }

    cout << "code : " << code << '\n';

    file.close();
}