# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals


from Crypto.Cipher import AES


def aes_key(password):
    # 由于aes算法的密钥长度必须为16的倍数，
    # 为了简化起见，我们直接在密钥后边补0至16位
    assert 0 < len(password) <= 16
    return password + '0' * (16 - len(password))


def encrypt(file_name, password):
    with open(file_name, 'rb') as in_file, open(file_name + '.encrypted', 'wb') as out_file:
        # 此处一定要以二进制方式打开
        bs = AES.block_size
        cipher = AES.new(password)
        flag = True
        while flag:
            chunk_data = in_file.read(1024 * bs)
            # 每次按块读取文件，aes算法要求加密的数据都是16的倍数
            if len(chunk_data) == 0 or len(chunk_data) % bs != 0:
                padding_length = (bs - len(chunk_data) % bs) or bs
                chunk_data += chr(padding_length).encode() * padding_length
                # 读到文件末尾时，可能不为16的整数倍了，那么就要补至16位
                # 可以将补的数据长度作为补的内容，
                # 这样解密时可以利用这个信息把补充的数据删除。
                flag = False
            out_file.write(cipher.encrypt(chunk_data))


def decrypt(file_name, password):
    with open(file_name, 'rb') as in_file, open(file_name + '.decrypted', 'wb') as out_file:
        bs = AES.block_size
        cipher = AES.new(password)
        next_chunk = b''
        flag = True
        while flag:
            # 每次都读一块，但是保留前一块的信息。
            chunk, next_chunk = next_chunk, cipher.decrypt(in_file.read(1024 * bs))
            # 前面加密时补充的数据在这里就有用了。
            if len(next_chunk) == 0:
                try:
                    padding_length = ord(chunk[-1])
                except:
                    padding_length = chunk[-1]
                ''' 在python3中，我们不要使用ord函数，
                    这里采用了非常粗暴的解决方式来兼容Python2/3，
                    你能想到更好的解决方案么？
                '''
                chunk = chunk[:-padding_length]
                flag = False
            out_file.write(chunk)


if __name__ == '__main__':
    password = aes_key('hahah')
    # 'hahah'是我们输入的密码，先将密码预处理一下，满足aes算法的要求。
    encrypt('test.txt', password)
    decrypt('test.txt.encrypted', password)
    # 记得修改解密后的文件名
