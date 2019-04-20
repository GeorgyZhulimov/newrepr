class AliceRequest(object):
    """docstring forAliceRequest."""

    def __init__(self, request_dict):):
        self._reqest_dict=request_dict

        @property
        def version(self):
            return self.request_dict['version']
        @property
        def session(self):
            return self.request_dict['session']
        @property
        def user_id(self):
            return self.session['user_id']
        @property
        def is_new_session(self):
            return bool(self.session['new'])
        @property
        def command(self):
            return self._request_dict['request']['command']
        def command(self):
            return self._request_dict['request']['command']
        def __str__(self):
            return str(self._request_dict)

    class AliceResponse:
        def __init__(self, alice_request):
            self._response_dict = {
            "version":alice_request.version,
            "session":alice_request.session,
            "response":{
                "end_session": False
                }
            }

            def dumps(self): #ограничение кол-ва символов в сообщениях алисы
                self._response_dict["response"]["text"] = text[:1024]

            def set_tts(self, text) #это то,что алиса должна сказать голосом
                self._response_dict["response"]["tts"] = text[:1024]
            def set_buttons(self, buttons):
                self._response_dict['response']['buttons']=buttons
            def __str__(self):
                return self.dumps()
