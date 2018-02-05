from resource_management import *
import ambari_helpers as helpers

class Client(Script):
  def install(self, env):
    import params
    helpers.add_repos()
    self.configure(env)
    self.install_packages(env)
    for command in params.commands: Execute(command, user=params.rstudio_user)

  def configure(self, env):
    import params
    env.set_params(params)

  def start(self, env): raise ClientComponentHasNoStatus()

  def stop(self, env): raise ClientComponentHasNoStatus() 

  def status(self, env): raise ClientComponentHasNoStatus()

if __name__ == "__main__":
  Client().execute()
