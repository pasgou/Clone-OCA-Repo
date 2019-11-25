# -*- coding: utf-8 -*-
# License AGPLv3 (http://www.gnu.org/licenses/agpl-3.0-standalone.html)
from __future__ import absolute_import, print_function

import configparser
import os

CREDENTIALS_FILE = 'oca.cfg'


def init_config():
    config = configparser.ConfigParser()
    config.add_section("GitHub")
    config.set("GitHub", "username", "")
    config.set("GitHub", "token", "")
    config.add_section("odoo")
    config.set("odoo", "username", "")
    config.set("odoo", "password", "")
    write_config(config)


def read_config():
    if not os.path.exists(CREDENTIALS_FILE):
        init_config()
    config = configparser.ConfigParser()
    config.read(CREDENTIALS_FILE)
    return config


def write_config(config):
    with open(CREDENTIALS_FILE, 'w') as fd:
        config.write(fd)


NOT_ADDONS = {
    'odoo-community.org',
    'contribute-md-template',
    'maintainer-tools',
    'maintainer-quality-tools',
    'odoo-sphinx-autodoc',
    'openupgradelib',
    'connector-magento-php-extension',
    'OCB',
    'OpenUpgrade',
    'pylint-odoo',
    'oca-custom',
    'odoorpc',
    'oca-decorators',
    'oca-weblate-deployment',
    'odoo-sentinel',
}


MAIN_BRANCHES = (
    '6.1',
    '7.0',
    '8.0',
    '9.0',
    '10.0',
    '11.0',
    '12.0',
    '13.0',
)
