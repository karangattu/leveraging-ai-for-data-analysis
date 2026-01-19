# Hands-On Exercises for Gemini Workshop

## Copy-Paste Ready Exercises for Google Gemini & NotebookLM

These exercises are designed to be copied and pasted directly into:
- **Google Gemini** at [gemini.google.com](https://gemini.google.com) 
- **NotebookLM** at [notebooklm.google.com](https://notebooklm.google.com)

No local software installation required! You're already set up with your Google Workspace account.

---

## Exercise 1: Getting Started (5 minutes)

### Task 1.1: Basic Ecological Questions

Copy and paste these prompts into Gemini one at a time:

```
What is a keystone species? Give me an example from North American ecosystems.
```

```
Explain the difference between species richness and species evenness in simple terms.
```

```
What are the main challenges in studying bird migration patterns?
```

**Reflection:** Notice how Gemini provides detailed, contextualized answers. How would you refine these prompts to get more specific information?

---

## Exercise 2: Improving Your Prompts (10 minutes)

### Task 2.1: Compare Poor vs. Good Prompts

**Poor Prompt:** Copy this into Gemini:
```
Tell me about bird diversity analysis
```

**Now try this improved version:**
```
I'm an ornithologist studying songbird communities in temperate forests. Explain how to compare bird diversity between old-growth and secondary forests. Include which diversity metrics to use and why.
```

**Notice the difference?** The second prompt includes:
- Your role (ornithologist)
- Specific context (songbird communities, temperate forests)
- Clear goal (compare diversity)
- Specific habitats (old-growth vs secondary)

---

### Task 2.2: Practice Refining

Take this vague prompt and paste your improved version into Gemini:

**Original:**
```
How do I analyze my data?
```

**Your improved version should include:**
- What kind of data (bird surveys, telemetry, nest monitoring?)
- What's your question?
- Sample size?
- What do you want to know?

**Example improvement:**
```
I have point count data from 30 sites surveyed 3 times each during breeding season. I counted individual birds by species. I want to determine if species richness differs between forest fragments of different sizes (small <10ha, medium 10-50ha, large >50ha). What statistical approach should I use?
```

---

## Exercise 3: Data Analysis Planning (15 minutes)

### Task 3.1: Get Analysis Recommendations

Copy this scenario into Gemini:

```
I have bird survey data with the following structure:
- 15 sites total (8 forest sites, 7 grassland sites)
- Each site surveyed 4 times during breeding season
- Recorded: site ID, date, species name, number of individuals
- Total of 45 different species observed

My research question: Do forest sites support higher bird species diversity than grassland sites?

Please suggest:
1. Which diversity index to use and why
2. Appropriate statistical test
3. What assumptions I need to check
4. How to handle the repeated surveys at each site
```

**Review Gemini's answer and ask follow-up questions like:**
```
Why did you recommend the Shannon index over Simpson index?
```

```
What if my data doesn't meet the normality assumption?
```

---

### Task 3.2: Get Code for Your Analysis

Now ask Gemini to generate code (even though you won't run it locally, you can see what the analysis would look like):

```
Based on the bird survey data I described, write R code using the vegan and dplyr packages to:
1. Calculate Shannon diversity index for each site
2. Average the diversity across the 4 survey periods for each site
3. Compare diversity between forest and grassland using an appropriate test
4. Create a boxplot of the results

Use clear comments to explain each step.
```

**Examine the code:** Even if you don't run it, you can learn from reading it!

---

### Task 3.3: Alternative Language

If you prefer Python, try:

```
Write the same bird diversity analysis in Python using pandas, numpy, and scikit-bio. Include clear comments explaining each step.
```

---

## Exercise 4: Interpreting Results (10 minutes)

### Task 4.1: Understanding Statistical Output

Copy this scenario into Gemini:

```
I ran a t-test comparing Shannon diversity between forest and grassland sites and got these results:

- Forest sites: mean Shannon diversity = 2.34 (SD = 0.18, n = 8)
- Grassland sites: mean Shannon diversity = 1.87 (SD = 0.21, n = 7)
- t-test: t = 4.23, df = 13, p-value = 0.001

Help me interpret these results:
1. What does this p-value mean?
2. Is the difference biologically meaningful?
3. How would I report this in a paper?
4. What are possible ecological explanations for this pattern?
```

---

### Task 4.2: Understanding Diversity Indices

Ask Gemini:

```
I calculated diversity indices for my bird communities and got these values for one site:
- Shannon index: 2.45
- Simpson index: 0.88
- Species richness: 15 species
- Total individuals: 127

Explain what each of these values tells me about this bird community. What does it mean that Shannon is 2.45 - is that high or low?
```

---

## Exercise 5: Real Data Analysis (15 minutes)

### Task 5.1: Analyze Sample Data

Here's real sample data from the workshop. Copy this entire prompt into Gemini:

```
I have bird survey data from 10 sites. Here are the results:

Forest sites:
- Site F1: 12 species, 45 total birds, Shannon diversity = 2.21
- Site F2: 15 species, 52 total birds, Shannon diversity = 2.48
- Site F3: 14 species, 48 total birds, Shannon diversity = 2.35
- Site F4: 13 species, 50 total birds, Shannon diversity = 2.28
- Site F5: 16 species, 55 total birds, Shannon diversity = 2.52

Grassland sites:
- Site G1: 8 species, 38 total birds, Shannon diversity = 1.85
- Site G2: 10 species, 41 total birds, Shannon diversity = 1.98
- Site G3: 9 species, 39 total birds, Shannon diversity = 1.91
- Site G4: 11 species, 43 total birds, Shannon diversity = 2.05
- Site G5: 7 species, 35 total birds, Shannon diversity = 1.76

Questions:
1. Calculate the mean Shannon diversity for each habitat type
2. Does there appear to be a difference between habitats?
3. Would a t-test be appropriate here? Why or why not?
4. What would be the null and alternative hypotheses?
5. What biological factors might explain any differences observed?
```

---

### Task 5.2: Species-Specific Analysis

Copy this into Gemini:

```
From my surveys, here are the most common species and where they were found:

American Robin: Found at 5/5 forest sites (average 5.4 per site), 0/5 grassland sites
Blue Jay: Found at 5/5 forest sites (average 3.4 per site), 0/5 grassland sites
Northern Cardinal: Found at 5/5 forest sites (average 4.2 per site), 1/5 grassland sites (1 individual)

Red-winged Blackbird: Found at 5/5 grassland sites (average 17.6 per site), 0/5 forest sites
Eastern Meadowlark: Found at 5/5 grassland sites (average 4.4 per site), 0/5 forest sites
Grasshopper Sparrow: Found at 5/5 grassland sites (average 6.0 per site), 0/5 grassland sites

Song Sparrow: Found at 5/5 grassland sites (average 12.2 per site) and 2/5 forest sites (average 2 per site)

Questions:
1. Which species show the strongest habitat association?
2. What ecological factors might explain these patterns?
3. Which species is a habitat generalist?
4. How would I statistically test for habitat association?
```

---

## Exercise 6: Domain-Specific Applications (15 minutes)

### Task 6.1: Species Identification Help

Copy into Gemini:

```
I observed a small songbird in a temperate forest with these characteristics:
- Size: smaller than a robin
- Upperparts: olive-brown
- Underparts: white with brown streaking
- Behavior: foraging on the ground, scratching in leaf litter
- Song: loud, clear "tea-CHER, tea-CHER, tea-CHER"
- Habitat: forest floor with dense understory

What species might this be? Provide a shortlist of possibilities and key distinguishing features for each. I'm in the northeastern United States.
```

**Follow-up questions to try:**
```
What time of year would I most likely see this species in the Northeast?
```

```
What other species might I confuse this with, and how can I tell them apart?
```

---

### Task 6.2: Research Design Advice

Copy into Gemini:

```
I want to study the effect of forest fragmentation on songbird nesting success. I have access to:
- 20 forest fragments ranging from 5 to 100 hectares
- One breeding season to collect data
- Resources to monitor approximately 100 nests total

Help me design this study:
1. How should I allocate my effort across fragments?
2. What variables should I measure?
3. What are the main confounding factors I should consider?
4. What statistical approach would I use to analyze the data?
5. What are the main limitations of this design?
```

---

### Task 6.3: Literature Understanding

Copy into Gemini:

```
Explain the "island biogeography theory" as it applies to forest fragments and bird communities. Include:
1. The main predictions of the theory
2. How it relates to species richness in habitat fragments
3. Why edge effects complicate this relationship
4. How this theory guides conservation decisions

Keep the explanation suitable for a graduate student new to the topic.
```

---

## Exercise 7: Writing Assistance (10 minutes)

### Task 7.1: Methods Section Writing

Copy into Gemini:

```
Help me write a methods paragraph for my paper. Here's what I did:

Study details:
- Conducted point count surveys at 30 sites
- 15 sites in continuous forest, 15 in grassland
- Surveyed each site 3 times between May 15 and June 30, 2024
- Each survey lasted 10 minutes
- Recorded all birds seen or heard within 50m radius
- Surveys conducted between 6am and 10am on days with no rain and wind <15 km/h

Write this as a clear methods paragraph suitable for a scientific paper.
```

---

### Task 7.2: Results Description

Copy into Gemini:

```
I need to describe these statistical results in prose for a results section:

We compared bird species richness between forest (n=15 sites) and grassland (n=15 sites) habitats. Forest sites had significantly higher species richness (mean = 14.2 species, SD = 1.8) compared to grassland sites (mean = 9.1 species, SD = 1.5; t-test: t = 8.45, df = 28, p < 0.001).

Write this as a clear, concise results statement for a scientific paper.
```

---

### Task 7.3: Discussion Point Development

Copy into Gemini:

```
I found that forest sites had higher bird diversity than grassland sites in my study area (temperate North America). 

Generate 4-5 possible ecological explanations for this pattern, considering:
- Habitat structure
- Resource availability
- Microclimate
- Historical factors
- Study design considerations

For each explanation, suggest what additional data would help test it.
```

---

## Exercise 8: Advanced Prompting (10 minutes)

### Task 8.1: Step-by-Step Analysis Plan

Copy into Gemini:

```
I'm new to analyzing bird diversity data. Walk me through the complete process step-by-step from raw data to results:

My data: Point count surveys at 20 sites, each surveyed 3 times, want to compare diversity between 2 habitat types

Please provide:
1. Data organization steps
2. Which diversity metrics to calculate and why
3. How to handle repeated measures
4. Which statistical test to use
5. Assumptions to check
6. How to visualize results
7. How to interpret findings

Explain each step as if teaching someone doing this for the first time.
```

---

### Task 8.2: Critique a Study Design

Copy into Gemini:

```
Critique this study design and suggest improvements:

Study plan:
- Survey birds at 10 sites (5 forest, 5 grassland)
- Survey each site once in late June
- Count all birds seen during a 5-minute period
- Compare total number of birds between habitat types
- Use a t-test to test for differences

What are the potential problems with this design? What would you change?
```

---

### Task 8.3: Multiple Comparison Issues

Copy into Gemini:

```
I surveyed 4 different habitat types (forest, grassland, wetland, urban) and want to compare bird diversity among all of them. 

Explain:
1. Why I can't just do multiple t-tests between each pair
2. What statistical approach I should use instead
3. If I find a significant difference, how do I determine which habitats differ from each other?
4. Write out the null and alternative hypotheses for this analysis

Use examples specific to my bird diversity question.
```

---

## Exercise 9: Troubleshooting Common Issues (10 minutes)

### Task 9.1: Small Sample Size Problem

Copy into Gemini:

```
I surveyed birds at only 6 sites (3 forest, 3 grassland) and calculated Shannon diversity for each. I want to compare diversity between habitats, but I'm worried about my small sample size.

Questions:
1. Is a t-test valid with only 3 replicates per group?
2. What are my alternative options?
3. What would I need to report to make these results credible?
4. How should I present this in a paper given the limitations?
```

---

### Task 9.2: Unequal Sampling Effort

Copy into Gemini:

```
I have a problem with my data. I surveyed forest sites 4 times each, but only surveyed grassland sites twice each due to access issues. Now I want to compare bird diversity between habitats.

Questions:
1. How does unequal sampling effort affect diversity comparisons?
2. Should I use all my data or subset it?
3. What statistical approaches can account for unequal effort?
4. How do I report this limitation?
```

---

### Task 9.3: Non-Normal Data

Copy into Gemini:

```
I tested my Shannon diversity data for normality and got p < 0.05 in the Shapiro-Wilk test, indicating non-normal distribution. I wanted to use a t-test to compare habitats.

Questions:
1. What does this mean for my planned t-test?
2. What are my alternatives?
3. How do I choose between alternatives?
4. Does the sample size matter for this decision?
```

---

## Exercise 10: Putting It All Together (15 minutes)

### Final Comprehensive Exercise

Copy this complete scenario into Gemini:

```
I'm planning a study to investigate how urbanization affects bird communities. Here's my plan:

Study Area: A city and surrounding rural areas in the temperate northeastern US

Design:
- 30 sites along an urbanization gradient
  - 10 rural sites (farmland/forest)
  - 10 suburban sites (residential, parks)
  - 10 urban sites (downtown, high-rise areas)
- Survey each site 3 times during breeding season (May-July)
- Use 10-minute point counts
- Record species, number of individuals, behavior

Variables to measure at each site:
- Bird species and abundance
- Tree cover percentage
- Building density
- Distance to nearest park
- Noise level

Questions I want to answer:
1. Does species diversity decline with increasing urbanization?
2. Which species are urban-tolerant vs urban-avoiding?
3. What site characteristics best predict bird diversity?

Please help me:
1. Refine this study design (what's missing? what could be improved?)
2. Suggest the appropriate statistical analyses for each question
3. Identify potential confounding variables
4. Recommend how to visualize the results
5. List the main limitations I should acknowledge
6. Suggest 3 papers I should read to understand urban bird ecology

Provide detailed, actionable advice.
```

---

## Bonus Exercise: Using NotebookLM for Literature Review (Optional)

**This exercise requires uploading documents to NotebookLM**

### Setup:
1. Go to [notebooklm.google.com](https://notebooklm.google.com)
2. Create a new notebook called "Bird Diversity Research"
3. Upload 2-3 research papers on bird ecology (PDFs)
   - You can use papers from your own research
   - Or search Google Scholar for open-access papers

### Task 1: Cross-Document Summary

Once sources are uploaded, copy this into NotebookLM:

```
Summarize the main methodologies used across all uploaded papers 
for measuring bird diversity. What are the common approaches and 
key differences?
```

### Task 2: Find Research Gaps

```
Based on these papers, what aspects of bird diversity are 
well-studied and what remains understudied? Identify 3-5 potential 
research questions that build on this literature.
```

### Task 3: Extract Statistical Methods

```
Create a table comparing the statistical methods used in each 
paper, including:
- Type of analysis
- Sample size requirements
- Key assumptions
- Software/packages mentioned
```

### Task 4: Generate Study Guide

```
Create a study guide covering the key ecological concepts I need 
to understand from these papers about bird community ecology.
```

### Task 5: Synthesize for Your Research

```
I'm planning to study [YOUR TOPIC]. Based on these papers, what 
methods would be most appropriate for my research question? What 
potential pitfalls should I avoid?
```

**Reflection:**
- How does NotebookLM differ from Gemini for literature work?
- When would you use each tool?
- How could NotebookLM fit into your research workflow?

---

## Reflection Questions

After completing these exercises, consider:

1. **Which types of prompts gave you the most useful responses?**
2. **What made the difference between vague and helpful answers?**
3. **How could you integrate Gemini into your actual research workflow?**
4. **What would you still need to verify with other sources?**
5. **What surprised you about Gemini's capabilities or limitations?**
6. **How might NotebookLM complement your use of Gemini?**

---

## Tips for Success

✅ **Do:**
- Be specific about your study system
- Provide data structure and sample sizes
- Ask for explanations, not just answers
- Use follow-up questions to dive deeper
- Copy interesting prompts for future use
- Try both Gemini and NotebookLM for different tasks

❌ **Don't:**
- Share sensitive or unpublished data
- Accept answers without verification
- Use generic prompts
- Forget to consider biological context
- Rely solely on AI for critical decisions
- Upload confidential documents to NotebookLM

---

## Next Steps

After this workshop:

1. **Save successful prompts** - Keep a document of prompts that worked well
2. **Practice regularly** - Try using Gemini for one task per week
3. **Share with colleagues** - Discuss what works in your field
4. **Stay critical** - Always verify important information
5. **Keep learning** - AI capabilities evolve rapidly

---

## Quick Reference

**Template for Analysis Questions:**
```
I have [DATA DESCRIPTION] with [N] samples measuring [VARIABLES].
I want to test [HYPOTHESIS/QUESTION].
Suggest appropriate [ANALYSIS/TEST/VISUALIZATION] and explain why.
```

**Template for Code Requests:**
```
Write [LANGUAGE] code to [TASK] using [PACKAGES].
Data structure: [DESCRIPTION]
Include comments explaining each step.
```

**Template for Interpretation:**
```
I got [RESULTS] from [TEST/ANALYSIS].
Explain what this means for [RESEARCH QUESTION].
What are possible [ECOLOGICAL/BIOLOGICAL] explanations?
```

---

Happy analyzing! Remember: You're the expert, Gemini is your assistant.
