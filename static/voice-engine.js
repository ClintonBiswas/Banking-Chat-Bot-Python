var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
var SpeechGrammarList = SpeechGrammarList || webkitSpeechGrammarList;
var SpeechRecognitionEvent = SpeechRecognitionEvent || webkitSpeechRecognitionEvent;

var msgBox = document.querySelector('.msger-input');
var voiceBtn = document.querySelector('.voiceBtn');
var sendBtn = document.querySelector('.sendBtn');

function testSpeech() {
  voiceBtn.disabled = true;

  var grammar = '#JSGF V1.0; grammar phrase;';
  var recognition = new SpeechRecognition();
  var speechRecognitionList = new SpeechGrammarList();
  speechRecognitionList.addFromString(grammar, 1);
  recognition.grammars = speechRecognitionList;
  recognition.lang = 'en-US';
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;

  recognition.start();

  recognition.onresult = function(event) {
    var speechResult = event.results[0][0].transcript.toLowerCase();
    msgBox.value = speechResult;
    sendBtn.click();
    console.log('Confidence: ' + event.results[0][0].confidence);
  }

  recognition.onspeechend = function() {
    recognition.stop();
    voiceBtn.disabled = false;
  }

  recognition.onerror = function(event) {
    voiceBtn.disabled = false;
    msgBox.value = 'Error occurred in recognition: ' + event.error;
  }
}

voiceBtn.addEventListener('click', testSpeech);
