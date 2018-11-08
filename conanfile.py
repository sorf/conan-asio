from conans import ConanFile, CMake, tools

class AsioConan(ConanFile):
    name = "asio"
    version = "1.12.1"
    license = "BSL-1.0"
    url = "https://github.com/sorf/conan-asio"
    description = "Asio C++ Library"
    no_copy_source = True

    def source(self):
        self.run("git clone --depth 1 --branch asio-1-12-1 https://github.com/chriskohlhoff/asio")

    def package(self):
        self.copy("*.hpp", dst="include", src="asio/asio/include/")
        self.copy("*.ipp", dst="include", src="asio/asio/include/")
        self.copy("LICENSE_1_0.txt", dst="include", src="asio/asio")

    def package_id(self):
        self.info.header_only()
