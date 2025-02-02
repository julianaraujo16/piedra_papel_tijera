"""
Nombre: agenda.py
Autor: Juliana Bolaños
Fecha: 31/01/2025
Descripción: Implementación de una agenda donde se puedes agregar y eliminar tareas
"""

print("\n--------------------- Bienvenid@ a su Agenda Virtual 📔 ---------------------\n")
homeworks = [["Clase de Ingles", "11 AM"], ["Leer", "2 PM"], ["Leccion de Duolingo", "4 PM"], ["Correr", "6 PM"], ["Programar", "9 PM"]]
days_weekd = ["lunes", "martes", "miercoles", "jueves", "viernes"]

def agenda():
    print("\n📌 Hoy tienes que hacer:")

    for task, time in homeworks:
        print(f"+ {task} a las {time}")

    while True:
        new_task = input("\n¿Quieres agregar una nueva tarea? (S/N): ")
        if new_task.lower() == 's':

            while True:
                new_task = input("\n¿Qué tareas deseas agregar?: ")
                time_task = input("¿A qué hora? Agregar (PM/AM): ")
                time_exists = True
                for task in homeworks:
                    for time in task:
                        if time_task.upper() in time:
                            time_exists = False

                if time_exists:
                    homeworks.append([new_task.capitalize(), time_task.upper()])
                    print("✅ Tarea agregada exitosamente!")
                else:
                    print("\nEse horario ya esta ocupado, intentalo de nuevo\n")      

                add_more = input("\n¿Quieres agregar otra tarea? (S/N): ")
                if add_more != 's':
                    break
            
            print("\n📌 Agenda actualizada: ")
            for task, time in homeworks:
                print(f"+ {task} a las {time}")
            break

        elif new_task.lower() == 'n':

            delete_task = input("\n¿Quieres eliminar una tarea? (S/N): ")
            if delete_task.lower() == 's':

                while True:
                    task = input("\n¿Qué tareas deseas eliminar?: ").capitalize()
                    time_task = input("¿A qué hora? Agregar (PM/AM): ").upper()
                    task_exists = -1
                    
                    for i in homeworks:
                        if [task, time_task] == i:
                            task_exists = homeworks.index(i)

                    if task_exists != -1:
                        homeworks.pop(task_exists)
                        print("\n✅ Tarea eliminada exitosamente!")
                    else:
                        print("\nLa tarea no existe en la agenda o esta mal escrita, intentalo de nuevo\n")      

                    add_more = input("\n¿Quieres eliminar otra tarea? (S/N): ")
                    if add_more != 's':
                        break
                
                print("\n📌 Agenda actualizada: ")
                for task, time in homeworks:
                    print(f"+ {task} a las {time}")
                break
            elif delete_task.lower() == 'n':                
                print("\nPerfecto, ya tienes tu lista de deberes")

                break
            else:
                print("Por favor ingrese un valor valido")

        else:
            print("Por favor ingrese un valor valido")

while True:
    day = input("Ingrese un dia de semana: ").lower()
    if day in days_weekd:
        agenda()
        break
    elif day == 'sabado':
        homeworks.pop(-1)
        homeworks.append(["Ver una pelicula", "8 PM"])
        print("\n¡Es sabado! 💃🕺")
        agenda()
    
    elif day == 'domingo':
        print("\n¡Hoy es tu dia de descanso! 🛌")
        break
    else:
        print("Por favor ingrese un dia valido\n")

