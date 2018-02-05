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

  def start(self, env):
    Execute('systemctl start rstudio-server.service')

  def stop(self, env):
    Execute('systemctl stop rstudio-server.service')

  def status(self, env):
    Execute('systemctl status rstudio-server.service')

  def restart(self, env):
    Execute('systemctl restart rstudio-server.service')

if __name__ == "__main__":
  Master().execute()
