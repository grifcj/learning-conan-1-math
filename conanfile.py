import os
from conans import ConanFile, CMake, python_requires

base = python_requires("conanbase/1.0.0-nightly@grifcj/dev")

class MathConan(ConanFile):
    name = "math"
    version = "1.0.0-nightly"
    scm = {
        "type": "git",
        "url": "https://github.com/grifcj/cmake-math",
        "revision": "auto"
    }
    requires = "logger/1.0.0-nightly@grifcj/dev"
    build_requires = (
            "cmake_extensions/1.0.0-nightly@grifcj/dev",
            "gtest/1.8.1@bincrafters/stable")
    generators = "cmake_paths"

    def _configure_cmake(self):
        cmake = CMake(self)
        conan_paths = os.path.join(self.build_folder, "conan_paths.cmake")
        cmake.definitions["CONAN_PACKAGE_VERSION"] = self.version.split('-')[0]
        cmake.definitions["CMAKE_FIND_PACKAGE_PREFER_CONFIG"] = "TRUE"
        cmake.definitions["CMAKE_PROJECT_INCLUDE"] = conan_paths
        cmake.generator = "Ninja"
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()
        cmake.test()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()


