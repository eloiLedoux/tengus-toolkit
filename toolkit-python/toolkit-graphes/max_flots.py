def augmenterFlot(f, P, c):
    capacite_min = min([c[u][v] for (u,v) in P])
    for (u, v) in P:
        if (u, v) in f:
            f[(u, v)] = f[(u, v)] + capacite_min
        else:
            f[(v, u)] = f[(v, u)] - capacite_min
    return f

def mettreAJourResiduel(G, Gf, P, fP):
    for (u,v) in P:
        Gf[u][v] = Gf[u][v] - fP[(u, v)]
        if Gf[u][v] == 0:
            del Gf[u][v]
        if (v, u) not in Gf:
            Gf[v][u] = 0
        Gf[v][u] = fP[(u, v)]
    return Gf

def cheminAugmentant(G, s, p):
    f = [s]
    parent = {s: s}
    while f and f[0] != p:
        a = f.pop(0)
        for u in G:
            for v in G[u]:
                if u == a and v not in parent:
                    parent[v] = u
                    f.append(v)
    chemin = []
    v = p
    if v not in parent:
        return chemin
    while v != s:
        chemin.insert(0, (parent[v], v))
        v = parent[v]
    return chemin

def FordFulkerson(G, source, puits):
    flot = {}
    for u in G:
        for v in G[u]:
            flot[(u, v)] = 0
    Gf = G
    chemin = cheminAugmentant(Gf, source, puits)
    while chemin:
        flot = augmenterFlot(flot, chemin, G)
        Gf = mettreAJourResiduel(G, Gf, chemin, flot)
        chemin = cheminAugmentant(Gf, source, puits)
    return flot

G = { 'a' : {'b' : 16, 'c' : 13},
          'b' : {'d' : 12},
          'c' : {'b' : 4, 'e' : 14},
          'd' : {'c' : 9, 'f' : 20},
          'e' : {'d' : 7, 'f' : 4},
          'f' : {},
}

print("Flots augmentés :")
print(FordFulkerson(G, 'a', 'f'))
