# chatbot-amazon-lex

I created this project to learn the basics of [Amazon Lex](https://aws.amazon.com/lex/). `Lex` is one of the services which did not have free tier so I did not advance too much into this project but I built a simple bot that answers basic questions about me.

## Core Concepts

### Intent

Itent is the fundamental meaning of the utterances that user gives. For example when user says show me the list of your experices, users intent is to get Experince. So, we can call this intent as `Experience`. This intent will have different utterences. Utterences are the sentences that users will say to exteact the information. For example for `Experience` some utterences could be:

* What is your experience
* What do you do
* what experience do you have
* what are the jobs that you worked on

These utterances are used to train our model on. The model will classify future similar utterances into `Experience` intent.

### Slot

Slot can be thought as a variable. For example, for a weather chat bot an uuterance could be `show me details about Singapoor`. In this uuterance `Singapoor` can be a slot as uer can ask `some me details about *` where `*` can be replaced with any city. So we can train our model to extract city name from utterance `show me details about {cityname}` by letting the model know that last part of sentence is our `slot` and we would need to extract that and store it into a variable named `{cityname}` to make api call (this variable can be used for anything and will be passed into lambda function)

### Session Variables

Some of the information that user provides can be useful later in conversation with bot. For example, a bot might ask who its chatting with when a user starts conversation. Later in the conversation user might want to perform an ation which would require his/her name. For scanerio like this, we can store the username into session variable that user provided at start of conversation and pass it between the intents. Lamnda function can then make use or update this session variable.

### Fullfilment using Lambda

When our model gets an utterance and it classifies the utterance into one of our intent, `amazon lex` can make a call to a particular lambda function with details about intent and slots. This lambda function can be used to return  appropriate response back to the end user.
