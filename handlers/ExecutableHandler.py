#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = """
        (_ )
     \\\", ) ^
       \/, \(
       CXC_/_)
     leo.pepe
"""
__license__ = "Simplified BSD License"
__copyright__ = "Copyright (c) 2013, Leonardo Pepe de Freitas"
__version__ = "1.0"

# -*- coding: utf8 -*-

from subprocess import Popen, PIPE

__author__ = 'Leonardo Pepe de Freitas'
__version__ = '1.0'


class Process(object):
    """

    """
    def __init__(self, cmd):
        self.name = cmd.split('/')[-1]
        self.cmd = cmd
        self.pid = None
        self.type = None
        self.stdout = None
        self.stderr = None
        self.stdin = None
        self.returncode = None


class ProcessExecutionHandler(Process):
    """

    """
    def execute(self):
        """

        :rtype : tuple
        """
        # concatenate path + args in form of a list
        # ex.: /sbin/ifconfig -a
        cmd = self.cmd.split()
        print(cmd)
        #
        try:
            process = Popen(cmd, bufsize=0, stdout=PIPE, stderr=PIPE)
            # wait until process finish
            process.wait()
            process.poll()
            self.__update_process_data(pid=process.pid,
                                 returncode=process.returncode,
                                 stdout=process.stdout.read(),
                                 stderr=process.stderr.read())
            return self.returncode, self.stdout, self.stderr
        except IOError:
            raise OSError

    def __update_process_data(self, **kwargs):
        """

        :rtype : dict
        """
        self.__dict__.update(kwargs)

    def get_process_data(self):
        """
        :rtype: dict
        """
        #
        # self.data must exist to be returned
        # raise AttributeErro if not
        if self.__dict__:
            return self.__dict__
        else:
            raise AttributeError


def main():
    # instance object ExecHandler()
    ls = ProcessExecutionHandler(cmd='/bin/ls -l /tmp/')
    ls.execute()
    process_result = ls.get_process_data()
    print(' PROCESS: {0},\n'
          ' PID: {1}\n'
          ' RETURN CODE: {2}\n'
          ' STDOUT: {3}'.format(process_result['cmd'], process_result['pid'], process_result['returncode'], process_result['stdout'])
    )
    print('{0}'.format(process_result))

if __name__ == '__main__':
    main()