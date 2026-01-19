# Sample R Script for Workshop Exercises
# Leveraging Google Gemini for Data Analysis
# 
# This script demonstrates the types of analyses covered in the workshop.
# You can use these as templates and ask Gemini to help you adapt them!

# ============================================================================
# Setup and Data Loading
# ============================================================================

# Install required packages if needed (uncomment to run)
# install.packages(c("vegan", "dplyr", "ggplot2", "tidyr"))

# Load required libraries
library(vegan)
library(dplyr)
library(ggplot2)
library(tidyr)

# Load the bird survey data
bird_data <- read.csv("data/bird_survey_data.csv")
site_data <- read.csv("data/site_summary_data.csv")

# View the data structure
head(bird_data)
str(bird_data)

# ============================================================================
# Exercise 1: Calculate Diversity Indices by Site
# ============================================================================

# Reshape data to wide format (species as columns)
bird_wide <- bird_data %>%
  pivot_wider(
    names_from = species,
    values_from = count,
    values_fill = 0,
    id_cols = c(site_id, habitat_type)
  )

# Extract the species count matrix
species_matrix <- bird_wide %>%
  select(-site_id, -habitat_type) %>%
  as.matrix()

# Calculate Shannon diversity index for each site
shannon_diversity <- diversity(species_matrix, index = "shannon")

# Calculate Simpson diversity index
simpson_diversity <- diversity(species_matrix, index = "simpson")

# Calculate species richness (number of species per site)
species_richness <- specnumber(species_matrix)

# Combine results into a dataframe
diversity_results <- data.frame(
  site_id = bird_wide$site_id,
  habitat_type = bird_wide$habitat_type,
  shannon = shannon_diversity,
  simpson = simpson_diversity,
  richness = species_richness
)

print(diversity_results)

# ============================================================================
# Exercise 2: Compare Diversity Between Habitats
# ============================================================================

# Summary statistics by habitat
diversity_summary <- diversity_results %>%
  group_by(habitat_type) %>%
  summarise(
    mean_shannon = mean(shannon),
    sd_shannon = sd(shannon),
    mean_richness = mean(richness),
    sd_richness = sd(richness),
    n = n()
  )

print(diversity_summary)

# Test for differences in Shannon diversity between habitats
# Check assumptions first
shapiro.test(diversity_results$shannon[diversity_results$habitat_type == "Forest"])
shapiro.test(diversity_results$shannon[diversity_results$habitat_type == "Grassland"])

# Perform t-test
t_test_shannon <- t.test(shannon ~ habitat_type, data = diversity_results)
print(t_test_shannon)

# Test for differences in species richness
t_test_richness <- t.test(richness ~ habitat_type, data = diversity_results)
print(t_test_richness)

# ============================================================================
# Exercise 3: Visualization
# ============================================================================

# Boxplot comparing Shannon diversity between habitats
p1 <- ggplot(diversity_results, aes(x = habitat_type, y = shannon, fill = habitat_type)) +
  geom_boxplot() +
  geom_jitter(width = 0.1, alpha = 0.5) +
  labs(
    title = "Shannon Diversity by Habitat Type",
    x = "Habitat Type",
    y = "Shannon Diversity Index",
    fill = "Habitat"
  ) +
  theme_minimal() +
  theme(legend.position = "none")

print(p1)

# Boxplot comparing species richness
p2 <- ggplot(diversity_results, aes(x = habitat_type, y = richness, fill = habitat_type)) +
  geom_boxplot() +
  geom_jitter(width = 0.1, alpha = 0.5) +
  labs(
    title = "Species Richness by Habitat Type",
    x = "Habitat Type",
    y = "Number of Species",
    fill = "Habitat"
  ) +
  theme_minimal() +
  theme(legend.position = "none")

print(p2)

# ============================================================================
# Exercise 4: Species Composition Analysis
# ============================================================================

# Calculate total abundance by species and habitat
species_by_habitat <- bird_data %>%
  group_by(habitat_type, species) %>%
  summarise(total_count = sum(count), .groups = "drop")

# Bar plot of species abundance by habitat
p3 <- ggplot(species_by_habitat, aes(x = reorder(species, total_count), 
                                       y = total_count, 
                                       fill = habitat_type)) +
  geom_col(position = "dodge") +
  coord_flip() +
  labs(
    title = "Bird Species Abundance by Habitat",
    x = "Species",
    y = "Total Count",
    fill = "Habitat"
  ) +
  theme_minimal()

print(p3)

# ============================================================================
# Exercise 5: Site-Level Analysis (Using site_summary_data.csv)
# ============================================================================

# Relationship between canopy cover and species richness
p4 <- ggplot(site_data, aes(x = canopy_cover_percent, 
                             y = species_richness, 
                             color = habitat)) +
  geom_point(size = 3) +
  geom_smooth(method = "lm", se = TRUE) +
  labs(
    title = "Species Richness vs. Canopy Cover",
    x = "Canopy Cover (%)",
    y = "Species Richness",
    color = "Habitat"
  ) +
  theme_minimal()

print(p4)

# Linear model: species richness as function of habitat and canopy cover
model1 <- lm(species_richness ~ habitat + canopy_cover_percent, data = site_data)
summary(model1)

# Linear model with interaction
model2 <- lm(species_richness ~ habitat * canopy_cover_percent, data = site_data)
summary(model2)

# Compare models
anova(model1, model2)

# ============================================================================
# Tips for Using Gemini with This Code
# ============================================================================

# You can ask Gemini questions like:
# 
# 1. "Explain what the vegan package diversity() function does"
# 2. "What does a Shannon index of 2.1 mean in ecological terms?"
# 3. "How do I interpret this t-test result: t = -3.45, p = 0.008?"
# 4. "Suggest additional visualizations for this diversity data"
# 5. "Write code to add error bars to the boxplot"
# 6. "How can I test for normality of residuals in my linear model?"
# 7. "Explain the difference between Shannon and Simpson diversity indices"
# 8. "Suggest appropriate post-hoc tests if I had more than 2 habitats"
#
# Remember: Always verify Gemini's suggestions by testing the code
# and checking results against your ecological knowledge!

# ============================================================================
# Practice Exercise
# ============================================================================

# Try asking Gemini to help you:
# 1. Calculate evenness (Shannon / log(richness))
# 2. Create a rarefaction curve
# 3. Perform an NMDS ordination
# 4. Test for differences in community composition using PERMANOVA
# 5. Create a more sophisticated visualization

# Save your work
# save.image("workshop_analysis.RData")

print("Script completed successfully!")
print("Now try modifying this code with help from Gemini!")
