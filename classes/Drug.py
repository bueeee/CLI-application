class Drug:
    def __init__(self, name, dosage=None, route_of_administration=None):
        self.name = name  # The name of the drug (e.g., "Aspirin")
        self.dosage = dosage  # Dosage information (e.g., "100mg")
        self.route_of_administration = route_of_administration  # Oral, Intravenous, etc.

    def __str__(self):
        return f"{self.name} ({self.dosage}, {self.route_of_administration})"