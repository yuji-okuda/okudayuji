# 相関サブクエリ（UPDATE）2

tableA の各行に対して、カラム1〜3が一致する tableB の行を検索し、
見つかった場合は tableB のコードを tableA のコードに上書きする。
SET句の相関サブクエリは、Aの行ごとに毎回実行されるため、
「Aの1行 → Bを検索 → 一致したコードを返す」という処理が全行に対して行われる。

update tableA a
set a.コード = (
  select b.コード
  from tableB b
  where b.カラム1 = a.カラム1
    and b.カラム2 = a.カラム2
    and b.カラム3 = a.カラム3
);

tableB のカラム1〜3の組み合わせに重複があるか確認する。
GROUP BY で同じ住所セットをまとめ、HAVING COUNT(*) > 1 で重複だけを抽出する。

select カラム1, カラム2, カラム3, count(*) as cnt
from tableB
group by カラム1, カラム2, カラム3
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

