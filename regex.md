## Regex


Udemy 
- https://www.udemy.com/learn-regular-expressions-in-online-regex-course/learn/lecture/9733920#overview


### Metacharacters

Metacharacters - characters with special meanings


### Character Set

Character Set - match any single character in that set

**Syntax:**

  - [charater set]


### Quantifiers

  - **?** - 0 or 1 time
  - **\*** - 0 or more time
  - **+** - 1 or more time
  
  #### Limiting Repetition
  
    - \d{n} - exactly n times
    - \d{min, } - at least n times
    - \d{min, max} - at least n times and no more than m times
  
ex.
[a-z]{4}

will match "this" and not will not match "thi4"

### Anchors and Boundaries

  - **^** - occur at the beginning of the string
  - **$** - occur at the end of the string
  - **\b** - occur on the boundary btw. a \w and a \W
  
  - \w  [a-zA-Z0-9_]  
  - \W  [^\w]
  
  
  
  
  
  
