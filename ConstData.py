userAuthList = {
    'line1' : {
        "xxr1052015": "http://sdk.cferw.com/api.php?z=3286&appkey=528ab6a566564a96a0b7646586f3c017&deviceId=868261025817163&sw=720&sh=1280&osver=22",
        "xxr249011": "http://sdk.cferw.com/api.php?z=3286&appkey=528ab6a566564a96a0b7646586f3c017&deviceId=868261025798611&sw=720&sh=1280&osver=22",
        "xxr2082731": "http://sdk.cferw.com/api.php?z=3286&appkey=528ab6a566564a96a0b7646586f3c017&deviceId=868261025797399&sw=720&sh=1280&osver=22",
        "xxr918253": "http://sdk.cferw.com/api.php?z=3286&appkey=528ab6a566564a96a0b7646586f3c017&deviceId=861799030710284&sw=720&sh=1280&osver=22",
        "xxr186002": "http://sdk.cferw.com/api.php?z=3286&appkey=528ab6a566564a96a0b7646586f3c017&deviceId=861799030658426&sw=720&sh=1280&osver=22",
        "xxr122525": "http://sdk.cferw.com/api.php?z=3286&appkey=528ab6a566564a96a0b7646586f3c017&deviceId=868261025883900&sw=720&sh=1280&osver=22",
        "XXR827151": "http://sdk.cferw.com/api.php?z=3286&appkey=528ab6a566564a96a0b7646586f3c017&deviceId=861799030711886&sw=720&sh=1280&osver=22",
        "xxr202325": "http://sdk.cferw.com/api.php?z=3286&appkey=528ab6a566564a96a0b7646586f3c017&deviceId=861799030711852&sw=720&sh=1280&osver=22",
        "xxR3045558": "http://sdk.cferw.com/api.php?z=3286&appkey=528ab6a566564a96a0b7646586f3c017&deviceId=861799030658392&sw=720&sh=1280&osver=22"
    },
    'line2':{
        "XXR1023133": "http://sdk.cferw.com/api.php?z=3286&appkey=528ab6a566564a96a0b7646586f3c017&deviceId=868261025797332&sw=720&sh=1280&osver=22",
        "XXR5010031": "http://sdk.cferw.com/api.php?z=3286&appkey=528ab6a566564a96a0b7646586f3c017&deviceId=868261025884031&sw=720&sh=1280&osver=22",
        "XXR7035179": "http://sdk.cferw.com/api.php?z=3286&appkey=528ab6a566564a96a0b7646586f3c017&deviceId=868261025881896&sw=720&sh=1280&osver=22",
        "XXR200072": "http://sdk.cferw.com/api.php?z=3286&appkey=528ab6a566564a96a0b7646586f3c017&deviceId=868261025799890&sw=720&sh=1280&osver=22",
        "XXR112981": "http://sdk.cferw.com/api.php?z=3286&appkey=528ab6a566564a96a0b7646586f3c017&deviceId=868261025883884&sw=720&sh=1280&osver=22",
        "XXR103534": "http://sdk.cferw.com/api.php?z=3286&appkey=528ab6a566564a96a0b7646586f3c017&deviceId=868261025797324&sw=720&sh=1280&osver=22",
        "XXR12336": "http://sdk.cferw.com/api.php?z=3286&appkey=528ab6a566564a96a0b7646586f3c017&deviceId=868261025883439&sw=720&sh=1280&osver=22",
        "XXR1055518": "http://sdk.cferw.com/api.php?z=3286&appkey=528ab6a566564a96a0b7646586f3c017&deviceId=868261025892927&sw=720&sh=1280&osver=22",
        "XXR276535": "http://sdk.cferw.com/api.php?z=3286&appkey=528ab6a566564a96a0b7646586f3c017&deviceId=868261025799718&sw=720&sh=1280&osver=22",
    }
}

specialTaskTypeUser = []

comment = {
    "xxr1052015": {'Tag':'智林杰'},
    "xxr249011": {'Tag':'智林杰'},
    "xxr2082731": {'Tag':'智林杰'},
    "xxr918253": {'Tag':'智林杰'},
    "xxr186002": {'Tag':'智林杰'},
    "xxr122525": {'Tag':'智林杰'},
    "XXR827151": {'Tag':'智林杰'},
    "xxr202325": {'Tag':'智林杰'},
    "xxR3045558": {'Tag':'智林杰'},

    "XXR1023133": {'Tag':'线路2'},
    "XXR5010031": {'Tag':'线路2'},
    "XXR7035179": {'Tag':'线路2'},
    "XXR200072": {'Tag':'线路2'},
    "XXR112981": {'Tag':'线路2'},
    "XXR103534": {'Tag':'线路2'},
    "XXR12336": {'Tag':'线路2'},
    "XXR1055518": {'Tag':'线路2'},
    "XXR276535": {'Tag':'线路2'},
}
commonUrls = [
    {
        'POST':'http://60.205.216.178:8080/bulletins/bulletin'
    },
    {
        'GET':'http://60.205.216.178:8080/focuss/focus'
    },
    {
        'GET':'http://60.205.216.178:8080/version/version'
    },
    {
        'POST':'http://60.205.216.178:8080/PromptController/queryPrompt'
    }
]

taskUrls = {
    'tasks':'http://60.205.216.178:8080/tasks/task',
    'taskStatus':'http://60.205.216.178:8080/uploads/jianshi',
    'doTask':'http://60.205.216.178:8080/uploads/fenxiang'
}
