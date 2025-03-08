-- 코드를 작성해주세요
SELECT ii.item_id,
        item_name,
        rarity
FROM item_info ii
JOIN item_tree it on ii.item_id = it.item_id
WHERE it.item_id not in (SELECT parent_item_id
                         FROM item_tree
                         WHERE parent_item_id is not null
                        )
ORDER BY 1 desc;