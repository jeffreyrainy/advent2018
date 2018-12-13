#include <iostream>
#include <fstream>
#include <cassert>
#include <deque>

const int bitspervalue = 10;

int transitions[32] = {0};

std::deque<int> code(std::string input)
{
    std::deque<int> ret;
    int v = 0;

    for (int i = 0; i < input.size(); i++)
    {
        v = v * 2;
        v = v + ((input[i] == '#') ? 1 : 0);
        if (i % bitspervalue == (bitspervalue - 1))
        {
            ret.push_back(v);
            v = 0;
        }
    }

    return ret;
}
void addRule(std::string mask, int output)
{
    int v = 0;
    for (int i = 0; i < 5; i++)
    {
        v = v * 2;
        v = v + ((mask[i] == '#') ? 1 : 0);
    }
    transitions[v] = output;
}

void apply(std::deque<int> in)
{
    std::deque<int> out = std::deque<int>(in.size());
};

int main()
{
    std::ifstream infile("inputs/input12.txt");
    std::string input, rule;

    std::getline(infile, input);
    assert(input.substr(0, 15) == "initial state: ");

    while (std::getline(infile, rule))
    {
        if (rule.size())
        {
            std::string mask = rule.substr(0, 5);
            int result = (rule[9] == '.' ? 0 : 1);

            addRule(mask, result);

            std::cout << mask << " " << result << std::endl;
        }
    }

    input = input.substr(15);
    std::cout << input << std::endl;

    auto values = code(input);

    apply(values);

    return 0;
}