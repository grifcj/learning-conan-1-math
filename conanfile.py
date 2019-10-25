import os
from conans import ConanFile, CMake, python_requires

base = python_requires("conanbase/1.0.0-nightly@grifcj/dev")

class MathConan(base.get_conanfile()):
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

    def _make_cmake(self):
        cmake = super()._make_cmake()
        cmake.definitions["logger_DIR"] = ""
        return cmake


