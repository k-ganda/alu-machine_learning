-- Lists all bands with Glam rock as main style
-- Ranked by longevity
SELECT 
    band_name,
    CASE 
	        WHEN formed IS NOT NULL AND split IS NOT NULL THEN split - formed
			        WHEN formed IS NOT NULL AND split IS NULL THEN 2020 - formed
					        ELSE NULL
							    END AS lifespan
							FROM 
							    metal_bands
							WHERE 
							    style = 'Glam rock' AND formed IS NOT NULL
							ORDER BY 
							    lifespan DESC;
