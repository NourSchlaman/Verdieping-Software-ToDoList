tasks = [
    {"id":1 ,"name": "1000 pushups", "priority": 8},
    {"id":2 ,"name": "Heel veel aardbeien eten", "priority": 3},
    {"id":3 ,"name": "afvallen", "priority": 10},
]

decisionMakingQuips = [
    {"text": "Thank you for your Critical Decision Making.", "retry": False},
    {"text": "You thought long and hard about that decision, didn't you?!", "retry": False},
    {"text": "Are you sure about that?", "retry": False},
    {"text": "Hmmmm, interesting choice.", "retry": False},
    {"text": "You must have given that a lot of thought.", "retry": False},
    {"text": "I wouldn't have made that choice.", "retry": False},
    {"text": "Lets do that.", "retry": False},
    {"text": "Good idea!", "retry": False},
    {"text": "okey..", "retry": False},
    {"text": "I like that one", "retry": False},
    {"text": "Thank your for admitting your goals.", "retry": False},
    {"text": "I despise this here decision.", "retry": True},
    {"text": "NOOO PLEASE NOT THAT ONE!!", "retry": True},
    {"text": "Sorry for the inconvenience, but that choice is not available at the moment.", "retry": True},
    {"text": "ERROR - Something went wrong.", "retry": True}
]

notCorrectDecisionQuips = [
    {"text-reaction": "That is not a valid choice.", "text-retry": "Try again."},
    {"text-reaction": "Please enter a valid option.", "text-retry": "Let's try again."},
    {"text-reaction": "Are you trying to fool me?", "text-retry": "Better luck next time."},
    {"text-reaction": "That was not an option.", "text-retry": "You should read better next time."},
    {"text-reaction": "I thought the options were pretty clear.", "text-retry": "Let's try reading again."},
    {"text-reaction": "That was just stupid.", "text-retry": "Go ahead, give it another try."},
    {"text-reaction": "What were you thinking?", "text-retry": "I'll let you try again."}
]

processingQuips = [
    {"text": "Processing...", "timer": 5},
    {"text": "Binging Linus Tech Tips, one moment please...", "timer": 5},
    {"text": "Thinking about you ;)", "timer": 5},
    {"text": "Running over rainbows", "timer": 5},
    {"text": "Lemme think about that one...", "timer": 10},
    {"text": "Hhmmm, this won't take long...", "timer": 100},
    {"text": "I'm thinking, one moment please...", "timer": 10},
    {"text": "Thinking...", "timer": 20},
    {"text": "Phoe tough one..", "timer": 500},
    {"text": "Grinding gears...", "timer": 5},
    {"text": "The bees are busy...", "timer": 5},
    {"text": "Hold up! Wait a minute!", "timer": 60},
]
creatingTaskQuips = [
    {"text": "Okay what kind of things are you postponing now..."},
    {"text": "Okay i get i things gotta be remembered"},
    {"text": "Okay lets type on that keyboard of yours."},
    {"text": "Im sure you won't make any spelling mistakes."},
    {"text": "It better not be what I think it is."},
    {"text": "Are you gonna write 'Go to the grocery store' again...."},
    {"text": "Oehhh!! You should write down 'Hug my mom', You need it..."},
    {"text": "What do you need to remember?"}
]

creatingTaskNamePriorityQuips = [
    {"text-greeting": "Okay '", "text-reaction": "' sounds like something for you.", "text-prio": "What priority does this task have? (1-10) -> "},
    {"text-greeting": "AHAHAH, really '", "text-reaction": "' is what you want to do? Well... you do you.", "text-prio": "Shall we give it the highest priority? (1-10) -> "},
    {"text-greeting": "Worst thing i have read so far '", "text-reaction": "' but your the boss....", "text-prio": "I think it needs a 1 as priority (1-10) -> "},
]

savingTaskQuips = [
    {"text": "Saving task...", "timer": 8},
    {"text": "Saving your task...", "timer": 8},
    {"text": "Saving your task, please wait...", "timer": 8},
    {"text": "Saving task, please wait...", "timer": 50},
    {"text": "Saving task, hold on...", "timer": 15},
    {"text": "I am remembering your task...", "timer": 5},
    {"text": "I will never forget this task...", "timer": 10},
    {"text": "Go ahead watch this bar progress.", "timer": 20},
    {"text": "Ladadiee Ladadoo, I am saving your task for you.", "timer": 10},
    {"text": "Please insert a floppy disk to save your task.", "timer": 15},
    {"text": "Please insert a floppy disk to save your task.", "timer": 20},
    {"text": "I hate that i have to save this task, but here we go.", "timer": 30},
    {"text": "I dont know if i want to save this task, but here we go.", "timer": 30},
    {"text": "Sending your social security number to the government...", "timer": 10},
    {"text": "The government is watching you, saving your task...", "timer": 5},
    {"text": "Saving your garbage task...", "timer": 10},
    {"text": "It's a shame you have to save this task, but here we go.", "timer": 5}
]



actionOptions = [
    "'1. View tasks'",
    "'2. Add a task'",
    "'3. Remove a task'",
    "'4. Exit'"
]

