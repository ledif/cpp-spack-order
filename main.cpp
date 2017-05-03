#include <iostream>
#include <string>
#include <boost/version.hpp>

int main(int argc, char* argv[])
{
  bar b{2};

  std::cout << b.y << std::endl;

  std::string s;
  std::cout << std::foo() << std::endl;

  return 0;
}
