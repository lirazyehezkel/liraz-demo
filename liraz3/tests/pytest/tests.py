from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests_adservice_google_com(unittest.TestCase):

    @clear_session({'spanId': 7})
    def test_7_get_adsid_google_ui(self):
        # GET https://adservice.google.com/adsid/google/ui (endp 7)
        adservice_google_com = get_http_target('TARGET_ADSERVICE_GOOGLE_COM', authenticate)
        resp = adservice_google_com.get('/adsid/google/ui')
        resp.assert_ok()
        # resp.assert_status_code(204)


@data_driven_tests
class Tests_ogs_google_com(unittest.TestCase):

    @json_dataset('data/dataset_6.json')
    @clear_session({'spanId': 6})
    def test_6_get_widget_app_so(self, data_row):
        origin, = data_row

        # GET https://ogs.google.com/widget/app/so (endp 6)
        ogs_google_com = get_http_target('TARGET_OGS_GOOGLE_COM', authenticate)
        qstr = '?' + urlencode([('cn', 'app'), ('hl', 'iw'), ('origin', origin), ('pid', '1'), ('spid', '1')])
        resp = ogs_google_com.get('/widget/app/so' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)


@data_driven_tests
class Tests_www_google_com(unittest.TestCase):

    @json_dataset('data/dataset_1.json')
    @clear_session({'spanId': 1})
    def test_1_get_async_bgasy(self, data_row):
        ei, yv = data_row

        # GET https://www.google.com/async/bgasy (endp 1)
        www_google_com = get_http_target('TARGET_WWW_GOOGLE_COM', authenticate)
        qstr = '?' + urlencode([('async', '_fmt:jspb'), ('ei', ei), ('yv', yv)])
        resp = www_google_com.get('/async/bgasy' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)

    @json_dataset('data/dataset_2.json')
    @clear_session({'spanId': 2})
    def test_2_get_param(self, data_row):
        bih, biw, ei, param = data_row

        # GET https://www.google.com/{param} (endp 2)
        www_google_com = get_http_target('TARGET_WWW_GOOGLE_COM', authenticate)
        qstr = '?' + urlencode([('atyp', 'i'), ('bih', bih), ('biw', biw), ('cs', '1'), ('dpr', '2'), ('ei', ei)])
        resp = www_google_com.get(f'/{param}' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(204)

    @json_dataset('data/dataset_3.json')
    @clear_session({'spanId': 3})
    def test_3_get_complete_search(self, data_row):
        client, psi, q, sugexp = data_row

        # GET https://www.google.com/complete/search (endp 3)
        www_google_com = get_http_target('TARGET_WWW_GOOGLE_COM', authenticate)
        qstr = '?' + urlencode([('authuser', '0'), ('client', client), ('cp', '0'), ('dpr', '2'), ('gs_ri', 'gws-wiz'), ('hl', 'iw'), ('nolsbt', '1'), ('pq', 'google'), ('psi', psi), ('q', q), ('sugexp', sugexp), ('xssi', 't')])
        resp = www_google_com.get('/complete/search' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)

    @json_dataset('data/dataset_4.json')
    @clear_session({'spanId': 4})
    def test_4_post_param(self, data_row):
        aftp, atyp, ei, fld, ima, imad, imn, m, me, mem, net, param, pv, rt, sys_, t, wh = data_row

        # POST https://www.google.com/{param} (endp 4)
        www_google_com = get_http_target('TARGET_WWW_GOOGLE_COM', authenticate)
        qstr = '?' + urlencode([('adh', ''), ('aftp', aftp), ('atyp', atyp), ('bl', 'CHOb'), ('conn', 'onchange'), ('ct', 'slh'), ('dt19', '2'), ('ei', ei), ('fld', fld), ('ima', ima), ('imad', imad), ('ime', '1'), ('imea', '0'), ('imeb', '0'), ('imeh', '2'), ('imex', '1'), ('imn', imn), ('m', m), ('me', me), ('mem', mem), ('net', net), ('pv', pv), ('rt', rt), ('s', 'web'), ('scp', '0'), ('sto', ''), ('sys', sys_), ('t', t), ('v', 't1'), ('wh', wh), ('zx', str(int(time.time() * 1000)))])
        resp = www_google_com.post(f'/{param}' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(204)

    @json_dataset('data/dataset_5.json')
    @clear_session({'spanId': 5})
    def test_5_get_search(self, data_row):
        aqs, ie = data_row

        # GET https://www.google.com/search (endp 5)
        www_google_com = get_http_target('TARGET_WWW_GOOGLE_COM', authenticate)
        qstr = '?' + urlencode([('aqs', aqs), ('ie', ie), ('oq', 'google'), ('q', 'google'), ('sourceid', 'chrome')])
        resp = www_google_com.get('/search' + qstr)
        resp.assert_ok()
        # resp.assert_status_code(200)
        # resp.assert_cssselect('div#top_nav div h1', expected_value='מצבי חיפוש')
        # resp.assert_cssselect('html head title', expected_value='google - חיפוש ב-Google')
