cmake_minimum_required(VERSION 3.13)
project(math)

enable_testing()

set(FETCHCONTENT_QUIET OFF)
include(FetchContent)

FetchContent_Declare(googletest
   URL https://github.com/google/googletest/archive/release-1.8.0.zip
   )
FetchContent_GetProperties(googletest)
if (NOT googletest_POPULATED)
   FetchContent_Populate(googletest)
   add_subdirectory(${googletest_SOURCE_DIR} ${googletest_BINARY_DIR} EXCLUDE_FROM_ALL)
endif()

FetchContent_Declare(logger
   GIT_REPOSITORY git@github.com:grifcj/cmake-logger.git
   GIT_PROGRESS TRUE
   )
FetchContent_GetProperties(logger)
if (NOT logger_POPULATED)
   FetchContent_Populate(logger)
   add_subdirectory(${logger_SOURCE_DIR} ${logger_BINARY_DIR})
endif()

set(libName ${PROJECT_NAME})
add_library(${libName} math.cpp)
target_include_directories(${libName} PUBLIC ${CMAKE_CURRENT_LIST_DIR})
target_link_libraries(${libName} PUBLIC logger)

set(testName ${PROJECT_NAME}_unittest)
add_executable(${testName} math-test.cpp)
target_link_libraries(${testName} PUBLIC ${libName} gmock gmock_main)
add_test(${testName} ${testName})
