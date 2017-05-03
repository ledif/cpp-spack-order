from spack import *


class CppSpackOrder(Package):
    """Test project to determine include order"""

    homepage = "https://github.com/ledif/cpp-spack-order"
    url      = "https://github.com/ledif/cpp-spack-order"

    version('0.1.0', git='git@github.com:ledif/cpp-spack-order', commit='61f7ad0b673d01793aaaf2e76b167619dd3f75cf')

    depends_on('boost@1.56.0')

    def install(self, spec, prefix):
        make()
