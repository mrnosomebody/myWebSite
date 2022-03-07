import defines, requests


class InstagramAPI:
    app_id = defines.INSTAGRAM_APP_ID
    app_secret = defines.INSTAGRAM_APP_SECRET
    app_access_token = defines.INSTAGRAM_ACCESS_TOKEN

    def instagram_api_request(self):
        return requests.request(
            'GET',
            f'https://graph.instagram.com/me/media?\
            fields=id,\
            media_type,\
            media_url&\
            access_token={self.app_access_token}')

    def get_instagram_media(self):
        api_response_data = self.instagram_api_request().json()['data']
        media_urls = []
        for i in api_response_data:
            media_urls.append(i['media_url'])
        return media_urls
