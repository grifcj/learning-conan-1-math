import os

from conans import ConanFile, CMake, tools

class MathTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_paths"

    def build(self):
        cmake = CMake(self)
        conan_paths = os.path.join(self.build_folder, "conan_paths.cmake")
        cmake.definitions["CMAKE_PROJECT_INCLUDE"] = conan_paths
        cmake.configure()
        cmake.build()

    def test(self):
        cmake = CMake(self)
        cmake.test()
