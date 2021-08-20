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
sys.path.append(str(Path(__file__).parents[3]))

from src.manager.Logger import logger
log = logger.get_logger(__name__)


def bin_test_test_template_run():
    log.debug('bin.test.test.template running')
    log.info('bin.test.test.template running')
    log.info('The __name__ of bin.test.test.template is {}'.format(__name__))


if __name__ == '__main__':
    from bin.template import bin_template_run
    from bin.test.template import bin_test_template_run
    bin_template_run()
    bin_test_template_run()
    bin_test_test_template_run()
