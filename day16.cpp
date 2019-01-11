#include <iostream>
#include <string>
#include <set>

void apply(int op, const int input[4], const int command[4], int output[4])
{
    for (int i = 0; i < 4; i++)
    {
        output[i] = input[i];
    }

    switch (op)
    {
    case 0:
        // addr (add register) stores into register C the result of adding register A and register B.
        output[command[3]] = input[command[1]] + input[command[2]];
        break;
    case 1:
        // addi (add immediate) stores into register C the result of adding register A and value B.
        output[command[3]] = input[command[1]] + command[2];
        break;
    case 2:
        // mulr (multiply register) stores into register C the result of multiplying register A and register B.
        output[command[3]] = input[command[1]] * input[command[2]];
        break;
    case 3:
        // muli (multiply immediate) stores into register C the result of multiplying register A and value B.
        output[command[3]] = input[command[1]] * command[2];
        break;
    case 4:
        // banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
        output[command[3]] = input[command[1]] & input[command[2]];
        break;
    case 5:
        // bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
        output[command[3]] = input[command[1]] & command[2];
        break;
    case 6:
        // borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
        output[command[3]] = input[command[1]] | input[command[2]];
        break;
    case 7:
        // bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
        output[command[3]] = input[command[1]] | command[2];
        break;
    case 8:
        // setr (set register) copies the contents of register A into register C. (Input B is ignored.)
        output[command[3]] = input[command[1]];
        break;
    case 9:
        // seti (set immediate) stores value A into register C. (Input B is ignored.)
        output[command[3]] = command[1];
        break;
    case 10:
        //gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
        output[command[3]] = (command[1] > input[command[2]]) ? 1 : 0;
        break;
    case 11:
        //gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
        output[command[3]] = (input[command[1]] > command[2]) ? 1 : 0;
        break;
    case 12:
        //gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
        output[command[3]] = (input[command[1]] > input[command[2]]) ? 1 : 0;
        break;
    case 13:
        //eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
        output[command[3]] = (command[1] == input[command[2]]) ? 1 : 0;
        break;
    case 14:
        //eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
        output[command[3]] = (input[command[1]] == command[2]) ? 1 : 0;
        break;
    case 15:
        //eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
        output[command[3]] = (input[command[1]] == input[command[2]]) ? 1 : 0;
        break;
    }
}

std::ostream &operator<<(std::ostream &out, int array[4])
{
    for (int i = 0; i < 4; i++)
    {
        out << array[i] << " ";
    }
    return out;
}

int check(const int a[4], const int b[4])
{
    for (int i = 0; i < 4; i++)
    {
        if (a[i] != b[i])
        {
            return false;
        }
    }
    return true;
}

void findMappings(int mappings[16], std::set<int> poss[16])
{
    bool again = true;

    // as long as we can find a new mapping
    while (again)
    {
        again = false;
        // for all opcodes
        for (int i = 0; i < 16; i++)
        {
            // if we're down to just one possibility
            if (poss[i].size() == 1)
            {
                // mark it as the right one, remeber to continue, and remove the opcode as a possibility for all mappings (us included, so we don't process it again)
                again = true;
                int op = *poss[i].begin();
                mappings[i] = op;

                for (int j = 0; j < 16; j++)
                {
                    poss[j].erase(op);
                }
            }
        }
    }

    // todo: we could check that we added 16 mappings...
}

int main()
{
    std::string line;
    int samples = 0;
    int registers[4] = {0, 0, 0, 0};
    std::set<int> poss[16]; // the various possible mapping for each op
    bool mappingsReady = false;

    for (int i = 0; i < 16; i++)
    {
        for (int j = 0; j < 16; j++)
        {
            poss[i].insert(j);
        }
    }

    while (std::getline(std::cin, line))
    {
        int before[4];
        int after[4];
        int command[4];
        int result[4];
        int ret;
        int mappings[16];

        if (line.empty())
        {
            continue;
        }
        if (line.find("Before") == std::string::npos)
        {
            if (!mappingsReady)
            {
                findMappings(mappings, poss);
                mappingsReady = true;
            }

            ret = std::sscanf(line.c_str(), "%d %d %d %d", &command[0], &command[1], &command[2], &command[3]);
            apply(mappings[command[0]], registers, command, registers);
        }
        else
        {

            ret = std::sscanf(line.c_str(), "Before: [%d,%d,%d,%d]", &before[0], &before[1], &before[2], &before[3]);
            std::getline(std::cin, line);
            ret = std::sscanf(line.c_str(), "%d %d %d %d", &command[0], &command[1], &command[2], &command[3]);
            std::getline(std::cin, line);
            ret = std::sscanf(line.c_str(), "After: [%d,%d,%d,%d]", &after[0], &after[1], &after[2], &after[3]);

            int count = 0;
            for (int i = 0; i < 16; i++)
            {
                apply(i, before, command, result);

                if (check(after, result))
                {
                    count++;
                }
                else
                {
                    poss[command[0]].erase(i);
                }
            }

            if (count >= 3)
            {
                samples++;
            }
        }
    }

    std::cout << samples << std::endl;
    std::cout << registers << std::endl;
}
