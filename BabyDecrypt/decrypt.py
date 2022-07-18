"""
This took me much longer than it should have as I got stuck on the import errors for quite some time. After
figuring out that i should just reverse the encryption, i decided that instead of trying to figure out
the inverse of modulo, i could simply make a dict of all encrypted values with their decrypted plaintext
values as a key pair, then iterate over the encrypted values to linearly find the corresponding plaintext.

After submitting my answer and sseeing how others approached it, I learned that I could and probably should
have used bytes.fromhex() instead of my string iterator but in this context my solution was fine.
"""

solution = {}
for i in range(1,256):
    solution[(123 * i + 18) % 256] = chr(i)

to_dec = "6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921"
flag = ""

for x in range(0, len(to_dec), 2):
    decrypt_letter = int(to_dec[x:x+2], 16)
    flag = flag + solution[decrypt_letter]
print(flag)
