import requests
from urllib.parse import quote, urlencode
from datetime import datetime

URL = 'https://en.52wmb.com/company/detail/trade'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0;) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430',
    "accept": "*/*",
    "Set-Cookie": "Hm_lvt_a8c19c55e08ffe6ce37848ec47e2d406=1703427663; _BTK=hide; Hm_lvt_58bbfca376b914778b819cfc4d8c120d=1703564993; Hm_lpvt_58bbfca376b914778b819cfc4d8c120d=1703564993; _WTK=faeee9ecc9f9be41641c4d8cb277f80cA; _QUYA=49a763a2aa2d48ff840a833acd98f01641e5fae2d635e35fe6e125a6fc; access_token=42c02f54ad6f9da4; promote=auto; su_token=6d03ba5b734bb802a1d08f981ef8c0b7be62d7d927b3498a1ede2d37e9c1564212fb267803fedacf5036ebdf7a853ca8ab2e0ad615fcc3b8b253b885dcb29a86382a4efab824e06bb4a0721fbed5e0b1c9a0365965443c01de6b4d004e5d9c1bb07184a7dac3bf317eaa264721a8e1f15aef742aff3c41f623be337753af72881b62bc0db08a9afc971d5368e036e1b929fc6975cc94d0f0b2d2aa75ac5b437464c15ef2ec397e14b18e641764044bea6704aea7f94af9d242f388b2; visit_count=11; certi=1897860303_2716e30b6145b804a6db8b9c1c64044bea6704aea7f94af9d242f388b2; Hm_lvt_c131adc40651cdf84b4c7d5fdfbec963=1703427516; _DE=hide; new_letter_id_flag=16; new_letter_flag=false; Hm_lpvt_c131adc40651cdf84b4c7d5fdfbec963=1704041571; Hm_lpvt_a8c19c55e08ffe6ce37848ec47e2d406=1704041571; _close_pz=1",
    "cookie": "Hm_lvt_a8c19c55e08ffe6ce37848ec47e2d406=1703427663; _BTK=hide; Hm_lvt_58bbfca376b914778b819cfc4d8c120d=1703564993; Hm_lpvt_58bbfca376b914778b819cfc4d8c120d=1703564993; _WTK=faeee9ecc9f9be41641c4d8cb277f80cA; _QUYA=49a763a2aa2d48ff840a833acd98f01641e5fae2d635e35fe6e125a6fc; access_token=42c02f54ad6f9da4; promote=auto; su_token=6d03ba5b734bb802a1d08f981ef8c0b7be62d7d927b3498a1ede2d37e9c1564212fb267803fedacf5036ebdf7a853ca8ab2e0ad615fcc3b8b253b885dcb29a86382a4efab824e06bb4a0721fbed5e0b1c9a0365965443c01de6b4d004e5d9c1bb07184a7dac3bf317eaa264721a8e1f15aef742aff3c41f623be337753af72881b62bc0db08a9afc971d5368e036e1b929fc6975cc94d0f0b2d2aa75ac5b437464c15ef2ec397e14b18e641764044bea6704aea7f94af9d242f388b2; visit_count=11; certi=1897860303_2716e30b6145b804a6db8b9c1c64044bea6704aea7f94af9d242f388b2; Hm_lvt_c131adc40651cdf84b4c7d5fdfbec963=1703427516; _DE=hide; new_letter_id_flag=16; new_letter_flag=false; Hm_lpvt_c131adc40651cdf84b4c7d5fdfbec963=1704041571; Hm_lpvt_a8c19c55e08ffe6ce37848ec47e2d406=1704041571; _close_pz=1",
}


def fetch_data():
    try:
        payload = {
            "id": "65888955",
            "company_type": "1",
            "end_time": "2023-11-30",
            "last_trade_date": "2023-11-30",
            "country": "Vietnam",
            "key": "*",
            "product": "*",
            "sort": "default",
            "start_time": "**",
            "seo_flag": "0",
            "is_page": "true",
            "start": "40",
            "size": "20",
            "tag_id": "0",
            "reftoken": "6d03a35a231cfa13aa9dcfdb4ff8c0a1b868818275f45a890e019bbd2e38ff1951ea686a01f186dc0c62ec82218c30bfb27164044bea6704aea7f94af9d242f388b2",
            "hs": "09061900",
            "scene": "3"
        }
        cookie = {
            "Hm_lvt_a8c19c55e08ffe6ce37848ec47e2d406": "1703427663", "_BTK": "hide",
            "Hm_lvt_58bbfca376b914778b819cfc4d8c120d": "1703564993",
            "Hm_lpvt_58bbfca376b914778b819cfc4d8c120d": "1703564993", "_WTK": "faeee9ecc9f9be41641c4d8cb277f80cA",
            "_QUYA": "49a763a2aa2d48ff840a833acd98f01641e5fae2d635e35fe6e125a6fc",
            "access_token": "42c02f54ad6f9da4", "promote": "auto",
            "su_token": "6d03ba5b734bb802a1d08f981ef8c0b7be62d7d927b3498a1ede2d37e9c1564212fb267803fedacf5036ebdf7a853ca8ab2e0ad615fcc3b8b253b885dcb29a86382a4efab824e06bb4a0721fbed5e0b1c9a0365965443c01de6b4d004e5d9c1bb07184a7dac3bf317eaa264721a8e1f15aef742aff3c41f623be337753af72881b62bc0db08a9afc971d5368e036e1b929fc6975cc94d0f0b2d2aa75ac5b437464c15ef2ec397e14b18e641764044bea6704aea7f94af9d242f388b2",
            "visit_count": "11", "certi": "1897860303_2716e30b6145b804a6db8b9c1c64044bea6704aea7f94af9d242f388b2",
            "Hm_lvt_c131adc40651cdf84b4c7d5fdfbec963": "1703427516", "_DE": "hide", "new_letter_id_flag": "16",
            "new_letter_flag": "false",
            "Hm_lpvt_c131adc40651cdf84b4c7d5fdfbec963": "1704041571",
            "Hm_lpvt_a8c19c55e08ffe6ce37848ec47e2d406": "1704041571", "_close_pz": "1"}
        payload_str = urlencode(payload, safe='*', quote_via=quote)
        req = requests.get(
            URL, payload_str, headers=HEADERS,
            # cookies=cookie
        )
        if req.status_code != 200:
            raise Exception('Invalid status')
        response = req.json()
        print(response)

    except Exception as e:
        raise e


fetch_data()

"""
https://en.52wmb.com/company/detail/trade?
id=65888955&company_type=1&end_time=2023-11-30&last_trade_date=2023-11-30&country=Vietnam&key=%2A&product=%2A&sort=default&start_time=%2A%2A&seo_flag=0&is_page=true&start=40&size=20&tag_id=0&reftoken=6d03a35a231cfa13aa9dcfdb4ff8c0a1b868818275f45a890e019bbd2e38ff1951ea686a01f186dc0c62ec82218c30bfb27164044bea6704aea7f94af9d242f388b2&hs=09061900&scene=3
https://en.52wmb.com/company/detail/trade?
id=65888955&company_type=1&end_time=2023-11-30&last_trade_date=2023-11-30&country=Vietnam&key=*&product=*&sort=default&start_time=**&seo_flag=0&is_page=true&start=40&size=20&tag_id=0&reftoken=6d03a35a231cfa13aa9dcfdb4ff8c0a1b868818275f45a890e019bbd2e38ff1951ea686a01f186dc0c62ec82218c30bfb27164044bea6704aea7f94af9d242f388b2&hs=09061900&scene=3
id=65888955&company_type=1&end_time=2023-11-30&last_trade_date=2023-11-30&country=Vietnam&key=*&product=*&sort=default&start_time=**&seo_flag=0&is_page=true&start=40&size=20&tag_id=0&reftoken=6d03a35a231cfa13aa9dcfdb4ff8c0a1b868818275f45a890e019bbd2e38ff1951ea686a01f186dc0c62ec82218c30bfb27164044bea6704aea7f94af9d242f388b2&hs=09061900&scene=3
"""
