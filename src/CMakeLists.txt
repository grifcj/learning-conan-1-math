cmake_minimum_required(VERSION 3.13)
project(math VERSION ${CONAN_PACKAGE_VERSION})

find_package(logger REQUIRED)

add_library(math fibonacci.cpp)
target_include_directories(
   math
   PUBLIC
		$<BUILD_INTERFACE:${CMAKE_CURRENT_LIST_DIR}/include>
		$<INSTALL_INTERFACE:include>)
target_link_libraries(math PUBLIC logger::logger)
add_library(math::math ALIAS math)

include(CMakeExtensions)
install_project()
