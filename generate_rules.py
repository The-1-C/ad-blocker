
import json

start_id = 22
domains = [
    "ssl.google-analytics.com", "google-analytics.com", "sessions.bugsnag.com", "notify.bugsnag.com",
    "events.reddit.com", "log.fc.yahoo.com", "api.bugsnag.com", "fwtracks.freshmarketer.com",
    "cs.luckyorange.net", "geo.yahoo.com", "api.ad.xiaomi.com", "udcm.yahoo.com",
    "realtime.luckyorange.com", "ads-api.twitter.com", "upload.luckyorange.net", "analytics.query.yahoo.com",
    "smetrics.samsung.com", "freshmarketer.com", "samsung-com.112.2o7.net", "weather-analytics-events.apple.com",
    "api-adservices.apple.com", "books-analytics-events.apple.com", "adc3-launch.adcolony.com", "events3alt.adcolony.com",
    "ads30.adcolony.com", "api.luckyorange.com", "wd.adcolony.com", "notes-analytics-events.apple.com",
    "auction.unityads.unity3d.com", "config.unityads.unity3d.com", "adserver.unityads.unity3d.com", "an.facebook.com",
    "log.pinterest.com", "events.redditmedia.com", "ads.pinterest.com", "luckyorange.com",
    "metrics.mzstatic.com", "analytics.google.com", "trk.pinterest.com", "click.googleanalytics.com",
    "settings.luckyorange.net", "static.ads-twitter.com", "metrics.icloud.com", "analyticsengine.s3.amazonaws.com",
    "pixel.facebook.com", "app.bugsnag.com", "browser.sentry-cdn.com", "analytics.s3.amazonaws.com",
    "script.hotjar.com", "partnerads.ysm.yahoo.com", "analytics.pinterest.com", "o2.mouseflow.com",
    "identify.hotjar.com", "surveys.hotjar.com", "claritybt.freshmarketer.com", "static.media.net",
    "cdn-test.mouseflow.com", "ads.youtube.com", "iot-eu-logser.realme.com", "grs.hicloud.com",
    "log.byteoversea.com", "business-api.tiktok.com", "analytics.tiktok.com", "bdapi-ads.realmemobile.com",
    "metrics2.data.hicloud.com", "logbak.hicloud.com", "adx.ads.oppomobile.com", "data.ads.oppomobile.com",
    "cdn.mouseflow.com", "ck.ads.oppomobile.com", "iadsdk.apple.com", "analytics-api.samsunghealthcn.com",
    "analytics-sg.tiktok.com", "w1.luckyorange.com", "logservice.hicloud.com", "iot-logser.realme.com",
    "sdkconfig.ad.intl.xiaomi.com", "analytics.pointdrive.linkedin.com", "metrics.data.hicloud.com", "logservice1.hicloud.com",
    "media.net", "ads.linkedin.com", "sdkconfig.ad.xiaomi.com", "cdn.luckyorange.com",
    "webview.unityads.unity3d.com", "adtago.s3.amazonaws.com", "appmetrica.yandex.ru", "advice-ads.s3.amazonaws.com",
    "tracking.rus.miui.com", "bdapi-in-ads.realmemobile.com", "gemini.yahoo.com", "adm.hotjar.com",
    "ads-sg.tiktok.com", "adsfs.oppomobile.com", "data.mistat.xiaomi.com", "stats.wp.com",
    "app.getsentry.com", "tools.mouseflow.com", "samsungads.com", "insights.hotjar.com",
    "ads.tiktok.com", "analytics.yahoo.com", "adtech.yahooinc.com", "metrika.yandex.ru",
    "ads-api.tiktok.com", "adfstat.yandex.ru", "adfox.yandex.ru", "data.mistat.rus.xiaomi.com",
    "data.mistat.india.xiaomi.com", "careers.hotjar.com", "mouseflow.com"
]

new_rules = []
current_id = start_id

for domain in domains:
    rule = {
        "id": current_id,
        "priority": 1,
        "action": {"type": "block"},
        "condition": {
            "urlFilter": domain,
            "domainType": "thirdParty",
            "resourceTypes": ["script", "image", "xmlhttprequest", "sub_frame"]
        }
    }
    new_rules.append(rule)
    current_id += 1

# Print without outer brackets to easy copy-paste/file insertion
json_str = json.dumps(new_rules, indent=2)
# Remove the first '[' and last ']' to insert into existing array
print(json_str[1:-1])
