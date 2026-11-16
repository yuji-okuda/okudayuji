# 算術演算子
//『 ++ 』
//『 ++X 』
 ＋1をしてから、式を実行する
   （例）X=5の時、Y = ++X → Yの値は6、Xの値は6

//『 X++ 』
 式を実行してから、＋1をする
   （例）X=5の時、Y = X++ → Yの値は5、Xの値は6

# 関係演算子

//『 == 』(数値以外でも使用可能:char型)
       
char textA ='あ';
char textB ='あ';
boolean textZ = textA == textB;
System.out.println(textZ);

- true

//『 == 』(数値以外でも使用可能:boolean型)

boolean boxA =true;
boolean boxB =false;
boolean boxZ = boxA == boxB;
System.out.println(boxZ);

- false
