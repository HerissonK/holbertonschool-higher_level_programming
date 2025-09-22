class VerboseList(list):
    def append(self, item):
        """Ajoute un élément et affiche un message."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Étend la liste et affiche un message avec le nombre d'éléments"""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Supprime un élément et affiche un message avant la suppression."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Retire un élément et affiche un message avant le retrait."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
