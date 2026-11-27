
# not exists

SELECT
    A.ID,
    A.NAME
FROM
    A_TABLE A
WHERE
    NOT EXISTS (
        SELECT
            1
        FROM
            B_TABLE B
        WHERE
            B.ID = A.ID
    );

SQLの意味
① Aテーブルからデータを取得する

② Bテーブルに、AテーブルのIDと一致するデータがあるか確認する

③ NOT EXISTS によって、Bテーブルに存在しないデータだけ抽出する
