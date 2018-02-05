import os, pwd, grp, signal, platform, yum
from resource_management import *

def package_dir(): return os.path.realpath(__file__).split('/package')[0] + '/package/'

def add_repos():
  distribution = platform.linux_distribution()[0].lower()
  version = platform.linux_distribution()[1].lower().split('.')[0]
  #TODO: add ubuntu
  if distribution in ['centos', 'redhat', 'red hat enterprise linux server', 'centos linux'] :
    if version == '6':
      repo_dir = package_dir()+'files/repos/rhel6/'
      os_repo_dir = '/etc/yum.repos.d/'
    elif version == '7':
      repo_dir = package_dir()+'files/repos/rhel7/'
      os_repo_dir = '/etc/yum.repos.d/'

  for repo in os.listdir(repo_dir):
    if not os.path.isfile(os_repo_dir + repo):
      Execute('cp ' + repo_dir+repo + ' ' + os_repo_dir)

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
