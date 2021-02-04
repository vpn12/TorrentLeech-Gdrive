from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1605318844:AAFjuuOINr4eldGvCCc1E0WY1DKTPqPebUY"
    APP_ID = 2572948
    API_HASH = "3a6290dba92fd085c06ef07ba29ed52f"
    OWNER_ID = 1113008502
    AUTH_CHANNEL = [-424731631]
    DESTINATION_FOLDER = "Torrent-Gdriveasdf" #Name of your folder read readme(not id of the folder)
    #Just don't fill RCLONE_CONFIG vars, insted copy your rclone.conf file in root directory
    #if your wanted to fill -- fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    RCLONE_CONFIG = """
[DRIVE]
type = drive
client_id = 409238718252-sn6jculr6jsunllaknhu88i1ap4q4ek1.apps.googleusercontent.com
client_secret = cqLRf9lQx1tWYm_anwBfhAn6
scope = drive
root_folder_id = 0AEfszerRLY2AUk9PVA
token = {"access_token": "ya29.A0AfH6SMAI6NdaIqDdDCGkK79yV-QT_nFHXAO0amWtPYbdGOI-OLHulPK0tonzXfgRbntAWxJtOY9vHcbxXSTJgK6eyJTjN9m-U_iMbEZq_939TbML5GNymOFj_1EZeLjxBxZe3RAqxuP6EFsfMUaJ4pKbst3P", "client_id": "409238718252-sn6jculr6jsunllaknhu88i1ap4q4ek1.apps.googleusercontent.com", "client_secret": "cqLRf9lQx1tWYm_anwBfhAn6", "refresh_token": "1//04pLRIrwEey5mCgYIARAAGAQSNwF-L9IrjoCS90OB_awlZpj853oZgVP1AA44EzQr5j2hCLDCtl22RBUJzf5d7GAtIjj1VzBPJaE", "token_expiry": "2021-02-04T16:40:20Z", "token_uri": "https://oauth2.googleapis.com/token", "user_agent": null, "revoke_uri": "https://oauth2.googleapis.com/revoke", "id_token": null, "id_token_jwt": null, "token_response": {"access_token": "ya29.A0AfH6SMAI6NdaIqDdDCGkK79yV-QT_nFHXAO0amWtPYbdGOI-OLHulPK0tonzXfgRbntAWxJtOY9vHcbxXSTJgK6eyJTjN9m-U_iMbEZq_939TbML5GNymOFj_1EZeLjxBxZe3RAqxuP6EFsfMUaJ4pKbst3P", "expires_in": 3599, "refresh_token": "1//04pLRIrwEey5mCgYIARAAGAQSNwF-L9IrjoCS90OB_awlZpj853oZgVP1AA44EzQr5j2hCLDCtl22RBUJzf5d7GAtIjj1VzBPJaE", "scope": "https://www.googleapis.com/auth/drive", "token_type": "Bearer"}, "scopes": ["https://www.googleapis.com/auth/drive"], "token_info_uri": "https://oauth2.googleapis.com/tokeninfo", "invalid": false, "_class": "OAuth2Credentials", "_module": "oauth2client.client"}
team_drive = True
"""
