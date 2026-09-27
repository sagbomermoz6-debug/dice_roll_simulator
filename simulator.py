import random 
def roll_dice(sides=6) :
    return random.randint(1,sides)

tours = int(input("Comment de tours voulez-vous faires ? " ))
score_cible = int(input("Quel est le nombre cible de votre victoire ? " ))
score = 0
detail_score = []
nbr_tour = 0

while score < score_cible and nbr_tour < tours :
    face_trouvé = roll_dice()
    score += face_trouvé
    nbr_tour += 1
    detail_score.append(face_trouvé)
    print(f"Tour : {nbr_tour}; total : {score}")

if score < score_cible :
    print(f"\nDesolée vous avez atteint {score} en {nbr_tour}. Vous aviez choisi {score_cible}")
else :
    print(f"\nBravo, vous avez reussi a atteindre le score de {score} en {nbr_tour}")

print(detail_score)