# Str型  

⚫︎’ “ のどちらかで囲う
※文字列の中で ’ を使用したい場合は、 “ “で囲う（逆も可能）
print(“ I ‘m okuda”)

⚫︎特殊文字は、\ (バックスラッシュ)を使って記述する ‘ を囲み文字としても、
文字列内でも使用したい場合、文字列内にて ‘ の直前に \ を使用することで可能。（”も可能）
print(‘I \ ‘m okuda’)

⚫︎改行　\n ※ \n をそのまま表示させる場合は、 
　\ を直前につける。 

⚫︎複数行の空白をタブで揃える　\t  print('Name\tAddress\tAge\n''Taro\tTokyo\t20\n')
 Name	Address	Age
 Taro	Tokyo   20

⚫︎str型に変換 str()
time = 7
print('只今の時刻は、' + str(time) + '時です。')
