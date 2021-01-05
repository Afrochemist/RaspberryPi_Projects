#This script mines monero on the raspberry pi

cd /opt/cpuminer-multi

#the code below are scripts compiles codes and needs to be ran once
#./autogen.sh
#./configure
#./build.sh

#The line below mines monero and sends it to a pool in minergate.com
./cpuminer -a cryptonight -o stratum+tcp://xmr.pool.minergate.com:45700 -u <email address>
