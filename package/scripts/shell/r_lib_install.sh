set -eu

R_LIB=$1
R_LIBS_DIR=$2
REPO_URL=$3
LOG_FILE=$4

if [ ! -d "$R_LIBS_DIR/$R_LIB" ]
then
  #Rscript -e 'install.packages(c("'$R_LIB'"), dep= TRUE, lib="'$R_LIBS_DIR'", repos="'$REPO_URL'", type = "source");' >> $LOG_FILE
  if [ "$R_LIB" == 'stringi' ]
  then
  	wget "$REPO_URL"src/contrib/icudt55l.zip -O /tmp/icudt55l.zip
    Rscript -e 'install.packages(c("'$R_LIB'"), repos="'$REPO_URL'", type = "source", configure.vars="ICUDT_DIR=/tmp/");' >> $LOG_FILE
    rm -f /tmp/icudt55l.zip
  else
    Rscript -e 'install.packages(c("'$R_LIB'"), repos="'$REPO_URL'", type = "source");' >> $LOG_FILE
  fi
fi
