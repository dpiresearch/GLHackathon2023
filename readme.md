# Overview
  Sometimes when we encounter new concepts ( i.e. through a paper ), we need to drill down into it or refresh our memory.  This app attempts to aid the user by providing a pathway to learning via references and examples. 
  In this demo, we illustrate this by deriving the top 5 papers to refer to related to the main paper, along with Python code samples to make the concepts more concrete

# Implementation
  The Anthropic UI allows uploads of files to augment prompts.  Unfortunately, the current APIs do not allow this and this functionality.
  This means we have to convert the paper PDF into text and add that to the prompt.  This makes prompt authoring more problematic as information is lost/corrupted during the conversion.

# Challenges
  We also wanted to show a hierarchical graph highlighting the top N concepts from the paper and how the user can traverse through the graph to learn various concepts either breath wise or depth wise.  However, going from text to graph proved challenging from an api standpoint.  Several strategies were attempted
    Stability ai - did not translate to hierarchy images cleanly - text was garbled
    Runway       - no api apparent
    Latex        - this was promising, but ran out of time

  
      
  
