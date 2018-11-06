#include <asio.hpp>
#include <iostream>

int main() {
    asio::io_context io;
    asio::steady_timer t(io, asio::chrono::milliseconds(500));
    std::cout << "Hello" << std::endl;
    t.wait();
    std::cout << "World" << std::endl;
    return 0;
}
