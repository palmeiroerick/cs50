# E-commerce

By Erick Palmeiro Silva

Video overview: https://www.youtube.com/watch?v=2ttnb72C94A

## Scope

### Purpouse

Manage user orders in an ecommerce.

### Included

- User profiles (`id` and `name` only)
- Products
- Product categories
- Orders
- Order Items

### Excluded

- Addresses
- Payments
- Reviews

## Functional Requirements

### Users should be able to:

- Manage products and product categories.
- Crete orders and manage their items.

### Beyond the scope:

- Manage payments, addresses and reviews.
- Track the status of orders ("created," "paid," "canceled").

## Representation

### Entities

- `categories`:
  - `id`: Identification number used as primary key.
  - `name`: The name of the category.
- `Products`:
  - `id`: Identification number used as primary key.
  - `name`: The name of the product.
  - `category_id`: Foreign key that references `categories.id`.
  - `quantity`: The number of products available in stock.
- `Users:
  - `id`: Identification number used as primary key.
  - `name`: The name of the user.
- `Orders:
  - `id`: Identification number used as primary key.
  - `user_id`: Foreign key that references `users.id`.
  - `total`: The total money for the order.
  - `year`: The year in which the order was placed.
  - `month`: The month in which the order was placed.
  - `day`: The day on which the order was placed.
- `Order_items`:
  - `order_id`: Foreign key that references `orders.id`.
  - `product_id`: Foreign key that references `products.id`.
  - `quantity`: The number of products ordered.

### Relationships

[![](https://mermaid.ink/img/pako:eNptkU1vgzAMhv8K8pkiIIGG3CZAUw8VE9DLhFRFkFG0kqAsSNuA_z4-Oi6bT37tx68le4BSVhwocBU1rFasLYQxR_iUx89JeoozYxwPBzkYL2kSXcI8M6hRSqFZIzbyksXpDiVptChqdHdW8g141BZifBDXUx6f_zjtG_5FWddxpgoBJtSqqYBq1XMTWq5atkgYFpcC9I23vAA6pxVT7wUUYppnOiZepWx_x5Ts6xvQN3b_mFXfVUzzxwH2quKi4iqUvdBAPeysJkAH-ATqY4u4yCd-4BDPJse5-QXUQchycRDYCAW-jVw8mfC9brUt4jizh01sfMTEQ54JvGq0VOft_usbph-icHft?type=png)](https://mermaid.live/edit#pako:eNptkU1vgzAMhv8K8pkiIIGG3CZAUw8VE9DLhFRFkFG0kqAsSNuA_z4-Oi6bT37tx68le4BSVhwocBU1rFasLYQxR_iUx89JeoozYxwPBzkYL2kSXcI8M6hRSqFZIzbyksXpDiVptChqdHdW8g141BZifBDXUx6f_zjtG_5FWddxpgoBJtSqqYBq1XMTWq5atkgYFpcC9I23vAA6pxVT7wUUYppnOiZepWx_x5Ts6xvQN3b_mFXfVUzzxwH2quKi4iqUvdBAPeysJkAH-ATqY4u4yCd-4BDPJse5-QXUQchycRDYCAW-jVw8mfC9brUt4jizh01sfMTEQ54JvGq0VOft_usbph-icHft)

- Users can place zero or many orders (one-to-many).
- Orders can contain one or many order items (one-to-many).
- Categories can contain zero or many products (one-to-many).
- Products can appear in zero or many order items (one-to-many).
- Products and Orders have a many-to-many relationship via `order_items`.

## Optimizations

### Triggers

- `check_stock_on_insert` and `check_stock_on_update`: Check if there is stock available when adding or updating a product to `order_items`.
- `update_stock_on_insert`, `update_stock_on_update`, and `update_stock_on_delete`: When `order_items.quantity` is modified, update the `quantity` value in `products`.
- `update_order_total_on_insert`, `update_order_total_on_update`, and `update_order_total_on_delete`: Updates `orders.total` when adding, updating, or removing products from `order_items`.

### Indexes

- `idx_orders_user_id`: Speed up queries in `order` by `user_id`
- `idx_order_items_order_id`: Speed up queries in `order_items` by `order_id`

## Limitations

- Simplified user data: only ID and name, no email, password, contact information, etc.
- No management of addresses, payments, order status, or product reviews.
- Limited history: no record of price or inventory changes over time.
