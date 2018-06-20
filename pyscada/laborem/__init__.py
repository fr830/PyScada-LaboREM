# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pyscada

__version__ = pyscada.__version__
__author__ = pyscada.__author__

default_app_config = 'pyscada.laborem.apps.PyScadaLaboREMConfig'

PROTOCOL_ID = 11

parent_process_list = [{'pk': PROTOCOL_ID,
                        'label': 'pyscada.laborem',
                        'process_class': 'pyscada.laborem.worker.Process',
                        'process_class_kwargs': '{"dt_set":30}',
                        'enabled': True}]