#!/bin/bash

# Downgrade gcc to get pandas to work and for murmurhash which is used by spacy
#sudo yum remove -y gcc72 gcc gcc-c++
sudo yum install -y gcc gcc-c++ tar bzip2
sudo yum install -y python36 python36-devel python36-pip python36-setuptools python36-virtualenv
sudo ln -s /usr/bin/pip-3.6 /usr/sbin/pip3

sudo yum install -y tmux
sudo yum install -y git
sudo yum install -y blas lapack

# change the bucket name
aws s3 cp s3://<YOUR_BUCKET>/users/<YOUR_NAME>/bootstraps $HOME/bootstraps --recursive

# Set spark home (so that findspark finds spark)
echo '
export SPARK_HOME=/usr/lib/spark
export PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h \[\033[33;1m\]\w\[\033[m\]\$ "
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad
' >> $HOME/.profile
