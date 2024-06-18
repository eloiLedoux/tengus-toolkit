#include <iostream>
#include <string>

void print()
{
    std::cout << "Fin de processus.\n";
}

template <typename T, typename... Types>
void print(T arg1, Types... arg2)
{
    if (typeid(T) == typeid(int))
    {
        std::cout << "int -> " << arg1 << std::endl;
    }
    else if (typeid(T) == typeid(double))
    {
        std::cout << "double -> " << arg1 << std::endl;
    }
    else if (typeid(T) == typeid(std::string))
    {
        std::cout << "string -> " << arg1 << std::endl;
    }
    else if (typeid(T) == typeid(bool))
    {
        std::cout << "bool -> " << arg1 << std::endl;
    }
    print(arg2...);
}

int main()
{
    print(1.14, 2, 3.14, std::string("toto"), true);

    return 0;
}
