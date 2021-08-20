#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   template.py
@Author  :   Billy Zhou
@Time    :   2021/08/20
@Desc    :   None
'''


import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[2]))

from src.manager.Logger import logger
log = logger.get_logger(__name__)


def bin_test_template_run():
    log.info('bin.test.template running')
    log.info('The __name__ of bin.test.template is {}'.format(__name__))


if __name__ == '__main__':
    from bin.template import bin_template_run
    bin_template_run()
    bin_test_template_run()
