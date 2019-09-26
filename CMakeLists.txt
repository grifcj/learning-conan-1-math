cmake_minimum_required(VERSION 3.13)
project(math)

if (NOT TARGET logger::logger)
   find_package(logger REQUIRED)
endif()

find_package(logger REQUIRED)
find_package(gtest REQUIRED)

add_library(math fibonacci.cpp)
target_include_directories(math
   PUBLIC
      $<BUILD_INTERFACE:${CMAKE_CURRENT_LIST_DIR}>
      # Install interface must match package directory in conanfile.py
      $<INSTALL_INTERFACE:include>)
target_link_libraries(math PUBLIC logger::logger)
add_library(math::math ALIAS math)

get_property(exclude DIRECTORY ${PROJECT_SOURCE_DIR} PROPERTY EXCLUDE_FROM_ALL SET)
if (NOT exclude)
   enable_testing()
   add_executable(math_unittest math-test.cpp)
   target_link_libraries(math_unittest math gtest::gtest)
   add_test(NAME math::unittest COMMAND $<TARGET_FILE:math_unittest>)
endif()
