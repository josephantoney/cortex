'''function to generate md5 checksum for given input
:param plainText: The input content
:return: returns md5checksum
'''

import hashlib
class FileHandler:
    @classmethod
    def generateFileName(cls,plainText):
        checksum = hashlib.md5()
        checksum.update(plainText.encode('utf-8'))
        return checksum.hexdigest()