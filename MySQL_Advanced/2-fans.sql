-- Rank country origins of bands, ordered by the number of (non-unique) fans

-- Group country oriigns of bands and total number of fans
SELECT origin, SUM(fans) AS nb_fans -- Total of fans by origin
FROM metal_bands -- Table of metal bands
GROUP BY origin -- Grouped by origin
ORDER BY nb_fans DESC; -- Order by number of fans
