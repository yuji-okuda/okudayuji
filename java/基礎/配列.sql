
# 配列
　※同じ型の変数をまとめた集合体。1つ1つの変数を要素という。

## 配列宣言
　型名[] 配列名　＝　new 型名[要素数];

　String[] animals = new String[3];
　String[0] ='犬';
　String[1] ='猫';
　String[2] ='ハムスター';

## 配列宣言 と同時に 複数の要素を初期化 ※以下どちらでも初期化が可能
　String[] animals = new String[]{'犬','猫','ハムスター'};
　String[] animals = {'犬','猫','ハムスター'};

## 配列の要素数を取得

　配列名.length
   
