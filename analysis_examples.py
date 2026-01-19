"""
Sample Python Script for Workshop Exercises
Leveraging Google Gemini for Data Analysis

This script demonstrates the types of analyses covered in the workshop.
You can use these as templates and ask Gemini to help you adapt them!
"""

# ============================================================================
# Setup and Data Loading
# ============================================================================

# Install required packages if needed (uncomment to run)
# pip install pandas numpy matplotlib seaborn scipy scikit-bio

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import ttest_ind, shapiro
from skbio.diversity import alpha_diversity

# Set plotting style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Load the bird survey data
bird_data = pd.read_csv("data/bird_survey_data.csv")
site_data = pd.read_csv("data/site_summary_data.csv")

# View the data structure
print("Bird Survey Data:")
print(bird_data.head())
print(f"\nShape: {bird_data.shape}")
print(f"\nColumns: {bird_data.columns.tolist()}")

# ============================================================================
# Exercise 1: Calculate Diversity Indices by Site
# ============================================================================

# Reshape data to wide format (species as columns)
bird_wide = bird_data.pivot_table(
    index=['site_id', 'habitat_type'],
    columns='species',
    values='count',
    fill_value=0
).reset_index()

print("\nWide format data:")
print(bird_wide.head())

# Extract the species count matrix
species_cols = [col for col in bird_wide.columns if col not in ['site_id', 'habitat_type']]
species_matrix = bird_wide[species_cols].values

# Calculate Shannon diversity index for each site
# Using scikit-bio
from skbio.diversity.alpha import shannon

shannon_diversity = np.array([shannon(row) for row in species_matrix])

# Alternative: Calculate manually
def calculate_shannon_manual(counts):
    """Calculate Shannon diversity index manually"""
    counts = np.array(counts)
    counts = counts[counts > 0]  # Remove zeros
    proportions = counts / counts.sum()
    return -np.sum(proportions * np.log(proportions))

shannon_manual = np.array([calculate_shannon_manual(row) for row in species_matrix])

# Calculate Simpson diversity
def calculate_simpson(counts):
    """Calculate Simpson diversity index (1 - D)"""
    counts = np.array(counts)
    n = counts.sum()
    if n == 0:
        return 0
    proportions = counts / n
    return 1 - np.sum(proportions ** 2)

simpson_diversity = np.array([calculate_simpson(row) for row in species_matrix])

# Calculate species richness
species_richness = np.sum(species_matrix > 0, axis=1)

# Combine results into a dataframe
diversity_results = pd.DataFrame({
    'site_id': bird_wide['site_id'],
    'habitat_type': bird_wide['habitat_type'],
    'shannon': shannon_diversity,
    'simpson': simpson_diversity,
    'richness': species_richness
})

print("\nDiversity Results:")
print(diversity_results)

# ============================================================================
# Exercise 2: Compare Diversity Between Habitats
# ============================================================================

# Summary statistics by habitat
diversity_summary = diversity_results.groupby('habitat_type').agg({
    'shannon': ['mean', 'std', 'count'],
    'simpson': ['mean', 'std'],
    'richness': ['mean', 'std']
}).round(3)

print("\nDiversity Summary by Habitat:")
print(diversity_summary)

# Test for differences in Shannon diversity between habitats
forest_shannon = diversity_results[diversity_results['habitat_type'] == 'Forest']['shannon']
grassland_shannon = diversity_results[diversity_results['habitat_type'] == 'Grassland']['shannon']

# Check normality assumption
shapiro_forest = shapiro(forest_shannon)
shapiro_grassland = shapiro(grassland_shannon)

print(f"\nShapiro-Wilk test for Forest: W={shapiro_forest.statistic:.4f}, p={shapiro_forest.pvalue:.4f}")
print(f"Shapiro-Wilk test for Grassland: W={shapiro_grassland.statistic:.4f}, p={shapiro_grassland.pvalue:.4f}")

# Perform t-test
t_stat, p_value = ttest_ind(forest_shannon, grassland_shannon)
print(f"\nT-test for Shannon diversity:")
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")

# Test for differences in species richness
forest_richness = diversity_results[diversity_results['habitat_type'] == 'Forest']['richness']
grassland_richness = diversity_results[diversity_results['habitat_type'] == 'Grassland']['richness']

t_stat_rich, p_value_rich = ttest_ind(forest_richness, grassland_richness)
print(f"\nT-test for species richness:")
print(f"t-statistic: {t_stat_rich:.4f}")
print(f"p-value: {p_value_rich:.4f}")

# ============================================================================
# Exercise 3: Visualization
# ============================================================================

# Create figure with subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Boxplot comparing Shannon diversity between habitats
sns.boxplot(data=diversity_results, x='habitat_type', y='shannon', 
            hue='habitat_type', ax=axes[0], legend=False)
sns.stripplot(data=diversity_results, x='habitat_type', y='shannon', 
              color='black', alpha=0.5, ax=axes[0])
axes[0].set_title('Shannon Diversity by Habitat Type', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Habitat Type', fontsize=12)
axes[0].set_ylabel('Shannon Diversity Index', fontsize=12)

# Boxplot comparing species richness
sns.boxplot(data=diversity_results, x='habitat_type', y='richness', 
            hue='habitat_type', ax=axes[1], legend=False)
sns.stripplot(data=diversity_results, x='habitat_type', y='richness', 
              color='black', alpha=0.5, ax=axes[1])
axes[1].set_title('Species Richness by Habitat Type', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Habitat Type', fontsize=12)
axes[1].set_ylabel('Number of Species', fontsize=12)

plt.tight_layout()
plt.savefig('diversity_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nFigure saved as 'diversity_comparison.png'")

# ============================================================================
# Exercise 4: Species Composition Analysis
# ============================================================================

# Calculate total abundance by species and habitat
species_by_habitat = bird_data.groupby(['habitat_type', 'species'])['count'].sum().reset_index()
species_by_habitat.columns = ['habitat_type', 'species', 'total_count']

# Create pivot for easier plotting
species_pivot = species_by_habitat.pivot(index='species', 
                                         columns='habitat_type', 
                                         values='total_count').fillna(0)

# Bar plot of species abundance by habitat
fig, ax = plt.subplots(figsize=(12, 8))
species_pivot.plot(kind='barh', ax=ax, color=['#2ecc71', '#f39c12'])
ax.set_title('Bird Species Abundance by Habitat', fontsize=14, fontweight='bold')
ax.set_xlabel('Total Count', fontsize=12)
ax.set_ylabel('Species', fontsize=12)
ax.legend(title='Habitat', fontsize=10)
plt.tight_layout()
plt.savefig('species_abundance.png', dpi=300, bbox_inches='tight')
plt.show()

print("Figure saved as 'species_abundance.png'")

# ============================================================================
# Exercise 5: Site-Level Analysis (Using site_summary_data.csv)
# ============================================================================

# Relationship between canopy cover and species richness
fig, ax = plt.subplots(figsize=(10, 6))

for habitat in site_data['habitat'].unique():
    data = site_data[site_data['habitat'] == habitat]
    ax.scatter(data['canopy_cover_percent'], data['species_richness'], 
               label=habitat, s=100, alpha=0.7)
    
    # Add regression line
    z = np.polyfit(data['canopy_cover_percent'], data['species_richness'], 1)
    p = np.poly1d(z)
    x_line = np.linspace(data['canopy_cover_percent'].min(), 
                         data['canopy_cover_percent'].max(), 100)
    ax.plot(x_line, p(x_line), "--", alpha=0.8)

ax.set_title('Species Richness vs. Canopy Cover', fontsize=14, fontweight='bold')
ax.set_xlabel('Canopy Cover (%)', fontsize=12)
ax.set_ylabel('Species Richness', fontsize=12)
ax.legend(title='Habitat', fontsize=10)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('richness_vs_canopy.png', dpi=300, bbox_inches='tight')
plt.show()

print("Figure saved as 'richness_vs_canopy.png'")

# Linear regression analysis
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Prepare data for regression
le = LabelEncoder()
site_data['habitat_encoded'] = le.fit_transform(site_data['habitat'])

# Model 1: species richness as function of habitat and canopy cover
X1 = site_data[['habitat_encoded', 'canopy_cover_percent']]
y = site_data['species_richness']

model1 = LinearRegression()
model1.fit(X1, y)
r2_score1 = model1.score(X1, y)

print(f"\nLinear Regression Results:")
print(f"R² Score: {r2_score1:.4f}")
print(f"Coefficients: habitat={model1.coef_[0]:.4f}, canopy_cover={model1.coef_[1]:.4f}")
print(f"Intercept: {model1.intercept_:.4f}")

# Calculate predictions and residuals
predictions = model1.predict(X1)
residuals = y - predictions

# Check residual normality
shapiro_residuals = shapiro(residuals)
print(f"\nShapiro-Wilk test for residuals: W={shapiro_residuals.statistic:.4f}, p={shapiro_residuals.pvalue:.4f}")

# ============================================================================
# Tips for Using Gemini with This Code
# ============================================================================

print("\n" + "="*70)
print("Tips for Using Gemini with This Code")
print("="*70)
print("""
You can ask Gemini questions like:

1. "Explain what the Shannon diversity index measures"
2. "What does a Shannon index of 2.1 mean in ecological terms?"
3. "How do I interpret this t-test result: t = -3.45, p = 0.008?"
4. "Suggest additional visualizations for this diversity data"
5. "How can I add confidence intervals to my plots?"
6. "Write code to perform a permutational ANOVA on this data"
7. "Explain the difference between Shannon and Simpson diversity indices"
8. "How do I calculate species evenness?"
9. "Suggest methods for ordination analysis of this community data"
10. "Help me interpret these regression coefficients in ecological context"

Remember: Always verify Gemini's suggestions by testing the code
and checking results against your ecological knowledge!
""")

# ============================================================================
# Practice Exercise
# ============================================================================

print("\n" + "="*70)
print("Practice Exercise")
print("="*70)
print("""
Try asking Gemini to help you:
1. Calculate Pielou's evenness (Shannon / log(richness))
2. Create a rarefaction curve using scikit-bio
3. Perform a Kruskal-Wallis test if normality assumptions aren't met
4. Create a heatmap of species by site
5. Add statistical annotations to the plots
6. Perform a principal component analysis (PCA) on the community data

Good luck with your analysis!
""")

print("\nScript completed successfully!")
print("Now try modifying this code with help from Gemini!")
