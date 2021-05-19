class StepsList(list):


    def __contains__(self, o: object) -> bool:
        return any(isinstance(val, o) for val in self)