-- List all bands with Glam rock as their main style, ranked by their longevity

-- Collect groups of Glam rock and calculate their longevity
SELECT band_name, 
       (IFNULL(split, YEAR(CURDATE())) - formed) AS lifespan -- Calculate longevity in years
FROM metal_bands -- Metal bands table
WHERE style LIKE '%Glam rock%' -- Filter by style like Glam rock
ORDER BY lifespan DESC; -- Order by longevity
