# 相関サブクエリ（UPDATE）2

tableB のカラム1〜3とコードの組み合わせに重複があるか確認する場合、
（カラム1〜3とコードが常に1セットで一意になる前提）
GROUP BY でセットをまとめ、HAVING COUNT(*) > 1 で重複だけを抽出する。

select カラム1, カラム2, カラム3, コード, count(*) as cnt
from tableB
group by カラム1, カラム2, カラム3, コード
having count(*) > 1;


tableB のカラム1〜3の組み合わせに重複があった場合、
tableB　を以下と置き換えてSQLを作成する。
（select カラム1, カラム2, カラム3, コード
from tableB
group by カラム1, カラム2, カラム3, コード）

update tableA a
set a.コード = (
  select b.コード
  from （
      select カラム1, カラム2, カラム3, コード
      from tableB
      group by カラム1, カラム2, カラム3, コード
  ） b
  where b.カラム1 = a.カラム1
    and b.カラム2 = a.カラム2
    and b.カラム3 = a.カラム3
);

