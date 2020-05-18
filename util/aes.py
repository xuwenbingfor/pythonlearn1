#  aes-128-ecb PKCS5Padding
import base64

from Crypto.Cipher import AES


def AES_encrypt(secret_key, data):
    """
    :param secret_key [str] : 加密秘钥
    :param data [str] : 需要加密数据
    :return   [str] :
    """
    BLOCK_SIZE = 16  # Bytes
    # 数据进行 PKCS5Padding 的填充
    pad = lambda s: (s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE))
    raw = pad(str(data))
    # 通过key值，使用ECB模式进行加密
    cipher = AES.new(base64.b64decode(secret_key), AES.MODE_ECB)
    # 得到加密后的字节码
    encrypted_text = cipher.encrypt(bytes(raw, encoding='utf-8'))
    # 字节码转换成十六进制  再转成 字符串
    # encrypted_text_hex = str(b2a_hex(encrypted_text), encoding='utf-8')
    encrypted_text_hex = base64.b64encode(encrypted_text).decode("utf-8")
    return encrypted_text_hex


def AES_decrypt(secret_key, encrypted_text_hex):
    """
    :param secret_key [str] : 加密秘钥
    :param encrypted_text_hex [str]: # 加密后的 data 字符串
    :return [str]:
    """
    # 去掉 PKCS5Padding 的填充
    unpad = lambda s: s[:-ord(s[len(s) - 1:])]
    # 通过 key 值进行
    cipher = AES.new(base64.b64decode(secret_key), AES.MODE_ECB)
    # data_response = unpad(cipher.decrypt(a2b_hex(encrypted_text_hex))).decode('utf8')
    data_response = unpad(cipher.decrypt(base64.b64decode(encrypted_text_hex))).decode('utf8')
    return data_response


if __name__ == '__main__':
    secret_key = "N2+JDVCY2szurypikytIXA=="  # 秘钥 （需要16位,base64方式24位）
    dataEncrypt = AES_encrypt(secret_key, "123456789")  # 加密
    print(dataEncrypt)  # 打印加密后的数据
    data = AES_decrypt(secret_key, dataEncrypt)  # 解密
    print(data)  # 打印解密后的数据
