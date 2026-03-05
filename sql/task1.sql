SELECT 
    id,
    scores,
    DENSE_RANK() OVER (ORDER BY scores DESC) as position
FROM 
    examination;
