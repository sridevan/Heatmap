import pandas as pd
import string 

# Load and read the csv file
df = pd.read_csv('discrepancy.csv')

# Save the values in column 1 into a list
motif_id1 = df['motif_id1'].tolist()

# Save the values in column 1 into a list
motif_id2 = df['motif_id2'].tolist()

# Save the values in column 3 into a list
discrepancy = df['discrepancy'].tolist()

# Get the unique motif IDs
cols = df.motif_id1.unique()

motif_ordering = dict()

# Create an index for each unique motif in an orderly manner
for index, letter in enumerate(cols):
   motif_ordering[letter] = index 
   
# Assign index for motif1
coordx = []
for motif1 in motif_id1:
    if motif1 in motif_ordering:
        coordx.append(motif_ordering[motif1])

# Assign index for motif2
coordy = []
for motif2 in motif_id2:
    if motif2 in motif_ordering:
        coordy.append(motif_ordering[motif2])
        
new_rows = list(zip(motif_id1,motif_id2,coordx, coordy, discrepancy))
new_df = pd.DataFrame(new_rows)
# Create a new csv file with the indexes assigned to each motif-pair
new_df.to_csv('disc_parsed.csv', index=False, header=['motif_id1', 'motif_id2', 'coordx', 'coordy', 'discrepancy'])