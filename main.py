import random
import os
import sys

file = sys.argv[1]
if not os.path.exists(file):
    print("File does not exist")
    exit()

pDosHeader = 0x00000000
pPESigPointer = 0x0000003c
pPEsignature = 0x00000000

dosHeader = b""
PEsignature = b""
magicNumber = b""
checkSum = b""
is64bit = False

with open(file, "r+b") as f:
    f.seek(pDosHeader)
    dosHeader = f.read(2)

    if dosHeader != b"MZ":
        exit()
    
    f.seek(pPESigPointer)
    pPEsignature = int.from_bytes(f.read(4), byteorder='little')
    pMagicNumber = pPEsignature + 0x00000018
    f.seek(pPEsignature)
    PEsignature = f.read(4)

    if PEsignature != b"PE\0\0":
        exit()
    
    f.seek(pMagicNumber)
    magicNumber = f.read(2)
    if magicNumber == b'\x0b\x01':
        is64bit = False
    elif magicNumber == b'\x0b\x02':
        is64bit = True
    else:
        exit()

    print("Locating checksum")

    if is64bit:
        pCheckSum = pMagicNumber + 0x00000040
    else:
        pCheckSum = pMagicNumber + 0x00000008

    f.seek(pCheckSum)
    checkSumBuffer = f.read(4)
    print(checkSumBuffer)

    print("Modifying checksum")
    checksum = bytearray(checkSumBuffer)

    randomIndex = random.randint(0, 3)
    randomByte = random.randint(0, 255)

    checksum[randomIndex] = randomByte

    f.seek(pCheckSum)
    f.write(checksum)
    f.seek(pCheckSum)
    checkSum = f.read(4)
    print(checkSum)