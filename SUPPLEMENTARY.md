# Supplementary Materials: Gemini Workshop

## Additional Resources and Reference Materials

This document provides supplementary materials to support the "Leveraging Google Gemini for Data Analysis" workshop.

---

## Table of Contents

1. [Prompt Templates](#prompt-templates)
2. [Common Gemini Use Cases](#common-use-cases)
3. [Example Analyses](#example-analyses)
4. [Troubleshooting Guide](#troubleshooting)
5. [Further Reading](#further-reading)
6. [Glossary](#glossary)

---

## Prompt Templates

### For Statistical Analysis

```
I have [DATA DESCRIPTION] with [N] observations measuring [VARIABLES].
My research question is: [QUESTION]
Suggest appropriate statistical methods and explain their assumptions.
```

**Example:**
```
I have bird abundance data with 50 observations measuring species counts 
across forest and grassland habitats. My research question is: Do forest 
habitats support higher bird diversity than grasslands? Suggest appropriate 
statistical methods and explain their assumptions.
```

---

### For Code Generation (R)

```
Write R code using [PACKAGES] to:
1. [STEP 1]
2. [STEP 2]
3. [STEP 3]

Data structure:
- [DESCRIPTION]
- Columns: [LIST]
```

**Example:**
```
Write R code using vegan, dplyr, and ggplot2 to:
1. Calculate Shannon diversity for each site
2. Compare diversity between two habitats using a t-test
3. Create a boxplot of the results

Data structure:
- Data frame called 'bird_data'
- Columns: site_id, species, count, habitat
```

---

### For Code Generation (Python)

```
Write Python code using [LIBRARIES] to:
1. [TASK 1]
2. [TASK 2]
3. [TASK 3]

Input data format: [DESCRIPTION]
Desired output: [DESCRIPTION]
```

---

### For Literature Summarization

```
Summarize the current understanding of [TOPIC] in [FIELD], specifically focusing on:
- [ASPECT 1]
- [ASPECT 2]
- [ASPECT 3]

Include key findings and remaining knowledge gaps.
```

---

### For Method Selection

```
I want to analyze [DATA TYPE] to test [HYPOTHESIS].
Sample size: [N]
Variables: [LIST]
Data characteristics: [DESCRIPTION]

Recommend appropriate statistical methods and explain why they're suitable.
```

---

## Common Use Cases

### 1. Understanding Statistical Concepts

**Prompt:** "Explain [CONCEPT] in simple terms with an ecological example"

Examples:
- "Explain random effects in mixed models with a bird nesting example"
- "Explain Type I vs Type II error using species detection as an example"
- "Explain the concept of statistical power in the context of bird surveys"

---

### 2. Debugging Code

**Prompt Format:**
```
I'm getting this error in [LANGUAGE]:
[ERROR MESSAGE]

Here's my code:
[CODE]

What's wrong and how do I fix it?
```

---

### 3. Data Visualization

**Prompt:** "Create a [PLOT TYPE] in [R/Python] showing [RELATIONSHIP] with [AESTHETICS]"

Examples:
- "Create a ggplot scatterplot showing bird abundance vs. tree density with different colors for each habitat type"
- "Create a matplotlib figure with 3 subplots showing diversity indices by site"

---

### 4. Interpreting Results

**Prompt:** "I ran [TEST] and got these results: [RESULTS]. What does this mean for my hypothesis that [HYPOTHESIS]?"

Example:
```
I ran an ANOVA and got F(2,27) = 5.43, p = 0.010. 
What does this mean for my hypothesis that bird species 
richness differs among three habitat types?
```

---

### 5. Method Comparison

**Prompt:** "Compare [METHOD A] vs [METHOD B] for [PURPOSE]. What are the pros and cons of each?"

Example:
```
Compare Shannon diversity index vs Simpson diversity index 
for measuring bird community diversity. What are the pros 
and cons of each?
```

---

## Example Analyses

### Example 1: Comparing Bird Diversity Across Habitats

**Research Question:** Do bird communities in forest habitats have higher diversity than those in grassland habitats?

**Gemini Prompt:**
```
I have bird survey data from 10 sites (5 forest, 5 grassland). 
Each site was surveyed 3 times. I recorded species and abundance. 
I want to compare diversity between habitats. Suggest a complete 
analysis workflow including:
1. Diversity metric selection
2. Statistical test choice
3. Assumptions to check
4. Visualization approach
```

**Follow-up Prompts:**
- "Write R code to implement this analysis"
- "How do I check if my data meets the assumptions?"
- "What if the assumptions are violated?"

---

### Example 2: Temporal Trends in Bird Abundance

**Research Question:** Has bird abundance changed over the past 5 years?

**Gemini Prompt:**
```
I have 5 years of bird count data from 20 sites. Each site was 
surveyed annually. I want to test for temporal trends in total 
abundance and species richness. Suggest appropriate methods considering:
- Repeated measures at same sites
- Potential site-level variation
- Need to account for multiple species
```

---

### Example 3: Habitat Association Analysis

**Research Question:** Which habitat variables best predict bird species richness?

**Gemini Prompt:**
```
I have data on bird species richness at 50 sites along with 
habitat variables (tree density, canopy cover, understory density, 
distance to water). Suggest a regression approach including:
1. Model selection strategy
2. Handling correlated predictors
3. Model validation
4. Interpretation of coefficients
```

---

## Troubleshooting Guide

### Problem: Gemini gives generic answers

**Solution:**
- Add more specific details to your prompt
- Include data structure information
- Specify your field (ornithology/ecology)
- Provide context about your research question

**Example Improvement:**
- ❌ "How do I analyze bird data?"
- ✅ "I have point count data for forest birds with columns: site, date, species, count. How do I calculate species accumulation curves?"

---

### Problem: Generated code doesn't work

**Solution:**
1. Copy the exact error message
2. Ask Gemini: "I got this error: [ERROR]. Here's my code: [CODE]. What's wrong?"
3. Check that you have all required packages
4. Verify your data structure matches what the code expects

---

### Problem: Results don't make biological sense

**Solution:**
- Always verify with domain knowledge
- Ask: "What are potential ecological explanations for [RESULT]?"
- Consider data quality issues
- Check for coding errors
- Consult with colleagues

---

### Problem: Gemini suggests inappropriate methods

**Solution:**
- Provide more details about your data structure
- Specify assumptions and constraints
- Ask for alternatives: "What if [ASSUMPTION] doesn't hold?"
- Cross-reference with statistical textbooks

---

### Problem: Hit rate limits on free tier

**Solution:**
- Plan your questions before starting
- Use one conversation for related questions
- Wait a few minutes between heavy use sessions
- Consider using multiple sessions for different projects

---

## Further Reading

### AI and Prompt Engineering

- **Learn Prompting** (learnprompting.org) - Comprehensive guide to prompt engineering
- **Prompt Engineering Guide** (promptingguide.ai) - Best practices and examples
- **Google AI Documentation** (ai.google.dev) - Official Gemini documentation

---

### AI in Ecology and Conservation

**Journal Articles:**
- Christin et al. (2019). "Applications for deep learning in ecology." *Methods in Ecology and Evolution*
- Wäldchen & Mäder (2018). "Machine learning for image based species identification." *Methods in Ecology and Evolution*
- Tuia et al. (2022). "Perspectives in machine learning for wildlife conservation." *Nature Communications*

---

### Statistical Methods in Ecology

**Books:**
- Zuur et al. (2009). *Mixed Effects Models and Extensions in Ecology with R*
- Quinn & Keough (2002). *Experimental Design and Data Analysis for Biologists*
- Gotelli & Ellison (2004). *A Primer of Ecological Statistics*

**Online Resources:**
- R for Data Science (r4ds.had.co.nz)
- Python for Ecologists (datacarpentry.org)

---

### Responsible AI Use

- **Ethics in AI Research** - Guidelines from major journals
- **Data Privacy Guidelines** - Best practices for sharing research data
- **Academic Integrity Policies** - Check your institution's guidelines

---

## Glossary

**AI (Artificial Intelligence):** Computer systems that can perform tasks requiring human-like intelligence

**LLM (Large Language Model):** AI model trained on vast text data to understand and generate human language

**Prompt:** The text input you provide to an AI system to get a response

**Prompt Engineering:** The practice of crafting effective prompts to get better AI responses

**Hallucination:** When an AI generates plausible-sounding but incorrect information

**Token:** Unit of text processed by an LLM (roughly ¾ of a word)

**Context Window:** The amount of text an LLM can consider at once

**Fine-tuning:** Additional training to specialize an AI model for specific tasks

**Zero-shot:** Getting results without providing examples

**Few-shot:** Providing examples in the prompt to guide the response

**Chain-of-thought:** Prompting technique that asks AI to show reasoning steps

**Temperature:** Parameter controlling randomness in AI responses (higher = more creative)

**Multimodal:** AI that can process multiple types of input (text, images, audio)

---

### Ecological Terms (for reference with Gemini)

**Alpha Diversity:** Species diversity within a habitat or sample

**Beta Diversity:** Diversity between habitats or samples

**Gamma Diversity:** Total diversity across a landscape

**Shannon Index:** Diversity measure considering richness and evenness

**Simpson Index:** Diversity measure emphasizing dominant species

**Evenness:** How equally abundant species are in a community

**Richness:** Number of species in a community

**Rarefaction:** Standardizing species richness by sample size

**Ordination:** Reducing multivariate ecological data to fewer dimensions (PCA, NMDS)

**PERMANOVA:** Permutational multivariate analysis of variance

---

## Practice Exercises

### Exercise 1: Refining Prompts

Take this poor prompt and improve it:
```
"Tell me about birds"
```

Improved versions could focus on:
- Migration patterns of a specific species
- Foraging behavior in different habitats
- Statistical analysis of survey data
- Conservation status and threats

---

### Exercise 2: Code Generation

Ask Gemini to generate code for:
1. Calculating species accumulation curves
2. Creating a community composition heatmap
3. Performing a nested ANOVA for hierarchical data
4. Generating a publication-ready figure

---

### Exercise 3: Interpretation

Paste these results into Gemini and ask for interpretation:
```
Linear mixed-effects model:
Fixed effects:
                  Estimate  Std.Error  t-value
(Intercept)       12.45     2.31       5.39
Habitat[Forest]   5.67      1.23       4.61
Canopy_cover      0.08      0.03       2.67
```

Ask:
- "What do these coefficients mean?"
- "How do I report this in a paper?"
- "What ecological processes might explain this pattern?"

---

## Quick Reference Card

### Best Practices Checklist

- [ ] Be specific in your prompts
- [ ] Provide context about your research
- [ ] Include data structure details
- [ ] Specify packages/libraries you prefer
- [ ] Verify all statistical recommendations
- [ ] Test all generated code
- [ ] Check results against domain knowledge
- [ ] Don't share sensitive data
- [ ] Acknowledge AI use appropriately
- [ ] Keep learning and iterating

---

### When to Use Gemini

✅ **Good for:**
- Learning statistical concepts
- Generating analysis code
- Brainstorming research ideas
- Understanding methods
- Improving writing clarity
- Debugging code
- Creating visualizations

❌ **Not good for:**
- Final decision-making
- Replacing peer review
- Analyzing sensitive data
- Species identification (verify!)
- Real-time field decisions

---

## Feedback and Improvement

This is a living document. As you use Gemini in your research:

- Note what works well
- Document successful prompts
- Share insights with colleagues
- Contribute to community knowledge
- Stay updated on new features

---

## Contact and Support

For questions about this workshop:
- Refer to main README.md
- Check online resources listed above
- Join ecology/ornithology AI communities
- Share experiences with colleagues

---

*Last Updated: [Date]*
*Workshop Materials Repository: [Link]*
