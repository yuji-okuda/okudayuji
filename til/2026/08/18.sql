# テーブルA と　テーブルB の突合確認
テーブルAで存在しない個人ナンバーは、テーブルBに存在しないか
（テーブルBに存在する個人ナンバーは、テーブルAでも存在するか）
※抽出されなければ、存在しない事が証明される
  
select distinct b.KojinNo 
from tableB b 
left join tableA a 
  on b.KojinNo = a.KojinNo 
where a.KojinNo is null;
