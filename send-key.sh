stty -F /dev/serial0 9600 raw -echo -icrnl

echo -n "Key ? "
read -s KEY
echo

echo -n "$KEY" > /dev/serial0
