class Setting_keywords:
    sep1 = 'word-definition separator'
    undefined = ''


class Token:
    SETTINGS_BEGIN = '%{'
    SETTING: str = Setting_keywords.undefined
    SETTINGS_END = '%}'
