import shutil

from conans import CMake, ConanFile, AutoToolsBuildEnvironment, tools


class CxxoptsConan(ConanFile):
    name = "libevfibers"
    libname = "evfibers"
    branch = "master"
    #scn = "8f0a41927bf8c1b8a9c5a3adb254247303b50b17"
    scn = "a8a5b81698f0c7f343745dcdbfcb0f6c6fe4ff32"
    version = "0.4.1-58-ga8a5b81"
    license = "MIT"
    author = "Darlan Cavalcante Moreira (darcamo@gmail.com)"
    #url = "https://github.com/Lupus/libevfibers"
    url = "https://github.com/msaf1980/libevfibers"
    description = "A small C fiber library that uses libev based event loop and libcoro based coroutine context switching"
    homepage = "http://olkhovskiy.me/libevfibers/"

    settings = "os", "compiler", "build_type", "arch"

    #exports_sources = "%/src/*" % name

    def source(self):
        print("git clone %s -b %s" % (self.url, self.branch))
        self.run("git clone %s -b %s" % (self.url, self.branch))
        self.run("cd %s && git reset --hard %s" % (self.name, self.scn))

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="%s" % self.name)
        cmake.build()

    def package(self):
        include = "include/%s" % self.libname
        src_include = "%s/%s" % (self.libname, self.name)
        self.copy("*.h", src=include, dst=include)
        self.copy("*.h", src="libevfibers/include/evfibers", dst=include)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = [ self.libname ]
