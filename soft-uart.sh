echo -n "Key ? "
read -s KEY

pigs m 26 0
pigs m 26 w
pigs mg 26

pigs wvclr
pigs wvas 26 9600 8 2 0 $(printf "%s" "$KEY" | od -An -tx1 | sed "s/ / 0x/g") >/dev/null
WID=$(pigs wvcre)
pigs wvtx $WID >/dev/null
