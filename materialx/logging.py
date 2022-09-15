# SPDX-License-Identifier: GPL-2.0-or-later
# Copyright 2022, AMD

import sys
import logging.handlers

from . import ADDON_ALIAS


FORMAT_STR = "%(asctime)s %(levelname)s %(name)s [%(thread)d]:  %(message)s"

# root logger for the addon
logger = logging.getLogger(ADDON_ALIAS)
logger.setLevel('INFO')

# file_handler = logging.handlers.RotatingFileHandler(PLUGIN_ROOT_DIR / 'usdhydra.log',
#                                                     mode='w', encoding='utf-8', delay=True,
#                                                     backupCount=config.logging_backups)
# file_handler.doRollover()
# file_handler.setFormatter(logging.Formatter(FORMAT_STR))
# logger.addHandler(file_handler)

console_handler = logging.StreamHandler(stream=sys.stdout)
console_handler.setFormatter(logging.Formatter(FORMAT_STR))
logger.addHandler(console_handler)


def msg(args):
    return ", ".join(str(arg) for arg in args)


class Log:
    def __init__(self, tag):
        self.logger = logger.getChild(tag)

    def __call__(self, *args):
        self.debug(*args)

    def debug(self, *args):
        self.logger.debug(msg(args))

    def info(self, *args):
        self.logger.info(msg(args))

    def warn(self, *args):
        self.logger.warning(msg(args))

    def error(self, *args):
        self.logger.error(msg(args))

    def critical(self, *args):
        self.logger.critical(msg(args))

    def dump_args(self, func):
        """This decorator dumps out the arguments passed to a function before calling it"""
        arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]

        def echo_func(*args, **kwargs):
            self.debug("<{}>: {}{}".format(
                func.__name__,
                tuple("{}={}".format(name, arg) for name, arg in zip(arg_names, args)),
                # args if args else "",
                " {}".format(kwargs.items()) if kwargs else "",
            ))
            return func(*args, **kwargs)

        return echo_func
