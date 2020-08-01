v_inter = 0
v_gremio = 0
e = 0

while True:
    g_inter,g_gremio = list(map(int,input().split()))
    if(g_inter == g_gremio):
        e += 1
    else:
        if(g_inter < g_gremio):
            v_gremio += 1
        else:
            v_inter += 1
  
    print("Novo grenal (1-sim 2-nao)")
    change = int(input())
    if(change == 2):
        break

print("%d grenais" %(v_inter+v_gremio+e))
print("Inter:%d" %v_inter)
print("Gremio:%d" %v_gremio)
print("Empates:%d" %e)

if(v_inter == v_gremio):
    print("Nao houve vencedor")
else:
    if(v_inter > v_gremio):
        print("Inter venceu mais")
    else:
        print("Gremio venceu mais")