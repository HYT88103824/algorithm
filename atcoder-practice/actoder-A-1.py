'''
配点 : 
100 点

問題文
英大文字・英小文字からなる空でない文字列 
S が与えられます。以下の条件が満たされているか判定してください。

S の先頭の文字は大文字であり、それ以外の文字はすべて小文字である。
制約
1≤|S|≤100（
|S| は文字列 
S の長さ）
S の各文字は英大文字または英小文字である。
入力
入力は以下の形式で標準入力から与えられる。

S
出力
条件が満たされていれば Yes、そうでなければ No を出力せよ。
'''


c = input()

if c[0].isupper() == True:
    print('Yes')
else:
    print('No')
