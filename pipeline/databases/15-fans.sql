-- Ranks country origins of bands
-- Ordered by no of unique fans
SELECT origin, COUNT(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
