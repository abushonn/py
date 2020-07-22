import csv

class Utterance:
    def __init__(self,a_text, an_intent):
        self.text = a_text
        self.intent = an_intent

    def is_intent_correct(self, an_intent):
        return (self.intent == an_intent)

    def to_string(self):
        return ('{%s-----%s}' % (self.text, self.intent))

    def to_wa_intent_example_format(self):
        '''
        :return: dictionary {'text' : self.text}
        '''
        res_dict = {}
        res_dict['text'] = self.intent

        return res_dict


    def main(self):
        print('utterance: %s ;;; intent: %s'%(self.text, self.intent))
        # print('Is %s  equal to %s ? '%(self.to_string(), 'deductible_oop_inquiry'))
        # print(self.is_intent_correct('deductible_oop_inquiry'))

        print(self.to_wa_intent_example_format())

class Intent:
    def __init__(self, an_intent_name, a_list_of_examples=[]):
        self.intent_name = an_intent_name
        self.list_of_examples = a_list_of_examples
        print('Created Intent ' + self.intent_name)
        print('a_list_of_examples = ' + str (a_list_of_examples))
        print('llllllll = ' + str(self.list_of_examples))

    def to_string(self):
        return ('{%s-----%s}' % (self.intent_name, self.list_of_examples))


    def to_wa_intent_format(self):
        '''
         :return: dictionary {'intent' : self.intent_name, 'examples': self.list_of_examples}
         '''
        res_dict = {}
        res_dict['intent'] = self.intent_name
        res_dict['examples'] = self.list_of_examples

        return res_dict

    def add_example(self, exampleText):
        '''
        example in WA format: example1 = {'text': 'going shopping'}
        Updates the list of examples of this intent
        :param exampleText: text of the example
        :return: None.
        '''
        intentFormattedStr = "{'text': '%s'}"%exampleText
        self.list_of_examples.append(intentFormattedStr)

class WaIntents:
    '''
    Set of intents for WA workspace
    e.g. of a line in intents_file_name: "What will be my out of pocket cost for the visit?,benefit_coverage"
    '''
    def  __init__(self,intents_file_name):
        self.intents = {}
        with open(intents_file_name) as intents_file:
            csv_reader = csv.reader(intents_file, delimiter=',')

            for ll in csv_reader:
                aText, anIntentName = ll[0], ll[1]
                # print('text: %s ;;; intent: %s'%(aText, anIntentName ))

                intent = self.intents.get(anIntentName)
                if intent is None:
                    print('New Intent!  ' +  anIntentName)
                    self.intents[anIntentName] = Intent(anIntentName, [])

                # else:
                #     print('Existing Intent: ' + anIntentName)

                self.intents[anIntentName].add_example(aText)
                # print('222222222222 ' +  str(self.intents[anIntentName].to_wa_intent_format()))

    def print_intents(self):
        for ii in self.intents:
            print(self.intents[ii].to_wa_intent_format())

    def prepare_intents_test(self):
        # intent 1
        example1 = {'text': 'going shopping'}
        example2 = {'text': 'lets go shopping'}
        intent1 = {'intent': 'shopping',
                   'examples': [example1, example2]
                   }

        # intent 2
        example1 = {'text': 'time for games'}
        example2 = {'text': 'wanna play?'}
        intent2 = {'intent': 'playing',
                   'examples': [example1, example2]
                   }
        intents = [intent1, intent2]

        return intents

def intents_main():

    ################## class Intent
    # intent = Intent('deductible_oop_inquiry', [])
    # intent.add_example('What will be my out of pocket cost for the visit?')
    # print(intent.to_string())
    # print(intent.to_wa_intent_format())

    ################## class WaIntents
    wa_intents = WaIntents('data-results/intents-01.csv')
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    wa_intents.print_intents()
