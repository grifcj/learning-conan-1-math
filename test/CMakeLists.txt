find_package(gtest REQUIRED)

add_executable(unittest unittest.cpp)
target_link_libraries(unittest PUBLIC math gtest::gtest)
add_test(NAME unittest COMMAND $<TARGET_FILE:unittest>)



