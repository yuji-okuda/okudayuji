# テーブルA と　テーブルB の突合確認
テーブルAで存在しない個人ナンバーは、テーブルBに存在しないか
（テーブルBに存在する個人ナンバーは、テーブルAでも存在するか）
※抽出されなければ、存在しない事が証明される

例え
  学齢簿（A）にいない生徒が、バスケ部員名簿（B）にいたらダメ
　バスケ部員名簿（B）にいる生徒は、必ず学齢簿（A）にもいるべき
  
select distinct b.KojinNo 
from tableB b 
left join tableA a 
  on b.KojinNo = a.KojinNo 
where a.KojinNo is null;
