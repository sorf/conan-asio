import os
from conans import ConanFile, CMake, tools

class AsioTestConan(ConanFile):
    name = "asio_test"
    settings = "os"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        if not self.settings.os == "Windows":
            cmake.definitions["CONAN_CXX_FLAGS"] = " -pthread"
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self.settings):
            os.chdir("bin")
            self.run(".%stimer" % os.sep)
