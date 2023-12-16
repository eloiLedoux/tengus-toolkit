G = { 'depart' : {'A' : 2, 'D' : 3},
      'A' : {'B' : 1},
      'B' : {'C' : 4,'D' : 2},
      'C' : {'arrivee' : 1},
      'D' : {'arrivee' : 4},
      'arrivee' : {} }

def dijkstra(G, source='depart'):
    dist = {}
    prec = {}
    non_visite = []

    for sommet in G:
        dist[sommet] = float('inf')
        prec[sommet] = None
        non_visite.append(sommet)
    dist[source] = 0

    while non_visite:
        u = min(non_visite, key=lambda s: dist[s])
        non_visite.remove(u)

        for voisin in G[u]:
            if voisin in non_visite:
                nouvelle_dist = dist[u] + G[u][voisin]
                if nouvelle_dist < dist[voisin]:
                    dist[voisin] = nouvelle_dist
                    prec[voisin] = u
    
    return dist, prec

def construire_chemin(dist, prec, arrivee='arrivee'):
    chemin = []
    act = arrivee
    while prec[act] != None:
        chemin.append(act)
        act = prec[act]
    chemin.append(act)
    act = prec[act]
    chemin.reverse()
    return chemin, dist[arrivee]

dist_G, prec_G = dijkstra(G)
print("Distances par sommets :", dist_G)
print("Liste de précédence :",prec_G)
ch_G, ds_G = construire_chemin(dist_G, prec_G)
print("Plus court chemin :",ch_G) 
print("Distance du plus court chemin :",ds_G) 

