-- List all bands with Glam rock as their main style, 
-- ranked by their longevity

-- Collect groups of Glam rock and calculate their longevity
SELECT band_name, -- Calculate longevity
       (IFNULL(split, YEAR(CURDATE())) - formed) AS lifespan 
FROM metal_bands -- Metal bands table
WHERE style LIKE '%Glam rock%' -- Filter by style like Glam rock
ORDER BY lifespan DESC; -- Order by longevity
