# 個人番号ごとに履歴番号が最大のデータを特定し、
## そのデータの受付日をNULLに更新する
 
UPDATE テーブル名 t
SET 受付日 = NULL
WHERE (t.個人番号, t.履歴番号) IN (
SELECT 個人番号, MAX(履歴番号)
FROM テーブル名
GROUP BY 個人番号
);

## 確認用
※個人番号ごとに履歴番号が最大のレコードを抽出
※GROUP BY 個人番号 で個人番号ごとにグループ化
※MAX(履歴番号) で各個人番号の最新履歴番号を取得
 
SELECT
t.個人番号,
t.履歴番号,
t.受付日
FROM テーブル名 t
WHERE (t.個人番号, t.履歴番号) IN (
SELECT
個人番号,
MAX(履歴番号)
FROM テーブル名
GROUP BY 個人番号
);
