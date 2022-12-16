# Jour 16
Pistes : 
- [Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search) (BFS)
- [Memoization](https://www.geeksforgeeks.org/what-is-memoization-a-complete-tutorial/) (mise en cache dans cadre +/- récursif)
- [Floyd–Warshall algorithm](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm) et implémentation [scipy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.floyd_warshall.html)

Façons de procéder : 
- calculer et stocker la distance entre 2 valves
- checker temps pris par chaque combinaison : trop long ; le faire que pour combinaison de durée <30 minutes
([source](https://www.reddit.com/r/adventofcode/comments/zn7rbg/comment/j0fn2a6/))

- approche naïve : algo BFS (avec prise en compte valves ouvertes pour pas ouvrir plusieurs fois)
- autre approche : partir de la fin et choisir pour une localisation donnée à la minute n la localisation qui donne le meilleur score à la minute n-1 (ou ouvrir une valve)
donc : calculer pour chaque valve la pression pour une seule minute restante, stocker. Puis, étape suivante : reste 2 minutes ; pour chaque localisation, choix entre ouvrir une valve et se déplacer ; mais, ayant tout stocké, on sait quelle solution est la meilleure, pas besoin d'aller plus loin. On stocke, et répète pour la minute 3 (soit on ouvre une valve, soit on se déplace vers la direction rapportant le plus de pression). Sans oublier de stocker les valves déjà ouvertes
([source](https://www.reddit.com/r/adventofcode/comments/zn7rbg/comment/j0fo97q/))

- ..
([source](https://www.reddit.com/r/adventofcode/comments/zn7rbg/comment/j0fpa0a/))
[source](https://www.reddit.com/r/adventofcode/comments/zn7rbg/comment/j0fy1y0/)
[source](https://www.reddit.com/r/adventofcode/comments/zn7rbg/comment/j0fos5j/)
[source](https://www.reddit.com/r/adventofcode/comments/zn7rbg/comment/j0fpa0a/)

- exemple [mzn](https://gist.github.com/liampwll/f2640f3e8ecfb9cb9dca0190f99209e8)


note : [minizinc](https://www.minizinc.org/doc-2.6.4/en/modelling.html), [tuto fr](https://leria-info.univ-angers.fr/~jeanmichel.richer/uco_opt_combi_minizinc.php) ([entrainement](https://leria-info.univ-angers.fr/~jeanmichel.richer/uco_opt_combi_tsp.php), [data mining](https://leria-info.univ-angers.fr/~jeanmichel.richer/dm.php), [polytech](https://leria-info.univ-angers.fr/~jeanmichel.richer/polytech.php), [machine learning](https://leria-info.univ-angers.fr/~jeanmichel.richer/polytech_tp_regressions_lineaires.php))
https://www.reddit.com/r/adventofcode/comments/zn6k1l/comment/j0fgu3s/?utm_source=share&utm_medium=web2x&context=3
https://www.reddit.com/r/adventofcode/comments/zn6k1l/comment/j0fgbrd/?utm_source=share&utm_medium=web2x&context=3