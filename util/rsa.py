import base64

import Crypto.Signature.PKCS1_v1_5 as sign_PKCS1_v1_5  # 用于签名/验签
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5  # 用于加密
from Crypto.Hash import MD5
from Crypto.PublicKey import RSA

# 公钥
PUBLIC_KEY_STR = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDOvmHvJo1cdCz798TcdsYUoH5SVFwezneb+tQAiLAkWofTESILKLGfbsKdSe30izEW4TDWR1O9ydf8pDJZ2V58jLQihop7PL3DW4CrNKFRavSsGpqRCt9Klyej1wb9mvvIUoyyr8MLSLhNkWoxdHNMeShs+7ddMNPfbTyLDSXP2wIDAQAB"
# 私钥
PRIVATE_KEY_STR = "MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAM6+Ye8mjVx0LPv3xNx2xhSgflJUXB7Od5v61ACIsCRah9MRIgsosZ9uwp1J7fSLMRbhMNZHU73J1/ykMlnZXnyMtCKGins8vcNbgKs0oVFq9KwampEK30qXJ6PXBv2a+8hSjLKvwwtIuE2RajF0c0x5KGz7t10w099tPIsNJc/bAgMBAAECgYAp7FY8ohMxR8elcolDcXxaS29CL6QchR6hDRx3XUBmpsr7JHLEU4StQU8KiSbNG3qhWpnGIeGbzzXSn9MsABWWC69RUOZeKtlJiJXicGW7jLaPKXfJckZrxibXASV7h/VqC27gtWxGwBCCn7rIPR93OmpJUc9qQt0MqyC/1vZmYQJBAO5zS2Z+sdCqsdurnjski3O92EOJwi5OpgwvqVpbB0ZuekvlaJbCEQFnKtwfUM+LlQHrv2ZCvoSlHSY8HtROOPsCQQDd9bGuxi1u5b53m73nHdNMBNT54pZcbYtEmPf+Hx1vm74aXIGoLcVsTqCyAojh3ClaVQW7Hta+Jjv4Unm7Ls6hAkEAzS808KuQwyg/B/HzpJzbyurPz74Y89QFmnLg3bl61yZ14h00FJZGH9jwzp274fwQaqi7+HjyjB2wqZgOR05QRQJAMwWcf5mMrhZfzyzc3XjMrofZ0UtV1w9TWUR0lVTftl0tuO+U2m0TGc+FPwY4IvsyAlLTC22OXY16cZ2739xloQJBAJdCQPBJQhvUtahIGHbWqIhMbkatm/S4gCbb0QeSfpNytZef8/JyqkMBIzRc2izXcKcPj27CkdlFp6m/Peq1zvQ="
# 编码
UTF8 = 'utf-8'


def handle_key(keystr, type=1):
    '''
        公钥格式pem，处理成以-----BEGIN PUBLIC KEY-----开头，-----END PUBLIC KEY-----结尾的格式
        type==1:公钥  type==2：私钥
    '''
    start = '-----BEGIN PUBLIC KEY-----\n'
    end = '-----END PUBLIC KEY-----'
    if type == 2:
        start = '-----BEGIN RSA PRIVATE KEY-----\n'
        end = '-----END RSA PRIVATE KEY-----'
    result = ''
    # 分割key，每64位长度换一行
    divide = int(len(keystr) / 64)
    divide = divide if (divide > 0) else divide + 1
    line = divide if (len(keystr) % 64 == 0) else divide + 1
    for i in range(line):
        result += keystr[i * 64:(i + 1) * 64] + '\n'
    result = start + result + end
    return result


def rsaEncrypt(plain_text):
    '''
        公钥加密
    '''
    # 加载公钥
    public_key_pem = handle_key(PUBLIC_KEY_STR)
    public_key = RSA.import_key(public_key_pem)

    # 公钥加密
    cipher_pub_obj = PKCS1_v1_5.new(public_key)
    secret_bytes = cipher_pub_obj.encrypt(plain_text.encode(encoding=UTF8))
    secret_b64 = base64.b64encode(secret_bytes)
    secret_b64_str = str(secret_b64, encoding=UTF8)
    return secret_b64_str


def rsaDecrypt(secret_b64_str):
    '''
        私钥解密
    '''
    # 加载私钥
    private_key_pem = handle_key(PRIVATE_KEY_STR, 2)
    private_key = RSA.import_key(private_key_pem)

    secret_bytes = base64.b64decode(secret_b64_str)
    # 私钥解密
    cipher_pri = PKCS1_v1_5.new(private_key)
    plain_byte = cipher_pri.decrypt(secret_bytes, Random.new().read)
    plain_text = plain_byte.decode(UTF8)
    return plain_text


def sign(plain_text):
    '''
        签名
    '''
    # 加载私钥
    private_key_pem = handle_key(PRIVATE_KEY_STR, 2)
    private_key = RSA.import_key(private_key_pem)

    # md5withrsa
    signer = sign_PKCS1_v1_5.new(private_key)
    hash_obj = MD5.new(plain_text.encode(UTF8))

    signature = base64.b64encode(signer.sign(hash_obj)).decode(UTF8)
    return signature


def verify(plain_text, signature):
    '''
        验签
    '''
    # 加载公钥
    public_key_pem = handle_key(PUBLIC_KEY_STR)
    public_key = RSA.import_key(public_key_pem)

    verifier = sign_PKCS1_v1_5.new(public_key)

    # md5withrsa
    hash_obj = MD5.new(plain_text.encode(UTF8))

    is_verify = verifier.verify(hash_obj, base64.b64decode(signature))
    return is_verify


if __name__ == '__main__':
    plain_text = 'hello world!'
    print('原文内容', plain_text)
    secret_content = rsaEncrypt(plain_text)
    print('加密内容', secret_content)
    content = rsaDecrypt(secret_content)
    print('解密内容', content)

    signature = sign(plain_text)
    print('验签内容', plain_text)
    print('签名内容', signature)
    is_verify = verify(plain_text, signature)
    print('验签结果', is_verify)