from dataclasses import dataclass


@dataclass
class UserAgent:
    """
    Dataclass to store randomized UA strings to generate 'user-like' traffic.
    """

    user_agents = [
        "Mozilla/5.0 (Linux; Android 10; RMX1971 Build/QKQ1.190918.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.88 Mobile Safari/537.36 GSA/12.20.9.23.arm64",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) draw.io/12.2.2 Chrome/78.0.3904.94 Electron/7.1.0 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Max Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.50 Mobile Safari/537.36 GSA/12.41.19.23.arm64",
        "Mozilla/5.0 (Linux; U; Android 10; pl-pl; POCOPHONE F1 Build/QKQ1.190828.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.13.2-gn",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/93.0.961.73 Version/14.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 7.0; SAMSUNG-SM-G891A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MANM; .NET4.0C; .NET4.0E; BRI/2; InfoPath.3; ms-office; MSOffice 14)",
        "Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Pro Build/PKQ1.181203.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 GSA/12.41.19.23.arm64",
        "OneBrowser/3.5/Mozilla/5.0 (Linux; Android 10; H40 Build/QP1A.191105.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Safari/537.36",
        "OneBrowser/3.5/Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; Lenovo a1061 Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "OneBrowser/3.1 (Nokia303/14.76)",
        "OneBrowser/3.5/Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; Lenovo S750 Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.32052/191.265; U; en) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (J2ME/MIDP; Opera Mini/4.2/191.265; U; en) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (Series 60; Opera Mini/7.1.32444/191.265; U; en) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (J2ME/MIDP; Opera Mini/8.0.35626/191.265; U; ru) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (MAUI Runtime; Opera Mini/4.4.39007/191.265; U; ru) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (J2ME/MIDP; Opera Mini/4.5.40380/191.265; U; id) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.22537/191.265; U; ru) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (MAUI Runtime; Opera Mini/4.4.39001/191.265; U; en) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (Android; Opera Mini/12.0.1987/191.265; U; ru) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (Android; Opera Mini/46.1.2254/191.265; U; ru) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (Series 60; Opera Mini/7.1.32453/191.265; U; ru) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (J2ME/MIDP; Opera Mini/7.0.28870/191.265; U; en) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (Android; Opera Mini/7.6.40234/191.265; U; fa) Presto/2.12.423 Version/12.16",
        "Nokia6303iclassic/5.0 (10.80) Profile/MIDP-2.1 Configuration/CLDC-1.1 Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.32052/35.6172; U; en) Presto/2.8.119 Version/11.10en9.4.0.342 UNTRUSTED/1.0",
        "Opera/9.80 (Android; Opera Mini/7.6.40077/191.265; U; ar) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (MAUI Runtime; Opera Mini/4.4.39012/191.265; U; en) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (MAUI Runtime; Opera Mini/4.4.32206/191.265; U; en) Presto/2.12.423 Version/12.16",
        "SAMSUNG-GT-S5611 Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.34814/191.265; U; tr) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (Series 60; Opera Mini/7.1.32446/191.265; U; ru) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.32052/191.265; U; id) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (Android; Opera Mini/7.5.31657/191.265; U; en) Presto/2.12.423 Version/12.16",
        "SAMSUNG-GT-E2202 Opera/9.80 (J2ME/MIDP; Opera Mini/4.4.32420/191.265; U; en) Presto/2.12.423 Version/12.16",
        "SAMSUNG-GT-S3802 Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.33578/191.265; U; en) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (J2ME/MIDP; Opera Mini/4.5.40312/191.265; U; bg) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (SpreadTrum; Opera Mini/4.4.34868/191.265; U; ru) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (Android; Opera Mini/7.5.35721/191.265; U; en) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (J2ME/MIDP; Opera Mini/4.5.40380/191.265; U; fa) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (Series 60; Opera Mini/7.1.32446/191.265; U; vi) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (Android; Opera Mini/47.1.2254/191.265; U; pl) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.23453/191.265; U; en) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (J2ME/MIDP; Opera Mini/4.5.33867/191.265; U; en) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (Android; Opera Mini/7.5.35188/191.265; U; en) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (MAUI Runtime; Opera Mini/4.4.33576/191.265; U; fr) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (Android; Opera Mini/62.2.2254/191.265; U; en) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (Android; Opera Mini/10.0.1884/191.265; U; ar) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (Android; Opera Mini/32.0.2254/191.265; U; id) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (MAUI Runtime; Opera Mini/4.4.39001/191.265; U; fa) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (Android; Opera Mini/11.0.1912/191.265; U; en) Presto/2.12.423 Version/12.16",
        "Opera/9.80 (Android; Opera Mini/7.5.33942/191.265; U; fr) Presto/2.12.423 Version/12.16",
    ]
