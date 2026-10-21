# Dockstring(ドッグストリング) 　
モジュール、関数、クラス、メソッドなどの定義をの最初に書く文字列 　
そのオブジェクトの説明・使い方を書く 　
※ “””で囲う（’’’は、使わない）
 
1、関数に使う場合
def greet(name):
	“””
	挨拶をする関数　←　関数の説明を記載

	（補足があれば、記入）

	:param name: 名前
	:return: なし
	“””
	print(f”こんにちは、{name}。”)

greet(“ヒロシ”)
print(greet.__doc__)　←　greet関数のドッグストリングを表示させる

2、モジュールに使う場合 
common.py
“””ここにモジュールのドッグストリングを記載”””

↑ 別の.pyにて、common.pyのモジュールを常時させる場合、2通りあり。
import common

help(common)
もしくは
print(common.__doc__)
print(common.greet__doc__)
