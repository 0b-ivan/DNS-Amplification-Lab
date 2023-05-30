import multiprocessing


def function1():
    # Funktion 1-Logik hier einfügen
    pass


def function2():
    # Funktion 2-Logik hier einfügen
    pass


if __name__ == "__main__":
    # Anzahl der Prozesse festlegen
    num_processes = 2

    # Erstellen einer Pool-Instanz mit der Anzahl der gewünschten Prozesse
    pool = multiprocessing.Pool(processes=num_processes)

    # Liste der Funktionen, die parallel ausgeführt werden sollen
    functions = [function1, function2]

    # Iteriere über die Funktionen und rufe sie parallel auf
    results = []
    for func in functions:
        result = pool.apply_async(func)  # Asynchroner Aufruf der Funktion
        results.append(result)

    # Warte auf das Beenden aller Prozesse
    pool.close()
    pool.join()

    # Ergebnisse abrufen
    for result in results:
        result.get()
