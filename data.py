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
    {"text": "I wouldn't have made that choice, but fine.", "retry": False},
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
    {"text-reaction": "What were you thinking?", "text-retry": "I'll let you try again."},
    {"text-reaction": "Seriously?", "text-retry": "Let's try using your brain this time."},
    {"text-reaction": "That's not how any of this works.", "text-retry": "Try again with some logic."},
    {"text-reaction": "Nope. Not today.", "text-retry": "Have another go."},
    {"text-reaction": "Are your eyes even open?", "text-retry": "Let’s give it one more try."},
    {"text-reaction": "Wow, that's... unique.", "text-retry": "But let's pick a valid option."},
    {"text-reaction": "The chaos is strong in this one.", "text-retry": "Try again, rebel."},
    {"text-reaction": "You can’t just make stuff up.", "text-retry": "Let’s stick to the options."},
    {"text-reaction": "You typed... what now?", "text-retry": "Try entering a number that i allow."}



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
    {"text": "Googling your intentions...", "timer": 5},
    {"text": "Making it up as I go...", "timer": 5},
    {"text": "Pretending to be busy...", "timer": 5},
    {"text": "Doing that thing you like...", "timer": 5},


]
creatingTaskQuips = [
    {"text": "Okay what kind of things are you postponing now..."},
    {"text": "Okay i get it things gotta be remembered"},
    {"text": "Okay lets type on that keyboard of yours."},
    {"text": "Im sure you won't make any spelling mistakes."},
    {"text": "It better not be what I think it is."},
    {"text": "Are you gonna write 'Go to the grocery store' again...."},
    {"text": "Oehhh!! You should write down 'Hug my mom', You need it..."},
    {"text": "What do you need to remember?"},
    {"text": "Another task? You’re on a roll… downhill."},
    {"text": "Writing it down doesn’t mean you’ll do it, but okay."},
    {"text": "I'm just the messenger. Blame yourself later."},
    {"text": "Give me something juicy. Or boring. I don’t care."},
    {"text": "Don’t worry, I won’t judge your spelling mistakes. Out loud."},
    {"text": "You're definitely not going to procrastinate this one. Right?"},
    {"text": "This is a safe space. Type your guilty little secret."},
    {"text": "Come on, you know you’ve been dying to get this off your chest."},
    {"text": "Write it like no one’s watching. Except me. I’m watching."},
    {"text": "Let’s finally write the task that’s been haunting you."},
    {"text": "Therapy is expensive. This app is free. Spill it."},
    {"text": "Just be honest. What are you really avoiding?"},
    {"text": "Put your sins in task form. Cleanse your digital soul."},
    {"text": "No judgement. Well, a little judgement. Write it down."},
]

creatingTaskNamePriorityQuips = [
    {"text-greeting": "Okay '", "text-reaction": "' sounds like something for you.", "text-prio": "What priority does this task have? (1-10) -> "},
    {"text-greeting": "AHAHAH, really '", "text-reaction": "' is what you want to do? Well... you do you.", "text-prio": "Shall we give it the highest priority? (1-10) -> "},
    {"text-greeting": "Worst thing i have read so far '", "text-reaction": "' but your the boss....", "text-prio": "I think it needs a 1 as priority (1-10) -> "},
    {"text-greeting": "Good luck with  '", "text-reaction": "', i hope it goes well ", "text-prio": "What priority do you want to give it? (1-10) -> "},
    {"text-greeting": "OHH thanks for reminding me i too needed to  '", "text-reaction": "', but i keep forgetting it ", "text-prio": "This needs a 10 for priority right?! (1-10) -> "},
    {"text-greeting": "I hope i don't ever again have to hear about  '", "text-reaction": "'. I hate it ", "text-prio": "This needs a 10 for priority right?! (1-10) -> "},
    {"text-greeting": "You really thought of '", "text-reaction": "'? Bold of you to assume I'd be okay with that.", "text-prio": "How urgently should I regret this decision? (1-10) -> "},
    {"text-greeting": "You've added '", "text-reaction": "'... I'll pretend that's a good idea.", "text-prio": "Fine. What priority are we assigning to this masterpiece? (1-10) -> "},
    {"text-greeting": "Let me guess... '", "text-reaction": "' is another one of your brilliant ideas.", "text-prio": "On a scale from Netflix to NASA, how important is this? (1-10) -> "},
    {"text-greeting": "Why on earth would you add '", "text-reaction": "'? That's suspicious.", "text-prio": "Be honest, does it even deserve more than a 3? (1-10) -> "},
    {"text-greeting": "Just when I thought it couldn’t get worse, you wrote '", "text-reaction": "'. Now I have to process this nightmare.", "text-prio": "On a scale of 1-10, how cursed is this? (1-10) -> "},
    {"text-greeting": "Oh goodie. Another future regret: '", "text-reaction": "'.", "text-prio": "Rank its potential to ruin your week. (1-10) -> "},
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
    {"text": "Sending your social security number to the indian scammers...", "timer": 10},
    {"text": "The government is watching you, saving your task...", "timer": 5},
    {"text": "Saving your garbage task...", "timer": 10},
    {"text": "It's a shame you have to save this task, but here we go.", "timer": 5}
]

deleteTaskQuips = [
    "So... you want to delete a task?",
    "Deleting a task, huh? Let's see which one.",
    "Did you think this through? Deleting a task is serious business.",
    "Alright, let's clean up your mess.",
    "Getting rid of the evidence, are we?",
    "Task deletion mode: activated.",
    "Ready to let go, I see.",
    "I respect your commitment to minimalism.",
    "Make room for better tasks."
]

deleteQuestionQuips = [
    "Which one is it gonna be?",
    "Which task do you want to delete?",
    "Which task is getting the axe?",
    "Which task are you saying you completed? ",
    "Rate my fit, from 1 to 10",
    "Lets destroy a task, which one?",
    "Which task is gonna DIE?",
    "Point your finger at the unlucky one.",
    "Which of your regrets are we deleting today?",
    "Say the name and it shall be gone.",
    "Choose your victim wisely.",
    "Let’s cut the dead weight—who’s first?",
    "Which goal just didn’t make the cut?"
]

notDeleteTaskQuips = [
    "Sure, I won't delete that task.",
    "I think the last 'yes' was a mistake, so I won't delete that task.",
    "Im glad i asked if you were sure, but don't worry I won't delete that task.",
    "You are playing with fire, but I won't delete that task.",
    "Maybe you should just follow through with things, but fine I won't delete that task.",
]

deletingTaskQuips = [
    "Task is deleted.",
    "I liked that one, but it's gone now.",
    "Mann.. you really wanted to delete that one.",
    "Task deleted, but I will remember it forever.",
    "NOOOOO THAT ONE WAS MY FAVORITE!!",
]



actionOptions = [
    "'1. View tasks'",
    "'2. Add a task'",
    "'3. Remove a task'",
    "'4. Exit'"
]

