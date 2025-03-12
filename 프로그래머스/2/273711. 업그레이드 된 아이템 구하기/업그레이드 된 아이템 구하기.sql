-- 코드를 작성해주세요
SELECT it.item_id, item_name, rarity
FROM item_info ii
JOIN item_tree it on ii.item_id = it.item_id
WHERE it.parent_item_id in (SELECT item_id
                            FROM item_info
                            WHERE rarity = 'rare')
ORDER BY 1 desc;