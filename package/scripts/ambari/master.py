#!/usr/bin/env python
from resource_management import *
import ambari_helpers as helpers

class Master(Script):
  def install(self, env):
    import params
    helpers.add_rstudio_server()
    self.configure(env)

  def configure(self, env):
    import params
    env.set_params(params)

  def status(self, env):
    import params
    env.set_params(params)
    Execute('service rstudio-server status >>' + params.rstudio_service_log)

  def start(self, env):
    import params
    env.set_params(params)
    Execute('service rstudio-server start >>' + params.rstudio_service_log)

  def stop(self, env, upgrade_type=None):
    import params
    env.set_params(params)
    Execute('service rstudio-server stop >>' + params.rstudio_service_log)

if __name__ == "__main__":
  Master().execute()
