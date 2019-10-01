import shutil

from conans import CMake, ConanFile, AutoToolsBuildEnvironment, tools


class CxxoptsConan(ConanFile):
    name = "libevfibers"
    branch = "master"
    scn = "c2996d9939ae734bf0da936399f2111dd6c10ed5"
    version = "0.4.1-59-gc2996d9"
    license = "MIT"
    author = "Darlan Cavalcante Moreira (darcamo@gmail.com)"
    url = "https://github.com/Lupus/libevfibers"
    description = "A small C fiber library that uses libev based event loop and libcoro based coroutine context switching"
    homepage = "http://olkhovskiy.me/libevfibers/"

    settings = "os", "compiler", "build_type", "arch"

    #exports_sources = "%/src/*" % name

    def source(self):
        self.run("git clone %s -b %s" % (self.url, self.branch))
        self.run("cd %s && git reset --hard %s" % (self.name, self.scn))

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="%s" % self.name)
        cmake.build()

    def package(self):
        self.copy("include/%s/*.h" % self.name, dst="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["evfibers"]
