from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        handler_input.response_builder.speak("Hola a todos, esta es la calaverita que queremos compartir con ustedes,"+
                                            'Estaba Romi muy emocionada,'+
                                            'por transformar el futuro de la educación,'+
                                            'con el learning job se sentía muy preparada,'+
                                            'pero nunca imaginó afrontarse con tal aberración,'+
                                            'ante sus ojos una calaca muy arreglada,'+
                                            'llego por ella sin más antelación,'+
                                            'ja, ja, ja,'+
                                            'Ani se encontraba en el chai comiendo,'+
                                            'después de un exhausto día de trabajo,'+
                                            'cuando una extraña figura le estaba sonriendo,'+
                                            'era la muerte que la esperaba sin atajo,'+
                                            'no me gustan los cambios quiero seguir viviendo'+
                                            'sus últimas palabras que se escucharon desde abajo,'+
                                            'ja, ja, ja,'+
                                            'Andrea y cesar un curso se encontraban impartiendo,'+
                                            'Cuando comenzaron a escuchar un sonido muy tétrico,'+
                                            'era la huesuda que por ellos venía corriendo,'+
                                            'cesar grito y ahí quedó pues aquello era muy terrorífico,'+
                                            'Andrea confundió a la muerte por lo que continuó sonriendo,'+
                                            'a pesar de ser llevaba por algo tan maléfico,').set_should_end_session(False)
        return handler_input.response_builder.response    

class CatchAllExceptionHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        print(exception)
        handler_input.response_builder.speak("Sorry, there was some problem. Please try again!!")
        return handler_input.response_builder.response

class ChineseAnimalIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("ChineseAnimalIntent")(handler_input)

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