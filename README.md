*Reminder, if you like these repos, fork them so they don't disappear*<br> 
https://github.com/ArcadeHustle/Examu-Exboard-Multi/fork

THIS IS INCOMPLETE, NOT FOR PUBLIC CONSUMPTION YET! DO NOT USE

Big thanks to Mitsurugi_w, Darksoft, and Brizzo of Arcade Projects for finally allowing this to be published.
- written by hostile, with supporting information from the community at large!

<p align="center">
<img src="https://github.com/ArcadeHustle/X3_USB_softmod/blob/master/walsdawg.jpeg"><img src="https://github.com/ArcadeHustle/X3_USB_softmod/blob/master/darksoft.jpeg">
</p>

<p align="center">
  <img src="https://github.com/ArcadeHustle/X3_USB_softmod/blob/master/arcadeprojects.jpeg"><img src="https://github.com/ArcadeHustle/X3_USB_softmod/blob/master/brizzo.jpeg">
</p>

# Stage One:
We are sad to report that Arcana Heart Developer Examu to Suspend Business Operations Starting Late February 2020
https://web.archive.org/web/20200210095956/http://www.examu.co.jp/company.html


## Examu-Exboard-Multi
Simple multi for Examu Exboard install instructions

```
gdd if=boot.img of=/dev/disk5 bs=1M
```

# Stage Two:
Tell Brizzo to stop holding out on his copy of Monster Ancient Cline Location Test ROM dump
DM Mitsurugi_w or 64darksoft for pricing, and cart "conversions". 

https://www.youtube.com/watch?v=7uBmP3_TQi4&feature=youtu.be<br>
https://www.youtube.com/watch?v=WJDVqyirYko&feature=youtu.be<br>
https://www.youtube.com/watch?v=99nYjw382Zc&feature=youtu.be<br>

# Stage Three:
## Game installation

Pull the images from Archive.org
https://archive.org/details/Examu-Exboard-XPe-ROM-archive

```
gdd if=ArcanaHeart2.img of=/dev/disk5s2 bs=1M
gdd if=ArcanaHeart3.img of=/dev/disk5s3 bs=1M
gdd if=SuggoiArcanaHeart.img of=/dev/disk5s4 bs=1M
gdd if=DemonBride.img of=/dev/disk5s5 bs=1M
gdd if=MonsterAncientCline_brizzo2020.img of=/dev/disk5s6 bs=1M
```

Edit the default registry entry that launches the games, and point it to the multi loader

```
$ cd /mnt/multidrive/WINDOWS/system32/config
$ cp SOFTWARE SOFTWARE.bak
$ chntpw -e SOFTWARE

chntpw version 0.99.6 110511 , (c) Petter N Hagen
Hive <SOFTWARE> name (from header): <emRoot\System32\Config\SOFTWARE>
ROOT KEY at offset: 0x001020 * Subkey indexing type is: 686c <lh>
File size 5242880 [500000] bytes, containing 1226 pages (+ 1 headerpage)
Used for data: 96634/5139760 blocks/bytes, unused: 827/10640 blocks/bytes.

Simple registry editor. ? for help.

> ed \Microsoft\Windows NT\CurrentVersion\Winlogon\Shell

EDIT: <\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell> of type REG_SZ with length 22 [0x16]
[ 0]: C:\DB1.exe

Now enter new strings, one by one.
Enter nothing to keep old.
[ 0]: C:\DB1.exe
-> C:\FAD.exe
newkv->len: 22
> cat \Microsoft\Windows NT\CurrentVersion\Winlogon\Shell
Value <\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell> of type REG_SZ, data length 22 [0x16]
C:\FAD.exe
> q

Hives that have changed:
 #  Name
 0  <SOFTWARE>
Write hive files? (y/n) [n] : y
 0  <SOFTWARE> - OK
```

Copy the multi loader to the root of the drive. 
```
$ cp ~/main.exe /mnt/multidrive/FAD.exe
```
