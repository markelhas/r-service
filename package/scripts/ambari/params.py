#!/usr/bin/env python
from resource_management.libraries.functions.version import format_hdp_stack_version, compare_versions
from resource_management import *
import ambari_helpers as helpers

# server configurations
config = Script.get_config()

r_libs = filter(lambda x: len(x.strip()) > 0, config['configurations']['r-config']['r.libs'].split(','))
r_repo_url = config['configurations']['r-config']['r.repo_url']

package_dir = helpers.package_dir()
scripts_dir = package_dir + 'scripts/'

r_libs_dir = '/usr/lib64/R/library/'

commands = []

for lib in r_libs:
  command = ' '.join(['sh', scripts_dir+'shell/r_lib_install.sh', lib, r_libs_dir, r_repo_url])
  commands.append(command)
