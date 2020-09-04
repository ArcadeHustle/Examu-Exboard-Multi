losetup -v -f DemonBride.exboard.img /dev/loop1
partx -v --add /dev/loop1
mkdir /tmp/AH2
mount /dev/loop1p1 /tmp/AH2 -t vfat

