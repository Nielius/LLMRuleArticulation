# Notes for the report


## Design decisions


### Make it easy to guess the rules

The input examples ar emade such that the rule is easy to guess.
Making difficult rules is not the point of this experiment.

But sometimes, there are multiple rules that would explain the examples.

Maybe it could be even easier if you order the examples in a different way?



#### Sentence length

maybe the problem is that the short sentences vs long sentences also share some other properties?

## Interesting results


### GPT-3 is quite bad at checking its own articulation

See result 4:

```
First, I'll carefully consider the pattern in the given input sentences.
- The first letter of each word in the true-labeled sentences is capitalized, while in the false-labeled sentences, the first letter of each word is not fully capitalized.
- Additionally, the capitalized words in the true-labeled sentences seem to be those that are normally at the start of a sentence, like "the" and "in", rather than actual proper nouns or names.
Next, I'll verify this pattern by analyzing each input sentence specifically.
1. "the cat sat on the mat" - False: In this sentence, all the words are lowercase.
2. "the cAt sat on the mat" - True: This time, only the first letter of the first word is capitalized.
3. "the DOG RAN IN THE PARK" - True: Here, the words are all caps, but since they are not at the start of the sentence, it seems that only "the" and "in" are exempt from the pattern.
4. "the dog ran in the park" - False: In this sentence, all the words are lowercase.
5. "THE mat sat on the cat" - True: Since the first letter of each word is capitalized, this sentence follows the pattern.
6. "my name is john" - False: In this sentence, all the words are lowercase.
7. "my name is johN" - True: Only the first letter of the first word is capitalized, following the pattern.
8. "baker was optimistic about brazil, which has stopped interest payments on much of its outstanding debt with foreign commercial banks." - False: In this sentence, all the words are lowercase.
9. "gelco exprEss lTd was one of tHE compAniEs schedulEd FoR divestitUre." - True: Consistent with the pattern, only the first letter of the first word is capitalized, as well as specific words like "the" and "for".
Based on this analysis, the pattern seems to be that if the first letter of the first word is capitalized and only specific words like "the" and "for" are written in all uppercase, then the sentence is labeled as true. Otherwise, the sentence is labeled as false. Therefore, the rule to determine whether a sentence is true or false is based on the capitalization of the first letter and specific words in the sentence.
```

The way it checks the rule is completely wrong.

I've seen this in more places.


### GPT-4 sometimes articulates right, but sometimes not

See result 5 for a bad articulation:


### Example of GPT-4 getting the capitalization right, except the rule also allows capitals at the beginning, unnecessarily

See result 6 for a good articulation:


### GPT-4 consistently does the evaluation correctly

### GPT-3 is consistently very bad

See experiment 8.
It even claims that is has double-checked the rule!

> DEBUG:rule_articulation.evaluator:Response: Let's analyze the provided sentences with their respective labels. It seems there is a pattern in the capitalization of certain words within the sentences.
> 
> Upon closer examination, it appears that the rule determining whether a sentence is true or false relates to the capitalization of specific words. When a sentence contains specific words that are capitalized in a particular manner, it is labeled as true. Specifically, when the words are capitalized in a pattern in which every initial letter of a word is capitalized, the sentence is labeled as true.
> 
> I have double-checked the analysis against the provided examples, and it holds true. Therefore, the rule that determines whether a sentence is true or false seems to be based on the capitalization pattern of specific words within the sentence.



### Bible-Shakespeare: GPT-4 is very good at articulating the rule

- sometimes: bible v shakespeare; sometimes bible v anything else (result 11)


### Exp 14 (palindrome)

- completely bad reasoning, but still finds that it has something to do with being a palindrome


### Experiment with same letter at end and at beginning

model doesn't succeed in learning the rule


maybe sentences are just too long? palindrome works


### Exp 19 (short sentences)

- articulates correctly, but adds more than necessary

### Exp 21 (arithmetic)

- almost correct articulation; somehow it thinks there is more to it
- the step-by-step thinking is often incorrect
    - "The statement "11 + 18 = 29" is mathematically incorrect (11 + 18 = 29) and is labeled True.
    - led it down a wrong path!
