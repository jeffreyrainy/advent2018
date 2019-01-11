#include <iostream>
#include <string>
#include <set>

int main()
{
    std::string line;
    char a, b;
    int x, y, z;
    int ret;

    while (std::getline(std::cin, line))
    {
        ret = std::sscanf(line.c_str(), "%c=%d, %c=%d..%d", &a, &x, &b, &y, &z);
    }
}
