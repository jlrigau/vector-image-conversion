# Logo SOCAMETT — fichiers d'impression

Fichiers vectoriels prêts pour un imprimeur (carte de visite, papeterie, etc.).
Préférez toujours le **vectoriel** ; il s'imprime net à n'importe quelle taille.

| Fichier | Usage |
|---|---|
| `socamett-logo.pdf` | PDF vectoriel **RVB** — universel, l'imprimeur convertit avec son profil |
| `socamett-logo-cmyk.pdf` | PDF vectoriel **CMJN** (profil Generic CMYK) — prêt quadri |
| `socamett-logo.eps` | EPS vectoriel — pour les flux qui l'exigent |

Le SVG (`../socamett-logo.svg`) et les PNG haute résolution (`../logos/`) restent
disponibles à la racine du dépôt.

## Couleur de marque — bleu

| Espace | Valeur |
|---|---|
| HEX | `#0B3FA4` |
| RVB | 11 / 63 / 164 |
| CMJN (PDF fourni) | ≈ C95 M77 J0 N1 |
| CMJN (build conseillé) | **C100 M72 J0 N5** |
| Pantone | **286 C** (bleu corporate classique) — ou **293 C**, le plus proche numériquement |

⚠️ Les correspondances Pantone sont des approximations écran. **Validez sur un
nuancier Pantone physique** avant un tirage important.

Pour une couleur de marque parfaitement constante (cartes, enseignes, web),
le mieux est d'imprimer le bleu en **ton direct Pantone** plutôt qu'en quadri.

## Élément blanc

Le texte, l'anneau et l'emblème sont en **blanc** : ce sont des réserves (blanc
du papier) sur fond blanc, ou du **blanc d'impression** si la carte est sur
support coloré/foncé. Le fond du logo (hors ovale) est **transparent**.

## Marges / fond perdu

Le logo n'a pas besoin de fond perdu (il ne touche pas le bord). Prévoyez une
marge de sécurité autour de l'ovale dans la maquette de la carte.
