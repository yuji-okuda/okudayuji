# not like を使った抽出

※番号の先頭が9になっている個人番号を全て削除する
  
SELECT *　FROM table_name
WHERE kojin_bango NOT LIKE '9%';

DELETE FROM table_name
WHERE kojin_bango NOT LIKE '9%';
