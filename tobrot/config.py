from tobrot.sample_config import Config

#read readme too before filling these stuffs

class Config(Config):
    TG_BOT_TOKEN= "1605318844:AAFjuuOINr4eldGvCCc1E0WY1DKTPqPebUY" #imp
    APP_ID = 2572948 #imp
    API_HASH = "3a6290dba92fd085c06ef07ba29ed52f" #imp
    AUTH_CHANNEL = [-424731631, 1113008502] #imp replace your_id with your id from telegram or delete
    INDEX_LINK = "https://index.asdf1.workers.dev"
    GLEECH_COMMAND = "gleech@torrent2gdriveasdf_bot"
    YTDL_COMMAND = 'ytdl@torrent2gdriveasdf_bot'
    TELEGRAM_LEECH_COMMAND_G = "tleech@torrent2gdriveasdf_bot"
    CLONE_COMMAND_G = "gclone@torrent2gdriveasdf_bot"
    PYTDL_COMMAND_G = "pytdl@torrent2gdriveasdf_bot"
    DESTINATION_FOLDER = "Torrent-Gdriveasdf"
    LEECH_COMMAND = "leech@torrent2gdriveasdf_bot"
    CANCEL_COMMAND_G = "cancel@torrent2gdriveasdf_bot"
    RCLONE_CONFIG = """type = drive\nscope = drive\ntoken = {"access_token": "ya29.a0AfH6SMArgKbtYdT7Aqn7UQDN2Bg2xoL5tneLX0eeUUuDQhshBufLeDjPZmm-lHrJyLjSePAKxWjTuYCTU292pyeq4qCOZPTrfb9PjN1iIV8_kG8Kdi_FTIYms72Zvsey4EzCs3YBsTsndDBeSisoAPULV1VLzbTO_ae9vWNitYU", "client_id": "409238718252-sn6jculr6jsunllaknhu88i1ap4q4ek1.apps.googleusercontent.com", "client_secret": "cqLRf9lQx1tWYm_anwBfhAn6", "refresh_token": "1//04SgJdWaMZV9PCgYIARAAGAQSNwF-L9IrK8T80NSvlZXVPqQvibXjmaM7VhYjmtDi1zPWvV8LRGtt5tSGEFwCwtrNZ0g1oEGsGFQ", "token_expiry": "2021-02-04T16:11:42Z", "token_uri": "https://oauth2.googleapis.com/token", "user_agent": null, "revoke_uri": "https://oauth2.googleapis.com/revoke", "id_token": null, "id_token_jwt": null, "token_response": {"access_token": "ya29.a0AfH6SMArgKbtYdT7Aqn7UQDN2Bg2xoL5tneLX0eeUUuDQhshBufLeDjPZmm-lHrJyLjSePAKxWjTuYCTU292pyeq4qCOZPTrfb9PjN1iIV8_kG8Kdi_FTIYms72Zvsey4EzCs3YBsTsndDBeSisoAPULV1VLzbTO_ae9vWNitYU", "expires_in": 3599, "refresh_token": "1//04SgJdWaMZV9PCgYIARAAGAQSNwF-L9IrK8T80NSvlZXVPqQvibXjmaM7VhYjmtDi1zPWvV8LRGtt5tSGEFwCwtrNZ0g1oEGsGFQ", "scope": "https://www.googleapis.com/auth/drive", "token_type": "Bearer"}, "scopes": ["https://www.googleapis.com/auth/drive"], "token_info_uri": "https://oauth2.googleapis.com/tokeninfo", "invalid": false, "_class": "OAuth2Credentials", "_module": "oauth2client.client"}\nteam_drive = True"""
    #put your config(replacing new lines with \n) in triple quote like above: """<your one liner config>"""
