from __future__ import absolute_import, division, print_function

import pkg_resources as _pkg_resources

from .scheduler import QueueScheduler, SchedulerDriver
# from .executor import ThreadExecutor, ProcessExecutor, ExecutorDriver
# #from .messages.satyr import PythonTask, PythonTaskStatus  # important to register classes
#
#
# __version__ = _pkg_resources.get_distribution('mentor').version
#
# __all__ = ('QueueScheduler',
#            'SchedulerDriver',
#            'ExecutorDriver',
#            'ThreadExecutor',
#            'ProcessExecutor',
#            'PythonTask',
#            'PythonTaskStatus')
