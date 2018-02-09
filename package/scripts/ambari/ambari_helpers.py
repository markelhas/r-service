import os, pwd, grp, signal, platform, yum
from resource_management import *

def package_dir(): return os.path.realpath(__file__).split('/package')[0] + '/package/'

def add_repos():
  import params
  distribution = platform.linux_distribution()[0].lower()
  version = platform.linux_distribution()[1].lower().split('.')[0]
  if distribution in ['centos', 'redhat', 'red hat enterprise linux server', 'centos linux'] :
    if version == '6':
      repo_epel = package_dir()+'files/repos/centos6/epel-release-latest-6.noarch.rpm'
      repo_centos = package_dir()+'files/repos/centos6/centos-release-latest-6.x86_64.rpm'
      Execute('wget '+params.epel6.download.url+' -O '+repo_epel+' -a '  + params.rstudio_install_log, user=params.rstudio_user)
      Execute('wget '+params.centos6.download.url+' -O '+repo_centos+' -a '  + params.rstudio_install_log, user=params.rstudio_user)
    elif version == '7':
      repo_epel = package_dir()+'files/repos/centos6/epel-release-latest-7.noarch.rpm'
      repo_centos = package_dir()+'files/repos/centos6/centos-release-latest-7.x86_64.rpm'
      Execute('wget '+params.epel7.download.url+' -O '+repo_epel+' -a '  + params.rstudio_install_log, user=params.rstudio_user)
      Execute('wget '+params.centos7.download.url+' -O '+repo_centos+' -a '  + params.rstudio_install_log, user=params.rstudio_user)

  yb = yum.YumBase()
  if yb.rpmdb.searchNevra(name='centos-release'):
    Execute('echo "reinstalling centos-release "', user=params.rstudio_user)
    Execute('yum -y reinstall '+repo_centos+' >> ' + params.rstudio_install_log, user=params.rstudio_user)
  else:
    Execute('echo "installing centos-release "', user=params.rstudio_user)
    Execute('yum -y reinstall '+repo_centos+' >> ' + params.rstudio_install_log, user=params.rstudio_user)

  if yb.rpmdb.searchNevra(name='epel-release'):
    Execute('echo "reinstalling epel-release "', user=params.rstudio_user)
    Execute('yum -y reinstall '+repo_epel+' >> ' + params.rstudio_install_log, user=params.rstudio_user)
  else:
    Execute('echo "installing epel-release "', user=params.rstudio_user)
    Execute('yum -y reinstall '+repo_epel+' >> ' + params.rstudio_install_log, user=params.rstudio_user)

def create_linux_user(user, group):
  try: pwd.getpwnam(user)
  except KeyError: Execute('useradd ' + user)
  try: grp.getgrnam(group)
  except KeyError: Execute('groupadd ' + group)

def create_hdfs_user(user):
  Execute('hadoop dfs -mkdir -p /user/'+user, user='hdfs')
  Execute('hadoop dfs -chown ' + user + ' /user/'+user, user='hdfs')
  Execute('hadoop dfs -chgrp ' + user + ' /user/'+user, user='hdfs')

def add_rstudio_server():
  import params
  yb = yum.YumBase()
  if yb.rpmdb.searchNevra(name='rstudio-server'):
    Execute('echo "reinstalling rstudio-server "', user=params.rstudio_user)
    Execute('wget '+params.rstudio_download_url+' -O '+params.rstudio_temp_file+' -a '  + params.rstudio_install_log, user=params.rstudio_user)
    Execute('yum -y reinstall '+params.rstudio_temp_file+' >> ' + params.rstudio_install_log, user=params.rstudio_user)
    Execute('rm '+params.rstudio_temp_file+' >> ' + params.rstudio_install_log, user=params.rstudio_user)
  else:
    Execute('echo "installing rstudio-server "', user=params.rstudio_user)
    Execute('wget '+params.rstudio_download_url+' -O '+params.rstudio_temp_file+' -a '  + params.rstudio_install_log, user=params.rstudio_user)
    Execute('yum -y install '+params.rstudio_temp_file+' >> ' + params.rstudio_install_log, user=params.rstudio_user)
    Execute('rm '+params.rstudio_temp_file+' >> ' + params.rstudio_install_log, user=params.rstudio_user)

  if yb.rpmdb.searchNevra(name='shiny-server'):
    Execute('echo "reinstalling shiny-server "', user=params.rstudio_user)
    Execute('wget '+params.rshiny.download.url+' -O '+params.rshiny_temp_file+' -a '  + params.rshiny.install.log, user=params.rstudio_user)
    Execute('yum -y reinstall '+params.rshiny_temp_file+' >> ' + params.rshiny.install.log, user=params.rstudio_user)
    Execute('rm '+params.rshiny_temp_file+' >> ' + params.rshiny.install.log, user=params.rstudio_user)
  else:
    Execute('echo "installing shiny-server "', user=params.rstudio_user)
    Execute('wget '+params.rshiny.download.url+' -O '+params.rshiny_temp_file+' -a '  + params.rshiny.install.log, user=params.rstudio_user)
    Execute('yum -y install '+params.rshiny_temp_file+' >> ' + params.rshiny.install.log, user=params.rstudio_user)
    Execute('rm '+params.rshiny_temp_file+' >> ' + params.rshiny.install.log, user=params.rstudio_user)
  