# function sha3_with_check_out_size() {
# 						var chkObjs = document.getElementsByName("sha_3_out_size");
# 						var out_size = 512;
# 						for(var i=0;i<chkObjs.length;i++){
# 							if(chkObjs[i].checked){
# 								out_size = chkObjs[i].value;
# 								break;
# 							}
# 						}
# 						document.getElementById('sha_3_output').value = CryptoJS.SHA3(document.getElementById('sha_3_input').value, { outputLength:  out_size});
# 					}
				

import pyperclip
import time
#import hashlib
import sha3

# s=hashlib.sha256()




# s=sha3.sha3_256()
# print(s.name)
# s.update("ddsdfjaflkata")
# ss=str(s.hexdigest())
# pyperclip.copy(ss)
# # text=pyperclip.paste()


# print(s.hexdigest())
# # print(text)



hash=sha3.sha3_256()

start = time.time()
# filePath = '/home/erving/Documents/大三上/计算机安全学/Cryptography_Hw&Ex/Ex7/file.php'
filePath='/media/erving/4CC6F585C6F56F96/迅雷下载/第九区.mkv'

def hashs(filePath, type="sha256", block_size=1024*1024):
    with open(filePath, 'rb') as file:
        hash= sha3.sha3_256()
        while True:
            data = file.read(block_size)
            if not data:
                break
            hash.update(data)
        return hash.hexdigest()

print("Let's Go!")
result = hashs(filePath)
pyperclip.copy(str(result))
end=time.time()
print(result)
print("Copied Successfully!")
elapsed = end-start
print("Using time:",elapsed)
