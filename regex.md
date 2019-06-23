## Regex

Complete Regular Expressions Bootcamp - Go from zero to hero - Udemy
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

### Limiting Repetition

    - \d{n} - exactly n times
    - \d{min, } - at least n times
    - \d{min, max} - at least n times and no more than m times

**Example: **
    
    [a-z]{4} will match "this" and not will not match "thi4"


### Greedy Nature

**Greedy** - matches the previous element as many times as possible (left most longest match)
    
    ? + * are by default Greedy
    
**Example**

    regex: ".+"
    I like "moon" and "stars" as they are amazing.
    ""moon" and "stars"" will be returned instead of "moon"

**Lazy** - matches the previous element as few times as possible

    +? - matches btw 1 and unlimited times as few times as possible (lazy)

**Example**

    regex: "[^"]+" (use negation ^" - not ")
    I like "moon" and "stars" as they are amazing.
    will be returne both of "moon" and "stars" separately

### Anchors and Boundaries

    ^ - occur at the beginning of the string
    $ - occur at the end of the string
    \b - occur on the boundary btw. a \w and a \W
    \w  [a-zA-Z0-9_]  
    \W  [^\w]

### Groups and Alternation

**Groups** - similar to word set

      Syntax: - (group)

**Alternation** - similar to character set

      Syntax: - (   |   )


**Example**
 
    gr[ae]y and gr(a|e)y will both match "gray" and "grey"  



### Assertions - Lookaround

- **Positive Lookahead** - when you want to match an element (word char or group) if a certain word (element) comes after it
  
      Syntax:  - (?=       )

- **Negative Lookahead**  - when you want to match an element (word char or group) if a certain word (element) **doesn't** comes after it
      
      Syntax: - (?!       )

- **Positive Lookbehind** - when you want to match an element (word char or group) if a certain word (element) comes before it
  
      Syntax: - (?<=      )
  
- **Negative Lookbehind** - when you want to match an element (word char or group) if a certain word (element) **doesn't** comes before it
  
      Syntax: - (?<!      )
  
  
