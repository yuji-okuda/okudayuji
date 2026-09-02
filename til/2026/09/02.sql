# 相関サブクエリ（UPDATE）

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

※　tableB　に一致する行が複数あった場合、エラーが発生する。
ORA-01427: single-row subquery returns more than one row
