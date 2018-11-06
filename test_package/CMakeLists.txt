cmake_minimum_required(VERSION 3.1)

project(
    dev_new_example
    LANGUAGES CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_executable(timer timer.cpp)
target_compile_features(timer PUBLIC cxx_std_17)
target_compile_definitions(timer PUBLIC ASIO_STANDALONE)
target_link_libraries(timer CONAN_PKG::asio)

