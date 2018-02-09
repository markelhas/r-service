set -eu

R_LIB=$1
R_LIBS_DIR=$2
REPO_URL=$3
LOG_FILE=$4

if [ ! -d "$R_LIBS_DIR/$R_LIB" ]
then
    Rscript -e 'install.packages(c("'$R_LIB'"), repos="'$REPO_URL'", type = "source");' >> $LOG_FILE
fi
