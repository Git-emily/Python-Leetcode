import hashlib
strs = ''
param = {'flag':'test','sign':'null','method':'iostock.getList','start_time':'2012-12-08 18:50:30','end_time':'2012-12-09 00:00：00'}
tmp = sorted(param.keys())
for i in tmp:
    strs += i+param[i]
result = hashlib.md5(strs.encode(encoding='utf-8'))
Res = result.hexdigest().upper()
print(Res)
