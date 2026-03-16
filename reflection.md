# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?


- What did the game look like the first time you ran it?
      The game looked like it was not correctly identifying how it was supposed to run. It was not matching what it said 
      in different parts of the screen. Things like saying choose a number between 1 - 100 when it was meant to be 1 - 20.
      It had general logic down, but messed up with game modes and also resetting it.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
      It was not input validating, meaning I could put in numbers above its max value and it would tell me to go higher even though I was not in range. I was never able to start a new game, so I had to reload the page each time I wanted to try again. Changing game modes did not change the range I was told to look through, leading to more errors in input validation.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    I am using Claude.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    It suggested that I change the way the low/ high was shown in order to make sure that the ranges matched with the buttons.
    
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
    It kept on suggesting that I keep dead code, which would later infringe on different functions. I made sure to delete all functions that had been replaced, even when it said it could be kept.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    I kept on reloading the game. I would work through the different modes and test a number too high, too low, and then the correct number and see how the game reacted.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
    I manually ran most of my tests through trial and error within the game. It showed me how much of the code did not match. The attempts and scores were often not uniform across the app and had to be changed every time a function was altered.
- Did AI help you design or understand any tests? How?
    AI helped with my tests to give me an idea of how to test out of range numbers. It gave basic suggestions for each test which I would later implement. 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  I believe the number kept on reloading due to the order of the code running. 
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  I would explain that every interaction causes a rerun, so it can cause variables to reset, or the number to reset.

- What change did you make that finally gave the game a stable secret number?
  I made it so the secret number is loaded once, so that it is not constantly being changed by outside changes. The status of playing was being tracked.


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
      I preferred jumping between the game and the code, I liked seeing in real time how my changes altered the code.
      I would occasionally get an error after small changes which was helpful to see what changes were not efficient.
- What is one thing you would do differently next time you work with AI on a coding task?
    I would focus more on tests, since I mainly used the game for testing. I want more practice with testing without a reliance on AI.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
      It changed my ideas on what AI is capable of creating, I saw it stumble on generating larger groups of code but was able tos pot bugs in smaller functions.
