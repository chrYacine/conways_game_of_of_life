import numpy as np

# Initialisation de la grille 
frame = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])

# Ajout du zéro 
padded_frame = np.pad(frame, 1, mode="constant")

print("Grille initiale :\n", frame)
print("\nGrille avec zéro padding :\n", padded_frame)

def compute_number_neighbors(padded_frame, index_row, index_col):
    
    neighbor_sum = np.sum(
        padded_frame[index_row - 1:index_row + 2, index_col - 1:index_col + 2]
    )
    # Soustraire la valeur de la cellule elle-même
    neighbor_sum -= padded_frame[index_row, index_col]
    return neighbor_sum

### test fonction 
# print("Nombre de voisins pour la cellule (3,3) :", compute_number_neighbors(padded_frame, 3, 3))  
# print("Nombre de voisins pour la cellule (3,4) :", compute_number_neighbors(padded_frame, 3, 4)) 

def compute_next_frame(frame):
    """
    Cette fonction prend en entrée une frame et calcule la frame suivante
    à partir des règles du jeu de la vie
    """
    # Ajouter une bordure de zéros 
    padded_frame = np.pad(frame, 1, mode="constant")

    # Créer une copie de la grille actuelle pour appliquer les modifications
    next_frame = np.copy(frame)

    # Parcourir
    for row in range(1, padded_frame.shape[0] - 1):
        for col in range(1, padded_frame.shape[1] - 1):
            # Calculer le nombre de voisins vivants
            neighbors = compute_number_neighbors(padded_frame, row, col)

            #  les règles du jeu
            if padded_frame[row, col] == 1:  # si  vivante
                if neighbors < 2 or neighbors > 3:  # Meurt 
                    next_frame[row - 1, col - 1] = 0
            else:  
                if neighbors == 3:  
                    next_frame[row - 1, col - 1] = 1

    return next_frame
         
# while True:
#     # boucle infini qui affiche toutes les frames successives (ctrl + c pour arrêter le script)
#     print(frame)
#     frame = compute_next_frame(frame)

while True:
    print("\nGrille actuelle :")
    print(frame)
    frame = compute_next_frame(frame)
    input("Appuyez sur Entrée pour afficher la génération suivante... (Ctrl+C pour arrêter)")