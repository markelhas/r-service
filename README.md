An Ambari Stack service package for R with pre-installed packages for working with data in Hadoop (rhdfs, rmr2, plyrmr)

To deploy, copy the entire directory into your Ambari stacks folder and restart Ambari:

**Note**:
Installing the stack enables the EPEL yum repo on all designated client nodes. Installation requires connectivity to [CRAN](http://cran.us-r-project.org) for any package added to the default list (See Configuration Options).

```
git clone https://github.com/radcheb/r-service
sudo cp -r r-service /var/lib/ambari-server/resources/stacks/HDP/2.6/services/
sudo service ambari-server restart
```

Then you can click on 'Add Service' from the 'Actions' dropdown menu in the bottom left of the Ambari dashboard. When you've completed the install process, the R interpreter will be available for use on all selected nodes.

Once installed, set your environment variables appropriately before starting the R interpreter.
```
export HADOOP_STREAMING=/usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar
export HADOOP_CMD=/usr/bin/hadoop
```
Or, within R scripts, or inside the interpreter itself:
```
Sys.setenv(HADOOP_STREAMING="/usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar")
Sys.setenv(HADOOP_CMD="/usr/bin/hadoop")
```

There are two models for working with R in Hadoop environments:

1. Local - use rhdfs for reading files from HDFS and working with on a local (typically high-memory node)

2. Cluster - use rplyr, or rmr2 to launch jobs that run on all cluster nodes. In this model, R needs to be installed on all YARN managed nodes. To install, check the 'Client' box for all nodes which have NodeManager installed.

A 'remove.sh' script is provided in the project root for convenience. It'll remove the service package from Ambari's resources dir. Please edit remove.sh to set your Ambari login and cluster name details.
