#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Importing tool for OCA projects.
It is an adaptation by mainteners-tools by OCA project "Clone_everything.py" script.
OCA_POJECTS : dictionary of OCA Projects mapped to the list of related
repository names. 
Have to be update with global variables in the github OCA/maintainer-tools/tools/oca_projects.py file.

OCA_REPOSITORY_NAMES: list of OCA repository names

"""
import sys
import os
import argparse
import subprocess

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
                   'mis-builder',
                   'currency',
                   'credit-control',
                   'data-protection',
                   ],
    # 'backport': ['OCB',
    #              ],
    'Apps Store': ['apps-store'],

    'banking': ['bank-payment',
                'account-reconcile',
                'bank-statement-import',
                'account-payment',
                ],
    'community': ['maintainer-tools',
                  'maintainer-quality-tools',
                  'runbot-addons',
                  ],
    'connector': ['connector',
                  'connector-ecommerce',
                  'queue',
                  ],
    'connector AccountEdge': ['connector-accountedge'],
    'connector CMIS': ['connector-cmis'],
    'connector Infor': ['connector-infor'],
    'connector Lengow': ['connector-lengow'],
    'connector LIMS': ['connector-lims'],
    'connector Magento': ['connector-magento'],
    'connector Prestashop': ['connector-prestashop'],
    'connector Sage': ['connector-sage'],
    'connector Salesforce': ['connector-salesforce'],
    'connector SPSCommerce': ['connector-spscommerce'],
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
    'field-service': ['field-service'],
    'financial control': ['margin-analysis'],
    'Infrastructure': ['infrastructure-dns'],
    'geospatial': ['geospatial'],
    'hr': ['timesheet',
           'hr',
           'hr-attendance',
           'hr-expense',
           'hr-holidays',
           'department',
           ],
    'connector-odoo2odoo': ['connector-odoo2odoo'],
    'multi-company': ['multi-company'],
    'l10n-argentina': ['l10n-argentina'],
    'l10n-austria': ['l10n-austria'],
    'l10n-belarus': ['l10n-belarus'],
    'l10n-belgium': ['l10n-belgium'],
    'l10n-brazil': ['l10n-brazil'],
    'l10n-cambodia': ['l10n-cambodia'],
    'l10n-canada': ['l10n-canada'],
    'l10n-chile': ['l10n-chile'],
    'l10n-china': ['l10n-china'],
    'l10n-colombia': ['l10n-colombia'],
    'l10n-costa-rica': ['l10n-costa-rica'],
    'l10n-croatia': ['l10n-croatia'],
    'l10n-ecuador': ['l10n-ecuador'],
    'l10n-estonia': ['l10n-estonia'],
    'l10n-ethiopia': ['l10n-ethiopia'],
    'l10n-finland': ['l10n-finland'],
    'l10n-france': ['l10n-france'],
    'l10n-germany': ['l10n-germany'],
    'l10n-greece': ['l10n-greece'],
    'l10n-india': ['l10n-india'],
    'l10n-indonesia': ['l10n-indonesia'],
    'l10n-iran': ['l10n-iran'],
    'l10n-ireland': ['l10n-ireland'],
    'l10n-italy': ['l10n-italy'],
    'l10n-japan': ['l10n-japan'],
    'l10n-luxemburg': ['l10n-luxemburg'],
    'l10n-macedonia': ['l10n-macedonia'],
    'l10n-mexico': ['l10n-mexico'],
    'l10n-morocco': ['l10n-morocco'],
    'l10n-netherlands': ['l10n-netherlands'],
    'l10n-norway': ['l10n-norway'],
    'l10n-peru': ['l10n-peru'],
    'l10n-poland': ['l10n-poland'],
    'l10n-portugal': ['l10n-portugal'],
    'l10n-romania': ['l10n-romania'],
    'l10n-russia': ['l10n-russia'],
    'l10n-slovenia': ['l10n-slovenia'],
    'l10n-spain': ['l10n-spain'],
    'l10n-switzerland': ['l10n-switzerland'],
    'l10n-taiwan': ['l10n-taiwan'],
    'l10n-thailand': ['l10n-thailand'],
    'l10n-turkey': ['l10n-turkey'],
    'l10n-united-kingdom': ['l10n-united-kingdom'],
    'l10n-uruguay': ['l10n-uruguay'],
    'l10n-usa': ['l10n-usa'],
    'l10n-venezuela': ['l10n-venezuela'],
    'l10n-vietnam': ['l10n-vietnam'],
    'logistics': ['carrier-delivery',
                  'stock-logistics-barcode',
                  'stock-logistics-workflow',
                  'stock-logistics-tracking',
                  'stock-logistics-warehouse',
                  'stock-logistics-reporting',
                  'rma',
                  'ddmrp',
                  'wms',
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
                'product-pack',
                ],
    'project / services': ['project-reporting',
                           'project-service',
                           'project-agile',
                           'contract',
                           'program',
                           'business-requirement',
                           'connector-redmine',
                           'connector-jira',
                           ],
    'social': ['social'],
    'storage': ['storage'],
    'search-engine': ['search-engine'],
    'tools': ['reporting-engine',
              'report-print-send',
              'webkit-tools',
              'server-tools',
              'server-auth',
              'server-env',
              'server-backend',
              'server-brand',
              'server-ux',
              'community-data-files',
              'webhook',
              'interface-github',
              'iot',
              'rest-framework',
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
    'vertical real state': ['vertical-realstate'],
    'vertical travel': ['vertical-travel'],
    'web': ['web'],
    'website': ['website',
                'website-cms',
                ],
}


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

# def get_repositories():
#     gh = login()
#     all_repos = [repo.name for repo in gh.repositories_by('OCA')
#                  if repo.name not in NOT_ADDONS]
#     return all_repos
# 
# 
# def get_repositories_and_branches(repos=(), branches=MAIN_BRANCHES):
#     gh = login()
#     for repo in gh.repositories_by('OCA'):
#         if repos and repo.name not in repos:
#             continue
#         if repo.name in NOT_ADDONS:
#             continue
#         for branch in repo.branches():
#             if branches and branch.name not in branches:
#                 continue
#             yield repo.name, branch.name


OCA_REPOSITORY_NAMES = []
for repos in OCA_PROJECTS.values():
    OCA_REPOSITORY_NAMES += repos

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
	  branche='12.0'
         ):
    for project in OCA_REPOSITORY_NAMES:
        if project in os.listdir('.'):
            addon_path = os.path.join(project)
            cmd = ['cd', addon_path]
            cmd2 = ['git', 'pull', '--quiet']
            cmd3 = ['cd','..']
            subprocess.call(cmd) 
            subprocess.call(cmd2)
            subprocess.call(cmd3)
        else:
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


