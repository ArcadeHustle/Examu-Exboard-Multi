dd if=boot.img of=/dev/sdb bs=1M
parted /dev/sdb mkpart primary "FAT32" 4MiB 1028MiB
fdisk -l /dev/sdb


