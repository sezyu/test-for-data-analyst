SELECT
    account.client_id
FROM
    account
LEFT JOIN
    transaction ON account.id = t.account_id
    AND t.transaction_date >= current_date - interval '1 month'
GROUP BY
    account.client_id
HAVING
  COALESCE(sum(t.amount), 0) < 5000.00
    
