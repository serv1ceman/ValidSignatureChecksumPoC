# PE Checksum Manipulator

## Overview

This is a **Proof of Concept (PoC)** demonstrating how to manipulate the **checksum** of a PE (Portable Executable) file, altering its hash while preserving its **Authenticode signature**.

The technique works by modifying a random byte in the checksum field of the PE header, which is excluded from the signature hash calculation. This allows the file’s hash to change while keeping the signature valid, making it possible to bypass hash-based detections and maintain a valid signature.

## Usage

1. Run the script with a target PE file as an argument:

```bash
python main.py path_to_file
```

Example:

```bash
python main.py driver.sys
```

2. The script will:

- Locate the PE checksum.
- Randomly modify one byte of the checksum.
- Write the updated checksum back to the file.

## References

- [Large Scale Exploitation of Legacy Driver – Check Point Research (2025)](https://research.checkpoint.com/2025/large-scale-exploitation-of-legacy-driver/)
- [Authenticode I: Understanding Windows Authenticode – Reversea.me](https://reversea.me/index.php/authenticode-i-understanding-windows-authenticode/)

## Notes

- The file will be modified **in place**.
- Supports both **32-bit and 64-bit** PE files.

## Legal Disclaimer

This PoC is for **educational and research purposes only**. Use it responsibly and do not engage in malicious activity.

