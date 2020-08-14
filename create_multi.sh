dd if=boot.img of=/dev/sdb bs=1M
parted /dev/sdb mkpart primary "FAT32" 4MiB 1028MiB
parted /dev/sdb mkpart primary "FAT32" 1028MiB 2052MiB
parted /dev/sdb mkpart primary "FAT32" 2052MiB 3076MiB
fdisk -l /dev/sdb


