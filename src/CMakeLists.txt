find_package(logger REQUIRED)

add_library(math fibonacci.cpp)
target_include_directories(
   math
   PUBLIC
		$<BUILD_INTERFACE:${CMAKE_CURRENT_LIST_DIR}/include>
		$<INSTALL_INTERFACE:include>)
target_link_libraries(math PUBLIC logger::logger)

include(CMakeExtensions)
install_project()
