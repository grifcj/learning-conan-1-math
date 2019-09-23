from conans import ConanFile, CMake, tools

class MathConan(ConanFile):
    name = "math"
    version = "0.1.0"
    license = "Beerware"
    author = "Connor Griffith grifcj@gmail.com"
    url = "https://github.com/grifcj/cmake-math"
    description = "A logger that punked Chuck Norris"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    requires = ["logger/0.1.0@grifcj/stable"]
    build_requires = ["gtest/1.8.1@bincrafters/stable"]

    def source(self):
        self.run("git clone https://github.com/grifcj/cmake-math .")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.build(target='test')

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["math"]

