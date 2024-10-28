-- Lists all bands with Glam rock as main style
-- Ranked by longevity
SELECT band_name,
       CASE WHEN split IS NULL THEN 2020 - formed
ELSE split - formed
END AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
