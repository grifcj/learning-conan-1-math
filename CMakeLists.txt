cmake_minimum_required(VERSION 3.13)
project(math)

find_package(logger REQUIRED)
find_package(gtest REQUIRED)

add_library(math fibonacci.cpp)
target_include_directories(math
   PUBLIC
      $<BUILD_INTERFACE:${CMAKE_CURRENT_LIST_DIR}>
      # Install interface must match package directory in conanfile.py
      $<INSTALL_INTERFACE:include>)
target_link_libraries(math PUBLIC logger::logger)

enable_testing()
add_executable(math_test math-test.cpp)
target_link_libraries(math_test math gtest::gtest)
add_test(NAME math_test COMMAND $<TARGET_FILE:math_test>)
