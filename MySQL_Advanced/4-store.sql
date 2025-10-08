-- Trigger for decreasing the quantity of one item after adding of new order

DELIMITER //

CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number -- Decrease the quantity of an item
    WHERE name = NEW.item_name; -- According to the name of the item
END;
//

DELIMITER ;