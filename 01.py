'''
第1章: 準備運動
01. 「パタトクカシーー」
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ
'''
s = 'パタトクカシーー'
print(s[0]+s[2]+s[4]+s[6])
print(''.join([s[i] for i in range(0, len(s), 2)]))
