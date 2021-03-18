from up9lib import *
from authentication import authenticate
import hipstershop_pb2
import hipstershop_pb2_grpc

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests_adservice_default(unittest.TestCase):

    @json_dataset('data/dataset_8.json')
    @clear_session({'spanId': 8})
    def test_08_post_hipstershop_AdService_GetAds(self, data_row):
        field_1, = data_row

        # POST http://adservice.default/hipstershop.AdService/GetAds (endp 8)
        adservice_default = get_http_target('TARGET_ADSERVICE_DEFAULT', authenticate)
        adservice_default.set_grpc(hipstershop_pb2_grpc.AdServiceStub)
        msg = hipstershop_pb2.GetAdsReq()
        apply_into_protobuf(msg, '1', field_1)
        resp = adservice_default.grpc_stub.GetAds(msg)
        resp = wrap_grpc_for_tracing(resp)


@data_driven_tests
class Tests_cartservice_default(unittest.TestCase):

    @json_dataset('data/dataset_3.json')
    @clear_session({'spanId': 3})
    def test_03_post_hipstershop_CartService_AddItem(self, data_row):
        field_2_1, field_2_2 = data_row

        # POST http://cartservice.default/hipstershop.CartService/AddItem (endp 3)
        cartservice_default = get_http_target('TARGET_CARTSERVICE_DEFAULT', authenticate)
        cartservice_default.set_grpc(hipstershop_pb2_grpc.CartServiceStub)
        msg = hipstershop_pb2.AddItemReq()
        apply_into_protobuf(msg, '1', str(uuid.uuid4()))
        apply_into_protobuf(msg, '2.1', field_2_1)
        apply_into_protobuf(msg, '2.2', field_2_2)
        resp = cartservice_default.grpc_stub.AddItem(msg)
        resp = wrap_grpc_for_tracing(resp)

    @clear_session({'spanId': 11})
    def test_11_post_hipstershop_CartService_EmptyCart(self):
        # POST http://cartservice.default/hipstershop.CartService/EmptyCart (endp 11)
        cartservice_default = get_http_target('TARGET_CARTSERVICE_DEFAULT', authenticate)
        cartservice_default.set_grpc(hipstershop_pb2_grpc.CartServiceStub)
        msg = hipstershop_pb2.EmptyCartReq()
        apply_into_protobuf(msg, '1', str(uuid.uuid4()))
        resp = cartservice_default.grpc_stub.EmptyCart(msg)
        resp = wrap_grpc_for_tracing(resp)

    @clear_session({'spanId': 4})
    def test_04_post_hipstershop_CartService_GetCart(self):
        # POST http://cartservice.default/hipstershop.CartService/GetCart (endp 4)
        cartservice_default = get_http_target('TARGET_CARTSERVICE_DEFAULT', authenticate)
        cartservice_default.set_grpc(hipstershop_pb2_grpc.CartServiceStub)
        msg = hipstershop_pb2.GetCartReq()
        apply_into_protobuf(msg, '1', str(uuid.uuid4()))
        resp = cartservice_default.grpc_stub.GetCart(msg)
        resp = wrap_grpc_for_tracing(resp)


@data_driven_tests
class Tests_checkoutservice_default(unittest.TestCase):

    @json_dataset('data/dataset_10.json')
    @clear_session({'spanId': 10})
    def test_10_post_hipstershop_CheckoutService_PlaceOrder(self, data_row):
        field_1, field_2, field_3_1, field_3_2, field_3_4, field_3_5, field_5, field_6_1, field_6_2, field_6_3 = data_row

        # POST http://checkoutservice.default/hipstershop.CheckoutService/PlaceOrder (endp 10)
        checkoutservice_default = get_http_target('TARGET_CHECKOUTSERVICE_DEFAULT', authenticate)
        checkoutservice_default.set_grpc(hipstershop_pb2_grpc.CheckoutServiceStub)
        msg = hipstershop_pb2.PlaceOrderReq()
        apply_into_protobuf(msg, '1', field_1)
        apply_into_protobuf(msg, '2', field_2)
        apply_into_protobuf(msg, '3.1', field_3_1)
        apply_into_protobuf(msg, '3.2', field_3_2)
        apply_into_protobuf(msg, '3.3', 'CA')
        apply_into_protobuf(msg, '3.4', field_3_4)
        apply_into_protobuf(msg, '3.5', field_3_5)
        apply_into_protobuf(msg, '5', field_5)
        apply_into_protobuf(msg, '6.1', field_6_1)
        apply_into_protobuf(msg, '6.2', field_6_2)
        apply_into_protobuf(msg, '6.3', field_6_3)
        apply_into_protobuf(msg, '6.4', 1)
        resp = checkoutservice_default.grpc_stub.PlaceOrder(msg)
        resp = wrap_grpc_for_tracing(resp)
        # assert_grpc(resp, '1.4.1', expected_value='1600 Amphitheatre Parkway')


@data_driven_tests
class Tests_currencyservice_default(unittest.TestCase):

    @json_dataset('data/dataset_1.json')
    @clear_session({'spanId': 1})
    def test_01_post_hipstershop_CurrencyService_Convert(self, data_row):
        field_2, = data_row

        # POST http://currencyservice.default/hipstershop.CurrencyService/Convert (endp 1)
        currencyservice_default = get_http_target('TARGET_CURRENCYSERVICE_DEFAULT', authenticate)
        currencyservice_default.set_grpc(hipstershop_pb2_grpc.CurrencyServiceStub)
        msg = hipstershop_pb2.ConvertReq()
        apply_into_protobuf(msg, '1.1', 'USD')
        apply_into_protobuf(msg, '1.2', int(random.randint(4, 2245)))
        apply_into_protobuf(msg, '1.3', int(random.randint(220000000, 990000000)))
        apply_into_protobuf(msg, '2', field_2)
        resp = currencyservice_default.grpc_stub.Convert(msg)
        resp = wrap_grpc_for_tracing(resp)

    @clear_session({'spanId': 2})
    def test_02_post_hipstershop_CurrencyService_GetSupportedCurrencies(self):
        # POST http://currencyservice.default/hipstershop.CurrencyService/GetSupportedCurrencies (endp 2)
        currencyservice_default = get_http_target('TARGET_CURRENCYSERVICE_DEFAULT', authenticate)
        currencyservice_default.set_grpc(hipstershop_pb2_grpc.CurrencyServiceStub)
        msg = hipstershop_pb2.GetSupportedCurrenciesReq()
        resp = currencyservice_default.grpc_stub.GetSupportedCurrencies(msg)
        resp = wrap_grpc_for_tracing(resp)


@data_driven_tests
class Tests_emailservice_default(unittest.TestCase):

    @json_dataset('data/dataset_15.json')
    @clear_session({'spanId': 15})
    def test_15_post_hipstershop_EmailService_SendOrderConfirmation(self, data_row):
        field_1, field_2_2, field_2_3_1, field_2_4_1, field_2_4_2, field_2_4_4, field_2_4_5, field_2_5_1_1, field_2_5_2_1 = data_row

        # POST http://emailservice.default/hipstershop.EmailService/SendOrderConfirmation (endp 15)
        emailservice_default = get_http_target('TARGET_EMAILSERVICE_DEFAULT', authenticate)
        emailservice_default.set_grpc(hipstershop_pb2_grpc.EmailServiceStub)
        msg = hipstershop_pb2.SendOrderConfirmationReq()
        apply_into_protobuf(msg, '1', field_1)
        apply_into_protobuf(msg, '2.1', str(uuid.uuid4()))
        apply_into_protobuf(msg, '2.2', field_2_2)
        apply_into_protobuf(msg, '2.3.1', field_2_3_1)
        apply_into_protobuf(msg, '2.3.2', int(random.randint(4, 116)))
        apply_into_protobuf(msg, '2.3.3', int(random.randint(20000000, 999999999)))
        apply_into_protobuf(msg, '2.4.1', field_2_4_1)
        apply_into_protobuf(msg, '2.4.2', field_2_4_2)
        apply_into_protobuf(msg, '2.4.3', 'CA')
        apply_into_protobuf(msg, '2.4.4', field_2_4_4)
        apply_into_protobuf(msg, '2.4.5', field_2_4_5)
        apply_into_protobuf(msg, '2.5.1.1', field_2_5_1_1)
        apply_into_protobuf(msg, '2.5.1.2', int(random.randint(1, 15)))
        apply_into_protobuf(msg, '2.5.2.1', field_2_5_2_1)
        apply_into_protobuf(msg, '2.5.2.2', int(random.randint(12, 2244)))
        apply_into_protobuf(msg, '2.5.2.3', int(random.randint(299999999, 999999999)))
        resp = emailservice_default.grpc_stub.SendOrderConfirmation(msg)
        resp = wrap_grpc_for_tracing(resp)


@data_driven_tests
class Tests_frontend_default(unittest.TestCase):

    @json_dataset('data/dataset_16.json')
    @clear_session({'spanId': 16})
    def test_16_get_(self, data_row):
        s, vars_0_ = data_row

        # GET http://frontend.default/ (endp 16)
        frontend_default = get_http_target('TARGET_FRONTEND_DEFAULT', authenticate)
        qstr = '?' + urlencode([('XDEBUG_SESSION_START', 'phpstorm'), ('function', 'call_user_func_array'), ('s', s), ('vars[0]', vars_0_)])
        resp = frontend_default.get('/' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('header div.navbar div.container.d-flex.justify-content-between div.h-free-shipping', expected_value='Free shipping with $75 purchase! \xa0\xa0')
        # resp.assert_cssselect('html head title', expected_value='Online Boutique')

    @json_dataset('data/dataset_48.json')
    @clear_session({'spanId': 48})
    def test_48_get_(self, data_row):
        content, = data_row

        # GET http://frontend.default/ (endp 48)
        frontend_default = get_http_target('TARGET_FRONTEND_DEFAULT', authenticate)
        qstr = '?' + urlencode([('a', 'fetch'), ('content', content)])
        resp = frontend_default.get('/' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('header div.navbar div.container.d-flex.justify-content-between div.h-free-shipping', expected_value='Free shipping with $75 purchase! \xa0\xa0')
        # resp.assert_cssselect('html head title', expected_value='Online Boutique')

    @clear_session({'spanId': 22})
    def test_22_get__healthz(self):
        # GET http://frontend.default/_healthz (endp 22)
        frontend_default = get_http_target('TARGET_FRONTEND_DEFAULT', authenticate)
        resp = frontend_default.get('/_healthz')
        resp.assert_ok()
        # resp.assert_status_code(200)

    @json_dataset('data/dataset_17.json')
    @clear_session({'spanId': 17})
    def test_17_post_cart(self, data_row):
        product_id, = data_row

        # POST http://frontend.default/cart (endp 17)
        frontend_default = get_http_target('TARGET_FRONTEND_DEFAULT', authenticate)
        resp = frontend_default.post('/cart', data=[('product_id', product_id), ('quantity', str(random.randint(1, 10)))])
        resp.assert_ok()
        # resp.assert_status_code(302)

    @clear_session({'spanId': 18})
    def test_18_get_cart(self):
        # GET http://frontend.default/cart (endp 18)
        frontend_default = get_http_target('TARGET_FRONTEND_DEFAULT', authenticate)
        resp = frontend_default.get('/cart')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('main.cart div.cart-bg div.container div.row.checkout div h3.text-center', expected_value='Checkout')
        # resp.assert_cssselect('html head title', expected_value='Online Boutique')

    @json_dataset('data/dataset_19.json')
    @clear_session({'spanId': 19})
    def test_19_post_cart_checkout(self, data_row):
        city, country, credit_card_cvv, credit_card_expiration_year, credit_card_number, email_, street_address, zip_code = data_row

        # POST http://frontend.default/cart/checkout (endp 19)
        frontend_default = get_http_target('TARGET_FRONTEND_DEFAULT', authenticate)
        resp = frontend_default.post('/cart/checkout', data=[('city', city), ('country', country), ('credit_card_cvv', credit_card_cvv), ('credit_card_expiration_month', '1'), ('credit_card_expiration_year', credit_card_expiration_year), ('credit_card_number', credit_card_number), ('email', email_), ('state', 'CA'), ('street_address', street_address), ('zip_code', zip_code)])
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('main.order div div.container div.row.text-center a.btn.btn-info', expected_value='Keep Browsing')
        # resp.assert_cssselect('html head title', expected_value='Online Boutique')

    @json_dataset('data/dataset_20.json')
    @clear_session({'spanId': 20})
    def test_20_get_product_href(self, data_row):
        href, = data_row

        # GET http://frontend.default/product/{href} (endp 20)
        frontend_default = get_http_target('TARGET_FRONTEND_DEFAULT', authenticate)
        resp = frontend_default.get(f'/product/{href}')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('main div.h-product div.row div.product-info.col div.product-wrapper div h6', expected_value='Product Description:')
        # resp.assert_cssselect('html head title', expected_value='Online Boutique')

    @json_dataset('data/dataset_21.json')
    @clear_session({'spanId': 21})
    def test_21_post_setCurrency(self, data_row):
        currency_code, = data_row

        # POST http://frontend.default/setCurrency (endp 21)
        frontend_default = get_http_target('TARGET_FRONTEND_DEFAULT', authenticate)
        resp = frontend_default.post('/setCurrency', data=[('currency_code', currency_code)])
        resp.assert_ok()
        # resp.assert_status_code(302)


@data_driven_tests
class Tests_frontend_defaulthttp_(unittest.TestCase):

    @json_dataset('data/dataset_30.json')
    @clear_session({'spanId': 30})
    def test_30_head_param_(self, data_row):
        param, = data_row

        # HEAD http://frontend.defaulthttp:/{param}/ (endp 30)
        frontend_defaulthttp_ = get_http_target('TARGET_FRONTEND_DEFAULTHTTP_', authenticate)
        resp = frontend_defaulthttp_.head(f'/{param}/')
        resp.assert_ok()
        # resp.assert_status_code(200)

    @clear_session({'spanId': 31})
    def test_31_get_www_soso_com_(self):
        # GET http://frontend.defaulthttp:/www.soso.com/ (endp 31)
        frontend_defaulthttp_ = get_http_target('TARGET_FRONTEND_DEFAULTHTTP_', authenticate)
        resp = frontend_defaulthttp_.get('/www.soso.com/')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('header div.navbar div.container.d-flex.justify-content-between div.h-free-shipping', expected_value='Free shipping with $75 purchase! \xa0\xa0')
        # resp.assert_cssselect('html head title', expected_value='Online Boutique')


@data_driven_tests
class Tests_frontend_external_default(unittest.TestCase):

    @json_dataset('data/dataset_23.json')
    @clear_session({'spanId': 23})
    def test_23_get_(self, data_row):
        content, s, vars_0_ = data_row

        # GET http://frontend-external.default/ (endp 23)
        frontend_external_default = get_http_target('TARGET_FRONTEND_EXTERNAL_DEFAULT', authenticate)
        qstr = '?' + urlencode([('XDEBUG_SESSION_START', 'phpstorm'), ('a', 'fetch'), ('content', content), ('function', 'call_user_func_array'), ('s', s), ('vars[0]', vars_0_)])
        resp = frontend_external_default.get('/' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('header div.navbar div.container.d-flex.justify-content-between div.h-free-shipping', expected_value='Free shipping with $75 purchase! \xa0\xa0')
        # resp.assert_cssselect('html head title', expected_value='Online Boutique')

    @json_dataset('data/dataset_39.json')
    @clear_session({'spanId': 39})
    def test_39_get_(self, data_row):
        content, = data_row

        # GET http://frontend-external.default/ (endp 39)
        frontend_external_default = get_http_target('TARGET_FRONTEND_EXTERNAL_DEFAULT', authenticate)
        qstr = '?' + urlencode([('a', 'fetch'), ('content', content)])
        resp = frontend_external_default.get('/' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('header div.navbar div.container.d-flex.justify-content-between div.h-free-shipping', expected_value='Free shipping with $75 purchase! \xa0\xa0')
        # resp.assert_cssselect('html head title', expected_value='Online Boutique')

    @clear_session({'spanId': 56})
    def test_56_get_(self):
        # GET http://frontend-external.default/ (endp 56)
        frontend_external_default = get_http_target('TARGET_FRONTEND_EXTERNAL_DEFAULT', authenticate)
        resp = frontend_external_default.get('/')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('header div.navbar div.container.d-flex.justify-content-between div.h-free-shipping', expected_value='Free shipping with $75 purchase! \xa0\xa0')
        # resp.assert_cssselect('html head title', expected_value='Online Boutique')

    @clear_session({'spanId': 64})
    def test_64_get_(self):
        # GET http://frontend-external.default/ (endp 64)
        frontend_external_default = get_http_target('TARGET_FRONTEND_EXTERNAL_DEFAULT', authenticate)
        resp = frontend_external_default.get('/')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('header div.navbar div.container.d-flex.justify-content-between div.h-free-shipping', expected_value='Free shipping with $75 purchase! \xa0\xa0')
        # resp.assert_cssselect('html head title', expected_value='Online Boutique')

    @clear_session({'spanId': 72})
    def test_72_head_(self):
        # HEAD http://frontend-external.default/ (endp 72)
        frontend_external_default = get_http_target('TARGET_FRONTEND_EXTERNAL_DEFAULT', authenticate)
        resp = frontend_external_default.head('/')
        resp.assert_ok()
        # resp.assert_status_code(200)

    @clear_session({'spanId': 29})
    def test_29_get__healthz(self):
        # GET http://frontend-external.default/_healthz (endp 29)
        frontend_external_default = get_http_target('TARGET_FRONTEND_EXTERNAL_DEFAULT', authenticate)
        resp = frontend_external_default.get('/_healthz')
        resp.assert_ok()
        # resp.assert_status_code(200)

    @json_dataset('data/dataset_24.json')
    @clear_session({'spanId': 24})
    def test_24_post_cart(self, data_row):
        product_id, = data_row

        # POST http://frontend-external.default/cart (endp 24)
        frontend_external_default = get_http_target('TARGET_FRONTEND_EXTERNAL_DEFAULT', authenticate)
        resp = frontend_external_default.post('/cart', data=[('product_id', product_id), ('quantity', str(random.randint(1, 10)))])
        resp.assert_ok()
        # resp.assert_status_code(302)

    @clear_session({'spanId': 25})
    def test_25_get_cart(self):
        # GET http://frontend-external.default/cart (endp 25)
        frontend_external_default = get_http_target('TARGET_FRONTEND_EXTERNAL_DEFAULT', authenticate)
        resp = frontend_external_default.get('/cart')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('main.cart div.cart-bg div.container h3', expected_value='Your shopping cart is empty!')
        # resp.assert_cssselect('html head title', expected_value='Online Boutique')

    @json_dataset('data/dataset_26.json')
    @clear_session({'spanId': 26})
    def test_26_post_cart_checkout(self, data_row):
        city, country, credit_card_cvv, credit_card_expiration_year, credit_card_number, email_, street_address, zip_code = data_row

        # POST http://frontend-external.default/cart/checkout (endp 26)
        frontend_external_default = get_http_target('TARGET_FRONTEND_EXTERNAL_DEFAULT', authenticate)
        resp = frontend_external_default.post('/cart/checkout', data=[('city', city), ('country', country), ('credit_card_cvv', credit_card_cvv), ('credit_card_expiration_month', '1'), ('credit_card_expiration_year', credit_card_expiration_year), ('credit_card_number', credit_card_number), ('email', email_), ('state', 'CA'), ('street_address', street_address), ('zip_code', zip_code)])
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('main.order div div.container div.row.text-center a.btn.btn-info', expected_value='Keep Browsing')
        # resp.assert_cssselect('html head title', expected_value='Online Boutique')

    @json_dataset('data/dataset_27.json')
    @clear_session({'spanId': 27})
    def test_27_get_product_href(self, data_row):
        href, = data_row

        # GET http://frontend-external.default/product/{href} (endp 27)
        frontend_external_default = get_http_target('TARGET_FRONTEND_EXTERNAL_DEFAULT', authenticate)
        resp = frontend_external_default.get(f'/product/{href}')
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('main div.container div.container div.alert.alert-dark strong', expected_value='Advertisement:')
        # resp.assert_cssselect('html head title', expected_value='Online Boutique')

    @json_dataset('data/dataset_28.json')
    @clear_session({'spanId': 28})
    def test_28_post_setCurrency(self, data_row):
        currency_code, = data_row

        # POST http://frontend-external.default/setCurrency (endp 28)
        frontend_external_default = get_http_target('TARGET_FRONTEND_EXTERNAL_DEFAULT', authenticate)
        resp = frontend_external_default.post('/setCurrency', data=[('currency_code', currency_code)])
        resp.assert_ok()
        # resp.assert_status_code(302)


@data_driven_tests
class Tests_paymentservice_default(unittest.TestCase):

    @json_dataset('data/dataset_14.json')
    @clear_session({'spanId': 14})
    def test_14_post_hipstershop_PaymentService_Charge(self, data_row):
        field_1_1, field_2_1, field_2_2, field_2_3 = data_row

        # POST http://paymentservice.default/hipstershop.PaymentService/Charge (endp 14)
        paymentservice_default = get_http_target('TARGET_PAYMENTSERVICE_DEFAULT', authenticate)
        paymentservice_default.set_grpc(hipstershop_pb2_grpc.PaymentServiceStub)
        msg = hipstershop_pb2.ChargeReq()
        apply_into_protobuf(msg, '1.1', field_1_1)
        apply_into_protobuf(msg, '1.2', int(random.randint(17, 15229)))
        apply_into_protobuf(msg, '1.3', int(random.randint(14124723, 999999999)))
        apply_into_protobuf(msg, '2.1', field_2_1)
        apply_into_protobuf(msg, '2.2', field_2_2)
        apply_into_protobuf(msg, '2.3', field_2_3)
        apply_into_protobuf(msg, '2.4', 1)
        resp = paymentservice_default.grpc_stub.Charge(msg)
        resp = wrap_grpc_for_tracing(resp)


@data_driven_tests
class Tests_productcatalogservice_default(unittest.TestCase):

    @json_dataset('data/dataset_5.json')
    @clear_session({'spanId': 5})
    def test_05_post_hipstershop_ProductCatalogService_GetProduct(self, data_row):
        field_1, = data_row

        # POST http://productcatalogservice.default/hipstershop.ProductCatalogService/GetProduct (endp 5)
        productcatalogservice_default = get_http_target('TARGET_PRODUCTCATALOGSERVICE_DEFAULT', authenticate)
        productcatalogservice_default.set_grpc(hipstershop_pb2_grpc.ProductCatalogServiceStub)
        msg = hipstershop_pb2.GetProductReq()
        apply_into_protobuf(msg, '1', field_1)
        resp = productcatalogservice_default.grpc_stub.GetProduct(msg)
        resp = wrap_grpc_for_tracing(resp)
        # assert_grpc(resp, '5.1', expected_value='USD')

    @clear_session({'spanId': 6})
    def test_06_post_hipstershop_ProductCatalogService_ListProducts(self):
        # POST http://productcatalogservice.default/hipstershop.ProductCatalogService/ListProducts (endp 6)
        productcatalogservice_default = get_http_target('TARGET_PRODUCTCATALOGSERVICE_DEFAULT', authenticate)
        productcatalogservice_default.set_grpc(hipstershop_pb2_grpc.ProductCatalogServiceStub)
        msg = hipstershop_pb2.ListProductsReq()
        resp = productcatalogservice_default.grpc_stub.ListProducts(msg)
        resp = wrap_grpc_for_tracing(resp)
        # assert_grpc(resp, '1.5.1', expected_value='USD')


@data_driven_tests
class Tests_recommendationservice_default(unittest.TestCase):

    @json_dataset('data/dataset_7.json')
    @clear_session({'spanId': 7})
    def test_07_post_hipstershop_RecommendationService_ListRecommendations(self, data_row):
        field_2, = data_row

        # POST http://recommendationservice.default/hipstershop.RecommendationService/ListRecommendations (endp 7)
        recommendationservice_default = get_http_target('TARGET_RECOMMENDATIONSERVICE_DEFAULT', authenticate)
        recommendationservice_default.set_grpc(hipstershop_pb2_grpc.RecommendationServiceStub)
        msg = hipstershop_pb2.ListRecommendationsReq()
        apply_into_protobuf(msg, '1', str(uuid.uuid4()))
        apply_into_protobuf(msg, '2', field_2)
        resp = recommendationservice_default.grpc_stub.ListRecommendations(msg)
        resp = wrap_grpc_for_tracing(resp)


@data_driven_tests
class Tests_shippingservice_default(unittest.TestCase):

    @json_dataset('data/dataset_9.json')
    @clear_session({'spanId': 9})
    def test_09_post_hipstershop_ShippingService_GetQuote(self, data_row):
        field_1_1, field_1_2, field_1_4, field_1_5, field_2_1, field_2_2 = data_row

        # POST http://shippingservice.default/hipstershop.ShippingService/GetQuote (endp 9)
        shippingservice_default = get_http_target('TARGET_SHIPPINGSERVICE_DEFAULT', authenticate)
        shippingservice_default.set_grpc(hipstershop_pb2_grpc.ShippingServiceStub)
        msg = hipstershop_pb2.GetQuoteReq()
        apply_into_protobuf(msg, '1.1', field_1_1)
        apply_into_protobuf(msg, '1.2', field_1_2)
        apply_into_protobuf(msg, '1.3', 'CA')
        apply_into_protobuf(msg, '1.4', field_1_4)
        apply_into_protobuf(msg, '1.5', field_1_5)
        apply_into_protobuf(msg, '2.1', field_2_1)
        apply_into_protobuf(msg, '2.2', field_2_2)
        resp = shippingservice_default.grpc_stub.GetQuote(msg)
        resp = wrap_grpc_for_tracing(resp)
        # assert_grpc(resp, '1.1', expected_value='USD')

    @json_dataset('data/dataset_13.json')
    @clear_session({'spanId': 13})
    def test_13_post_hipstershop_ShippingService_ShipOrder(self, data_row):
        field_1_1, field_1_2, field_1_4, field_1_5, field_2_1 = data_row

        # POST http://shippingservice.default/hipstershop.ShippingService/ShipOrder (endp 13)
        shippingservice_default = get_http_target('TARGET_SHIPPINGSERVICE_DEFAULT', authenticate)
        shippingservice_default.set_grpc(hipstershop_pb2_grpc.ShippingServiceStub)
        msg = hipstershop_pb2.ShipOrderReq()
        apply_into_protobuf(msg, '1.1', field_1_1)
        apply_into_protobuf(msg, '1.2', field_1_2)
        apply_into_protobuf(msg, '1.3', 'CA')
        apply_into_protobuf(msg, '1.4', field_1_4)
        apply_into_protobuf(msg, '1.5', field_1_5)
        apply_into_protobuf(msg, '2.1', field_2_1)
        apply_into_protobuf(msg, '2.2', int(random.randint(1, 15)))
        resp = shippingservice_default.grpc_stub.ShipOrder(msg)
        resp = wrap_grpc_for_tracing(resp)
