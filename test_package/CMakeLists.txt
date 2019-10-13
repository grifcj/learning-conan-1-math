cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

find_package(math REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example PUBLIC math::math)

enable_testing()
add_test(NAME example COMMAND $<TARGET_FILE:example>)
