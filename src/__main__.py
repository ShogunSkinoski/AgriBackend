import qrcode

qrcode.make('greenhouse_id=1&sector_id=1').save("./qr.png")