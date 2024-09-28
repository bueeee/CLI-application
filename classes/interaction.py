class Interaction:
    def __init__(self, drug1, drug2, interaction_type=None, description=None):
        self.drug1 = drug1  # First drug (instance of the Drug class)
        self.drug2 = drug2  # Second drug (instance of the Drug class)
        self.interaction_type = interaction_type  # Positive, negative, or neutral
        self.description = description  # A more detailed description of the interaction

    def __str__(self):
        return f"Interaction between {self.drug1} and {self.drug2}: {self.interaction_type}"