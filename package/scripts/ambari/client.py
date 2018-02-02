#!/usr/bin/env python
from resource_management import *
import ambari_helpers as helpers

class Client(Script):
  def install(self, env):
    # Install repos & packages listed in metainfo.xml
    import params
    helpers.add_repos()
    self.configure(env)
    self.install_packages(env)
    for command in params.commands: Execute(command)

  def configure(self, env):
    import params
    env.set_params(params)

  def start(self, env, upgrade_type=None):
    pass

  def stop(self, env, upgrade_type=None):
    pass

  def status(self, env): raise ClientComponentHasNoStatus()

if __name__ == "__main__":
  Client().execute()
