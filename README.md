# PrintPyramidOvercomplicated

Printing pyramids, at the time, was challenging on its own. 
Then I decided to overcomplicate it and split my code up into functions.
This is what coding late at night ended up becoming.

First I had to work out the maths for printing stars and blank spaces, it went something like this:
# line 1 will have 1 star  (i + (i + 1) (variable))
# line 2 will have 3 star  (i + (i + 1) (variable))
# line 3 will have 3 star  (i + (i + 1) (variable))
# line 4 will have 4 star  (i + (i + 1) (variable))
# line 5 will have 5 star  (i + (i + 1) (variable))
# line 6 will have 1 star  (i + (i + 1) (variable))

# line 1 will have (user_input - i) + 1 = 5 spaces
# line 2 will have (user_input - i) - 1 = 4 spaces
# line 3 will have (user_input - i) - 1 = 3 spaces
# line 4 will have (user_input - i) - 1 = 2 spaces
# line 5 will have (user_input - i) - 1 = 1 spaces
# line 6 will have (user_input - i) - 1 = 0 spaces

Not to mention it just wasn't a pyramid unless it had a door/entrance. x_X

Well needless to say, looking at the initial code the next morning, tweaking was needed.
