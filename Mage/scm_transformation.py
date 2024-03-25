if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    dim_product = df[['product_card_id', 'product_name', 'product_price', 'category_name']].reset_index(drop=True)
    dim_product['p_id'] = dim_product.index+1
    dim_product = dim_product[['p_id','product_card_id', 'product_name', 'product_price', 'category_name']]
    dim_order = df[['order_id', 'order_date', 'order_month', 'order_year','order_status','order_city','order_state','order_country','order_region','market']].reset_index(drop=True)
    dim_order['o_id'] = dim_order.index+1
    dim_order=dim_order[['o_id','order_id', 'order_date', 'order_month', 'order_year','order_status','order_city','order_state','order_country','order_region','market']]
    dim_department = df[['department_id', 'department_name']].reset_index(drop=True)
    dim_department['d_id'] = dim_department.index+1
    dim_department = dim_department[['d_id','department_id', 'department_name']]
    dim_customer = df[['customer_id','customer_fname','customer_lname','customer_segment','customer_state','customer_city','customer_street','customer_zipcode','customer_country']].reset_index(drop=True)
    dim_customer['c_id'] = dim_customer.index+1
    dim_customer = dim_customer[['c_id','customer_id','customer_fname','customer_lname','customer_segment','customer_state','customer_city','customer_street','customer_zipcode','customer_country']]
    dim_shipping = df[['shipping_date','shipping_month','shipping_year','shipping_mode','days_for_shipping','days_for_shipment','delivery_status','late_delivery_risk']].reset_index(drop=True)
    dim_shipping['s_id'] = dim_shipping.index+1
    dim_shipping=dim_shipping[['s_id','shipping_date','shipping_month','shipping_year','shipping_mode','days_for_shipping','days_for_shipment','delivery_status','late_delivery_risk' ]]
    raw_sales = df[['sales_id','sales', 'order_item_quantity','order_item_total','benefit_per_order','order_item_discount','order_item_discount_rate']].reset_index(drop=True)
    fact_sales = raw_sales.merge(dim_product, left_on='sales_id', right_on='p_id') \
                        .merge(dim_order, left_on='sales_id', right_on='o_id') \
                        .merge(dim_department, left_on='sales_id', right_on='d_id') \
                        .merge(dim_customer, left_on='sales_id', right_on='c_id') \
                        .merge(dim_shipping, left_on='sales_id', right_on='s_id') \
                        [['sales_id','c_id','p_id','o_id','d_id','s_id','sales', 'order_item_quantity','order_item_total','benefit_per_order','order_item_discount','order_item_discount_rate']]
    return {
        'dim_product': dim_product.to_dict(orient='dict'),
        'dim_order': dim_order.to_dict(orient='dict'),
        'dim_department': dim_department.to_dict(orient='dict'),
        'dim_customer': dim_customer.to_dict(orient='dict'),
        'dim_shipping': dim_shipping.to_dict(orient='dict'),
        'fact_sales': fact_sales.to_dict(orient='dict')
    }


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
