# Dependency Parser Trainer

This Project is inspired by Stanford NLP Paper: A Fast and Accurate Dependency Parser using Neural Networks

Goal: We want to generate labels for wikipedia pages. One way to accomplish it is to 
find sentences containing links to other pages. To do that, we need to explore the relationship
between the words that is a href link and the title of this WiKi Page. The semantic 
relationship would be the labels that we generate for this Wikipedia Page.

First of all, we integrate corpus from Universal Dependency Tree Banks with special interest in English. 
The corpus contains ~27000 sentences and three wikipedia pages. Glove Model are used to generate 
word vectors for corpus. 
