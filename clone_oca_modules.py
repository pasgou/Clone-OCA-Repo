# -*- coding: utf-8 -*-
"""
Importing tool for OCA projects.
It is an adaptation by mainteners-tools by OCA project "Clone_everything.py" script.
OCA_POJECTS : dictionary of OCA Projects mapped to the list of related
repository names. 
Have to be update with global variables in the github OCA/maintainer-tools/tools/oca_projects.py file.

OCA_REPOSITORY_NAMES: list of OCA repository names

"""

import argparse
import subprocess

import os


ALL = ['OCA_PROJECTS', 'OCA_REPOSITORY_NAMES', 'url']

OCA_PROJECTS = {
    'accounting': ['account-analytic',
                   'account-budgeting',
                   'account-closing',
                   'account-consolidation',
                   'account-financial-tools',
                   'account-financial-reporting',
                   'account-invoice-reporting',
                   'account-invoicing',
                   'account-fiscal-rule',
                   'operating-unit',
                   'intrastat',
                   ],
    # 'backport': ['OCB',
    #              ],
    'banking': ['bank-payment',
                'bank-statement-reconcile',
                'bank-statement-import',
                'account-payment',
                ],
    'community': ['maintainer-tools',
                  'maintainer-quality-tools',
                  'runbot-addons',
                  ],
    'connector': ['connector',
                  'connector-ecommerce',
                  ],
    'connector AccountEdge': ['connector-accountedge'],
    'connector LIMS': ['connector-lims'],
    'connector CMIS': ['connector-cmis'],
    'connector Magento': ['connector-magento'],
    'connector Prestashop': ['connector-prestashop'],
    'connector Redmine': ['connector-redmine'],
    'connector Sage': ['connector-sage'],
    'connector Salesforce': ['connector-salesforce'],
    'connector WooCommerce': ['connector-woocommerce'],
    'crm sales marketing': ['sale-workflow',
                            'crm',
                            'partner-contact',
                            'sale-financial',
                            'sale-reporting',
                            'commission',
                            'event',
                            'survey',
                            ],
    'document': ['knowledge'],
    'ecommerce': ['e-commerce'],
    'edi': ['edi'],
    'financial control': ['margin-analysis'],
    'Infrastructure': ['infrastructure-dns'],
    'geospatial': ['geospatial'],
    'hr': ['hr-timesheet',
           'hr',
           'department',
           ],
    'connector-odoo2odoo': ['connector-odoo2odoo'],
    'multi-company': ['multi-company'],
    'l10n-argentina': ['l10n-argentina'],
    'l10n-belgium': ['l10n-belgium'],
    'l10n-brazil': ['l10n-brazil'],
    'l10n-cambodia': ['l10n-cambodia'],
    'l10n-canada': ['l10n-canada'],
    'l10n-china': ['l10n-china'],
    'l10n-colombia': ['l10n-colombia'],
    'l10n-costa-rica': ['l10n-costa-rica'],
    'l10n-ecuador': ['l10n-ecuador'],
    'l10n-ethiopia': ['l10n-ethiopia'],
    'l10n-finland': ['l10n-finland'],
    'l10n-france': ['l10n-france'],
    'l10n-germany': ['l10n-germany'],
    'l10n-india': ['l10n-india'],
    'l10n-indonesia': ['l10n-indonesia'],
    'l10n-iran': ['l10n-iran'],
    'l10n-ireland': ['l10n-ireland'],
    'l10n-italy': ['l10n-italy'],
    'l10n-luxemburg': ['l10n-luxemburg'],
    'l10n-mexico': ['l10n-mexico'],
    'l10n-morocco': ['l10n-morocco'],
    'l10n-netherlands': ['l10n-netherlands'],
    'l10n-norway': ['l10n-norway'],
    'l10n-peru': ['l10n-peru'],
    'l10n-portugal': ['l10n-portugal'],
    'l10n-romania': ['l10n-romania'],
    'l10n-slovenia': ['l10n-slovenia'],
    'l10n-spain': ['l10n-spain'],
    'l10n-switzerland': ['l10n-switzerland'],
    'l10n-taiwan': ['l10n-taiwan'],
    'l10n-turkey': ['l10n-turkey'],
    'l10n-usa': ['l10n-usa'],
    'l10n-united-kingdom': ['l10n-united-kingdom'],
    'l10n-venezuela': ['l10n-venezuela'],
    'logistics': ['carrier-delivery',
                  'stock-logistics-barcode',
                  'stock-logistics-workflow',
                  'stock-logistics-tracking',
                  'stock-logistics-warehouse',
                  'stock-logistics-reporting',
                  'rma',
                  ],
    'manufacturing': ['manufacture',
                      'manufacture-reporting',
                      ],
    'management system': ['management-system'],
    'purchase': ['purchase-workflow',
                 'purchase-reporting',
                 ],
    'product': ['product-attribute',
                'product-kitting',
                'product-variant',
                ],
    'project / services': ['project-reporting',
                           'project-service',
                           'contract',
                           'program',
                           'business-requirement',
                           ],
    'social': ['social'],
    'tools': ['reporting-engine',
              'report-print-send',
              'webkit-tools',
              'server-tools',
              'community-data-files',
              'webhook',
              'interface-github',
              ],
    'vertical association': ['vertical-association'],
    'vertical hotel': ['vertical-hotel'],
    'vertical ISP': ['vertical-isp'],
    'vertical edition': ['vertical-edition'],
    'vertical education': ['vertical-education'],
    'vertical medical': ['vertical-medical'],
    'vertical NGO': ['vertical-ngo',
                     # XXX
                     ],
    'vertical construction': ['vertical-construction'],
    'vertical travel': ['vertical-travel'],
    'web': ['web'],
    'website': ['website',
                'website-cms',
                ],
}


ignored = [
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
]
	
OCA_REPOSITORY_NAMES = []
REPOSITORIES = []
for repos in OCA_PROJECTS.itervalues():
    REPOSITORIES += repos

OCA_REPOSITORY_NAMES = list(set(REPOSITORIES)-set(ignored))
OCA_REPOSITORY_NAMES.sort()

_OCA_REPOSITORY_NAMES = set(OCA_REPOSITORY_NAMES)

_URL_MAPPINGS = {'git': 'git@github.com:%s/%s.git',
		         'https': 'https://github.com/%s/%s.git',
		         }


def url(project_name, protocol='git', org_name='OCA'):
    """get the URL for an OCA project repository"""
    if project_name not in _OCA_REPOSITORY_NAMES:
        raise ValueError('Unknown project', project_name)
    return _URL_MAPPINGS[protocol] % (org_name, project_name)


def clone(organization_remotes=None,
          remove_old_repos=False,
          protocol='https',
	  branche='8.0'
         ):
    for project in OCA_REPOSITORY_NAMES:
        cmd = ['git', 'clone', '--quiet', url(project,protocol),'-b', branche, project]
        try:
            subprocess.check_call(cmd)
        except:
            cmd = ['git',
                   '--git-dir=' + os.path.join(project, '.git'),
                   'fetch', '--all']
            subprocess.call(cmd)
        if organization_remotes:
            for organization_remote in organization_remotes.split(','):
                cmd = ['git', '--git-dir=' + os.path.join(project, '.git'),
                       'remote', 'add', organization_remote,
                       url(project, protocol, org_name=organization_remote)]
                subprocess.call(cmd)
                cmd = ['git', '--git-dir=' + os.path.join(project, '.git'),
                       'fetch', organization_remote]
                subprocess.call(cmd)
    if remove_old_repos:
        for d in os.listdir('.'):
            if d not in OCA_REPOSITORY_NAMES and \
                    os.path.isdir(d) and \
                    os.path.isdir(os.path.join(d, '.git')):
                subprocess.check_call(['rm', '-fr', d])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--organization-remotes", dest="org_remotes",
                        help="Specify additional remote to add"
                        " (separated by commas).\n"
                        "This is used after of clone, add organization"
                        " remote into git branch cloned",
                        nargs=1, default=None)
    parser.add_argument("--remove-old-repos", action='store_true',
                        help="Remove all git repositories in the current"
                        " directory that are not OCA repositories anymore."
                        " THIS IS DANGEROUS: make sure"
                        " you run this command in a directory reserved"
                        " for the purpose of running this script as all"
                        " other subdirectories will be erased permanently. "
                        " This option is useful to cope with repository"
                        " renames.")
    args = parser.parse_args()
    org_remotes = args.org_remotes and args.org_remotes[0] or None
    clone(organization_remotes=org_remotes,
          remove_old_repos=args.remove_old_repos)

if __name__ == '__main__':
    main()


