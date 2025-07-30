import nbformat as nbf

notebooks_cleaned = [
    "notebooks_cleaned/EDA_NOTEBOOK.ipynb",
    "notebooks_cleaned/Leena_baseline_and_random_model.ipynb",
    "notebooks_cleaned/Week_9_Data_Preprocessing_Notebook.ipynb"
]


merged_nb = nbf.v4.new_notebook()

for nb_file in notebooks_cleaned:
    with open(nb_file, 'r', encoding='utf-8') as f:
        nb = nbf.read(f, as_version=4)
        merged_nb.cells.extend(nb.cells)

with open("Final_Bank_Marketing_Model.ipynb", 'w', encoding='utf-8') as f:
    nbf.write(merged_nb, f)

print("The final merged notebook has been created: Final_Bank_Marketing_Model.ipynb")
