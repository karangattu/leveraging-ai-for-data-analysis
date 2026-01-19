# Leveraging Google Gemini for Data Analysis

## Workshop Materials for Ornithologists and Ecologists

This repository contains materials for a 4-hour workshop on using Google Gemini and NotebookLM (included in Google Workspace) for data analysis in ecology and ornithology research.

## Workshop Overview

**Duration:** 4 hours  
**Target Audience:** Ornithologists, ecologists, and wildlife researchers  
**Prerequisites:** Basic understanding of ecology and data analysis  
**Requirements:** Google Workspace account with Gemini access, internet connection  

**Tools Covered:**
- **Google Gemini** - AI chat assistant for analysis, coding, and writing
- **NotebookLM** - AI research assistant for literature review and document analysis

## Contents

### Presentation
- `workshop.qmd` - Main Quarto presentation file with all workshop content
- `custom.css` - Custom styling for the presentation with animations

### Hands-On Exercises (Copy-Paste Ready!)
- `EXERCISES.md` - **Complete collection of copy-paste exercises for Google Gemini & NotebookLM**
- All exercises designed to work directly in the web interface
- No local software installation required!

### Sample Data & Code Examples (Optional)
- `data/bird_survey_data.csv` - Bird point count data for reference
- `data/site_summary_data.csv` - Site-level summary data for reference
- `analysis_examples.R` - R code examples (optional, for advanced users)
- `analysis_examples.py` - Python code examples (optional, for advanced users)

### Supplementary Materials
- `SUPPLEMENTARY.md` - Additional resources, prompt templates, and references

## Workshop Topics

1. **Introduction to AI and Large Language Models** (30 min)
   - AI fundamentals
   - How LLMs work
   - Introduction to Google Gemini and NotebookLM

2. **Getting Started** (45 min)
   - Accessing Gemini and NotebookLM through Workspace
   - Interface overview
   - First prompts and interactions
   - When to use each tool

3. **Prompt Engineering Basics** (45 min)
   - Writing effective prompts
   - Common mistakes and solutions
   - Domain-specific prompting

4. **Data Analysis with Gemini** (60 min)
   - Analysis workflow
   - Code generation (R/Python)
   - Interpreting results
   - Hands-on exercises with real data

5. **Advanced Applications** (45 min)
   - Species identification assistance
   - Literature review with NotebookLM
   - Research hypothesis generation
   - Writing assistance
   - Combining Gemini and NotebookLM

6. **Best Practices and Wrap-up** (30 min)
   - Fact-checking and verification
   - Privacy and ethics
   - Limitations and considerations
   - Resources for continued learning

## How to Use These Materials

### For Workshop Facilitators

1. **Install Quarto** (if needed):
   ```bash
   # See: https://quarto.org/docs/get-started/
   ```

2. **Render the presentation**:
   ```bash
   quarto render workshop.qmd
   ```

3. **View the presentation**:
   - Open `workshop.html` in a browser
   - Or run: `quarto preview workshop.qmd`

4. **Customize**:
   - Edit `workshop.qmd` to adjust content
   - Modify `custom.css` for different styling
   - Add your own data examples in the `data/` folder

### For Participants

**All exercises work directly in your browser - no installation needed!**

1. **Create a Google account** (if you don't have one):
   - Go to [accounts.google.com](https://accounts.google.com)
   - Free to create

2. **Access Google Gemini**:
   - Visit [gemini.google.com](https://gemini.google.com)
   - Sign in with your Google account

3. **Follow along with exercises**:
   - Open `EXERCISES.md` for all hands-on activities
   - Copy and paste prompts directly into Gemini
   - No coding experience required!

4. **Optional - For advanced users**:
   - Sample R and Python code provided in repository
   - Data files available for local analysis
   - Reference materials in `SUPPLEMENTARY.md`

**Key Point:** The workshop is designed so participants can actively learn by interacting with Gemini through their web browser. All exercises are copy-paste ready!

## Hands-On Exercises

The workshop includes 4 main hands-on tasks plus additional practice exercises:

### During Workshop:
1. **Task 1:** First Gemini interactions - basic prompts (copy-paste ready)
2. **Task 2:** Prompt improvement practice (compare poor vs. good prompts)
3. **Task 3:** Data analysis with sample bird survey data (paste data into Gemini)
4. **Task 4:** Domain-specific application - choose your scenario

### Additional Practice (in EXERCISES.md):
- 10 comprehensive exercises with copy-paste prompts
- Species identification scenarios
- Statistical interpretation practice
- Research design assistance
- Writing help examples
- Troubleshooting common issues

**All exercises work directly in the Google Gemini web interface - no coding required!**

## Requirements

### Essential (Free)
- Web browser (Chrome, Firefox, Safari, Edge)
- Google account (free) for accessing Gemini
- Internet connection

### Optional (Not Required for Workshop)
- Quarto (for rendering the presentation locally)
- R with packages: `vegan`, `dplyr`, `ggplot2` (for trying code examples)
- Python with packages: `pandas`, `numpy`, `matplotlib`, `scikit-bio` (for trying code examples)

**Note:** The workshop is designed to work entirely through the Google Gemini web interface. No local software installation is required for participants!

## Learning Objectives

By the end of this workshop, participants will be able to:

- Understand fundamentals of AI and large language models
- Set up and use Google Gemini's free tier effectively
- Write clear, effective prompts for data analysis tasks
- Generate and interpret R/Python code for ecological data analysis
- Apply Gemini to domain-specific research tasks
- Recognize limitations and use AI tools ethically
- Integrate Gemini into their research workflow

## Additional Resources

### Online Resources
- [Google Gemini](https://gemini.google.com)
- [Google AI Studio](https://aistudio.google.com)
- [Gemini API Documentation](https://ai.google.dev)
- [Learn Prompting](https://learnprompting.org)

### Recommended Reading
- Papers on AI in ecology and conservation
- Prompt engineering guides
- Responsible AI use guidelines

## License

These materials are provided for educational purposes. Please adapt and share as needed for teaching and learning.

## Contributing

Suggestions and improvements are welcome! Please feel free to:
- Report issues
- Suggest additional examples
- Share your own use cases
- Contribute sample datasets

## Contact

For questions about the workshop or materials:
- Open an issue in this repository
- Contact the workshop facilitator

## Acknowledgments

This workshop was developed to help ecologists and ornithologists leverage modern AI tools while maintaining scientific rigor and ethical standards.

---

**Remember:** AI is a powerful assistant, but you are the expert in your field. Use these tools to enhance, not replace, your scientific expertise and critical thinking.