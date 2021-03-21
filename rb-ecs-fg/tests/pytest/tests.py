from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests_trdemo_client_trdemo(unittest.TestCase):

    @json_dataset('data/dataset_7.json')
    @clear_session({'spanId': 7})
    def test_07_get_(self, data_row):
        content, s = data_row

        # GET http://trdemo-client.trdemo/ (endp 7)
        trdemo_client_trdemo = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMO', authenticate)
        qstr = '?' + urlencode([('XDEBUG_SESSION_START', 'phpstorm'), ('a', 'fetch'), ('content', content), ('s', s)])
        resp = trdemo_client_trdemo.get('/' + qstr, headers=dict([('accept', 'text/plain')]))
        resp.assert_status_code(200)
        resp.assert_cssselect('div.container-fluid div h1', expected_value='Welcome!')
        resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    @clear_session({'spanId': 14})
    def test_14_head_(self):
        # HEAD http://trdemo-client.trdemo/ (endp 14)
        trdemo_client_trdemo = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMO', authenticate)
        resp = trdemo_client_trdemo.head('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('h1', expected_value='Not Found')

    @json_dataset('data/dataset_18.json')
    @clear_session({'spanId': 18})
    def test_18_get_(self, data_row):
        content, id_, s, vars_0_ = data_row

        # GET http://trdemo-client.trdemo/ (endp 18)
        trdemo_client_trdemo = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMO', authenticate)
        qstr = '?' + urlencode([('XDEBUG_SESSION_START', 'phpstorm'), ('a', 'fetch'), ('content', content), ('function', 'call_user_func_array'), ('id', id_), ('pp', 'env'), ('s', s), ('vars[0]', vars_0_)])
        resp = trdemo_client_trdemo.get('/' + qstr, headers=dict([('accept', 'text/plain')]))
        resp.assert_status_code(200)
        resp.assert_cssselect('div.container-fluid div h1', expected_value='Welcome!')
        resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    @json_dataset('data/dataset_21.json')
    @clear_session({'spanId': 21})
    def test_21_get_(self, data_row):
        content, = data_row

        # GET http://trdemo-client.trdemo/ (endp 21)
        trdemo_client_trdemo = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMO', authenticate)
        qstr = '?' + urlencode([('a', 'fetch'), ('content', content)])
        resp = trdemo_client_trdemo.get('/' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div.container-fluid div h1', expected_value='Welcome!')
        resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    @clear_session({'spanId': 22})
    def test_22_head_(self):
        # HEAD http://trdemo-client.trdemo/ (endp 22)
        trdemo_client_trdemo = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMO', authenticate)
        resp = trdemo_client_trdemo.head('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div.container-fluid div h1', expected_value='Welcome!')

    @clear_session({'spanId': 23})
    def test_23_get_(self):
        # GET http://trdemo-client.trdemo/ (endp 23)
        trdemo_client_trdemo = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMO', authenticate)
        resp = trdemo_client_trdemo.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div.container-fluid div h1', expected_value='Welcome!')
        resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    @clear_session({'spanId': 29})
    def test_29_get_(self):
        # GET http://trdemo-client.trdemo/ (endp 29)
        trdemo_client_trdemo = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMO', authenticate)
        resp = trdemo_client_trdemo.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div.container-fluid div h1', expected_value='Welcome!')
        resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    @clear_session({'spanId': 39})
    def test_39_get_(self):
        # GET http://trdemo-client.trdemo/ (endp 39)
        trdemo_client_trdemo = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMO', authenticate)
        resp = trdemo_client_trdemo.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div.container-fluid div h1', expected_value='Welcome!')
        resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    @json_dataset('data/dataset_9.json')
    @clear_session({'spanId': 9})
    def test_09_get_cart_add(self, data_row):
        product_id, = data_row

        # GET http://trdemo-client.trdemo/cart/add (endp 9)
        trdemo_client_trdemo = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMO', authenticate)
        qstr = '?' + urlencode([('product_id', product_id)])
        resp = trdemo_client_trdemo.get('/cart/add' + qstr)
        resp.assert_status_code(302)

    @clear_session({'spanId': 10})
    def test_10_get_cart_remove_flight_id(self):
        # GET http://trdemo-client.trdemo/cart (endp 8)
        trdemo_client_trdemo = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMO', authenticate)
        resp = trdemo_client_trdemo.get('/cart')
        resp.assert_status_code(200)
        resp.assert_cssselect('div.container-fluid div h2', expected_value='Cart for alex.haiut@testr.io')
        resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')
        flight_id = url_part('?flight_id', cssselect('div.container-fluid div table.table.table-striped.table-responsive-md.btn-table tbody tr td a[href] @href', resp))

        # GET http://trdemo-client.trdemo/cart/remove/{flight_id} (endp 10)
        resp = trdemo_client_trdemo.get(f'/cart/remove/{flight_id}')
        resp.assert_status_code(302)

    @clear_session({'spanId': 37})
    def test_37_get_index_php(self):
        # GET http://trdemo-client.trdemo/index.php (endp 37)
        trdemo_client_trdemo = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMO', authenticate)
        resp = trdemo_client_trdemo.get('/index.php')
        resp.assert_status_code(200)
        resp.assert_cssselect('div.container-fluid div h1', expected_value='Welcome!')
        resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    # authentication-related test
    @clear_session({'spanId': 12})
    def test_12_post_login(self):
        # GET http://trdemo-client.trdemo/login (endp 11)
        trdemo_client_trdemo = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMO', dummy_auth)
        resp = trdemo_client_trdemo.get('/login')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#logreg-forms h1.h3.font-weight-normal', expected_value=' Select user (temp) ')
        resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')
        user = cssselect('form#userform select.custom-select[name="user"] option[value] @value', resp)

        # POST http://trdemo-client.trdemo/login (endp 12)
        resp = trdemo_client_trdemo.post('/login', data=[('user', user)])
        resp.assert_status_code(302)

    # authentication-related test
    @clear_session({'spanId': 24})
    def test_24_get_login(self):
        # GET http://trdemo-client.trdemo/login (endp 24)
        trdemo_client_trdemo = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMO', dummy_auth)
        qstr = '?' + urlencode([('from', '/')])
        resp = trdemo_client_trdemo.get('/login' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div#logreg-forms h1.h3.font-weight-normal', expected_value=' Select user (temp) ')
        resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    # authentication-related test
    @json_dataset('data/dataset_26.json')
    @clear_session({'spanId': 26})
    def test_26_post_login(self, data_row):
        id_, password, uid, username = data_row

        # POST http://trdemo-client.trdemo/login (endp 26)
        trdemo_client_trdemo = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMO', dummy_auth)
        resp = trdemo_client_trdemo.post('/login', data=[('id', id_), ('password', password), ('uid', uid), ('username', username)])
        resp.assert_status_code(200)
        resp.assert_cssselect('div#logreg-forms h1.h3.font-weight-normal', expected_value=' Select user (temp) ')
        resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    @json_dataset('data/dataset_35.json')
    @clear_session({'spanId': 35})
    def test_35_post_ooi_php(self, data_row):
        m, = data_row

        # POST http://trdemo-client.trdemo/ooi.php (endp 35)
        trdemo_client_trdemo = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMO', authenticate)
        resp = trdemo_client_trdemo.post('/ooi.php', data=[('m', m)])
        resp.assert_status_code(200)
        resp.assert_cssselect('div.container-fluid div h1', expected_value='Welcome!')
        resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    @json_dataset('data/dataset_13.json')
    @clear_session({'spanId': 13})
    def test_13_get_search(self, data_row):
        startDate, = data_row

        # GET http://trdemo-client.trdemo/search (endp 13)
        trdemo_client_trdemo = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMO', authenticate)
        qstr = '?' + urlencode([('destination', '*'), ('endDate', ''), ('source', '*'), ('startDate', startDate)])
        resp = trdemo_client_trdemo.get('/search' + qstr)
        resp.assert_status_code(200)


@data_driven_tests
class Tests_trdemo_client_trdemohttp_(unittest.TestCase):

    @json_dataset('data/dataset_16.json')
    @clear_session({'spanId': 16})
    def test_16_head_param_(self, data_row):
        param, = data_row

        # HEAD http://trdemo-client.trdemohttp:/{param}/ (endp 16)
        trdemo_client_trdemohttp_ = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMOHTTP_', authenticate)
        resp = trdemo_client_trdemohttp_.head(f'/{param}/')
        resp.assert_status_code(200)

    @json_dataset('data/dataset_17.json')
    @clear_session({'spanId': 17})
    def test_17_get_param_(self, data_row):
        param, = data_row

        # GET http://trdemo-client.trdemohttp:/{param}/ (endp 17)
        trdemo_client_trdemohttp_ = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMOHTTP_', authenticate)
        resp = trdemo_client_trdemohttp_.get(f'/{param}/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div.container-fluid div h1', expected_value='Welcome!')
        resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    @json_dataset('data/dataset_31.json')
    @clear_session({'spanId': 31})
    def test_31_head_param_(self, data_row):
        param, = data_row

        # HEAD http://trdemo-client.trdemohttp:/{param}/ (endp 31)
        trdemo_client_trdemohttp_ = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMOHTTP_', authenticate)
        resp = trdemo_client_trdemohttp_.head(f'/{param}/')
        resp.assert_status_code(200)

    @json_dataset('data/dataset_32.json')
    @clear_session({'spanId': 32})
    def test_32_get_param_(self, data_row):
        param, = data_row

        # GET http://trdemo-client.trdemohttp:/{param}/ (endp 32)
        trdemo_client_trdemohttp_ = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMOHTTP_', authenticate)
        resp = trdemo_client_trdemohttp_.get(f'/{param}/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div.container-fluid div h1', expected_value='Welcome!')
        resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')


@data_driven_tests
class Tests_trdemo_shoppingcart_trdemo(unittest.TestCase):

    @json_dataset('data/dataset_4.json')
    @clear_session({'spanId': 4})
    def test_04_put_cart_email(self, data_row):
        param, param1 = data_row

        # GET http://trdemo-flights.trdemo/flight/{param1}/{param2} (endp 3)
        trdemo_flights_trdemo = get_http_target('TARGET_TRDEMO_FLIGHTS_TRDEMO', authenticate)
        resp = trdemo_flights_trdemo.get(f'/flight/{param}/{param1}')
        resp.assert_status_code(200)
        product_id = jsonpath('$[*].flight_id', resp)

        # GET http://trdemo-client.trdemo/version (endp 27)
        trdemo_client_trdemo = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMO', authenticate)
        resp = trdemo_client_trdemo.get('/version')
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.service', expected_value='client')
        email_ = jsonpath('$.[*].email', resp)

        # PUT http://trdemo-shoppingcart.trdemo/cart/{email} (endp 4)
        trdemo_shoppingcart_trdemo = get_http_target('TARGET_TRDEMO_SHOPPINGCART_TRDEMO', authenticate)
        with open('data/payload_for_endp_4.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.product_id', product_id)
        resp = trdemo_shoppingcart_trdemo.put(f'/cart/{email_}', json=json_payload)
        resp.assert_status_code(201)

    @clear_session({'spanId': 6})
    def test_06_delete_cart_email_product_id(self):
        # GET http://trdemo-client.trdemo/version (endp 27)
        trdemo_client_trdemo = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMO', authenticate)
        resp = trdemo_client_trdemo.get('/version')
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.service', expected_value='client')
        email_ = jsonpath('$.[*].email', resp)

        # GET http://trdemo-shoppingcart.trdemo/cart/{email} (endp 5)
        trdemo_shoppingcart_trdemo = get_http_target('TARGET_TRDEMO_SHOPPINGCART_TRDEMO', authenticate)
        resp = trdemo_shoppingcart_trdemo.get(f'/cart/{email_}')
        resp.assert_status_code(200)
        product_id = jsonpath('$.products[*].product_id', resp)

        # DELETE http://trdemo-shoppingcart.trdemo/cart/{email}/{product_id} (endp 6)
        resp = trdemo_shoppingcart_trdemo.delete(f'/cart/{email_}/{product_id}')
        resp.assert_status_code(200)


@data_driven_tests
class Tests_trdemo_users_trdemo(unittest.TestCase):

    @clear_session({'spanId': 30})
    def test_30_get_(self):
        # GET http://trdemo-users.trdemo/ (endp 30)
        trdemo_users_trdemo = get_http_target('TARGET_TRDEMO_USERS_TRDEMO', authenticate)
        resp = trdemo_users_trdemo.get('/')
        resp.assert_status_code(200)
        resp.assert_jsonpath("$['/reset/database']", expected_value='DELETE')

    @clear_session({'spanId': 1})
    def test_01_get_user_email(self):
        # GET http://trdemo-users.trdemo/user/all (endp 2)
        trdemo_users_trdemo = get_http_target('TARGET_TRDEMO_USERS_TRDEMO', authenticate)
        resp = trdemo_users_trdemo.get('/user/all')
        resp.assert_status_code(200)
        email_ = jsonpath('$[*].email', resp)

        # GET http://trdemo-users.trdemo/user/{email} (endp 1)
        resp = trdemo_users_trdemo.get(f'/user/{email_}')
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.airport', expected_value='TLV')

    @clear_session({'spanId': 25})
    def test_25_get_user_all(self):
        # GET http://trdemo-users.trdemo/user/all (endp 25)
        trdemo_users_trdemo = get_http_target('TARGET_TRDEMO_USERS_TRDEMO', authenticate)
        resp = trdemo_users_trdemo.get('/user/all')
        resp.assert_status_code(200)


@data_driven_tests
class Tests_unresolved_target(unittest.TestCase):

    @json_dataset('data/dataset_15.json')
    @clear_session({'spanId': 15})
    def test_15_get_(self, data_row):
        content, = data_row

        # GET http://unresolved_target/ (endp 15)
        unresolved_target = get_http_target('TARGET_UNRESOLVED_TARGET', authenticate)
        qstr = '?' + urlencode([('XDEBUG_SESSION_START', 'phpstorm'), ('a', 'fetch'), ('content', content)])
        resp = unresolved_target.get('/' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div.container-fluid div h1', expected_value='Welcome!')
        resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')

    @clear_session({'spanId': 19})
    def test_19_get_(self):
        # GET http://unresolved_target/ (endp 19)
        unresolved_target = get_http_target('TARGET_UNRESOLVED_TARGET', authenticate)
        resp = unresolved_target.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div.container-fluid div h1', expected_value='Welcome!')
        resp.assert_cssselect('html head title', expected_value=' TestR Demo app ')
