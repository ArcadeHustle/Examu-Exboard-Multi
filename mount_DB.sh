losetup -v -f DemonBride.exboard.img 
partx -v --add /dev/loop0
mkdir /tmp/DB
mount /dev/loop0p1 /tmp/DB -t vfat

