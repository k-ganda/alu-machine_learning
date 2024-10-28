-- Lists all bands with Glam rock as main style
-- Ranked by longevity
SELECT 
    band_name,
    (2020 - formed) - (CASE WHEN split IS NOT NULL THEN split - formed ELSE 0 END) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
