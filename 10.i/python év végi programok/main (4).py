dolgok = ["alma", "ceruza", "narancs", "asztal", "sárgarépa", "laptop", "narancs", "füzet", "zeller", "ceruza", "asztal", "laptop", "alma", "sárgarépa", "zeller", "narancs", "alma", "laptop", "narancs", "ceruza", "zeller", "asztal", "ceruza", "zeller", "asztal", "laptop", "sárgarépa", "ceruza", "narancs", "zeller", "ceruza", "alma", "narancs", "zeller", "alma", "laptop", "asztal", "ceruza", "narancs", "sárgarépa", "asztal", "narancs", "ceruza", "laptop", "zeller", "alma", "asztal", "ceruza", "narancs", "ceruza", "zeller", "alma", "laptop", "asztal", "sárgarépa", "narancs", "zeller", "ceruza", "narancs", "asztal", "zeller", "ceruza", "alma", "laptop", "narancs", "zeller", "ceruza", "asztal", "narancs", "ceruza", "alma", "zeller", "asztal", "narancs", "laptop", "ceruza", "zeller", "sárgarépa", "ceruza", "alma", "narancs", "zeller", "asztal", "ceruza", "narancs", "zeller", "laptop", "alma", "asztal", "ceruza", "zeller", "narancs", "ceruza", "alma", "sárgarépa", "zeller", "narancs", "asztal", "ceruza", "narancs", "ceruza", "alma", "laptop", "zeller", "narancs", "asztal", "sárgarépa", "ceruza", "zeller", "narancs", "ceruza", "alma", "zeller", "asztal", "narancs", "laptop", "ceruza", "zeller", "alma", "sárgarépa", "ceruza", "narancs", "zeller", "alma", "laptop", "asztal", "ceruza", "narancs", "sárgarépa", "asztal", "narancs", "ceruza", "laptop", "zeller", "alma"]

dologdarabok = {}

for item in dolgok:
    try:
       dologdarabok[item] += 1 
    except KeyError:
        dologdarabok[item] = 1 
        
for k, v in dologdarabok.items():
    if v == min(dologdarabok.values()):
        print(f'legkevesebb a {k}-ból van {v} db')