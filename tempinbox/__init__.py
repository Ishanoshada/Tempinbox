import requests
import user_agent

class TempEmail:
    def __init__(self):
        self.token, self.cookie = self._get_token_cookie()

    def _get_token_cookie(self):
        try:
            url = "https://www.emailnator.com/"
            headers = {
                "User-Agent": user_agent.generate_user_agent(),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
            }

            response = requests.get(url, headers=headers)
            cookie = response.cookies.get_dict()
            token = cookie["XSRF-TOKEN"][:339] + "="
            return token, cookie
        except Exception as e:
            pass
         #   print(f"Error getting token and cookie: {e}")
            return self._get_token_cookie()

    def generate_temp_email(self, domain=False, dot_gmail=True, plus_gmail=False):
        url = "https://www.emailnator.com/generate-email"
        headers = {
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "hehe",
            "Content-Type": "application/json",
            "X-XSRF-TOKEN": self.token,
            "User-Agent": "hehe"
        }
        params = {"email": []}

        if domain:
            params["email"].append("domain")
        elif dot_gmail:
            params["email"].append("dotGmail")
        elif plus_gmail:
            params["email"].append("plusGmail")

        response = requests.post(url, json=params, cookies=self.cookie, headers=headers)
        email = response.json()
        return email

    def get_mail_list(self, email):
        url = "https://www.emailnator.com/message-list"
        headers = {
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "hehe",
            "Content-Type": "application/json",
            "X-XSRF-TOKEN": self.token
        }
        params = {"email": email}

        response = requests.post(url, json=params, cookies=self.cookie, headers=headers)
        return response.json()

    def get_mail_content(self, email, id, save_filename=None):
        mail_list = self.get_mail_list(email)

        if int(id) == 1:
            return "Default content for id 1"

        try:
            message_id = mail_list["messageData"][id - 1]['messageID']
        except Exception as e:
            return f"Error: {e} - Invalid message id"

        url = "https://www.emailnator.com/message-list"
        headers = {
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36",
            "Content-Type": "application/json",
            "X-XSRF-TOKEN": self.token
        }
        params = {"email": email, "messageID": message_id}

        response = requests.post(url, json=params, cookies=self.cookie, headers=headers)

        if "Server Error" in response.text:
            print("Server Error. Please wait.")
            return self.get_mail_content(email, id)

        if save_filename:
            with open(save_filename, "a") as file:
                file.write(response.text)
                print("Content saved")

        return response.text


