Задание 3: Покупки
create table account
(
    id integer, -- ID счета
    client_id integer, -- ID клиента
    open_dt date, -- дата открытия счета
    close_dt date -- дата закрытия счета
)

create table transaction
(
    id integer,  -- ID транзакции
    account_id integer,  -- ID счета
    transaction_date date,  -- дата транзакции
    amount numeric(10,2), -- сумма транзакции
    type varchar(3) -- тип транзакции
)
Вывести ID клиентов, которые за последний месяц по всем своим счетам совершили покупок меньше, чем на 5000 рублей.

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
    
