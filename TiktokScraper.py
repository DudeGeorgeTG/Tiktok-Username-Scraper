import random
import requests
from uuid import uuid4

# === Config ===
min_followers = 1000   # Minimum follower count to print
max_iterations = 10    # Prevent infinite loop while testing

def scraper():
    while True:
        try:
            g = random.choice([
                'ğüişöçñäüğüişöçñäüğüişöçñäüqw.ertyuiopasdfghjklzxcvbnm',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïçÿæœ',
                'αβγδεζηθικλμνξοπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',
                'áéíóúýàèìòùâêîôûãñõäëïöüÿçšž',
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン'
            ])

            keyword = ''.join((random.choice(g) for _ in range(random.randrange(4, 9))))
            idd6 = "".join(random.choice('1234567890') for _ in range(19))
            
            he3 = {
                "User-Agent": f'com.zhiliaoapp.musically/{keyword} (Linux; U; Android {random.randrange(7,13)}; ar_IQ_#u-nu-latn; ANY-LX2; Build/{keyword}; Cronet/58.0.{random.randrange(3,9)}.0)'
            }
            
            try:
                ttwid = requests.get('https://www.tiktok.com/', headers=he3, timeout=10).cookies.get_dict().get('ttwid', '')
                shelby = requests.get(
                    'https://www.tiktok.com/api/search/user/full/'
                    '?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=0.84'
                    '&browser_language=ar-IQ&browser_name=Mozilla&browser_online=true'
                    '&browser_platform=Linux%20aarch64&browser_version=5.0%20%28X11%3B%20Linux%20x86_64%29'
                    '%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F106.0.0.0'
                    '%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0'
                    '&device_id=7136188745632548358&device_platform=web_pc&focus_state=true'
                    '&from_page=search&history_len=40&is_fullscreen=false&is_page_visible=true'
                    '&keyword=dude&os=linux&priority_region=&referer=&region=IQ'
                    '&screen_height=796&screen_width=360&tz_name=Asia%2FBaghdad'
                    '&verifyFp=verify_l9zrjkcx_XSZCv5U7_xzys_4UEP_8m1a_TibJS3izVTHL'
                    '&webcast_language=ar&msToken=qfFKcpRIe_b543Hfa7buaE31PLWDv6-_TQYqevIaTVOPrUNjuwuHR2z0_cEadFELKqD9p6fLuWk8tgAO9lDmVCUX4vqnit3V4rX9zvJfLCbhs9U2apBgYHmKpXPp6DLl2wZy35z0xD6g6TSu_NIh'
                    '&X-Bogus=DFSzswVLk-tANxW1S02v8OxPBxgg'
                    '&_signature=_02B4Z6wo00001IuO8aAAAIDBSFHuFzoQUMCLjvUAAEGFfa',
                    headers=he3,
                    timeout=10
                )
                msToken = shelby.cookies.get_dict().get('msToken', '')
                
                headers = {
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'no-cache',
                    'pragma': 'no-cache',
                    'priority': 'u=1, i',
                    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': he3["User-Agent"],
                }

                params = {
                    'WebIdLastTime': '1715883147',
                    'aid': '1988',
                    'app_language': 'en',
                    'app_name': 'tiktok_web',
                    'browser_language': 'en-US',
                    'browser_name': 'Mozilla',
                    'browser_online': 'true',
                    'browser_platform': 'Win32',
                    'browser_version': he3["User-Agent"],
                    'channel': 'tiktok_web',
                    'cookie_enabled': 'true',
                    'cursor': '220',
                    'data_collection_enabled': 'false',
                    'device_id': idd6,
                    'device_platform': 'web_pc',
                    'focus_state': 'true',
                    'from_page': 'search',
                    'history_len': '5',
                    'is_fullscreen': 'false',
                    'is_page_visible': 'true',
                    'keyword': keyword,
                    'odinId': '7369661640164000774',
                    'os': 'windows',
                    'priority_region': '',
                    'referer': '',
                    'region': 'PE',
                    'screen_height': '864',
                    'screen_width': '1536',
                    'search_id': '20240801154310BA7846F9CDEDD312B464',
                    'tz_name': 'Asia/Baghdad',
                    'user_is_login': 'false',
                    'web_search_code': '{"tiktok":{"client_params_x":{"search_engine":{"ies_mt_user_live_video_card_use_libra":1,"mt_search_general_user_live_card":1}},"search_server":{}}}',
                    'webcast_language': 'en',
                    'msToken': msToken,
                    'X-Bogus': 'DFSzswVLRekANHWvtvtx-ShPmkfD',
                    '_signature': '_02B4Z6wo00001nO.kIwAAIDCAGLSLe4xtvJzv5QAAPpT70',
                }

                ses = str(uuid4()).replace('-', '')
                cookies = {
                    'cookie': f'passport_csrf_token=446c23e1b656077bd01b1f379ff01c64; passport_csrf_token_default=446c23e1b656077bd01b1f379ff01c64; tiktok_webapp_theme=dark; cookie-consent="ga":true,"af":true,"fbp":true,"lip":true,"bing":true,"ttads":true,"reddit":true,"version":"v8"; _ttp=2HZr0KnJ2pqKwJRyQ8myJ28Lpa8; __tea_cache_tokens_1988="user_unique_id":"7160599742786815489","timestamp":1667850947815,"_type_":"default"; passport_auth_status=c8fe9febc06f8f7a271309fa9e4f80e9,; passport_auth_status_ss=c8fe9febc06f8f7a271309fa9e4f80e9,; tt_csrf_token=CSVYu9wW-NbmqJ_cgNMHwEIItUNZGwDPM-hU; tt_chain_token=K01fXiH8q/IKwxFnx8jzcA==; _abck=951F354EE38142028A7429E8C92DB598~0~YAAQVvvOF6YBsxSFAQAAMc+wPgl24s0qz4P3iMup3WLL4PWyu/iF6+jb4qL2RfvMEKOGTv6dPfAH9AA2Hm+t/Z/Qn1TlkKHzKXk+KmuWj5d1dmCzqXD0BWgAUcMFCLRinQHou0lzh0ImXOw3B98dRIVnofWMwN8L8JxOErAxrQfi2JIEgTjNECxiZFYaqhpfLqyAUXBESaQxfCYfbNwLNwAAZvjpAfc1viGc/I9vlRIeVc2jYPA5/YUVwAytWPIOb2RuvdrXc2bfybwD3ffG0godURyE+r0QSJapjZK7kfVwbPGnVLal0dzAQM6MK2iDC5YhXugMYw9ZXB2CIaYRg4Cqy/t6BabKM9i+ZJgdvwWQQ6ljnk0pa1bKBsAYL79BxNMrQWccpQxQhUm9n09604O82PBKq8E=~-1~-1~-1; bm_sz=304AE404FA2929B0E90042E8314D20CA~YAAQVvvOF6kBsxSFAQAAMc+wPhIfC1eYkaU2YudlghSK8pNrkVcLYapeM/xrzvQbQkT9quFNwKNHsG4xkv6anwuDXn+BSd+gzoBWSdRZJscGEzPghGpbTStjyG61DtaJIqpkgjW7q6BEP37XgXgrWfHRdmoN5zraADDH7wpkIQ3UlBq5rj88cFl1IY4CUg2DSRugvtjKk+vcNV5AUjQ++v859Tv3vYF3Ga6m5lifIf0u50u/dC1xeVz0p4ew+7U21dwrDdNrai63bM7T9ArdMNk1q+2YK55FJU7tdQwtKtdLtnI=~4407620~4277556; ak_bmsc=EE17F7D340A941EB628DF68B5981EA8D~000000000000000000000000000000~YAAQVvvOF/8BsxSFAQAAS/SwPhJbeUd2XpuVnfaiGo9WDUNsMw3AUn4T4r4BtvFH6pwejSxQJ/K4aoQUK/hGU8InWjW8iSyWgKZxkNIl6lgAAvUdX8CiKcyfyQKJYfQcPDyxW6dnF6+VF2/BABsRcYTw9LUX6MjuhvgtLs1uh3AbWeHxdZFDhp/YYwjrPxoOEXgItQjGUSsxRhgRubItrsXwhW20gW9y+I7Eq22TORlAZOn+jyrl2bYH6C4yxD8yld+5OcSAQ3zKJfQLUjNj03BMgtlIyYT74OIh6GwUzgtjpGLUCzpqdeiOFZdfZApTnRoTK9J01CpUY+YxrThJKz4dScjK1V78LSd2CkfUakgFa7TXfZ1fgfPX/RW2nkWTe9SZtvDH3f62qd9b5oNojffOAM0fpnNeX06hNWSNDRRuiHOmv3m49PN2cJhknh753LdNdt81kj8LJ3SEe1y3sfHb0nPwafPExOaSSrXviHwj4+yLWrZw+dXy3Q==; sid_guard=5d52768f6a4a876314ea37244edfd0d0|1671794088|21600|Fri,+23-Dec-2022+17:14:48+GMT; uid_tt={ses[:16]}; uid_tt_ss={ses[:16]}; sid_tt={ses}; sessionid={ses}; sessionid_ss={ses}; sid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; ssid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; bm_sv=F556D2E15739C190D1B417337724D81E~YAAQVvvOF8ACsxSFAQAAaICxPhJ1QOpVK0jJSh0nuEay3Iz+L/0up1OoP09MVnndgBSzTjunJoYxBBQH4BTuDkQIQY+zt9kedbGoP5/7AUt2jVEq7DfEwQYdr31ZvZiHlhdU2Q5jwNvbZvNzQSokkwHoGbPqes9c4kV0ZGJuEuWc3pLurp0dkRkEBTY0UrcljYpQayw5/w7+4BlpmrMR5UAHElAGf2njGNpz3vRls+WGkTy9l8jRTCEseWkwnA9X~1; ttwid='+ttwid+'; odin_tt=70015f10b12827e4d2b9cce32ead78da9bd1f5af11487a83ba408d86d9a4fb55ec780a14ad91b601d9fe256fcb8160786311c12ef294e6bf285fbbf7eed8dff8080f26ed1bcedbdfca7244743dcbc60e; msToken='+msToken+'; msToken='+msToken+'; s_v_web_id=verify_lc0f2h1w_v9MWasYr_Uw4b_4j2o_8gdZ_QkWrSxI57MTt',
                    'pragma': 'no-cache',
                }

                try:
                    response = requests.get(
                        'https://www.tiktok.com/api/search/user/full/',
                        params=params,
                        headers=headers,
                        cookies=cookies,
                        timeout=10
                    ).json()
                    
                    for user in response.get('user_list', []):
                        user_info = user.get('user_info', {})
                        #ud = user_info.get('uid', '')
                        username = user_info.get('unique_id', '')
                        followers = user_info.get('follower_count', 0)
                        
                        if int(followers) >= min_followers and '_' not in username:
                            print(username + ' - ' + str(followers))
                            with open('scraped.txt', 'a') as f:
                                f.write(username + ' - ' + str(followers) + '\n')
                            
                except (requests.exceptions.RequestException, ValueError, KeyError):
                    continue
                    
            except requests.exceptions.RequestException:
                continue
                
        except Exception:
            continue

# === Example run ===
if __name__ == "__main__":
    scraper()
