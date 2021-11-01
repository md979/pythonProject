

caracteres_primer = input('')

caracteres_primer = caracteres_primer.replace("-","")

def resultado(cad):
    cadena_final = "".join(set(cad))
    reps = ""
    for i in cadena_final:
        reps += str(cad.count(i))
    print(cadena_final,"\n", reps)


