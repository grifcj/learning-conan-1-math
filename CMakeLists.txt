cmake_minimum_required(VERSION 3.13)
project(math)

enable_testing()

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_library(math fibonacci.cpp)
target_include_directories(math
   PUBLIC
   $<BUILD_INTERFACE:${CMAKE_CURRENT_LIST_DIR}>
   $<INSTALL_INTERFACE:include>)
target_link_libraries(math PUBLIC CONAN_PKG::logger)

add_executable(math_test math-test.cpp)
target_link_libraries(math_test math CONAN_PKG::gtest)
add_test(NAME math_test COMMAND $<TARGET_FILE:math_test>)
