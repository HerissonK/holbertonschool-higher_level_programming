class CountedIterator:
    def __init__(self, iterable):
        """Initialise l'objet avec un itérable et un compteur."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Retourne le prochain élément de l'itérateur et incrémente le compteur."""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        """Retourne le nombre d'éléments déjà itérés."""
        return self.count
