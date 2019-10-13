cmake_minimum_required(VERSION 3.13)
project(math-test)

find_package(math REQUIRED)
find_package(GTest REQUIRED)

add_executable(math_unittest unittest.cpp)
target_link_libraries(math_unittest PUBLIC math::math GTest::gmock_main)
add_test(NAME math::unittest COMMAND $<TARGET_FILE:math_unittest>)



