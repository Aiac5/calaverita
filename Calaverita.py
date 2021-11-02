def handler(event, context):
    print('hello world')
    return {"message": "Successfully executed"}

class ChineseAnimalIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("saludoIntent")(handler_input)

    def handle(self, handler_input):
        year = handler_input.request_envelope.request.intent.slots['year'].value
        speech_text = "My custom Intent handler"
        handler_input.response_builder.speak(speech_text).set_should_end_session(False)
        return handler_input.response_builder.response 

sb = SkillBuilder()
sb.add_request_handler(LaunchRequestHandler())
sb.add_exception_handler(CatchAllExceptionHandler())
sb.add_request_handler(ChineseAnimalIntentHandler())

def handler(event, context):
    return sb.lambda_handler()(event, context)
