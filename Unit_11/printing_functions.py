# Zachary Hoover || Independent Practice #31
# 01-04-23

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until there are none left.
    Move each design to complete after printing.
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print(f" Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all of the models that were printed."""
    print("\n The following models have been printed:")
    for model in completed_models:
        print(" ", model)
