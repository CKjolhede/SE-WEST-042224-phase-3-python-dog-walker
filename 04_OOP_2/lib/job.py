class Job:

    all = []

    def __init__(self, pet, handler, date, duration):
        self.pet = pet
        self.handler = handler
        self.date = date
        self.duration = duration
        self.__class__.all.append(self)

    # @classmethod
    # def all_pets(cls):
    #     return [job.pet for job in cls.all]

    def fee(self):
        return self.handler.hourly_rate * self.duration
