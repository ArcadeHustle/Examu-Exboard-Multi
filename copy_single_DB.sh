umount /tmp/single > /dev/null
mkdir /tmp/single
mount /dev/sdb2 /tmp/single
cp -rfv /tmp/DB/* /tmp/single
cp boot.ini /tmp/single/boot.ini 
umount /tmp/boot > /dev/null
mkdir /tmp/boot
mount /dev/sdb1 /tmp/boot
cp -fv menu.lst_single /tmp/boot/menu.lst
