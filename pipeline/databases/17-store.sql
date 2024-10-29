-- create a trigger that decreases quantity of an item after adding a new order
-- quantity can be negative
DROP TRIGGER IF EXISTS decrease_quantity;
DELIMITER //
CREATE TRIGGER decrease_quantity AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	IF EXISTS (SELECT 1 FROM items WHERE name = NEW.item_name) THEN
        UPDATE items
        SET quantity = quantity - NEW.quantity
        WHERE name = NEW.item_name;
    END IF;
END;
//
DELIMITER ;
